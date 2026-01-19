# CLUCK!

{{For|the pet battle ability|Cluck}}
{{Questbox
 | id = 3861
 | name = CLUCK!
 | faction = Neutral
 | category = Special
 | level = {{Level|full}}
 | levelreq = 1
 | start = [[Chicken]]
 | shareable = Yes
 | repeatable = Yes
 | experience = 5
 | rewards = [[Chicken Egg]]
}}

'''CLUCK!''' is a quest that allows you to obtain [[Chicken Egg]], which teaches you how to summon the Westfall Chicken [[companion]]. Any [[chicken]] critter has a small chance of offering you the quest when you use the <code>/chicken</code> (or <code>/flap</code>) emote while it is targeted.

The chicken will emote the following whenever the quest is available.
*{{text|emote|Chicken looks up at you quizzically. Maybe you should inspect it?}}

==Objectives==
Find some [[Special Chicken Feed]] and return to your befriended [[chicken]].

==Description==
"Cluck... cluck... cluck... BACAW!

Cluck... cluck... cluck."

The chicken looks up at you and then starts to scratch its claws into the ground. You think it is spelling out a word, but you are not sure what it is. Could it be... S-A-L-D-E-A-N? Before you can ask, the chicken turns away and goes about its business.

==Rewards==
You will receive:
*5 [[XP]]

==Progress==
The chicken stares at you with dark, cold eyes. It waits for you hungrily.

"BACAAAW!

Cluck...cluck...cluck."

==Completion==
"BACAW!!!"

The chicken starts to gobble up the feed you put down.

After a moment, the chicken looks around, startled. It uncomfortably shuffles back and forth. Is this chicken pregnant? You think you better check underneath it.

==Loot==
After completing the quest a [[Farm Chicken Egg]] will appear, which can be looted for a [[Chicken Egg]] - [[Westfall Chicken]] [[small pet]]. 
*Everyone will be able to loot the egg, even if they haven't done the quest. <!-- "or have already completed the quest." - this may no longer be true. The client has blocked me from obtaining a PoB pet I already knew how to summon; may be the same for this chicken. -->
*The egg disappears after it is looted. This means that only one character can loot it.
*With patch 3.1.0 this quest is also available to Horde characters.

==Walkthrough==
Note: It may be convenient to buy the [[Special Chicken Feed]] before initiating the quest. 
#Find and target (left click) a [[chicken]]. These are found around human settlements. You do not have to do the quest in Westfall.
#Repeatedly use the <code>/chicken</code> (or <code>/flap</code>) emote while the chicken is targetted. Creating a simple [[macro]] helps.
#The chicken will eventually emote "Chicken looks up at you quizzically. Maybe you should inspect it?" At this point, it will turn friendly and offer the CLUCK! quest. You might not see the {{Queststart}} unless you are [[tracking]] Low Level Quests on your minimap. Any nearby character can get the quest for the brief time that the chicken is friendly and offering the quest.
#Quickly accept the quest, then acquire some [[Special Chicken Feed]] from {{NPC|Alliance|Farmer Saldean}} in [[Westfall]] or {{NPC|Horde|William Saldean}} in [[Brill]] if you have not done so already.
#Find a chicken (it does not have to be the original one) and <code>/cheer</code> at it. It will emote "Chicken looks at you expectantly" and let you turn in the quest.
#After you have completed the quest the chicken will lay a [[Farm Chicken Egg]], which you can loot for [[Chicken Egg]].

==Notes==
Each <code>/chicken</code> or <code>/flap</code> attempt has a low chance to make the chicken responsive. In the ballpark of fifty to one hundred attempts is typical. 

{{NPC|Alliance|Farmer Saldean}} in [[Westfall]] sells the [[Special Chicken Feed]]. He is the only Alliance [[vendor]] for the feed. The feed is not [[soulbound]] and can be [[mail]]ed to [[alt]]s or sold in the [[auction house]]. {{NPC|Horde|William Saldean}} in [[Brill]] sells the Feed for Horde characters.

It is possible to do this quest multiple times, even if you already have the pet, and it is possible to have several lootable [[Farm Chicken Egg]] spawned simultaneously by completing the quest multiple times in succession. The [[Farm Chicken Egg]]s persist for at least several minutes.<!-- Could be much longer --> You won't derive any particular benefit from extra {{loot|common|Chicken Egg|chicken eggs}}, but you might do this on behalf of others.

The chicken that spawns the [[Farm Chicken Egg]] remains under the egg while the egg is spawned, and does not roam. Looting the egg, causing it to disappear, frees the chicken. If the chicken is killed while it is under the egg, the egg will fade out and disappear, but it can take several seconds. 

The [[Special Chicken Feed]] is a food item that you can eat, and it counts towards [[Tastes Like Chicken]].

In ''[[Classic]]'', [[Horde]] players are able to receive the emote, but the quest is not offered as it has been added for Horde players in ''[[Wrath of the Lich King]]''.

The quest is shareable so players have jokingly shared it in cases where players may ask for a weekly quest to be shared (such as the weekly [[Timewalking]] quest).

==Macro==
A macro is strongly recommended for completing this quest in a short amount of time. Creating the above-described macro with 255 lines of /chicken or /flap is the most effective and often allows only doing the macro once before it procs. However, for some users this creates an error or lag which will disconnect them or they will miss the opportunity to accept the quest.

This macro will do the chicken emote 50 times:
: /run for i = 1, 50 do DoEmote("CHICKEN") end

==Patch changes==
*{{Patch 3.1.0|note=Horde can now complete this quest.}}

==See also==
*The [[Chicken Egg]] article was the source for the macros.

==External links==
{{Elinks-quest|3861}}

[[Category:Westfall quests]]