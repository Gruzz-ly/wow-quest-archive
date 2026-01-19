# License Not Required

{{Questbox
 | id = 86618
 | name = License Not Required
 | category = Undermine
 | level = {{level|tww-max}}
 | levelreq = {{level|tww-max}}
 | type = Important Quest
 | start = [[Nanny Talullah]] {{co|47.4|48.9|Undermine}}
 | experience = 12,200
 | rewards = [[G-99 Breakneck]]
 | money = {{cost|23|40|}}
 | shareable = No
 | previous = [[No More Walkin' Here]]
}}

==Objectives==
Learn how to drive the [[G-99 Breakneck]].
* Talk to [[Nanny Talullah]]
* Get in the G-99 Breakneck
* Use the escape chains to reach the streets of Undermine (Optional)
* Drive around Undermine (0/100%)
* Reach the D.R.I.V.E.
* Exit the G-99 Breakneck and install a turbo at the D.R.I.V.E.
* Get back in the G-99 Breakneck and activate your boost
* Regain boost meter by drifting (30)
* Get a job from Nanny Talullah
* Complete your job from Nanny Talullah

==Description==
Alright. Before you go out and run somebody over let's make sure you know how to do it properly.

We'll introduce you to the car, the D.R.I.V.E. service we offer, and how to drive it in style.

==Rewards==
You will receive:
* [[G-99 Breakneck]]
* {{cost|23|40|}}
* 12,200 [[XP]]

==Progress==
Just put your foot on the pedal and the rest will come naturally.

==Completion==
Great job out there! Now these vehicles don't come with insurance so if you get into any trouble you're gonna have to solve it yourself.

==Notes==
Speak with Nanny again:
{{dialogue|Driving's easy, toots. Just look where you wanna go and hold the pedal.

{{gossip|quest=|<Take the keys to the G-99 Breakneck.>}}<br>
{{gossip|quest=|<Skip tutorial.>}}
}}

Either option adds the [[G-99 Breakneck]] to the zone action button. Drag it to an action bar, as it's not a mount, or use a macro like this:

<syntaxhighlight lang="lua">
#showtooltip
/run UIErrorsFrame:SuppressMessagesThisFrame() 
/cast G-99 Breakneck
/run C_MountJournal.SummonByID(0)
/stopcasting
</syntaxhighlight>

Down on ground level, hop in to enter the vehicle interface:

#{{abilities|Boost}}
#{{abilities|Honk the Horn!}}
#&nbsp;
#&nbsp;
#{{abilities|Start Job}}
#{{abilities|Eject!}}

Drive around to fill the bar and get a feel for the vehicle. Once it hits 100%, a green arrow will appear over the vehicle, aiming at [[Shipping and Handling (subzone)|Shipping and Handling]]. Exit the vehicle and speak with [[Mobber]]:

{{dialogue|Need some tuning?

{{gossip|<Access D.R.I.V.E.>}}<br>
{{gossip|Can I find more parts for my car?}}

Of course youse can. Lotsa folks are looking to sell stuff, and sometimes youse can even find nice stuff in the trash. Bring it here and I'll put it in.}}

Access the D.R.I.V.E. interface and install the turbo (fourth button down). If the default engine is too fast, use the second option from the top to swap.

After installing the turbo, reenter the vehicle:
:Holding spacebar while turning lets you drift. Drifting recovers your turbo meter.

Hit 1 to Turbo, then hold space while turning to refill the drift meter. After refilling 30 drift points, the #5 option lights up:
:Get your first job from Nanny Talullah. You can also cancel jobs and pick up new ones.
:{{text|say|Nanny Talullah|Time to work, sugar. Ready, set, go!}}

This pops up a random [[Shipping and Handling]] task. Use the green arrow to head to the location. Complete the task, then return to Nanny to turn in.

==Progression==
{{Undermine Awaits}}

==Patch changes==
* {{Patch 11.1.0|note=Added.}}

==External links==
{{Elinks-quest|86618}}