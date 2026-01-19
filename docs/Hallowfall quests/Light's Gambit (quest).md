# Light's Gambit (quest)

{{Questbox
 | id = 79168
 | name = Light's Gambit
 | image = Light's Gambit - Faerin and Anduin.jpg
 | imagecaption = Faerin and Anduin at the Light's Gambit board
 | category = Hallowfall
 | level = {{Level|Tww-max}}
 | levelreq = {{Level|Tww-max}}
 | start = [[Faerin Lothar]]{{Co|43.17|52.35|Hallowfall}}
 | end = [[Anduin Wrynn]]{{Co|43.18|52.43|Hallowfall}}
 | money = {{cost|23|40}}
 | experience = 12,200
 | reputation = +500 [[Hallowfall Arathi]]
 | rewards = [[Commemorative Light's Gambit Championship Signet]]<br>10x [[Valorstones]]
 | previous = [[Crowdsourcing]]
}}

'''Light's Gambit''' completes the optional "Rest at Last" chapter of the [[Hallowfall storyline]]. Completing it unlocks the [[Light's Gambit]] minigame and [[Light's Gambit (world quest)|corresponding world quest]].

==Objectives==
Grab the castle piece to start a game of [[Light's Gambit]] with [[Faerin Lothar|Faerin]] and [[Anduin Wrynn|Anduin]].
* Light's Gambit played
* Stay a while and chat (Optional)

==Description==
It's fine! We can catch you up on the rest of the rules later!

Resolving combat is the most fun, anyway!

You and Anduin can team up against me. Perhaps with the both of you together, you'll stand a chance!

<Faerin laughs.>

==Rewards==
You will receive:
*[[Commemorative Light's Gambit Championship Signet]]
*{{cost|23|40}}
*12,200 [[XP]]
*10x [[Valorstones]]
*+500 reputation with [[Hallowfall Arathi]]

==Completion==
I hope you found that relaxing, too, <name>. I didn't realize how much we all needed a break.

==Notes==
===Light's Gambit===
[[File:Light's Gambit.jpg|thumb|The Light's Gambit game in progress.]]
On accept:
:{{Text|say|Faerin Lothar|Sit down, join us! Grab that castle piece when you're ready to play.}}
:{{Text|say|Anduin Wrynn|It's a good game so far, <name>. I think you'll like it.}}

Faerin's dialogue:
{{Dialogue|Light's Gambit is full of interesting decisions. Will you hold your cleric back to protect your castle? Or send it forward to heal your knight?

There are other encounters, too. Different situations call for different strategies... though I personally think you can't go wrong by just blasting your enemy to bits as quickly as possible, in every situation!}}

Anduin's dialogue:
{{Dialogue|I can't remember the last time I did something as simple as... playing a game. Can you?}}

There is an empty chair between Faerin and Anduin if the player prefers to sit. Interact with the castle piece labeled "Light's Gambit" to enter the minigame's vehicle interface.
:{{Text|say|Faerin Lothar|It's your team against my one unit! Easy! You win by getting my unit's health to zero. I win by getting each of your unit's health to zero.}}
:{{Text|say|Faerin Lothar|Look carefully at each of your unit's abilities! Don't worry, I won't start until you make your first move.}}
:{{Text|say|Faerin Lothar|Your castle has a powerful ranged attack, but it can't move. The other two can move and have both ranged and melee abilities.}}
:{{Text|say|Faerin Lothar|Try using an ability!}}

Faerin has a single Enemy Castle, while the player has a Castle, a Knight, and a Cleric. The player can switch between pieces by clicking on them or using their Switch Piece ability.
:{{Abilities|Switch Piece|id=436222|Switch control to another game piece with the lowest cooldown.<br>Pieces can also be switched by clicking on the piece itself.|range=4|icon=ability_paladin_handoflight}}

;Castle
:{{Abilities|Cannon Fire!|id=431255|Shoot a cannon, heavily damaging enemy units in a targeted area.|range=3|cd=13 sec|icon=ability_vehicle_demolisherflamecatapult}}

;Knight
:{{Abilities|Move|id=431087|Move to a targeted location within the game board.|range=1|cd=6 sec|icon=petbattle_speed}}
:{{Abilities|Divine Explosion|id=436051|Conjure a burst of holy power to deal damage to enemies nearby.|range=3|cd=6 sec|icon=spell_holy_surgeoflight}}
:{{Abilities|Holy Assault|id=436060|Charge to a targeted location, damaging enemies at your destination.|range=1|cd=6 sec|icon=ability_warrior_victoryrush}}

;Cleric
:{{Abilities|Move|id=431087|Move to a targeted location within the game board.|range=1|cd=6 sec|icon=petbattle_speed}}
:{{Abilities|Heal|id=436084|Conjure a wave of light, healing nearby allies.|range=3|cd=8 sec|icon=spell_holy_greaterheal}}
:{{Abilities|Smite|id=436094|Smite an enemy in a targeted area.|range=3|cd=8 sec|icon=spell_holy_holysmite}}

Use any ability to start the game.
:{{Text|say|Faerin Lothar|Each unit can only do one ability, then it has to recharge. While it's recharging, switch to another unit!}}
:{{Text|say|Faerin Lothar|Move your pieces around the board to avoid my attacks and deal your own! The first player to wipe out the other side's team wins! Let's do this!}}

Upon destroying the Enemy Castle, the player automatically exits the game.
:{{Text|bossemote|You won!}}
:{{Text|say|Faerin Lothar|Firecrackers! You got me! That was a good game. You'll be [[Mereldar]]'s new champions before you know it!}}
:{{Text|emote|Faerin suddenly looks away.}}
:{{Text|say|Faerin Lothar|I-- thank you for this. I'm having fun. [[Andari]] would have loved playing with you two.}}
:{{Text|say|Anduin Wrynn|We're still here for you, if you want to talk about it.}}
:{{Text|say|Faerin Lothar|I think... yeah, I think I'd like that.}}

===Dialogue===
After the game, both Faerin and Anduin have an extensive amount of branching dialogue. The player can exit the scene and complete the quest objective at any time by selecting the "{{Gossip|I think it's time we get going.}}" option.

====Faerin Lothar====
{{Dialogue|class=plainlist|Light's Gambit is full of interesting decisions. Will you hold your cleric back to protect your castle? Or send it forward to heal your knight?

There are other encounters, too. Different situations call for different strategies... though I personally think you can't go wrong by just blasting your enemy to bits as quickly as possible, in every situation!

{{Gossip|Do you have family in Hallowfall?}}
{{Dialogue-child|
*{{Text|emote|Faerin chuckles.}}
*{{Text|say|Faerin Lothar|No, [[Lothar|my family]] is still in [[Arathi Empire|the Empire]]. I stowed away on the Expedition because I, too, heard [[Beledar]]'s call. I was never supposed to be here.}}
*{{Text|say|Anduin Wrynn|You left home so young... your parents must be worried sick.}}
*{{Text|say|Faerin Lothar|If my parents had their way, I'd be locked in a library, drafting documents on economics or something.}}
*{{Text|say|Faerin Lothar|I chose this life. My parents never saw me as anything other than a disappointment.}}
*{{Text|say|Anduin Wrynn|... I used to think [[Varian Wrynn|my father]] was just as disappointed in me. By the end... I like to think we finally started to understand each other.}}
*{{Text|say|Anduin Wrynn|I hope you get the same chance, with your family.}}
*{{Text|emote|Faerin smiles ruefully.}}
*{{Text|say|Faerin Lothar|That would require me ever going back.}}
}}

{{Gossip|Which was Andari's favorite figurine?}}
{{Dialogue-child|
*{{Text|say|Faerin Lothar|That one, painted in red! It was the first I tried to paint. It was difficult, given--}}
*{{Text|emote|Faerin waves what remains of her lost arm.}}
*{{Text|say|Faerin Lothar|I lost my arm and eye when our ships arrived in Hallowfall. All I remember is a flash of light, then... I was under something. Screaming.}}
*{{Text|emote|Faerin shudders.}}
*{{Text|say|Faerin Lothar|When I came back to, my arm and eye were gone. I was so unbalanced, I had to lean to walk again, like a child.}}
*{{Text|say|Faerin Lothar|[[General Steelstrike|Steelstrike]] had been the one to dig me out. She said my choice to stow away meant I was a soldier, not a child.}}

{{Dialogue-child|
*{{Gossip|Do you regret stowing away?}} / {{Gossip|Stowing away was a foolish thing to do.}} / {{Gossip|Steelstrike was too harsh on you. I'm sorry.}}
{{Dialogue-child|
*{{Text|say|Faerin Lothar|I don't regret anything. I wanted to live up to Steelstrike's expectations. I refused to be any less than the rest of [[Arathi Army|the army]]. I trained endlessly.}}
*{{Text|say|Faerin Lothar|Andari convinced me to play Light's Gambit to learn strategy. By the time I realized they were actually getting me to rest, I was hooked.}}
*{{Text|emote|Faerin looks fondly at the red painted knight.}}
*{{Text|say|Faerin Lothar|When we lost pieces, I wanted to make new ones. Because of my missing arm, I had to figure out new ways to fight, to eat, to dress myself, even.}}
*{{Text|say|Faerin Lothar|And yet, crafting this tiny game piece with one arm was my greatest challenge yet. Because of Andari, I rose to it not with grim determination, but joy.}}
*{{Text|say|Faerin Lothar|Andari healed me. Not my wounds... not my missing limbs. And not with magic. But something inside. And now, they're gone--}}
*{{Text|emote|Faerin chokes on a sob.}}
{{Dialogue-child|
*{{Gossip|Andari sounds very kind. I'm sorry for your loss.}} / {{Gossip|<Give Faerin a gentle pat on the shoulder.>}} / {{Gossip|<Say nothing.>}}
{{Dialogue-child|
*{{Text|emote|Faerin wipes tears from her eyes.}}
*{{Text|say|Faerin Lothar|Thank you. Thank you both for listening.}}
*{{Text|say|Faerin Lothar|I've fought so hard to be seen as strong. To earn my place. I love my people. But it's hard to let... to let the walls down.}}
*{{Text|say|Anduin Wrynn|You... have to let the walls down eventually. Before they all come crumbling down around you. You don't have to do it alone... be kinder to yourself.}}
*{{Text|emote|Faerin smiles through tears.}}
*{{Text|say|Faerin Lothar|Care to take your own advice?}}
*{{Text|emote|Anduin snorts.}}
*{{Text|say|Anduin Wrynn|I think it was you who [[The Light at the End of the Tunnel|said something like that]] to me, first.}}
*{{Text|say|Anduin Wrynn|Perhaps... we both need to learn to take our own advice.}}
}}
*{{Gossip|Let's talk about something else. {{Text|red|<End current conversation.>}}}}
*{{Gossip|I think it's time we get going. {{Text|red|<Complete quest objective.>}}}}
}}
}}
*{{Gossip|Let's talk about something else. {{Text|red|<End current conversation.>}}}}
*{{Gossip|I think it's time we get going. {{Text|red|<Complete quest objective.>}}}}
}}
{{Gossip|Tell me more about the [[Arathi Empire]].}}
{{Dialogue-child|
*{{Text|say|Faerin Lothar|Vast, powerful, and bathed in the [[Light]]... the Empire is a force to be reckoned with.}}
*{{Text|say|Anduin Wrynn|It sounds like a visit would be an interesting journey.}}
*{{Text|emote|Faerin grimaces.}}
*{{Text|say|Faerin Lothar|To be honest, I'm not sure how kindly the mainland would take to the... variety of peoples you all keep company with.}}
*{{Text|say|Faerin Lothar|Particularly you, <name>, for embracing the darkness as you have.}} ''([[Undead (playable)|Undead]], [[void elf (playable)|void elves]], [[death knight]]s, [[demon hunter]]s, [[Priest#Shadow|Shadow priests]], and [[warlock]]s only)''
*{{Text|say|Faerin Lothar|We in Hallowfall know beggars can't be choosers. We need all the help we can get. And you all have proven to be fine folk. But the Empire is not so... open-minded. Or so desperate.}}
*{{Text|say|Anduin Wrynn|Don't you miss home?}}
*{{Text|emote|Faerin laughs wryly.}}
*{{Text|say|Faerin Lothar|I really, truly thought I would. But I became the person I am under Beledar's Light. This is my home, now.}}
*{{Text|say|Faerin Lothar|And were I to leave, I would much sooner travel the lands you all hail from! This [[Stormwind (kingdom)|Stormwind]] you speak of! If you don't take me someday, I'll go stomping around up there myself!}}
*{{Text|emote|Anduin chuckles.}}
}}
{{Gossip|I think it's time we get going. {{Text|red|<Complete quest objective.>}}
}}
}}
}}

====Anduin Wrynn====
{{Dialogue|class=plainlist|I can't remember the last time I did something as simple as... playing a game. Can you?

{{Gossip|Do you miss [[Stormwind (kingdom)|Stormwind]]?}}
{{Dialogue-child|
*{{Text|say|Anduin Wrynn|Of course. Of course I miss home.}}
*{{Text|say|Faerin Lothar|A new human kingdom... what's it like?}}
*{{Text|say|Anduin Wrynn|Grand. Beautiful. Filled with so many different types of people. I miss the fresh bread at the [[Gilded Rose]]. Magical accidents in the [[Mage Quarter|Mage District]]. The festivals. The people.}}
*{{Text|say|Faerin Lothar|So then why don't you go back?}}
*{{Text|emote|Anduin sighs.}}
*{{Text|say|Anduin Wrynn|I can't. Not yet. Who would want to see what their king has become? No... no.}}
*{{Text|say|Faerin Lothar|Soon. One step at a time.}}
*{{Text|emote|Anduin nods.}}
}}

{{Gossip|You seem to like board games, Anduin.}}
{{Dialogue-child|
*{{Text|emote|Anduin chuckles.}}
*{{Text|say|Anduin Wrynn|[[Varian Wrynn|My father]] would play with me, sometimes. We'd go to the [[War Room|war room]] and he'd let me play with the figures.}}
*{{Text|say|Anduin Wrynn|We made up all sorts of games together. None of them made much sense. But we had fun.}}
*{{Text|say|Faerin Lothar|He sounds like a wonderful father.}}
*{{Text|emote|Anduin smiles ruefully.}}
*{{Text|say|Anduin Wrynn|It was complicated. He did his best. I've spent so long trying to be him. To be the great warrior king that leads the charge. To be the hero everyone wants me to be.}}
*{{Text|say|Anduin Wrynn|Some hero I am. Couldn't save anyone, much less myself.}}

{{Dialogue-child|
*{{Gossip|The tides can turn at any time. Like how you could decimate Faerin's army right now if you use your healer to revive the cavalry next to her knight.}}
{{Dialogue-child|
*{{Text|say|Faerin Lothar|Hey! Don't help him!}}
*{{Text|say|Anduin Wrynn|And here I was trying to figure out how to get my footman forward without losing him! Leaving your knight out in the open, Faerin? Risky.}}
*{{Text|say|Faerin Lothar|You kept ignoring your healer! How was I supposed to resist taking advantage of that?!}}
{{Dialogue-child|
*{{Gossip|That game would have been lost without the healer.}}
{{Dialogue-child|
*{{Text|say|Faerin Lothar|<name> is right. Things can change, if you make the move to change them.}}
*{{Text|say|Faerin Lothar|So what's your move, Anduin?}}
*{{Text|emote|Anduin looks between the two of you for a long moment, then smiles slightly.}}
*{{Text|say|Anduin Wrynn|I'm here, aren't I? Perhaps the move has already been made. But... I will think more on the next one.}}
}}
*{{Gossip|Let's talk about something else. {{Text|red|<End current conversation.>}}}}
*{{Gossip|I think it's time we get going. {{Text|red|<Complete quest objective.>}}
}}
}}
}}
*{{Gossip|Let's talk about something else. {{Text|red|<End current conversation.>}}}}
*{{Gossip|I think it's time we get going. {{Text|red|<Complete quest objective.>}}}}
}}
}}
{{Gossip|[[Wrathion]] has done much since returning to the [[Dragon Isles]]. Have you had any contact?}}
{{Dialogue-child|
*{{Text|say|Anduin Wrynn|He's tried. I've been dodging [[Blacktalon]]s almost as much as [[SI:7]]. I know he just wants to help. Like the others. But what could they say? What could I say?}}
*{{Text|say|Anduin Wrynn|Wrathion had his greatest wish before him in the Dragon Isles. To reunite with [[Black dragonflight|his flight]]. The last thing I would want would be to distract him from that purpose.}}
*{{Text|say|Faerin Lothar|Wait a moment. You're... friends with a dragon?}}
*{{Text|say|Faerin Lothar|A DRAGON?! You're just casually friends with a legendary beast known to scour lands and grant wishes?}} ''(non-dracthyr)'' / {{Text|say|A DRAGON?! I mean, <name> here is clearly draconic, but a full, true, dragon? A legendary beast known to scour lands and grant wishes?}} ''([[Dracthyr (playable)|Dracthyr]] only)''
*{{Text|emote|Anduin blinks, then laughs.}}
*{{Text|say|Anduin Wrynn|I don't think Wrathion would be keen on either of those things. He's self-centered and boastful and... a good friend I should not have neglected for so long.}}
*{{Text|say|Anduin Wrynn|We also often played [[Jihui|a game]] together, much like this. I think this one is even more suited to his tastes. He'd like it.}}
*{{Text|say|Faerin Lothar|Well, then! When you go to apologize, you'll have to introduce me!}}
*{{Text|say|Anduin Wrynn|I'm not sure Stormwind would survive the chaos caused by the two of you in one room.}}
}}
{{Gossip|I think it's time we get going. {{Text|red|<Complete quest objective.>}}}}
}}

===Outro===
[[File:Light's Gambit - end.jpg|thumb|Faerin and Anduin after the end of the conversation.]]
Upon completing the objective, both Faerin and Anduin get to their feet.
:{{Text|say|Faerin Lothar|I should be getting back to my post. Thank you both for this.}}
:{{Text|say|Anduin Wrynn|I think I needed that, too.}}

On completion, they both walk over to the stairs and despawn.
:{{Text|say|Faerin Lothar|You two had better make time to come and play me again.}}
:{{Text|say|Anduin Wrynn|Next time, we could play [[Jihui|the game]] I learned in [[Pandaria]]. Faerin, I think you find its approach to victory as... interesting as Wrathion did.}}
:{{Text|say|Faerin Lothar|I have no idea what that means but I'm excited to find out!}}

==Progression==
{{Rest at Last}}

==Patch changes==
*{{Patch 11.0.2|note=Added.}}

==External links==
{{Elinks-quest|79168}}

[[Category:Hallowfall Arathi quests]]