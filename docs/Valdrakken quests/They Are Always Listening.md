# They Are Always Listening

{{Questbox
|name=They Are Always Listening
|start=[[Bobby Carlisle]] {{co|47.9|46.8|Valdrakken}}
|end=[[Fangli Hoot]] {{co|26.7|53.9|Valdrakken}}
|finish=[[Fangli Hoot]]
|level={{level|df}}
|category=Valdrakken
|rewards=[[Great Places to Visit in Valdrakken]]
|previous=[[A Proper Burial]]
|next=[[A Complete Inventory]]
|id=77928
}}
{{WorldEvent/Secrets of Azeroth|quest}}

'''They Are Always Listening''' begins the twelfth day of [[Secrets of Azeroth]] activities.

==Objectives==
Speak with [[Fangli Hoot]] near the [[Valdrakken]] barber shop.

==Description==
Remember my contact, Fangli Hoot? Seems she has another theory about the one behind these artifact thefts.

I'm a bit weary after the last tip went nowhere, but we can't turn down a lead. Journalistic integrity demands we at least hear her out.

You'll find her by the barber shop.

==Rewards==
You will receive:
*[[Great Places to Visit in Valdrakken]]

==Completion==
Ok, this time I'm sure. I tracked everyone, yes everyone, even you.

[[Tithris]] is behind everything. He's been meeting with shady characters all over the city to secure supplies for something big. My guess is an expedition. 

You need to investigate several caches of his purchases. I noted coordinates for the general locations. Put that thinking cap to work! And that idol of yours can help you narrow in on their exact location.

==Notes==
The notes read:

{{:Great Places to Visit in Valdrakken}}

From the fountain at {{co|49.4|57.9|Valdrakken}} in front of the [[Seat of the Aspects]], equip the [[Idol of Ohn'ahra]] and reset the [[Tricked-Out Thinking Cap]] to (0, 0), then navigate to (-8, -4) to find the [[Auction House Bill of Sale]] at {{co|44.2|60.4|Valdrakken}} on a barrel to the left of the Auction House entrance. It reads:

{{book|content=The auction house tag reads, "Bedding and travel trunks. Winner - Tithris, Roasted Ram Inn."}}

Head east to the [[Engine of Innovation]] and reset the cap at {{co|83.9|52.8|Valdrakken}} in front of the device, then navigate to (-14, -4) to find a [[Void Storage Receipt]] by the [[Void Storage]] and [[Transmogrifier]] ethereals at {{co|74.0|57.5|Valdrakken}} which reads:

{{book|content=The note reads, "Tithris - Innkeeper - Roasted Ram. Books and personal items removed from void storage. Hold for pickup."}}

Head to the [[Ruby Feast]] at {{co|61.1|10.8|Valdrakken}} at the tea table, reset the cap, then navigate to (-12, -17) to find a [[Garden Supply Receipt]] on a barrel at {{co|53.0|28.5|Valdrakken}} by the two [[Quarreling Gardener]]s that reads:

{{book|content=The note reads, "Deliver to Roasted Ram Inn. Replacement garden tools, maintenance items, and expedition supplies for an Adventurers Night Party."}}

Head to {{co|48.5|13.9|Valdrakken}} northeast of the [[Sapphire Enclave]] to find [[Noah Scribeson]] in front of a bunch of magicked candles and reset the thinking cap there. Find the [[Researcher's Note]] at {{co|37.6|37.2|Valdrakken}} on some books in the southwest corner of the room with [[Rethelshi]], [[Ezra]], and [[Mythressa]] that reads:

{{book|content=The note reads, "Copied titan volumes for Roasted Ram reading room."}}

Head to the sandbox at {{co|13.2|63.2|Valdrakken}} on the south side of [[Little Scales Daycare]] and reset the thinking cap, then navigate to (27, -7) behind the General Goods store in the [[Artisan's Market]] to find the [[Hastily Scrawled Note (Valdrakken)|Hastily Scrawled Note]] at {{co|31.6|70.3|Valdrakken}} on some crates that reads:

{{book|content=A scrawled note reads, "Tithris' last minute requests. Salted argali, dried thresher, and tallstrider jerky. There must have been a run on his adventurer's packs. A reminder that I need to charge him extra for the additional bribe since my regular guard contact was not on duty. -N."}}

Head to the [[Roasted Ram]] inn and <code>/bow</code> or <code>/kneel</code> before the [[Odd Statue]] to reach the [[Dragon's Hoard]] downstairs. Equip the [[Idol of Ohn'ahra]] and follow it to the northwest corner to find the [[Note to Kritha]] on some crates at {{co|46.0|41.4|Valdrakken}} that reads:

{{book|content=The note reads, "Kritha, these canteens are for our Adventurers Night Party. - Tithris."
}}

Reading the last note causes players to create the [[Compiled Report]], which starts [[A Complete Inventory]].

<gallery mode="packed">
File:Auction House Bill of Sale.jpg|[[Auction House Bill of Sale]]
File:Void Storage Receipt.jpg|[[Void Storage Receipt]]
File:Garden Supply Receipt.jpg|[[Garden Supply Receipt]]
File:Researcher's Note.jpg|[[Researcher's Note]]
File:Hastily Scrawled Note Valdrakken.jpg|[[Hastily Scrawled Note (Valdrakken)|Hastily Scrawled Note]]
File:Note to Kritha.jpg|[[Note to Kritha]]
</gallery>

{|class="darktable zebra"
|+Valdrakken notes
! # !! Coords !! Location !! Note !! Quest
|-
! 1
| {{co|44.2|60.4|Valdrakken}} || Auction house || [[Auction House Bill of Sale]] || 78053
|-
! 2
| {{co|74.0|57.5|Valdrakken}} || Transmogrifier || [[Void Storage Receipt]] || 78054
|-
! 3
| {{co|53.0|28.5|Valdrakken}} || [[Ruby Enclave]] || [[Garden Supply Receipt]] || 78055
|-
! 4
| {{co|37.6|37.2|Valdrakken}} || [[Sapphire Enclave]] || [[Researcher's Note]] || 78056
|-
! 5
| {{co|31.6|70.3|Valdrakken}} || [[Artisan's Market]] || [[Hastily Scrawled Note (Valdrakken)|Hastily Scrawled Note]] || 78057
|-
! 6
| {{co|46.0|41.4|Valdrakken}} || [[Dragon's Hoard]] || [[Note to Kritha]] || 78058
|}

To check which notes have been read, copy and paste this command into the chat window:

<code>/run local i,q=0;for q=78053,78058 do i=i+1;print('Note '..i..': '..(C_QuestLog.IsQuestFlaggedCompleted(q) and 'YES' or 'NO')) end </code>

{{Zone Map|zone=Valdrakken|notes=
{{Zone Map Note|44.2|60.4|1|Auction House Bill of Sale|link=Auction House Bill of Sale}}
{{Zone Map Note|74.0|57.5|2|Void Storage Receipt|link=Void Storage Receipt}}
{{Zone Map Note|53.0|28.5|3|Garden Supply Receipt|link=Garden Supply Receipt}}
{{Zone Map Note|37.6|37.2|4|Researcher's Note|link=Researcher's Note}}
{{Zone Map Note|31.6|70.3|5|Hastily Scrawled Note|link=Hastily Scrawled Note (Valdrakken)}}
{{Zone Map Note|46.0|41.4|6|Note to Kritha|link=Note to Kritha}}
}}

==Progression==
{{Secrets of Azeroth}}

==Patch changes==
*{{hotfix|date=2023-09-13|note=On the secret day starting with "They Are Always Listening", you should now get the quest "[[A Complete Inventory]]" from [[Fangli Hoot]] if you do not get it automatically by investigating all 6 notes.}}
*{{Patch 10.1.5|note=Added.}}

==External links==
{{Elinks-quest|77928}}