# Securing an Artifact

{{Questbox
|name=Securing an Artifact
|start=[[Tithris]] {{co|47.4|46.6|Valdrakken}}
|level={{level|df}}
|category=Valdrakken
|previous=[[Preservationist Cleared]]
|rewards=[[Preservationist's Dispatch]]
|next=[[Artifact Secured]]
|id=77281
}}
{{WorldEvent/Secrets of Azeroth|quest}}
[[File:Life-Binder Conservatory inn building.jpg|thumb|The inn of the [[Life-Binder Conservatory]] in the [[Waking Shores]], bounded by lava]]

'''Securing an Artifact''' begins the fourth day of [[Secrets of Azeroth]] activities.

==Completion==
One of [[Preservationist Kathos|the Preservationist's]] colleagues left this note.  

It says the [[Primalists]] are threatening the [[Life-Binder Conservatory]] and an important artifact is at risk. I need you to locate and secure it before the looters do. 

The coordinates on the note should work with that funny looking "[[Tricked-Out Thinking Cap|Thinking Cap]]" you have.

==Rewards==
You will receive:
*[[Preservationist's Dispatch]]

==Notes==
The dispatch reads:

{{:Preservationist's Dispatch}}

[[File:Ancient Lever (Waking Shores).png|thumb|upright|An [[Ancient Lever (Waking Shores)|Ancient Lever]] at [[Life-Binder Conservatory]]]]
The [[Life-Binder Conservatory]] is west of [[Scalecracker Keep]] in northeastern [[Waking Shores]]. Enter the big inn building and head to {{co|54.7|20.4|Waking Shores}} to find the hearth. Reset the [[Tricked-Out Thinking Cap]] to (0, 0) then navigate using cogs-bolts to find the three [[Ancient Lever (Waking Shores)|Ancient Levers]]:

{|class="darktable zebra"
|+Ancient Lever locations
! # !! Cogs-Bolts !! Coords !! QuestID
|-
! 1
| (15, -1) || {{co|56.6|20.3|Waking Shores}} || 77401
|-
! 2
| (24, -18) || {{co|57.7|23.8|Waking Shores}} || 77402
|-
! 3
| (19, -27) || {{co|57.1|25.6|Waking Shores}} || 77403
|}

To check whether the levers were pulled, copy and paste this command into chat:

<code>/run local i,q=0;for q=77401,77403 do i=i+1;print('Lever '..i..': '..(C_QuestLog.IsQuestFlaggedCompleted(q) and 'YES' or 'NO')) end </code>

[[File:Torch of Pyrreth.png|thumb|upright|The [[Torch of Pyrreth (item)]] in the hearth]]
After pulling all three levers, return to the inn. Inside the hearth on the left wall of the fireplace at {{co|54.6|20.4|Waking Shores}} is the [[Torch of Pyrreth (item)]], which immediately starts the [[Artifact Secured]] quest.

{{Zone Map|zone=Waking Shores|notes=
{{Zone Map Note|54.7|20.4|Ping|Hearth/Torch}}
{{Zone Map Note|56.6|20.3|1|Lever #1}}
{{Zone Map Note|57.7|23.8|2|Lever #2}}
{{Zone Map Note|57.1|25.6|3|Lever #3}}
}}

==Progression==
{{Secrets of Azeroth}}

==Patch changes==
*{{Patch 10.1.5|note=Added.}}

==External links==
{{Elinks-quest|77281}}