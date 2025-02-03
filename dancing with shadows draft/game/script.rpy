# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Narrator")
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
image golem = "golem.jpg"
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

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play music "main.mp3"

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

        $ darkness += 1

        scene rightroom
        with pixellate

        show golem
        
        n "You find yourself in some sort of store room. In the corner sits a very out of place golem"

        j "What is this creature doing here?" 

        if choosen == "golemactive":
            j "The thing is glowing, I should return to the task at hand"
            hide golem 
            scene room1
            jump LookLeftLookRight
        elif choosen == "goleminactive":
            j "I should leave it alone, I need to return to my mission"
            hide golem 
            scene room1
            jump LookLeftLookRight

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

    n "more golem and room desciptions"

    j " something something should I touch it?"

    menu:

        "touch the golem":
            jump touchgolem

        "leave it alone":
            jump leavegolem

    label touchgolem:

        n "you reach out your hand and gently touch the golem"
        n "more text about the magic activing"
        $ choosen = "golemactive"

        j "wow, I wonder what kind of magic that was but it doesnt seem to change anything but glowing"
        j "I should get back to task at hand"
        hide golem
        
        scene room1
        with pixellate
        
        n "where will you go?"

        jump LookLeftLookRight
    
    label leavegolem:

        n "you decide to leave it alone"
        $ choosen = "goleminactive"
        
        j "I should be touching things I have no idea what they do"

        n "seeing nothing else of note, you leave and return to the atrium"

        hide golem
        scene room1
        
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
    if choosen == "nolight"
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
