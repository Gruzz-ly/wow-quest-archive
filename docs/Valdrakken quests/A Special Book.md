# A Special Book

{{Questbox
|name=A Special Book
|start=[[Bobby Carlisle]] {{co|47.9|46.8|Valdrakken}}
|level={{level|df}}
|category=Valdrakken
|rewards=[[Kirin Tor Contact's Note]]
|previous=[[A Proper Burial]]
|next=[[A Legacy of Secrets]]
|id=77865
}}
{{WorldEvent/Secrets of Azeroth|quest}}

'''A Special Book''' begins the eleventh day of [[Secrets of Azeroth]] activities.

==Completion==
Well, if it isn't my trusty investigator. 

There's a contact in the [[Kirin Tor]] who owes me a favor. They gave me a tip about a book in [[Karazhan]] that might help us decipher those tablets you recovered. You know, the ones from [[Unveiled Tablet Rubbing|the Azure Span]] and [[Incomplete Tablet|Shifting Sands]]?

But we both know you're the one with the securing skills here. Here's the note my contact left. Should help you find the book!

==Rewards==
You will receive:
*[[Kirin Tor Contact's Note]]

==Notes==
[[File:Secrets - Karazhan starting point.jpg|thumb|The starting point in Karazhan]]

The note reads:
{{:Kirin Tor Contact's Note}}

Head to the [[Karazhan (raid)|Karazhan]] raid entrance via the front door at {{co|46.9|74.8|Deadwind Pass}} in [[Deadwind Pass]], and clear to the [[Guardian's Library]] by defeating [[Moroes (tactics)|Moroes]], the [[Opera event]], and [[The Curator]].

For a more detailed walk-through: enter the front door, head through the [[Gatehouse]] and go upstairs to the north to reach the [[Grand Ballroom]]. Take a left to enter the [[Banquet Hall]] and defeat Moroes. Return to the Grand Ballroom and exit to the northeast to get upstairs. Head west to enter the [[Opera Hall]], and take a right and travel along the north side of the room to get down to the orchestra pit and backstage. Speak with [[Barnes]] to start the Opera event.

Once done, exit to the south, and head upstairs through the mezzanine and balcony layers of the opera hall. On the balcony layer, take the exit to the southeast, jump down the stairs, and take the ramp at the southern end of the next room clockwise uphill to the north, then follow the path through the [[Master's Terrace]] and the [[Broken Stair]] to get to the [[Menagerie (Karazhan)|Menagerie]] and the Curator encounter.

After turning the corner to the Guardian's Library, stand in the square at the base of the ramp (at roughly {{co|48|48|Karazhan|8}}), reset the [[Tricked-Out Thinking Cap]] to (0, 0), equip the [[Idol of Ohn'ahra]], then head west to (-12, -1).

Note that the [[Mana Feeder]]s are immune to magic, so melee damage is required to defeat them.

At (-12, -1) (or roughly {{co|32|49|Karazhan|8}}), find an [[Ancient Tome (Karazhan)|Ancient Tome]] on the middle shelf of a bookshelf. It reads:
{{book|content=A note inside the book reads, "Re-shelved Tyr's Legacy in the titan section (3, 6)."}}

<gallery mode="packed" caption="Book one">
File:Secrets - Karazhan book one.jpg|Book one, middle shelf, middle book, on top of the other angled book
File:Ancient Tome (Karazhan).png|Book one close-up
</gallery>

The thinking cap does not reset, so re-equip it, then navigate to (3, 6) (or roughly {{co|36.8|37.4|Karazhan|8}}) on the leftmost booskelf on the north wall, second shelf from the bottom, second book from the right, is the second Ancient Tome, which reads:

{{book|content=A note inside this book reads, "Re-shelved Tyr's Legacy in the Guardian's of Tirisfal section (8, -14)."}}

<gallery mode="packed" caption="Book two">
File:Secrets - Karazhan book two.jpg|Book two, left bookshelf, second from bottom, second from right
File:Ancient Tome - Red (Karazhan).png|Book two close-up
</gallery>

Head that direction (at roughly {{co|47.3|64.4|Karazhan|8}}) on the bookshelf in the corner, third shelf from the bottom, second book from the left, is the third Ancient Tome that reads:

{{book|content=A note inside this book reads, "This must stay with the other records of the Dragon Isles. However, it should be shelved under U for its original name of Uldorus, not Tyrhold (-11, 7)."
}}

<gallery mode="packed" caption="Book three">
File:Secrets - Karazhan book three.jpg|Book three, left bookshelf, third from bottom, second from left
File:Ancient Tome - Green (Karazhan).png|Book three close-up
</gallery>

Return to the area where the first book was (at roughly {{co|33.1|51.4|Karazhan|8}}) to locate in the bookshelf closest to the corner, on the second shelf from the bottom, horizontally over the first two books from the left, a copy of [[Tyr's Legacy]], which starts [[A Legacy of Secrets]].

<gallery mode="packed" caption="Book four: Tyr's Legacy">
File:Secrets - Karazhan Tyr's Legacy.jpg|Tyr's Legacy, right bookshelf, second from bottom, horizontal over the first two from left
File:Tyr's Legacy.png|Tyr's Legacy close-up
</gallery>

{{Zone Map|zone=Karazhan|section=8|notes=
{{Zone Map Note|48|48|0|Starting position}}
{{Zone Map Note|32|49|1|First book}}
{{Zone Map Note|36.8|37.4|2|Second book}}
{{Zone Map Note|47.3|64.4|3|Third book}}
{{Zone Map Note|33.1|51.4|4|Tyr's Legacy}}
}}

{| class="darktable zebra"
|-
! Book !! Coords !! Quest
|-
! 1
| {{co|32|49|Karazhan|8}} || 78050
|-
! 2
| {{co|36.8|37.4|Karazhan|8}} || 78051
|-
! 3
| {{co|47.3|64.4|Karazhan|8}} || 78052
|-
! 4
| {{co|33.1|51.4|Karazhan|8}} || n/a
|}

To check which books have been read, copy and paste this command into the chat window:

<code>/run local i,q=0;for q=78050,78052 do i=i+1;print('Book '..i..': '..(C_QuestLog.IsQuestFlaggedCompleted(q) and 'YES' or 'NO')) end </code>

==Progression==
{{Secrets of Azeroth}}

==Patch changes==
*{{Patch 10.1.5|note=Added.}}

==External links==
{{Elinks-quest|77897}}