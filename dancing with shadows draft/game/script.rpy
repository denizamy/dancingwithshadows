# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Narrator")
define d = Character("Archdruid",color="164622")
define j = Character("Julian",color="#3366cc")
define f = Character("Julian",color="#3366cc")
define g = Character("Goblin",color="60e683")
image sword = "sword.png"
image shield = "Shield.webp"
image backpack = "backpack.png"
image unlit = "unlit.webp"
image shadow = "shadow.png"
image lit = "lit.webp"
image dog = "dog.png"
image ghost = "ghost.png"
image goblin = "goblin.jpg"
image golem = "golem.png"
image druid = "druid.png"
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



# The game starts here.

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

        d "Its a bit of a rarity, nowadays..."

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


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    label crypttime:


    play music "Floating Cities.mp3"

    n "Julian undergoes a three-day travel through the city, to the outskirts. "
    
    n "Primarily, Julian spent the time reflecting on his mission and the Archdruid, and speculated on what was to come. "

    n " These days, he didn't get much comfort in anything, and this journey was no exception. "

    n "He wasted no time attending to the dubious duty he took as his yoke, all in the promise of gold."

    scene crypt
    with fade
    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.
    "Recently, you have accepted a contract from the Archdruid to investigate the local crypt."

    "As of late, locals have been harassed when mourning their dead, statues and monuments have been toppled, and unsettling shadows have darted around the crypt, irrespective of the lack of wind and torch."

    f "The Archdruid told me my quarry is a Demon of Shadow - not a trivial, nor a major demon. I should be on my guard."

    f "I should take note of my tools of the trade."

    hide crypt with dissolve

    show black with dissolve
    show screen inventory_display_toggle
   
    n "Slay and banish the presence, whatever it may be, from this formerly sanctified place of rest."
    $ inventory_items.append("Contract")

    j "A steel arming sword plated with silver along the edge - said to scourge demons. The druids placed a blessing on it. Normal weapons can't even scratch their flesh. I might stand a chance with this blade, if I'm lucky."
    $ inventory_items.append("Demonsalying blade")

    j "The sheen on this steel heater is phenomenal, and as long as there is even a scant amount of light, the Archdruid reassured me none of the demon's shadow magic can harm me."
    $ inventory_items.append("Blessed Shield")

    j "I don't even want to think about hardtack if I can't soften it up first. It's about as hard and appetizing as a brick."
    $ inventory_items.append("Hardtack")

    j "It's filled with three-day-old small beer. Smells sour. I probably shouldn't, unless I really need to."
    $ inventory_items.append("Waterskin")
   
    j "That's it."

    hide screen inventory_display_toggle
    show black with Dissolve(3)
    
    show crypt at deadcenter

    
    f "Okay enough stalling, lets do this"

    menu:

        "Enter Crypt":
            jump choice1_enter

    label choice1_enter:

    scene room1
    with pixellate

    "A large stone room, far underground."

    "Torchlight glints off of brass embellishments on the sarcophagi populating this moderately impressive tomb."

    stop music

    play sound "gateclose.wav"

    scene closinggate

    play music "darkest_child.mp3"
    

    "You hear hydraulic mechanisms automatically shut the large steel gate behind you. A security measure by the townsfolk, surely. You are trapped down here with the demon, and it with you, until one of you perishes."

    scene room1
    with pixellate

    n "A quick scan of the area reveals passageways to your left and right as well as a stone arch leading deeper into the crpt"
    
    n "It would also seem that a torch was left for you"

    j "The druids must have left me this."

    label picktorch:

    menu:

        "Pick up Torch":
            jump choice2_torch

        "Leave it":
            jump choice2_nopick
    
    label choice2_torch:
            $ choosen = "havetorch"
            
            show unlit at deadcenter
            with dissolve

            f "A sturdy branch topped with dry cloth soaked in pitch and an alchemical mixture. I can ignite it by striking it against the wall. These don’t last forever…"
            $ inventory_items.append("Torch")

            hide unlit
            with dissolve

            jump choice2_done

    label choice2_nopick:
        $ choosen = "notorch"

        f "I dont need this, I should just keep moving."

        n "You leave the torch behind"
        
        jump choice2_done

    label choice2_done:
    
        show shadow at right
    
        hide shadow with fastdissolve

        n "On the periphery of your vision, you notice unusual fleeting shadows. The demon must not be far off, and it has nowhere to run. One of you must perish today."
        
        n "Where will you go?" 

    label LookLeftLookRight:

    menu:

        "go left":
            jump choice1_left

        "go right":
            jump choice1_right

        "Go Forward":
            jump choice1_forward

    label choice1_left:

        $ darkness += 1

        scene leftroom
        with pixellate

        n "You see a room with a ladder leading down "
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

        jump golemchoice

    label choice1_forward:

        n "You go forward."

        jump choice1_done

    label goblinchoice:

    j "This isnt where my contract is, do I really want to abandon it?"

    menu:
        
        "Continue on abandon contract":
            jump meetgoblin
        
        "Go back and find the demon":
            jump nogoblin
    
    label meetgoblin:
        
        j "this job isnt worth my life, ill see where this leads"

        n "you choose to abandon your contract and proceed down the ladder"

        scene goblinroom
        with pixellate

        show goblin at deadcenter

        n "before you is a goblin girl"

        g "uhhh who are you what are you doing here? "

        n "she looks very confused to see you, she does not seem very threatening but you never know"

        n "more text about the sisuation.. she seems to be waiting for a response"

        label talktogoblin:

        menu:

            "friendly":
                jump friendlygoblin

            "flirt":
                jump flirtygoblin

            "attack":
                jump attackgoblin

        label friendlygoblin:
        $ choosen = "leftwithgoblin"
        j "says something friendly but not flirty"
        
        g "still pretty flirty, offers to show you back to the city"

        j "agrees"

        hide goblin
        scene city
        with pixellate

        jump witchstart

        label flirtygoblin:
        $ choosen = "leftwithgoblin"

        j "lays on the charm"

        g "blushes, offers to show you back to the city"

        j "agrees"

        hide goblin
        scene city
        with pixellate

        n "Julian leaves the crypt and demon alone with his new goblin companion"
       

        jump witchstart

    label attackgoblin:
    $ choosen = "goblindead"

    j "im not taking any chances not in this place die you fiend"

    hide goblin

    n "you violently attack and kill the goblin"

    j "it had to be done"

    scene city
    with pixellate

    n "eventually you find a path leading back to the city, contract abandon and nothing to show for it"

    jump witchstart

label nogoblin:

    j "no I can't abandon my mission now"

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
            $ choosen = "boltcutters"

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

    f "As unsettling as they are, they don’t present a threat unless I provoke them."
    
    show lit at deadcenter
    with dissolve

    play sound "torchlighting.mp3"

    hide lit
    with dissolve

   
    show ghost at offright:
        alpha .3
       

    f  "I can’t see it at all without my torch." 

    n "Maimed Wraithspawn,  This one suffered a major injury in life."

    n "its spine folds like an accordion, and its arm drags limply at its side." 

    f "It doesn’t seem to be in pain, at least. I wonder if it knows where it is?"


    show dog at offleft:
        alpha .3 
    
    n "Canine Wraithspawn - A beloved family pet, perhaps?"
     
    n "It paces throughout the chamber as if seeking out its master."
     
    f "Why was this innocent creature cursed to wander like this?"





    

    

    # This ends the game.

    return




































































    # The end little bitch

    return
