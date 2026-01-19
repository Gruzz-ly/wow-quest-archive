# Maelie, The Wanderer

{{for|the cloudrunner|Maelie the Wanderer}}
{{Questbox
 | id = 64292
 | name = Maelie, The Wanderer
 | category = Korthia
 | faction = Neutral
 | level = {{level|sl-max}}
 | levelreq = {{level|sl-max}}
 | start = [[Tinybell]] {{co|60.7|21.9|Korthia}}
 | rewards = [[Reins of the Wanderer]]
}}

[[File:Maelie the Wanderer.jpg|thumb|[[Maelie the Wanderer]]]]
'''Maelie, The Wanderer''' is offered by [[Tinybell]] to players who have found [[Maelie the Wanderer]] in her six different locations in [[Korthia]] across different days.

==Objectives==
Accept responsibility for [[Maelie the Wanderer|Maelie]].

==Description==
I can't thank you enough for finding Maelie! You know, I think she's just a little bit more than I can handle.

Would you mind watching over her? I think she's really taken a liking to you!

==Rewards==
You will receive:
*[[Reins of the Wanderer]]

==Completion==
Take care of Maelie, Maw Walker.

==Tracking macro==
To check whether Maelie has been found, copy and paste this into the chat window:

<code>/run local i,c=0,{{api|C_QuestLog.IsQuestFlaggedCompleted}};for q=64293,64299 do if q~=64298 then i=i+(c(q)and 1 or 0)end end;print('Tinybell '..(c(64298)and 'is NOT'or'is')..' looking for Maelie now. You have found Maelie '..i..' of 6 times.')</code>

==Patch changes==
* {{Patch 9.1.0|note=Added.}}

==External links==
{{Elinks-quest|64292}}