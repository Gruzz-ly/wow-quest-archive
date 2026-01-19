import requests
import os
import time
import re
import logging
import sys

# CONFIGURATION
# ----------------------------------------------------
BASE_URL = "https://warcraft.wiki.gg/api.php"

ROOT_CATEGORIES = [
    "Category:Quests by zone",       
    "Category:Dungeon quests",       
    "Category:Raid quests",          
    "Category:World Event quests",   
    "Category:Profession quests"     
]

OUTPUT_DIR = "docs" 
DELAY = 2.0  
BATCH_SIZE = 50 

# GLOBAL STATE
SKIP_EXISTING = False  # Will be set by user input
# ----------------------------------------------------

# SETUP LOGGING
logging.basicConfig(
    filename='crash_log.txt', 
    level=logging.ERROR, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

HEADERS = {
    'User-Agent': 'QuestArchiver/5.0 (Smart Resume; contact: me@localhost)'
}

def clean_filename(name):
    """Removes illegal characters and keeps filenames short."""
    name = name.replace("Category:", "").replace("Quests in ", "").replace("Quests of ", "")
    clean = re.sub(r'[\\/*?:"<>|]', "", name).strip()
    return clean[:100] 

def get_category_members(category_name):
    """Asks the API for everything in a category."""
    print(f"   Scanning root: {category_name}...")
    members = []
    params = {
        "action": "query",
        "list": "categorymembers",
        "cmtitle": category_name,
        "cmlimit": "max",
        "format": "json"
    }
    
    while True:
        try:
            response = requests.get(BASE_URL, params=params, headers=HEADERS)
            data = response.json()
            members.extend(data['query']['categorymembers'])
            if 'continue' in data:
                params.update(data['continue'])
            else:
                break
        except Exception as e:
            print(f"Error fetching category: {e}")
            logging.error(f"Error fetching category {category_name}: {e}")
            break
            
    return members

def get_batched_content(page_ids):
    """Fetches text for up to 50 Page IDs."""
    if not page_ids:
        return {}

    ids_string = "|".join(str(pid) for pid in page_ids)
    params = {
        "action": "query",
        "prop": "revisions",
        "rvprop": "content",
        "pageids": ids_string,
        "format": "json"
    }
    
    retries = 0
    max_retries = 5
    
    while retries < max_retries:
        try:
            response = requests.post(BASE_URL, data=params, headers=HEADERS)
            
            if response.status_code == 429:
                wait_time = (2 ** retries) * 5
                print(f"    [!] Server throttle (429). Sleeping {wait_time}s...")
                time.sleep(wait_time)
                retries += 1
                continue
            
            data = response.json()
            pages = data.get('query', {}).get('pages', {})
            results = {}
            
            for pid, page_data in pages.items():
                if 'revisions' in page_data:
                    results[page_data['title']] = page_data['revisions'][0]['*']
            
            return results

        except Exception as e:
            print(f"Error in batch: {e}")
            logging.error(f"Batch Error: {e}")
            return {}
            
    print("    [!!!] Max retries exceeded. Skipping batch.")
    return {}

def process_zone(zone_cat_title):
    """Downloads all quests in a specific Zone/Category."""
    folder_name = clean_filename(zone_cat_title)
    
    try:
        zone_path = os.path.join(OUTPUT_DIR, folder_name)
        os.makedirs(zone_path, exist_ok=True)
        
        # 1. Get all quests in this sub-category
        members = get_category_members(zone_cat_title)
        quest_pages = [m for m in members if m['ns'] == 0] 
        
        if not quest_pages:
            return 

        # 2. SMART FILTER: Remove quests we already have (if user selected Update)
        if SKIP_EXISTING:
            original_count = len(quest_pages)
            quest_pages = [
                q for q in quest_pages 
                if not os.path.exists(os.path.join(zone_path, f"{clean_filename(q['title'])}.md"))
            ]
            skipped_count = original_count - len(quest_pages)
            if skipped_count > 0:
                print(f"   [SKIPPED] {skipped_count} quests already exist.")

        if not quest_pages:
            print(f"   [COMPLETE] All quests in {folder_name} are up to date.")
            return

        print(f"\n[DOWNLOADING] {folder_name} ({len(quest_pages)} new quests)")

        # 3. Download the remaining ones
        for i in range(0, len(quest_pages), BATCH_SIZE):
            batch = quest_pages[i:i + BATCH_SIZE]
            batch_ids = [p['pageid'] for p in batch]
            
            contents = get_batched_content(batch_ids)
            
            for title, content in contents.items():
                try:
                    filename = os.path.join(zone_path, f"{clean_filename(title)}.md")
                    with open(filename, "w", encoding="utf-8") as f:
                        f.write(f"# {title}\n\n{content}")
                except Exception as e:
                    print(f"    [SKIP] Failed to write '{title}': {e}")
                    logging.error(f"Write error for {title}: {e}")
            
            print(f"    Saved batch {i} to {i+len(batch)}...")
            time.sleep(DELAY)
            
    except Exception as e:
        print(f"CRITICAL ERROR IN ZONE {folder_name}: {e}")
        logging.error(f"Zone failure {folder_name}: {e}")

def main():
    global SKIP_EXISTING
    try:
        print("--- STARTING THE ORACLE ARCHIVE v5.0 ---")
        
        # CHECK FOR EXISTING DATA
        if os.path.exists(OUTPUT_DIR) and os.listdir(OUTPUT_DIR):
            print("\n[!] Existing archive data found.")
            print("    [O]verwrite - Re-download everything (Updates text)")
            print("    [U]pdate    - Only download missing quests (Resumes crash)")
            choice = input("Select mode (O/U): ").lower().strip()
            
            if choice == 'u':
                SKIP_EXISTING = True
                print(">>> UPDATE MODE: Skipping existing files.")
            else:
                SKIP_EXISTING = False
                print(">>> OVERWRITE MODE: Downloading fresh copies.")
        else:
            os.makedirs(OUTPUT_DIR, exist_ok=True)

        # Loop through ALL the root categories
        for root in ROOT_CATEGORIES:
            print(f"\n>>> PROCESSING ROOT: {root}")
            subcats = get_category_members(root)
            
            for sub in subcats:
                if sub['ns'] == 14: 
                    process_zone(sub['title'])
                
    except Exception as e:
        print(f"\n!!! FATAL SCRIPT CRASH !!!\nError: {e}")
        logging.critical(f"Fatal Crash: {e}", exc_info=True)

if __name__ == "__main__":
    main()
    print("\n\nJob's done! (See crash_log.txt for errors)")
    input("Press Enter to close this window...")