# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Narrator",color="808080")
define d = Character("Archdruid",color="164622")
define j = Character("Julian",color="#3366cc")
define f = Character("Julian",color="#3366cc")
define g = Character("Goblin",color="60e683")
define u = Character("Demoness")
define x = Character("Unknown Voice",color="652EAF")
define i = Character("Inya",color ="ff5dcf")
define t = Character("Tess",color="eebf00")
define gl = Character("Golem")


image sword = "sword.png"
image shield = "Shield.webp"
image backpack = "backpack.png"
image unlit = "unlit.webp"
image shadow = "shadow.png"
image lit = "lit.webp"
image dog = "dog.png"
image ghost = "ghost.png"
image goblin = "goblin.png"
image druid = "druid.png"
image blackscreen = "blackscreen.jpg"
image coin = "thecoin.png"
image golem = "golem.png"
image adesse = "adessefull.jpg"
image adesse_angry = "adesse_angry.jpg"
image adesse_distant = "adesse_distant.jpg"
image adesse_flirty = "adesse_flirty.jpg"
image adesse_flirty_melancholic = "adesse_flirty_melancholic.jpg"
image adesse_hurt = "adesse_hurt.jpg"
image adesse_neutral = "adesse_neutral.jpg"



transform deadcenter:
    xalign 0.5
    yalign 0.5
define fastdissolve = Dissolve(.8)
transform offleft:
    xalign 0.3
    yalign 0.7
transform offright:
    xalign 1.0
    yalign 0.7

screen inventory_display_toggle:
        zorder 92
        frame:
            background "#9F99"
            xalign 0.05
            yalign 0.1

            textbutton "Inventory":
                action ToggleScreen("inventory_item_description")

        on "hide" action Hide("inventory_item_description")

define longdissolve = Dissolve(3.0)





default item_descriptions = {"key" : "a mysterious key", "bottle" : "it's full of... something", "broom" : "it sweeps. or rather, you do. with it.", "Cholula" : "yum!"}
default inventory_items = []
default item_description = ""

default darkness = 0

style inv_button is frame:
    xsize 200
    ysize 100

style inv_button_text:
    xalign 0.5
    yalign 0.5

screen inventory_item_description:
    # use this based on your preference
    # modal True
    window:
        background "#AAA9"
        xsize 600
        ysize 150
        xalign 0.5
        yalign 0.1
        text item_description:
            xfill True
            yfill True
    
    window:
        background "#99F9"
        xsize 1290
        ysize 600
        xalign 0.5
        yalign 0.7
        hbox:
            box_wrap True
            box_wrap_spacing 10
            spacing 10
            xoffset 20
            yoffset 20
            style_prefix "inv"
            for item in inventory_items:
                textbutton item:
                    action SetVariable("item_description", item_descriptions.get(item))
                    selected False













# The game starts here ######################################################################

label start:

    
    play music "Deep Haze.mp3"
    scene blackscreen

    j "Follow a hidden path down the alleys. Three lefts and a right, then close your eyes for twelve seconds."

    j "Remain calm and still, breathing shallowly, and keep your hands at your side..."

    j "It sounded like nonsense, but nonsense was my only lead."

    j "I pitied that beggar, and that's really why I'm here, I guess. Meager times create many beggars, with evil begetting evil and all that… "

    j "I guess this isn't a great evil if I'm just wasting my time here, in the grand scheme of things."

    j  "He didn't want anything from me. I've never had a good grasp on balancing naïvety and cynicism..."

    j "Plus, I need the work. That was my last copper gone in the tavern. My equipment is in good shape, I'm healthy and have a full belly, for now at least. Okay, it's been at least twelve seconds."

    scene druidgrove
    with pixellate

    j ".…I really just can't believe it. Do all druids work in such secrecy, or just 'Arch'druids when they're looking for a sucker to do their dirty work?" 

    j "I'm here. This is what I came here for. There's no sense in wasting any more time."

    scene druidhut
    with pixellate
    show druid at deadcenter:
        alpha .5


    n "A small, sincere smile colors the Archdruid's features upon spotting Julian - wicked away in an instant as he studies the young mercenary."

    n "Deep creases of worry fill the void in elderly man's expression as he strains his eyes in the firelight, as if beholding something only seen by him."

    n "He gestures at the open seat next to the fire and speaks with a soft woody baritone - akin to the rumble of straining mine supports deep in the earth."

    j "Magicians of any kind make me nervous. He seems friendly enough, but I shouldn't let my guard down."

    d "A friend told me you would come. Thank you for your interest in this assignment, young fellow. Take a seat and relax - this is a truly safe place. This world could use a few more of those."

    label druidchoice:

    menu:
        "Remain aloof":
            $ choosen = "noacceptdruid"
            jump druidchoice1
        "Take a seat and accept the Archdruid's hospitality":
            jump druidchoice2

    label druidchoice1:

        j "Ah yes, the vagrant…. I'd rather stand. I have a few scars from dealings with the 'magically inclined' and I'd rather not add another."

        n "A certain magic fades from the air, as if Julian's pronouncement conflicted with the place itself, despite the Archdruid remaining largely unfazed."

        n  "Julian sighs, realizing his faux pas."

        d "I shan't begrudge the intemperance of youth."

        d "You are wise to distrust what you cannot understand, but how can we come to an accord without even a wink of it? I mean trust, of course."

        n "The Archdruid hastily finishes his pipe and rises to his feet, joining Julian in the foyer."

        n "For a man of his impressive age, he walks gracefully, almost without even a hint of sound. There is a twinge of melancholy or regret coloring his expression, but not his voice."

        jump druidresolution

    label druidchoice2:

        j "Your… space is cozy."

        d "Thank you, young man."

        j "So - this job…."

        d "Perhaps a drink first. My treat, as the host."

    menu:
        "Accept the offer":
            $ choosen = "acceptdruid"
            jump acceptdruid
        "Decline":
            $ choosen = "noacceptdruid"
            n "Julian's reply is quick, with a hint of tension."

            j "I'd rather keep my wits about me. You have a job for me, right?"

            d "How impertinent of me."

            n "The Archdruid lets out a soft chuckle."

            d "A guest shouldn't be kept waiting."

            jump druidresolution

    label acceptdruid:

        j "I suppose… well, I don't see why not."

        n "The Archdruid rises from his seat and pours a dark orange liquid into two polished wooden cups. There's a bit of relief reflected in his dark eyes. He passes a cup to Julian, who hastily downs the contents."

        j "It's warming. What is this?"

        d "A bit of a house special. You'd call it Waldwine."

        d "It's a bit of a rarity, nowadays..."

        j "I've never heard of it, but it's nice. I'd kill a bottle or two."

        d "Spoken like a man of your trade - but save the violence for another time. I am glad it is to your liking, young man."

        j "There's something familiar about your face. Are you that fellow in the monastery murals? If that's you… what is it like being so old for such a long time?"

        n "The Archdruid serenely gazes into the fire. From seemingly nowhere, a squirrel perched itself on his shoulder. It mimics his calm yet distant expression and gaze."

        d "Time is secondary to our great mission. I have faith you will understand, one day, young man."

        n "Julian and the Archdruid spend a great amount of time talking. The night itself is like a dim, bleary haze. "

        n "At the end of it all, Julian cannot clearly remember what was discussed - only the anxiety he felt about this job and this unfamiliar place and person is gone, and he and this stranger will part as friends."

        d "I believe we lost track of time, Julian. You came here for a reason…"
        jump druidresolution

    label druidresolution:

    n "The Archdruid hands Julian a scroll bound with a wax seal, casting him an askance look."

    d "There is a demon infesting the local crypt. I need you to put an end to it."

    j "A demon?"

    d "A demon of shadow - neither a trivial, nor major example of its kind. It shan't be a trifle"

    d "Should you accept this trial, you will be adequately equipped and compensated."

    j "What do you consider to be adequate?"

    d "Oh, spare an old man the haggle. I'm offering you one hundred crowns for a job well done, and evidence of the slaying."

    n "Julian whistles slowly"

    j "No argruments here."

    d "To do battle with this fiend, you will need a silvered blade, crafted to scourge their impure flesh."

    d "To defend from its treacherous dark magic, a shield warded against such sorcery - but note, it requires a source of light, even if it is just a spark."

    d " Naturally, you will be allotted three days' rations for your journey."

    d "You'll find everything you need packed by the door. Complete the job, and return here for payment and debriefing."

    n "The neat bundle escaped Julian's notice entirely. It surely is where the druid said it was, but he couldn't be truly sure it was there when he entered."

    j "That seems straightforward enough. I kill the fiend with the blade you're providing me." 
    
    j "No strings?"

    d "None."

    d "Do as advised and take care to protect yourself against its deceit and wiles. Remain resolutely focused, and stay true to your task… and yourself."

    j "No complaints from me, oldtimer. I'll be going then. If I'm not back in a week or two, you'll know to send the next guy."

    n "The Archdruid grunts. It's not abundantly clear if he found some humor in Julian's statement, or if he's annoyed."

    d "Reflect on my words young man. Be safe and swift."

    hide druid

    scene druidgrove
    with pixellate

    n "Julian departs the druid's hut, and finds himself roughly where he expected - the same place he began the strange ritual to find the magician's hideaway."

    j "I'm not in any position to complain. One hundred crowns is more than I've seen in the last four jobs… "

    j "What could that oldtimer have meant by a demon's 'wiles'?"

    j "Maybe it's just an old way of speaking."

    j "I'd best not tarry."

    scene blackscreen
    with fade
    stop music fadeout 15.0

    if choosen == "acceptdruid":
        j "That place was like a dream. I remember the important bits, for now, but I ought to write it down in case I forget."

        j "He said his name is 'Kolya', I think… I've never met someone with such a strange name."

        j "I haven't been so at ease and relaxed as long as I can remember. It must have been that 'Waldwine' he had me drink… "

        j " Come to think of it, he must have been jesting about the murals. Some of them are at least one hundred years old. "

        j "I suppose when you're as old as he is, everyone starts to look a bit alike. Maybe he just has one of those familiar faces."

        j "Maybe. I'll have time to think about this more later. For now, the job."

        jump crypttime
    elif choosen == "noacceptdruid":
        j "I'll be six feet in the dirt if I ever deal with another magician after this job. If there is a next job."

        j "One hundred is about what I'd need to bother with another of these tricksters, and I have a nasty feeling it isn't the last of them on this journey."

        j "It's a pity he didn't give me an advance - I could pawn off this blade and shield and be two weeks distant from that creep."

        j "One hundred crowns is worth the effort, if it doesn't kill me."


    ########################################

    label crypttime:


    play music "Floating Cities.mp3"

    n "Julian undergoes a three-day travel through the city, to the outskirts. "
    
    n "Primarily, Julian spent the time reflecting on his mission and the Archdruid, and speculated on what was to come. "

    n " These days, he didn't get much comfort in anything, and this journey was no exception. "

    n "He wasted no time attending to the dubious duty he took as his yoke, all in the promise of gold."

    scene crypt
    with fade
    

    #########################################

    n "The Archdruid's contract led Julian to a crypt on the outskirts."

    n "Along the way, he heard rumors of locals being harassed when mourning their dead, statues and monuments within the crypt being toppled, and unsettling shadows darting around the crypt, irrespective of the lack of wind and torch."

    "The Archdruid told me my quarry is a Demon of Shadow - not a trivial, nor a major demon. I should be on my guard."

    "The blasted thing must be inside. I should keep stock of my belongings before I head in."

    hide crypt with dissolve

    show black with dissolve
    show screen inventory_display_toggle
   
    "Sealed with a wax stamp. Strange, it looks like the monastery sigil."

    n "It reads: Slay and banish the presence, whatever it may be, from this formerly sanctified place of rest."

    show sword at deadcenter
    hide sword with dissolve

    j "The sheen on this steel heater is phenomenal, and as long as there is even a scant amount of light, the Archdruid reassured me none of the demon’s shadow magic can harm me."

    show backpack at deadcenter

    j "I don’t even want to think about hardtack if I can’t soften it up first. It’s about as hard and appetizing as a brick."

    j "It’s filled with three-day old small beer. Smells sour. I probably shouldn’t, unless I really need to."

    hide backpack
    with dissolve

    j "That's it."

    hide screen inventory_display_toggle
    show black with Dissolve(3)
    
    show crypt at deadcenter

    
    f "Okay, enough stalling... let's do this"

    menu:

        "Enter Crypt":
            jump choice1_enter

    label choice1_enter:

    scene room1
    with pixellate
    label atrium:

    "A large stone room, far underground."

    "As you enter, you hear hydraulic mechanisms automatically shut the large steel gate behind you."

    stop music

    play sound "gateclose.wav"

    scene closinggate

    play music "darkest_child.mp3"
    

    "A security measure by the townsfolk, surely."

    n "You are trapped down here with the demon, and it with you, until one of you perishes."

    "Torchlight glints off of brass embellishments on the sarcophagi populating this moderately impressive tomb."

    
    show shadow at right
    
    hide shadow with fastdissolve

    "On the periphery of your vision, you notice unusual fleeting shadows. The demon must not be far off, and it has nowhere to run. One of you must perish today."

    scene room1
    with pixellate

    n "A great stone arch allows passage further in this dark place. It seems the townsfolk or druids left a torch here for your use."

    label picktorch:

    menu:

        "Pick up Torch":
            jump choice2_torch

        "Leave it":
            jump choice2_nopick
    
    label choice2_torch:
        $ choosen ="havetorch"
            
        show unlit at deadcenter
        with dissolve

        f "I should take it. A light source would be useful in this dark place… especially with a demon of shadow lurking nearby."
        $ inventory_items.append("Torch")


        hide unlit
        with dissolve

        jump choice2_done

    label choice2_nopick:
        $ choosen ="notorch"

        f "I'll be fine."

        n "You leave the torch behind"
        
        jump choice2_done

    label choice2_done:

        n "A service entrance to a cramped, dark tunnel lies to the left."

        n "A stone passage, comprised of stonework typical of the city proper lies to the right."

        n "Where will you go?" 

    label LookLeftLookRight:

    menu:

        "Investigate the service entrance to the left":
            jump choice1_left

        "Investigate the stone passage to the right":
            jump choice1_right

        "Head deeper into the crypt":
            jump choice1_forward

    label choice1_left:

        $ darkness += 1

        j "… Huh. "

        j "This looks a lot like an access tunnel to the city's sewers. It would make sense for something like this to be here in the outskirts, I suppose."

        j "It seems a bit insensitive to connect the sewers to a crypt, but I'm not the city planner."

        j "They're working with what space they have, I guess."    
        jump goblinchoice

    label choice1_right:

        if choosen == "golemactive":
            j "I'd rather not mingle any more with sorcerous experiments left in storage for a hundred years."
            j "Like I said, it's somebody else's problem now."
            j "If they want me to take care of it, well, another hundred crowns would be nice."
            hide golem 
            scene room1
            jump LookLeftLookRight
        elif choosen == "boltcutters":
            scene warehouse
            jump golemtouch
        elif choosen == "barricade":
            jump tunnel

        jump golemchoice

    label choice1_forward:

        n "You go forward."

        jump choice1_done

    label goblinchoice:

    j "The entrance is blocked by an iron grate. The bars are serviceably thick, but they're made of low grade iron with a lot of corrosion."

    j "If I found something to bend or break these, maybe I could exit to the city."

    j " Do I want to do that? I'd be abandoning my contract."

    j "Maybe I'm not cut out for this business involving magicians and demons."

    j " I'll have to give it a think."

    if choosen == "boltcutters":
        jump cutbolt

    jump cutbolt

    n "Julian returns to the Atrium"

    jump LookLeftLookRight
    
label cutbolt:

    menu:
        
        "Cut the bolts and abandon the contract":
            jump meetgoblin
        
        "Go back and find the demon":
            jump nogoblin
    
    label meetgoblin:
        
        j "I've had enough of this nonsense. I'm not about to die in a haunted crypt."

        j "This situation might be funny under other circumstances… circumstances I'm not in… "

        j  "It's time to get the hell out of here, and quick."

        j "I'll be damned twice if I end up dead doing the bidding of an out of touch old fart."

        n "Julian makes quick work of the bolts."

        n "The way to the sewers is clear, even though the hydraulic lock to the crypt holds fast. "

        n "There is a way out yet, even if it is a dismal path."

        scene goblinroom
        with pixellate

        play music "Leaving Home.mp3"

        j "What's that?"

        show goblin at deadcenter

        n "The lurking creature speaks, with a scratchy, but distinctly feminine voice. "

        g "Heya. I've been watching you."

        j "You what? I… What the hell are you"

        g "Haha. I'm a goblin."

        g " You've heard of goblins, right?"

        g "We're scary sewer dwelling bogeymen who steal babies, or something."

        g "Who are you?"

        n "Julian hesitates, eyeing the goblin's blowgun. Poisoned darts, no doubt. He quickly realized he needed to handle the situation with care."

        j "That really isn't important, and it certainly isn't your business."

        j "Who said you are the one asking questions?"

        g "Why not? You're really defensive, aren't you?" 
        
        g "I thought you'd be more exciting. Are you really that afraid of me?"

        label talktogoblin:

        menu:

            "Parley with the creature":
                jump flirtygoblin

            "Seize the opportunity and catch the goblin off guard":
                jump attackgoblin

        label flirtygoblin:
            $ choosen = "leftwithgoblin"

        "I can't believe I'm doing this."

        n "Julian exhales an annoyed sigh and sheathes his blade."

        j "No, I am not afraid of you, but I am confused. Haven't you heard there is a demon nearby, in this very crypt?"

        g "You sure have a weird way of talking. Did something happen to you?"

        j "Yeah, I guess a lot has…"

        g "That's what I thought!"

        g "Something happened to you to make you like this."

        j "You're not afraid of the demon?"

        g "The farmers talk about it and seem really afraid. I don't know what it is, reeeeaaallllyyy… and the farmers are afraid of a lot of things."

        n "The goblin shrugs her shoulders and smiles. She seems friendly, and not at all worldly - or at least not educated."

        j "You should be afraid of it, demons are dangerous."

        g "Another one? Did a demon steal your baby or something?"

        j "Don't joke about that. You'd be surprised…"

        g "No human invented tall tale, rumor, fancy, or gossip would surprise me. I'm a professional eavesdropper."

        g "But uh, that is why I'm here. I wanted to see if there's any substance to the rumors!"

        g "Some tales have truth to them, and some don't. The bars were disappointing - but now they're not! "

        g "Thanks Mr. human guy. What's your name?"

        j "Julian. Julian Grymwald."

        "I really need to stop being so impulsive."

        j "You're not a magician, or a magician's familiar… right?"

        g "Oooh, no."

        g "I'm not familiar with them, but I'd like to be. I haven't even met one, but the farmers are afraid of them too, like you. "

        g "Their tales about magicians are a little different like… the magicians cursed the crops, or made someone's baby be born under an 'ill omen'. But no kidnapping."

        j "Why are you so interested in humans? How did you even learn our language?"

        g "Weeeeellllll…"

        n "The goblin frowns for the first time."

        g "I really don't like talking about this. Do you really want to know?"

        j "Sure."

        g "Okay, but I'd rather not say."

        n "Julian sighs and looks over his shoulder."

        g "I'll spot anything coming, just like I spotted you. We goblins can see in the dark."

        j "Uh… I see. And yes, I really want to know."

        n "She continues on, frowning and obviously just a bit uncomfortable. At the same time, she seems desperate for social contact, and most likely doesn't have much experience socializing."

        g "When I was young, a bit too young, I was exiled from my tribe on account of my 'difference"

        n "The goblin gestures at herself, presumably indicating the ivory color of her skin, her pink eyes, and white hair."

        g "It's isolating, living alone, but I've got really good at it. My blowgun makes hunting easy. Just aim and… shoot."

        n "The goblin demonstrates, pointing the barrel of the blowgun at Julian. She takes a quiet, deep inhale, and mimes the action, exhaling through her nose."

        "I'm starting to reconsider this course of action… She seems friendly enough at least, if a bit unhinged."

        g "You'd find what I eat gross, but it's not gross for goblins. Well…"

        g "I've made a bit of a life for myself up here. Down here. Wherever 'here' is at the moment. "

        g "I'm really familiar with the sewers, because listening to the same rumors and legends gets pretty boring. I keep myself safe with my blowgun, aaaaannnnnd… "

        g "I pretty much never get lost. As for my tribe…You don't need to worry about them. They live much farther down."

        n "The silence seems to eat at her, irrespective of the fact that was quite a bit of information for Julian to process. She gives him a plaintive expression - almost comically."

        j "Whoa, it's okay. It sounds like you've done well, considering your situation."
    
        j "You're alive, right? And you taught yourself how to speak our language."

        g "For all the good that does me!"

        g "And trust me, I've tried to have a conversation or two with humans like you, and it never goes well. Until now, at least."

        g "You wouldn't believe how little humans look down. They always go running when I try to get their attention."

        j "It's like you said, something happened to me. I must not be of my right mind."

        n "Julian cracks a small smile, letting the goblin in on the joke. She returns the smile, a bit more slowly."

        j "It sounds lonely, living all by yourself in the sewers. What is your name, anyway?"

        g "It's not 'anyway', it's Inya."

        n "Julian cocks an eyebrow and waits for the punchline that never comes."

        j "Okay, in-ya what?"

        i "I… never thought of it like that. Hey…"

        n "The goblin seems genuinely perplexed by the realization her name can be made into a joke."

        i "I like 'Inya'. It sounds so much nicer and more refined than my goblin name." 

        i "And don't even ask, I'm not telling you."

        j "Okay, Inya it is."

        i "Yes, that's what I am."

        n "Julian deliberately nods, affirming their agreement to call Inya 'Inya'."

        j "Inya, do you know how I might get to the city?"

        i "Yeah, it's above you. Are you dumb?"

        j "I'm starting to feel that way, I confess… Can you lead me there, to the streets?"

        i "Oh! Sure! We can go together."

        j "Thank you."

        scene endingscreen
        with pixellate

        n "Julian, led by Inya, made their way to the streets. Silently indicating the direction of a culvert, Inya hurriedly catches up to Julian, and tugs on his arm to get his attention. She looks oddly emotional and introspective."

        i "I can see you again, right? We're friends?"

        j "Yes, Inya. You have been a friend to me. I might have died back there without your help."

        j "I'm going to have to lay low for a while because of… well, I'd better not say."

        i "Uh oh, you messed up big time?"

        j "Yeah, you could say that. But, we got to meet each other because I did, so it could be worse."

        i "Yeah! A lot worse. You could be dead, and I could be friendless."

        j "You certainly have a way of viewing the world."

        i "It's like I said, with or without the dark. Thanks for being my friend, Julian."

        i "We should set up a signal or something, like a flare."

        j "I could just come back here in three days, at nightfall."

        i "Can we make it two hours after nightfall? That's the best hunting, at dusk."

        j "Sure. I'll see you then, Inya"

        n "The goblin giggles."

        i "Yeah you will. I'll see you first though."

        n "The newly acquainted pair part, for now - Inya, back to the sewers, and Julian, to an uncertain fate in an unfriendly world."

        jump witchstart


    label attackgoblin:
        $ choosen = "goblindead"

    "I don't really know what I'm looking at, but I don't like it. It's time to get out of here - no witnesses."

    j "I'm actually a landed noble - the baron."

    j "I'm here on a mission to investigate rumors of goblins personally, to give the effort a hands-on approach."

    g "I don't know what that is or parti- grk…"

    hide goblin

    n "Approaching slowly during the conversation, Julian strikes down the goblin with his blade before she can react."

    "Well, that was easy. I feel guilty, but a bit less guilty this go around. I'd best keep moving and not think about it too hard."

    n "Julian, indeed, made his way through the sewers, into the city. "

    n "It was just as dreadful and stinky as he thought it would be, and in the end, he had nothing to show for his effort."

    n "Alone he remained, with only the stolen goods loaned to him by the Archdruid to keep him company."

    scene endingscreen
    with pixellate

    j "I had best lay low for a while. That magician will inevitably send cronies after me if he really did have one hundred crowns to just throw around. "

    j "What did he call these things - a silvered blade and a shield capable of deflecting dark magic?"

    j "I'll have to keep an ear to the ground for the right buyers."

    jump witchstart

label nogoblin:

    j "Lucky me, I have just the right tool for the job - but I can't be serious with this. I've come all this way for nothing?"

    j "One hundred crowns could keep me fed for months, and I could buy some new equipment, not even considering the connections the Archdruid might have for me."

    j "I'm better than this. Let's be thorough."

    n "You return back to artium"

    scene room1
    with pixellate

    n "where will you go?"

    jump LookLeftLookRight 
    
label golemchoice:

    n "Before you is tunnel that is barricaded by a few simple boards"

    j "Ugh, do I really want to be doing this?"

    j "There's a quarter inch of dust covering literally everything. If I found this demon in such a cramped space, I don't think I'd even be able to swing my sword…."

    menu:

        "Dismantle Barricade":
            jump gogolem

        "Turn Back":
            jump leavegolem

    label gogolem:

        j "Here goes nothing. These boards look simple enough to remove by hand. Dry rot and the ravages of time have reduced them practically to splinters."

        j "It's going to be a tight fit. I can't even stand up straight in this cramped tunnel."

        jump tunnel
    
label tunnel:

    scene tunnel
    with pixellate
        
if choosen == "havetorch":
        j "I should be on guard. It's unusually stuffy in this tunnel, and black as pitch."

        j "It reminds me of an abandoned factory, or that mage's study years past…" 
            
        j "Well, here goes nothing."

        jump warehouse

elif choosen == "notorch":
            
        j "I should come back with a light source."

        j "This place stinks of a trap. It would be foolish to fumble around in the dark and step on a nail, or worse."

        n "You go back the way you came."

        scene room1
        with pixellate

        n "where will you go?"

        jump LookLeftLookRight

label leavegolem:

        j "No, something is wrong about this place. It's like it has been pulled from a different place and time."

        j "I might come back to it, if this creature isn't anywhere else in this crypt, provided I can think of a plan…"
        
        n "You go back the way you came."

        scene room1
        with pixellate

        n "where will you go?"

        jump LookLeftLookRight

label warehouse:
        scene warehouse
        with pixellate

        show golem:
            alpha .3
        j "Whatever this was, it's a trash heap now."

menu:
        "Search rubble":
            j "I might as well try to find something useful while I'm here."

            n "You sort throught the rubble and find a set of bolt cutter"
            $ choosen ="boltcutters"

            j "Huh. These might come in handy, I guess. Nobody else is using them, I might as well bring them along."

            jump golemtouch

        "Turn back":
            j "Well, this is a dead end."

            j "There's plenty of this crypt left to explore. The demon is here somewhere."

            n "You go back the way you came."

            hide golem

            scene room1
            with pixellate

            n "where will you go?"

            jump LookLeftLookRight

label golemtouch:

        j "There is some strange text on these stones. Strange, it almost looks like an arm…"

        j "Maybe this was a sculptor's studio? That doesn't seem quite right."
        
menu:
        "Touch symbol":
            $ choosen = "golemactive"
            n "The pile of rubble begins to shake, and the runes in the rubble pile begin to glow with a dim blue light."

            j "I'm not getting paid enough for this. This isn't a demon, it's somebody else's problem. I'm getting out of here."

            n "You go back the way you came."
            hide golem
        
            scene room1
            with pixellate
        
            n "where will you go?"

            jump LookLeftLookRight
    
        "Turn back":
            j "I'd better not. There's plenty left to do here. I'll think about it."

            hide golem

            scene room1
            with pixellate

            n "where will you go?"

            jump LookLeftLookRight


label choice1_done:
    scene darkhall1
    with pixellate

    "The rooms ahead are shrouded in oppressive darkness - likely the work of this demon."
   
    if choosen == "havetorch":
        jump choice3_torch
    elif choosen == "notorch":
        jump choice3_done

    label choice3_torch:

    f "I should be well prepared for the push ahead...."

    show unlit at deadcenter
    with dissolve

    f "at the very least, I should have a light source."

    menu:
            "Light Torch":
                jump choice3_light

            "Save for later":
                jump choice3_nolight

    label choice3_light:
        $ choosen = "light"
        n "you stike the torch along the stone walls"

        hide unlit
            
        play sound "torchlighting.mp3"

        show lit at deadcenter
        with dissolve

        scene lithall
        with pixellate

        hide lit
        with dissolve

        f "If I squint, I can see solid silhouettes deeper in this place."

        jump choice3_done

    label choice3_nolight:
        $ choosen = "no light"
        j "these do not last long, I'll use it only if I absolutely need too"
        n "You leave the torch unlit"
        jump choice3_done

    label choice3_done:

    j "I must hurry, time is of the essence"

    scene wrathhall
    with pixellate
    if choosen == "nolight":
        jump killbywraith

    f "The Archdruid warned me about these Wraithspawn. They are the creations of my quarry, this Demon of Shadow."

    f "As unsettling as they are, they don't present a threat unless I provoke them."
    
    show lit at deadcenter
    with dissolve

    play sound "torchlighting.mp3"

    hide lit
    with dissolve

   
    show ghost at offright:
        alpha .3
       

    f  "I can't see it at all without my torch." 

    n "Maimed Wraithspawn,  This one suffered a major injury in life."

    n "its spine folds like an accordion, and its arm drags limply at its side." 

    f "It doesn't seem to be in pain, at least. I wonder if it knows where it is?"


    show dog at offleft:
        alpha .3 
    
    n "Canine Wraithspawn - A beloved family pet, perhaps?"
     
    n "It paces throughout the chamber as if seeking out its master."
     
    f "Why was this innocent creature cursed to wander like this?"


    hide dog
    hide ghost


    scene blackscreen
    # Room 3 - Monument Chamber

    n "placeholder for explaining your phsyical movement into the monument chamber"

    j "One thing is certain, this place has been vandalized. The locals surely wouldn't do this..."    

    j "Statues are torn from the podiums from which they rested, and stone slabs commemorating the deeds of the heroic dead have been toppled."

    n "Perhaps you should be on guard and gather your bearings before pushing ahead."

    n "Aside from the ladder down and the way you entered, it appears all of the connecting chambers are blocked by collapsed rubble."

    show coin at deadcenter


    j "The old farts at the monastery and maybe some of the druids remember when these were minted."

    j "They're at least half zinc, more than a quarter copper, but there's a bit of silver in there... I guess that's why they're called silver coins."

    j "It's strange to find something like this here."

    j "There is a puncture near the edge of the coin, as if it were attached as a necklace."

    j "How odd. Maybe one of the townies dropped it while fleeing...."

    menu:

        "Ignore it":
            jump choice2_ignore

        "Take the coin":
            jump choice2_take

    label choice2_ignore:
        $ choosen = "nocoin"

        f "Something is off about this. I should trust my gut. Much is amiss in this tomb, and I had best not tempt the spirits. One monster is enough…"

        n "You leave the coin and move on"

        hide coin

    label choice2_take:
            $ choosen = "havecoin"
            
            show coin at deadcenter
            with dissolve

            f "Whatever, it's mine now. Whoever lost it is long dead. In their place, I wouldn't begrudge me."
            $ inventory_items.append("coin")

            hide coin
            with dissolve

    n "Despite the flickering flame of the torch, the shadows stir - and speak!" 

    # sound

    n "Haphazardly drawing his blade, Julian stumbles backwards, caught off guard."

    x "Mortal, the light you bring to my domain is most unwelcome. Leave this place, or meet your end."

    # sound

    x "Return your filchings to their proper place, and forget all you have seen here."

    j "Unsettling. The torch has sent the fiend fleeing - I had best pursue it..."

menu:
        "Turn back":
            j "I need to get my bearings. I'm not sure I'm ready for all this just yet. I need to be absolutely sure before I hunt down this creature."
            jump atrium
            with longdissolve

        "Continue forward":
            jump memorials

label memorials:
            n "Toppled Memorials: Dedicated to heroes who were stalwart defenders of the people - soldiers and sellswords alike. Many of them fell to demons."

            j "It seems like a bit of a petulant tantrum, doesn't it? Perhaps my expectations of these creatures were too lofty."

            n "Ladder: A ladder in the center of the room, leading down to the peasant's graves. It looks freshly disturbed. "

            j "What purpose could this demon have disturbing the remains of the destitute?"

menu:
        "Go down the ladder":
            jump ladderdown

        "Return to the atrium":
            jump atrium
            with longdissolve

label ladderdown:

"The shadows dance here, I must be close. There is a narrow walkway encircling an open pit, where the less fortunate are tossed to rot."
"At least these are embalmed - a small courtesy for the poor."
"It's a dead end. The demon is surely here. But where?"
"Ugh, I don't think I can bear this stench for much longer…"


n "There - on the other side of the platform, the shadows take shape - the demon manifests."
# sound

"… … … "
"What in the world?"

#show adesse with slide Down

show adesse:
    size (1240, 1754)
    xalign 0.5 yalign 1.0
    linear 6.0 yalign 0.0


u "Many other mortals have fled, yet here you are… Did you mean to assail me here, in my chosen domain? Are you lost, Julian?"

label fightorquestiondemoness1:

    menu:
            "Fight the demoness":

                j "You will haunt this place no longer, foul demon! Face me!"        
            
                jump fightdemoness1              

            "Question the demoness":

                j "Are you? I see - you divined my name."
                
                "(stumbling over words)"
                
                j "You, uh... look different from uh, what I expected."
                
                jump questiondemoness1

label fightdemoness1:

    n "The demoness fires a barrage of needle-like spines of solid shadow."

    menu:
        "Dodge":
            jump dodgedemoness1
            
        "Block":
            jump blockdemoness1

        "Attack":
            jump attackdemoness1

label dodgedemoness1:

    j "I can see the shadows moving, I can dodge them!"
    n "Julian dodges the demoness' attack."
    j "I can do this. I can do this."
    n "The demoness fires another barrage of needle-like spines of solid shadow."
    jump fightdemoness2

label blockdemoness1:

    j "I can block them with my shield!"
    n "The dark magic spines melt like snow against Julian's blessed shield.  The deomoness gathers energy for her next spell, giving Julian an opportunity to strike."
    jump fightdemoness2

label attackdemoness1:
    j "I can strike her now!"
    n "Julian's opportunity to strike is lost as the demoness fires another barrage of needle-like spines of solid shadow."
    jump fightdemoness2

label fightdemoness2:

    menu:
        "Dodge":
            jump dodgedemoness2
    
        "Block":
            jump blockdemoness2

        "Attack":
            jump attackdemoness2

label dodgedemoness2:

    j "I've changed my mind, hold your strike and let's talk..."
    jump fightorquestiondemoness1

label blockdemoness2:

    n "Julian's opportunity to strike was squandered. The demoness finishes casting her spell, sending razorblades of darkness hurtling towards Julian from all directions. Perhaps thanks to his armor or an absurdly good stroke of luck, he manages to cling to life and consciousness, but only just."
    jump demonessresolution1

label attackdemoness2:
    n "A desperate, vicious strike. A fateful strike. Abandoning caution, Julian hurtles towards his foe. In a confluence of circumstance and power, desperation and need, he executes an overhead swing with his Demonslaying Blade. The demoness's self-satisfied expression fades as the blade slices through her cranium."
    
    j "There's… no blood. But it's gone. I can feel its absence."
    
    jump demonessresolution2

label demonessresolution1:

    n "Julian's vision blurs as he bleeds out against the cold stone. Revealed in blood-blurred snapshots as he blinks, unbelievably, he sees a warrior doing battle with the Demon of Shadow. A few moments of combat pass, and then silence."

    n "The room fills with the smell of sweet sulfur, and Julian, losing consciousness, feels a slight stab of pain. His hero - this masked avenger crouches down to check his vitals and speaks in a soft, deep female voice."

    t "You shouldn't be here. Did Nikolai put you up to this?"

    n "The warrior sighs, audibly unbuckling the clasp securing her pack, and withdraws salves, a splint kit, a needle, and thread."

    t "If you can hear me… I'm going to tend to your wounds. This is going to hurt a lot. You've proven your bravery, soldier. I just need you to hang in there just a little bit longer."

    n "The warrior sutures Julian's wounds and stops the worst of his bleeding. Time lost meaning to Julian, amidst the agony of his countless injuries. And yet, somehow, he clings to consciousness."

    t "C'mon, stay with me… you can't die on me just yet."

    t "I've tended to your scrapes and stopped the bleeding. You're doing great, but we're not out of the woods yet. I'm going to set your leg. Bite down if you need to, or you're going to bite through your tongue and suffocate on your own blood."

    n "Bleary-eyed, Julian scans the room. There is no trace of the demon - save a suspicious, soft-looking stone where she fell. Likewise, the shadows have stopped moving of their own accord. He looks over to his savior."

    n "Until she spoke, he had no indication this powerful warrior was a woman. She eschews armor for green and brown traveler's leathers, adorned with protective talismans. Her longboots are characteristic of the locality."

    n "Her saw-toothed metal staff and iron mask strike Julian as distinct, but wracking his brain, he comes up with nothing for their origin. Whomever she is, she is a skilled warrior and healer."

    n "The warrior slips a bit made of hard rubber into Julian's mouth and prepares to set his leg."

    t "Stay with me here..."

    t "3..."

    t "2..."

    t "1..."

    n "An audible crunch disturbs the silence of the chamber as she sets the bone. Julian, despite his wounded and half-conscious state, lets out a muffled wail, biting down hard on the bit."

    t "We're almost done. Hang in there. You're doing great."

    n "The warrior removes his plated leggings and rips his pant leg, using the material to bind the splint."

    t "I'm going to pick you up. It's going to hurt a bit. You really shouldn't be moved in this condition, but we're not exactly swimming in options. You're in good hands. You can leave as soon as you have recovered, but I'm going to have some questions for you first."

    t "You can call me Tess. I think you're brave, for whatever that's worth."

    n "Tess carefully heaves Julian over her shoulder. Julian passes out shortly thereafter."

    scene blackscreen
    with longdissolve

    stop music fadeout 15.0

    jump neutralend
        
label demonessresolution2:

    j "The deed is done. The demon is vanquished. Strange, it seems the foul harpy left a trinket among her remains. A soft, sulfurous stone - proof of my victory. It’s a shame to fell such a striking beauty. It invaded my mind… and seemed to know me."

    j "Perplexing, and dangerous. Why do I feel a sense of loss? An emptiness, left in the wake of my fallen foe? I had best put aside these thoughts. I should return promptly to the Archdruid, for he will want word of my success."

    scene blackscreen
    with longdissolve

    stop music fadeout 15.0

    jump neutralend

label questiondemoness1:

    hide adesse
    show adesse_angry:
        size (1240, 1754)
        xalign 0.5 yalign 0.0

    n "The demoness narrows her eyes and scowls."

    u "My nature dictates me to assume a form that resonates with the desires of those who behold me. Perhaps you would be best served reflecting on your own preferences... This parley tires me - accept this small mercy before I reconsider."

    u "I have harmed none of the hapless fools who wandered into my domain, and I extend the same courtesy to you - in honor of the dead. This place is meant for the grieving, is it not? Leave me to grieve."

    label fightorquestiondemoness2:
    
    menu:
        "Fight the demoness":

            n "Drawing your blade, you steel yourself for battle."
            
            j "The Archdruid cautioned me against the lies of your kind. You’re afraid, monster - and I am no fool. If you have an ounce of honor, face me. I offer you a duel. Your life or mine. Let us settle this now."
        
            jump fightdemoness1              

        "Question the demoness":

            n "Contemplating the small atrocities this fiend has personally wrought in this tomb, you withdraw the antique coin you collected on the upper levels."

            j "Your kind only sows grief with every new widow and orphan you leave to face this world alone. To grieve, you have to feel loss. What could you possibly know of grief"        
        
            jump questiondemoness2

label questiondemoness2:

    hide adesse_angry
    show adesse_distant:
        size (1240, 1754)
        xalign 0.5 yalign 0.0

    n "The demoness’s eyes look distant, and she appears forlorn."

    n "Her gaze drifts from the silver coin to the pit between you and her - this pit where the bodies of the destitute are unceremoniously thrown and left to rot."

    u "There was another mortal, not unlike yourself. We shared a bond, of sorts. Like you, she lived a fickle and fleeting life, and was taken from me - like you, she hesitated, and like you, she showed me mercy. She rests here, in this muck of unfortunates."

    menu:
        
        "How unusual. You have satisfied my curiosity. I offer you this - I inform the Archdruid that the disturbance has been dealt with, and you say your last goodbyes to your… paramour.":
            jump demonessresolution3

        "This coin was hers, then? The druids tell many horrible tales of your kind - never have I heard of a demon grieving for a lost mortal.":
            
            n "You continue on deliberately, despite your apprehension, ensuring to choose your words with great care. For the briefest moment, you consider if you were misled by the Archdruid. Ultimately, who could know?"
            
            j "May she rest in peace. Your fallen paramour must have been truly special."

            jump demonessresolution4

label demonessresolution3:

    hide adesse_distant
    show adesse_neutral:
        size (1240, 1754)
        xalign 0.5 yalign 0.0

    u "You are most unusual and merciful for one who has lived such a dastardly life, Julian. Only an orphan such as yourself could truly understand that sting of loss… The druids caution many against the worst atrocities of my kind, and they speak true…  We part, monster and murderer. We shall meet again."

    n "The demoness vanishes, and the dancing shadows in the room stall to a halt."

    j "What an ordeal… Demons are both very like and very unlike how Archdruid described them. I couldn’t have possibly prepared for this. Even so… I can’t help but have my thoughts wander to that beshadowed beauty. It’s a pity I never learned her name - although I shudder at the thought of meeting again."

    j "She seemed quite confident we would… but if she knows the worst of my crimes, how could she see anything good in me? Perhaps… I can only be my truest, deepest self with a demon. Nay, I should banish the thought."

    jump neutralend

label demonessresolution4:

    hide adesse_distant
    show adesse_flirty:
        size (1240, 1754)
        xalign 0.5 yalign 0.0

    n "The dark energies dance in the room, possibly reflecting the demon’s state of mind. Her expression softens. She seems incapable of tears, perhaps due to her nature."

    u "I am called Adesse, mortal. You have given me much to consider - but I believe this encounter draws to an end"

    u "I shall say my final farewell and depart. You may tell your superiors whatever you choose - but this is not our last meeting, Julian. You’re… intriguing - and you remind me of someone I once loved."

    n "A bittersweet smile colors Adesse’s ethereal features moments before she vanishes, and the dancing shadows in the room stall to a halt."

    j "She just vanished. Well, that’s great. Am I cursed now, haunted? I should be more worried about that, probably… but even though it has been but a moment, I can’t keep my thoughts off of her. I want to see her again. Adesse… such a peculiar name. I wonder if it was given to her."

    j "If I have been deceived, surely I will find the truth of things - for now, I shall report my success to the Archdruid."

    jump goodend

label neutralend:

	scene endingscreen
	with pixellate

	#if the golem is been activated, then jump to golem waking up
    if choosen == "golemactive":
        jump golemstart

    jump witchstart

label goodend:

	scene endingscreen
	with pixellate

	#if the golem is been activated, then jump to golem waking up
	if choosen == "golemactive":
		jump golemstart

	jump witchstart

label golemstart:

	scene golemroom
	with pixellate

	gl "Sensation… A touch…"

    gl "The touch is familiar, but so distant…"

    gl "Distant like another life."

    gl "Sculpted from stone, was I. Once inert, once lifeless, but given life by my creator. Where is my creator? Who am I?"

    gl "The memories are dark, with spots of color - feelings, and meaning almost indecipherable in the static."

    gl "The music is gone. This one's creator is missing. There is nothing left. I must press on."

    label golemmirror:

    $ golempulltogether = true
    $ golembreakmirror = true

    menu:
    
        "Pull yourself together" if golempulltogether:

            gl "Sundered, but not destroyed, I remain - and will persist, until this one's destruction."

            n "The Golem wills its body into its proper configuration. The clamor of objects flying through the room lit by a bright blue flash as its stone body reassembles is unnoticed - or perhaps is just unremarkable to the Golem."

            show golem:
                alpha .3
                alpha .5
                alpha .7
                alpha .9
                alpha 1.0

            n "A dirty mirror, covered in years of dust and grime. The Golem wipes away the thick coating of dust."

            gl "This one's appearance is clarified - but this one's objective is unclear. Identity is lost - purpose, undetermined."
    
            gl "These mirrors are created by covering a glass pane with a tin-quicksilver amalgam, then heating the pane to evaporate the quicksilver."

            gl "A protective covering of copper may be added to reduce corrosion. This one suspects this mirror has been treated with such a coating."

            gl "Much like this one, it has endured the ravages of time. Like this one, it presses on without its creator - without purpose. How long has it been?"

            gl "The memory is indistinct, but tangible - out of reach. I must press on."

            golempulltogether = false

            jump golemmirror

        "Break the mirror" if golembreakmirror:

            #TODO: Add sfx of glass breaking, image of broken mirror, etc.

            gl "Memories of fury - of violence. I wish not to reflect. I wish not to suffer. I must not yearn."

            gl "… I press on."

            golembreakmirror = false

            jump golemmirror

        "Leave":

            jump golempresson

label golempresson:

    #TODO: grayscale depiction of the cramped tunnel Julian passed through, with a trail of footprints / implied darkvision

    n "The path is dark and cramped. A recent trail is seen in the dust."

    gl "Footsteps in the dust. A human passed through here - not my creator . . . An interloper."

    menu:

        "Express Rage":
                
            gl "None may tread into my creator's sanctum. This interloper will be located, and exterminated."
                
            jump golemproceed

        "Express Gratitude":

            gl "This interloper stirred this one from an eternal reverie. This one is grateful. This one may seek its objective . . . once an objective is determined."

            jump golemproceed

        "Proceed":

            jump golemproceed

label golemproceed:

    n "The Golem retraces Julian's steps to the crypt's atrium. It studies its surroundings - a sealed door to its right, unfamiliar stonework leading to an access tunnel of some kind dead ahead, and a path deeper into the crypt to its left."

    gl "It is now clear to this one a considerable amount of time has passed in this one's reverie. I must press on."

    menu:

		"Press on ahead":

			jump golemahead

		"Press on to the left:

			jump golemleft

          
