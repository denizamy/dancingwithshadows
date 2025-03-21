## The script of the game goes in this file.

define n = Character("Narrator",color="808080")
define d = Character("Archdruid",color="664D43")
define j = Character("Julian",color="0032FF")
define vj = Character("Julian",color="F0BD00")
define g = Character("Goblin",color="FF5DCF")
define u = Character("Demoness",color="732ADC")
define x = Character("Unknown Voice",color="732ADC")
define i = Character("Inya",color="ff5dcf")
define t = Character("Tess",color="9e0000")
define gl = Character("Golem",color="0BC4ED")
define a = Character("Adesse",color="732ADC")
define dh = Character("Dahlia",color="2F6A33")
define uw = Character("Unknown Warrior",color="9e0000")


image sword = "longsword2.png"
image shield = "Shield.webp"
image backpack = "backpack.png"
image unlit = "unlittorch.png"
image shadow = "shadow.png"
image lit = "lit.webp"
image dog = "dog.png"
image ghost = "ghost.png"
image hardtack = "shipbiscuit.png"
image canteen = "canteen.png"
image contract = "letter.png"



image goblin = "goblin.png"
image druid = "archdruid.png"
image blackscreen = "blackscreen.jpg"
image coin = "thecoin.png"
image golem = "golem.png"
image adesse = "adessefull.png"
image adesse_angry = "adesse_angry.png"
image adesse_distant = "adesse_distant.png"
image adesse_flirty = "adesse_flirty.png"
image adesse_flirty_melancholic = "adesse_flirty_melancholic.png"
image adesse_hurt = "adesse_hurt.png"
image adesse_neutral = "adesse_neutral.png"
image julian = "julian.png"
image tess = "Tess.jpg"
image contract = "contract.png"
image druidhouse1 = im.Scale("druidhouseP1.png", 1920, 1080)
image druidhouse2 = im.Scale("druidhouseP2.png", 1920, 1080)
image druidhouse3 = im.Scale("druidhouseP3.png", 1920, 1080)
image druidentrance = im.Scale("druidentrance.png", 1920, 1080)
image crypt = im.Scale("cryptday.png", 1920, 1080)
image cryptnight = im.Scale("cryptnight.png", 1920, 1080)


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
transform topright:
    xalign 1.0
    yalign 1.0

define longpixellate = Pixellate(5.0)

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
define quickdissolve = Dissolve(0.3)
define meddissolve = Dissolve (1.5)




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





define acceptdruid = False
define noacceptdruid = False
define golemactive = False
define boltcutters = False
define barricade = True
define havetorch = False
define notorch = False
define nolight = False
define light = False
define havecoin = False
define nocoin = False
define deadjulian = False
define leftwithgoblin = False
define leftwithadesse = False
define leftwithtess = False
define golemleftwithtess = False
define golemleftwithgoblin = False
define adessedead = False







# The game starts here ######################################################################

label start:

    scene blackscreen
    "Disclaimer: This is a very early release of this prologue. There will be bugs. You may direct bug reports and feedback to slack."

    "Many art assets, soundtracks, vfx, and sfx are works in progress."

    "Thank you for playing."

    play music "Deep Haze.mp3"

    j "Follow a hidden path down the alleys. Three lefts and a right, then close your eyes for twelve seconds."

    j "Remain calm and still, breathing shallowly, and keep your hands at your side..."

    j "It sounded like nonsense, but nonsense was my only lead."

    j "I pitied that beggar, and that's really why I'm here, I guess. Meager times create many beggars, with evil begetting evil and all that… "

    j "I guess this isn't a great evil if I'm just wasting my time here, in the grand scheme of things."

    j "He didn't want anything from me. I've never had a good grasp on balancing naïvety and cynicism..."

    j "Plus, I need the work. That was my last copper gone in the tavern. My equipment is in good shape, I'm healthy and have a full belly, for now at least. Okay, it's been at least twelve seconds."

    scene druidentrance
    with pixellate

    j ".…I really just can't believe it. Do all druids work in such secrecy, or just \"Arch\" druids when they're looking for a sucker to do their dirty work?"

    j "I'm here. This is what I came here for. There's no sense in wasting any more time."

    scene druidhouse1 
    with pixellate

    show druid at deadcenter:
        size (550, 1100)
        xalign 0.4
        yalign 0.5

    play sound "fireplace.mp3"

    n "A small, sincere smile colors the Archdruid's features upon spotting Julian - wicked away in an instant as he studies the young mercenary."

    n "Deep creases of worry fill the void in the elderly man's expression as he strains his eyes in the firelight, as if beholding something only seen by him."

    n "He gestures at the open seat next to the fire and speaks with a soft woody baritone - akin to the rumble of straining mine supports deep in the earth."

    "Magicians of any kind make me nervous. He seems friendly enough, but I shouldn't let my guard down."

    d "A friend told me you would come. Thank you for your interest in this assignment, young fellow. Take a seat and relax - this is a truly safe place. This world could use a few more of those."

    label druidchoice:

    menu:
        "Remain aloof":
            $ noacceptdruid = True
            jump druidchoice1
        "Take a seat and accept the Archdruid's hospitality":
            jump druidchoice2

    label druidchoice1:

        j "Ah yes, the vagrant…. I'd rather stand. I have a few scars from dealings with the 'magically inclined' and I'd rather not add another."

        n "A certain magic fades from the air, as if Julian's pronouncement conflicted with the place itself, despite the Archdruid remaining largely unfazed."

        n "Julian sighs, realizing his faux pas."

        d "I shan't begrudge the intemperance of youth."

        d "You are wise to distrust what you cannot understand, but how can we come to an accord without even a wink of it? I mean trust, of course."

        n "The Archdruid hastily finishes his pipe and rises to his feet, joining Julian in the foyer."

        n "For a man of his impressive age, he walks gracefully, almost without even a hint of sound."
        
        n "There is a twinge of melancholy or regret coloring his expression, but not his voice."

        jump druidresolution

    label druidchoice2:
        scene druidhouse3 with pixellate
        show druid at deadcenter:
            size (550, 1100)
            xalign 0.8
            yalign 0.5

        j "Your… "
        j "space is cozy."

        d "Thank you, young man."

        j "So - this job…."

        d "Perhaps a drink first. My treat, as the host."

    menu:
        "Accept the offer":
            $ acceptdruid = True
            jump acceptdruid
        "Decline":
            $ noacceptdruid = True
            n "Julian's reply is quick, with a hint of tension."

            j "I'd rather keep my wits about me. You have a job for me, right?"

            d "How impertinent of me."

            n "The Archdruid lets out a soft chuckle."

            d "A guest shouldn't be kept waiting."

            jump druidresolution

    label acceptdruid:

        j "I suppose… well, I don't see why not."

        play sound "pouring.mp3"

        n "The Archdruid rises from his seat and pours a dark orange liquid into two polished wooden cups. There's a bit of relief reflected in his dark eyes. He passes a cup to Julian, who hastily downs the contents."

        play sound "fireplace.mp3"

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

    n "Julian whistles slowly."

    j "No argruments here."

    d "To do battle with this fiend, you will need a silvered blade, crafted to scourge their impure flesh."

    d "To defend from its treacherous dark magic, a shield warded against such sorcery - but note, it requires a source of light, even if it is just a spark."

    d "Naturally, you will be allotted three days' rations for your journey."

    d "You'll find everything you need packed by the door. Complete the job, and return here for payment and debriefing."

    n "The neat bundle escaped Julian's notice entirely. It surely is where the druid said it was, but he couldn't be truly sure it was there when he entered."

    j "That seems straightforward enough. I kill the fiend with the blade you're providing me."

    j "No strings?"

    d "None."

    d "Do as advised and take care to protect yourself against its deceit and wiles. Remain resolutely focused, and stay true to your task… and yourself."

    j "No complaints from me, oldtimer. I'll be going then. If I'm not back in a week or two, you'll know to send the next guy."

    n "The Archdruid grunts. It's not abundantly clear if he found some humor in Julian's statement, or if he's annoyed."

    d "Reflect on my words, young man. Be safe and swift."

    hide druid

    scene druidentrance
    with pixellate

    n "Julian departs the druid's hut, and finds himself roughly where he expected - the same place he began the strange ritual to find the magician's hideaway."

    j "I'm not in any position to complain. One hundred crowns is more than I've seen in the last four jobs… "

    j "What could that oldtimer have meant by a demon's 'wiles'?"

    j "Maybe it's just an old way of speaking."

    j "I'd best not tarry."

    scene blackscreen
    with fade
    stop music fadeout 15.0

    if acceptdruid:
        j "That place was like a dream. I remember the important bits, for now, but I ought to write it down in case I forget."

        j "He said his name is 'Kolya', I think… I've never met someone with such a strange name."

        j "I haven't been so at ease and relaxed as long as I can remember. It must have been that 'Waldwine' he had me drink… "

        j "Come to think of it, he must have been jesting about the murals. Some of them are at least one hundred years old. "

        j "I suppose when you're as old as he is, everyone starts to look a bit alike. Maybe he just has one of those familiar faces."

        j "Maybe. I'll have time to think about this more later. For now, the job."

        jump crypttime
    elif noacceptdruid:
        j "I'll be six feet in the dirt if I ever deal with another magician after this job. If there is a next job."

        j "One hundred is about what I'd need to bother with another of these tricksters, and I have a nasty feeling it isn't the last of them on this journey."

        j "It's a pity he didn't give me an advance - I could pawn off this blade and shield and be two weeks distant from that creep."

        j "One hundred crowns is worth the effort, if it doesn't kill me."


    ########################################

    label crypttime:


    play music "Floating Cities.mp3"

    n "Julian undergoes a daylong travel through the city, to the outskirts. "

    n "Primarily, Julian spent the time reflecting on his mission and the Archdruid, and speculated on what was to come. "

    n "These days, he didn't get much comfort in anything, and this journey was no exception. "

    n "He wasted no time attending to the dubious duty he took as his yoke, all in the promise of gold."

    scene crypt with fade

    #########################################

    n "The Archdruid's contract led Julian to a crypt on the outskirts."

    n "Along the way, he heard rumors of locals being harassed when mourning their dead, statues and monuments within the crypt being toppled, and unsettling shadows darting around the crypt, irrespective of the lack of wind and torch."

    "The Archdruid told me my quarry is a Demon of Shadow - not a trivial, nor a major demon. I should be on my guard."

    "The blasted thing must be inside. I should keep stock of my belongings before I head in."

    # i can't get this shit to transition smoothly without the fucking transparent checkerboard bullshit


    scene blackscreen
    with quickdissolve

    show contract at deadcenter

    j "Sealed with a wax stamp. Strange, it looks like the monastery sigil."

    j "I recall it reads: Slay and banish the presence, whatever it may be, from this formerly sanctified place of rest."

    hide contract
    with fastdissolve

    show sword at deadcenter

    n "A steel arming sword plated with silver along the edge."

    j "I might stand a chance with this blade, if I’m lucky."

    hide sword
    with fastdissolve

    show shield at deadcenter

    j "The sheen on this steel heater is phenomenal, and as long as there is even a scant amount of light, the Archdruid reassured me none of the demon’s shadow magic can harm me."

    hide shield
    with fastdissolve

    show canteen at deadcenter

    j "I don't even want to think about hardtack if I can't soften it up first. It's about as hard and appetizing as a brick."

    show hardtack at deadcenter

    j "And the waterskin..."

    j "It's filled with three-day old small beer. Smells sour. I probably shouldn't, unless I really need to."

    #nasty lil bottle of beer image maybe?

    hide backpack
    with dissolve

    j "That's it."

    show black with dissolve

    show crypt at deadcenter


    j "Okay, enough stalling... let's do this."

    menu:

        "Enter Crypt":
            jump choice1_enter

    label choice1_enter:

    scene room1
    with pixellate
    label atrium:

    n "A large stone room, far underground."

    n "As you enter, you hear hydraulic mechanisms automatically shut the large steel gate behind you."

    play sound "gateclose.wav"

    scene closinggate


    j "A security measure by the townsfolk, surely."

    n "You are trapped down here with the demon, and it with you, until one of you perishes."

    n "Torchlight glints off of brass embellishments on the sarcophagi populating this moderately impressive tomb."


    show shadow at deadcenter
    hide shadow with quickdissolve

    show shadow at topright
    hide shadow with quickdissolve

    n "On the periphery of your vision, you notice unusual fleeting shadows. The demon must not be far off, and it has nowhere to run. One of you must perish today."

    scene room1
    with pixellate

    n "A great stone arch allows passage further in this dark place."

    n "It seems the townsfolk or druids left a torch here for your use."

    j 'Oh, a torch.'

    label picktorch:

    menu:

        "Pick up Torch":
            jump choice2_torch

        "Leave it":
            jump choice2_nopick

    label choice2_torch:
        $ havetorch = True
        $ notorch = False

        show unlit at deadcenter
        with dissolve

        j "I should take it. A light source would be useful in this dark place… especially with a demon of shadow lurking nearby."
        $ inventory_items.append("Torch")

        j "A sturdy branch topped with dry cloth soaked in pitch and an alchemical mixture. I can ignite it by striking it against the wall. These don’t last forever…"

        hide unlit

        play sound "torchlighting.mp3"

        n "You strike the torch along the stone walls."


        show lit at deadcenter
        with dissolve
        hide lit
        with dissolve

        jump choice2_done

    label choice2_nopick:

        hide unlit

        j "I'll be fine."

        n "You leave the torch behind."

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

        "Pick Up Torch" if not havetorch:
            n "Upon reflection, the torch is still there."
            jump choice2_torch

    label choice1_left:

        $ darkness += 1

        j "… Huh. "

        j "This looks a lot like an access tunnel to the city's sewers. It would make sense for something like this to be here in the outskirts, I suppose."

        j "It seems a bit insensitive to connect the sewers to a crypt, but I'm not the city planner."

        j "They're working with what space they have, I guess."
        jump goblinchoice

    label choice1_right:

        if golemactive:
            j "I'd rather not mingle any more with sorcerous experiments left in storage for a hundred years."
            j "Like I said, it's somebody else's problem now."
            j "If they want me to take care of it, well, another hundred crowns would be nice."
            hide golem
            scene room1
            jump LookLeftLookRight
        elif boltcutters:
            scene warehouse
            jump golemtouch
        elif barricade:
            jump tunnel

        jump golemchoice

    label choice1_forward:

        n "You go forward."

        jump choice1_done

    label goblinchoice:

    j "The entrance is blocked by an iron grate. The bars are serviceably thick, but they're made of low grade iron with a lot of corrosion."

    j "If I found something to bend or break these, maybe I could exit to the city."

    j "Do I want to do that? I'd be abandoning my contract."

    j "Maybe I'm not cut out for this business involving magicians and demons."

    j "I'll have to give it a think."

    if boltcutters:
        jump cutbolt

    n "Julian returns to the Atrium."

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

        j "It's time to get the hell out of here, and quick."

        j "I'll be damned twice if I end up dead doing the bidding of an out of touch old fart."

        queue sound "cutbolt.mp3"
        queue sound "boltfloor.mp3"

        n "Julian makes quick work of the bolts. The way to the sewers is clear, even though the hydraulic lock to the crypt holds fast."

        n "There is a way out yet, even if it is a dismal path."

        scene goblinroom
        with pixellate

        play music "Inya Theme (First Encounter).mp3"

        j "What's that?"

        show goblin at deadcenter:
            size (1500,1700)
            xalign 0.5 yalign 1.0
            linear 6.0 yalign 0.0
        pause 6.5
            
        hide goblin
        with dissolve
        

        show goblin at deadcenter:
            size (550,800)
        with dissolve

        n "The lurking creature speaks, with a scratchy, but distinctly feminine voice."

        g "Heya. I've been watching you."

        j "You what? I… What the hell are you?"

        g "Haha. I'm a goblin."

        g "You've heard of goblins, right?"

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

        g "Some tales have truth to them, and some don't. The bars were disappointing - but now they're not!"

        g "Thanks Mr. human guy. What's your name?"

        j "Julian. Julian Grymwald."

        "I really need to stop being so impulsive."

        j "You're not a magician, or a magician's familiar… right?"

        g "Oooh, no."

        g "I'm not familiar with them, but I'd like to be. I haven't even met one, but the farmers are afraid of them too, like you."

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

        g "When I was young, a bit too young, I was exiled from my tribe on account of my 'difference.'"

        n "The goblin gestures at herself, presumably indicating the ivory color of her skin, her pink eyes, and white hair."

        g "It's isolating, living alone, but I've got really good at it. My blowgun makes hunting easy. Just aim and… shoot."

        n "The goblin demonstrates, pointing the barrel of the blowgun at Julian. She takes a quiet, deep inhale, and mimes the action, exhaling through her nose."

        "I'm starting to reconsider this course of action… She seems friendly enough at least, if a bit unhinged."

        g "You'd find what I eat gross, but it's not gross for goblins. Well…"

        g "I've made a bit of a life for myself up here. Down here. Wherever 'here' is at the moment."

        g "I'm really familiar with the sewers, because listening to the same rumors and legends gets pretty boring. I keep myself safe with my blowgun, aaaaannnnnd…"

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

        n "Julian deliberately nods, affirming their agreement to call Inya 'Inya.'"

        j "Inya, do you know how I might get to the city?"

        i "Yeah, it's above you. Are you dumb?"

        j "I'm starting to feel that way, I confess… Can you lead me there, to the streets?"

        i "Oh! Sure! We can go together."

        j "Thank you."

        scene endingscreen
        with pixellate

        n "Julian, led by Inya, made their way to the streets."

        n "Silently indicating the direction of a culvert, Inya hurriedly catches up to Julian, and tugs on his arm to get his attention. She looks oddly emotional and introspective."

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

        j "Sure. I'll see you then, Inya."

        n "The goblin giggles."

        i "Yeah you will. I'll see you first though."

        n "The newly acquainted pair part, for now - Inya, back to the sewers, and Julian, to an uncertain fate in an unfriendly world."

        define leftwithgoblin = True
        $ leftwithgoblin = True

        if golemactive:
            jump golemstart

        jump witchstart


    label attackgoblin:

    "I don't really know what I'm looking at, but I don't like it. It's time to get out of here - no witnesses."

    j "I'm actually a landed noble - the baron."

    j "I'm here on a mission to investigate rumors of goblins personally, to give the effort a hands-on approach."

    g "I don't know what that is or parti- grk…"

    hide goblin

    n "Approaching slowly during the conversation, Julian strikes down the goblin with his blade before she can react."

    "Well, that was easy. I feel guilty, but a bit less guilty this go around. I'd best keep moving and not think about it too hard."

    n "Julian, indeed, made his way through the sewers, into the city."

    n "It was just as dreadful and stinky as he thought it would be, and in the end, he had nothing to show for his effort."

    n "Alone he remained, with only the stolen goods loaned to him by the Archdruid to keep him company."


    scene endingscreen
    with pixellate

    j "I had best lay low for a while. That magician will inevitably send cronies after me if he really did have one hundred crowns to just throw around."

    j "What did he call these things - a silvered blade and a shield capable of deflecting dark magic?"

    j "I'll have to keep an ear to the ground for the right buyers."

    define goblindead = True
    $ leftwithgoblin = False

    if golemactive:
        jump golemstart


    jump witchstart

label nogoblin:

    j "Lucky me, I have just the right tool for the job - but I can't be serious with this. I've come all this way for nothing?"

    j "One hundred crowns could keep me fed for months, and I could buy some new equipment, not even considering the connections the Archdruid might have for me."

    j "I'm better than this. Let's be thorough."

    n "You return back to atrium."

    scene room1
    with pixellate

    n "Where will you go?"

    jump LookLeftLookRight

label golemchoice:

    n "Before you is tunnel that is barricaded by a few simple boards."

    j "Ugh, do I really want to be doing this?"

    j "There's a quarter inch of dust covering literally everything. If I found this demon in such a cramped space, I don't think I'd even be able to swing my sword…."

    menu:

        "Dismantle Barricade":
            $barricade = False
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

if havetorch:
        j "I should be on guard. It's unusually stuffy in this tunnel, and black as pitch."

        j "It reminds me of an abandoned factory, or that mage's study years past…"

        j "Well, here goes nothing."

        jump warehouse

elif notorch:

        j "I should come back with a light source."

        j "This place stinks of a trap. It would be foolish to fumble around in the dark and step on a nail, or worse."

        n "You go back the way you came."

        scene room1
        with pixellate

        n "Where will you go?"

        jump LookLeftLookRight

label leavegolem:

        j "No, something is wrong about this place. It's like it has been pulled from a different place and time."

        j "I might come back to it, if this creature isn't anywhere else in this crypt, provided I can think of a plan…"

        n "You go back the way you came."

        scene room1
        with pixellate

        n "Where will you go?"

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

            n "You sort through the rubble and find a set of bolt cutters."
            $ boltcutters = True

            j "Huh. These might come in handy, I guess. Nobody else is using them, I might as well bring them along."

            jump golemtouch

        "Turn back":
            j "Well, this is a dead end."

            j "There's plenty of this crypt left to explore. The demon is here somewhere."

            n "You go back the way you came."

            hide golem

            scene room1
            with pixellate

            n "Where will you go?"

            jump LookLeftLookRight

label golemtouch:

        j "There is some strange text on these stones. Strange, it almost looks like an arm…"

        j "Maybe this was a sculptor's studio? That doesn't seem quite right."

menu:
        "Touch symbol":
            $ golemactive = True
            play sound "rocks.mp3"
            n "The pile of rubble begins to shake, and the runes in the rubble pile begin to glow with a dim blue light."

            j "I'm not getting paid enough for this. This isn't a demon, it's somebody else's problem. I'm getting out of here."

            n "You go back the way you came."
            hide golem

            scene room1
            with pixellate

            n "Where will you go?"

            jump LookLeftLookRight

        "Turn back":
            j "I'd better not. There's plenty left to do here. I'll think about it."

            hide golem

            scene room1
            with pixellate

            n "Where will you go?"

            jump LookLeftLookRight


label choice1_done:
    scene darkhall1
    with pixellate

    "The rooms ahead are shrouded in oppressive darkness - likely the work of this demon."

    if havetorch:
        jump choice3_torch
    elif notorch:
        jump choice3_done

    label choice3_torch:

    play sound "torchlighting.mp3"

    show lit at deadcenter
    with dissolve

    scene lithall
    with pixellate

    hide lit
    with dissolve

    j "I should be well prepared for the push ahead. If I squint, I can see solid silhouettes deeper in this place."

    jump choice3_done

    label choice3_done:

    j "Let's keep moving."

    scene wrathhall
    with pixellate

    n "A massive subterranean corridor. Sarcophagi line each side of this room. The rooms ahead are shrouded in oppressive darkness."

    if notorch:
        jump killbywraith

    show lit at deadcenter
    with dissolve

    play sound "torchlighting.mp3"

    hide lit
    with dissolve


    show ghost at offright:
        alpha .3

    j "I vaguely remember texts from the monastery describing the spawn of demons of shadow… it's been a while, but I think they're called Wraithspawn."

    j "They are the creations of my quarry, if I'm right.. As unsettling as they are, they don’t present a threat unless I provoke them - so long as my torch lasts."

    j "They appear as they did at death - the old, the infirm, the maimed, and the beloved pets of the townsfolk as well."

    j "They didn’t embellish their tales. This is grim indeed."

    n "A dark silhouette like a blot in space."

    n "This one suffered a major injury in life."

    n "Its spine folds like an accordion, and its arm drags limply at its side."

    j "It doesn't seem to be in pain, at least. I wonder if it knows where it is?"


    show dog at offleft:
        alpha .3

    n "A beloved family pet, perhaps?"

    j "It paces throughout the chamber as if seeking out its master."

    j "Why was this innocent creature cursed to wander like this?"


    hide dog
    hide ghost

    jump monumentchamber

    label killbywraith:
        $deadjulian = True

    j "It's so dark. Something here is wrong… It's too dark."


    label badend:
    scene endingscreen
    with pixellate

    n "In the total darkness of the crypt, Julian is slain by the lurking spawn of the Demon of Shadow."

    n "This story, however, is far from over. Perchance, even Julian still has a role to play."

    if golemactive:
        jump golemstart
    jump witchstart


    label monumentchamber:

    scene monument
    # Room 3 - Monument Chamber

    n "One thing is certain, this place has been vandalized."

    n "Statues are torn from the podiums from which they rested, and stone slabs commemorating the deeds of the heroic dead have been toppled."

    n "The floor is littered with debris and dust. Despite this, there isn't a single footprint to be seen."

    n "Aside from the ladder down and the way you entered, it appears all of the connecting chambers are blocked by collapsed rubble."

    j "The locals surely wouldn't do this."

    j "I should be on guard and gather my bearings before pushing ahead."

    if nocoin or havecoin:
        jump aftercoinchoice

    menu:
        "Look around":
            n "You look around and see an antique silver coin."

    show coin at deadcenter
    #find a less stupid coin image with a transparent background

    j "The old farts at the monastery and maybe some of the druids remember when these were minted."

    j "They're at least half zinc, more than a quarter copper, but there's a bit of silver in there... I guess that's why they're called 'silver coins.'"

    j "It's strange to find something like this here."

    j "There is a puncture near the edge of the coin, as if it were attached as a necklace."

    j "How odd. Maybe one of the townies dropped it while fleeing...."

    menu:

        "Ignore it":
            jump choice2_ignore

        "Take the coin":
            jump choice2_take

    label choice2_ignore:
        $nocoin = True

        j "Something is off about this. I should trust my gut. Much is amiss in this tomb, and I had best not tempt the spirits. One monster is enough…"

        n "You leave the coin and move on."

        hide coin
        jump aftercoin

    label choice2_take:
        $havecoin = True

        show coin at deadcenter
        with dissolve

        j "Whatever, it's mine now. Whoever lost it is long dead. In their place, I wouldn't begrudge me."

        $ inventory_items.append("coin")

        hide coin
        with dissolve
        jump aftercoin

    label aftercoin:
    n "Despite the flickering flame of the torch, the shadows stir - and speak!"

    # sound

    n "Haphazardly drawing his blade, Julian stumbles backwards, caught off guard."

    x "Mortal, the light you bring to my domain is most unwelcome. Leave this place, or meet your end."

    # sound

    x "Return your filchings to their proper place, and forget all you have seen here."

    j "Unsettling. The torch has sent the fiend fleeing - I had best pursue it..."

label aftercoinchoice:

menu:
        "Turn back":
            scene blackscreen with pixellate
            hide monumentchamber with dissolve
            hide monument with dissolve

            j "I need to get my bearings. I'm not sure I'm ready for all this just yet. I need to be absolutely sure before I hunt down this creature."
            scene room1 with pixellate
            jump LookLeftLookRight
            with dissolve


        "Continue forward":
            jump memorials

label memorials:
            n "Dedicated to heroes who were stalwart defenders of the people - soldiers and sellswords alike. Many of them fell to demons."

            j "It seems like a bit of a petulant tantrum, doesn't it? Perhaps my expectations of these creatures were too lofty."

            n "A ladder in the center of the room, leading down to the peasant's graves. It looks freshly disturbed."

            j "What purpose could this demon have disturbing the remains of the destitute?"


menu:
        "Go down the ladder":
            $goblindead = False
            $leftwithgoblin = False
            jump ladderdown

        "Return to the atrium":
            n "You return to the Atrium."
            scene room1
            n "Where will you go?"
            jump LookLeftLookRight
            with longdissolve

label ladderdown:

"The shadows dance here, I must be close. There is a narrow walkway encircling an open pit, where the less fortunate are tossed to rot."

"At least these are embalmed - a small courtesy for the poor."

"It's a dead end. The demon is surely here. But where?"

"Ugh, I don't think I can bear this stench for much longer…"


n "There - on the other side of the platform, the shadows take shape - the demon manifests."
# sound

"… … …"

"What in the world?"

#show adesse with slide Down

show adesse_neutral:
    size (1240, 1754)
    xalign 0.5 yalign 1.0
    linear 6.0 yalign 0.0


u "Many other mortals have fled, yet here you are…"

u "Did you mean to assail me here, in my chosen domain? Are you lost, Julian?"

label fightorquestiondemoness1:

    menu:
            "Fight the demoness":

                j "You will haunt this place no longer, foul demon! Face me!"

                jump fightdemoness1

            "Question the demoness":

                j "Are {i}you{/i}? I see - you divined my name."

                "(stumbling over words)"

                j "You, uh... look different from uh, what I expected."

                jump questiondemoness1

label fightdemoness1:
    hide adesse_neutral

    show adesse_angry at deadcenter:
        size (1240, 1754)
        xalign 0.5 yalign 0.0
        


    n "The demoness fires a barrage of needle-like spines of solid shadow."

    menu:
        "Block":
            jump blockdemoness1

        "Attack":
            jump attackdemoness1

label blockdemoness1:

    j "I can block them with my shield!"
    n "The dark magic spines melt like snow against Julian's blessed shield."
    n "The demoness gathers energy for her next spell, giving Julian an opportunity to strike."
    jump fightdemoness2

label attackdemoness1:
    j "I can strike her now!"
    n "Julian's opportunity to strike is lost as the demoness fires another barrage of needle-like spines of solid shadow."
    jump fightdemoness2

label fightdemoness2:

    menu:
        "Block":
            jump blockdemoness2

        "Attack":
            jump attackdemoness2

label blockdemoness2:

    n "Julian's opportunity to strike was squandered. The demoness finishes casting her spell, sending razorblades of darkness hurtling towards Julian from all directions."

    n "Perhaps thanks to his armor or an absurdly good stroke of luck, he manages to cling to life and consciousness, but only just."

    jump demonessresolution1

label attackdemoness2:
    n "A desperate, vicious strike. A fateful strike. Abandoning caution, Julian hurtles towards his foe."

    n "In a confluence of circumstance and power, desperation and need, he executes an overhead swing with his Demonslaying Blade."
 

    #nasty cranium slicing sound

    hide adesse_angry
    with dissolve

    show adesse_hurt:
        size (1240, 1754)
        xalign 0.5 yalign 0.0


    n "The demoness's self-satisfied expression fades as the blade slices through her cranium."

    hide adesse_hurt
    with dissolve

    j "There's… no blood. But it's gone. I can feel its absence."

    jump demonessresolution2

label demonessresolution1:
    $leftwithtess = True

    hide adesse_neutral


    n "Julian's vision blurs as he bleeds out against the cold stone."

    scene blackscreen
    with longdissolve

    n "Revealed in blood-blurred snapshots as he blinks, unbelievably, he sees a warrior doing battle with the Demon of Shadow."

    n "A few moments of combat pass, and then silence."

    n "The room fills with the smell of sweet sulfur, and Julian, losing consciousness, feels a slight stab of pain."

    scene monument
    with longdissolve

    n "His hero - this masked avenger, crouches down to check his vitals and speaks in a soft, deep female voice."

    show tess

    uw "You shouldn't be here. Did Nikolai put you up to this?"

    n "The warrior sighs, audibly unbuckling the clasp securing her pack, and withdraws salves, a splint kit, a needle, and thread."

    uw "If you can hear me… I'm going to tend to your wounds. This is going to hurt a lot."

    uw "You've proven your bravery, soldier. I need you to hang in there just a little bit longer."

    n "The warrior sutures Julian's wounds and stops the worst of his bleeding."

    n "Time lost meaning to Julian, amidst the agony of his countless injuries. And yet, somehow, he clings to consciousness."

    uw "C'mon, stay with me… you can't die on me just yet."

    uw "I've tended to your scrapes and stopped the bleeding. You're doing great, but we're not out of the woods yet."

    uw "I'm going to set your leg. Bite down if you need to, or you're going to bite through your tongue and suffocate on your own blood."

    n "Julian's eyes widen, settling on his broken leg - snapped like a twig by the demoness's dark magic. Profound, terrifying force!"

    n "Bleary-eyed, Julian scans the room. There is no trace of the demon - save a suspicious, soft-looking stone where she fell."

    n "Likewise, the shadows have stopped moving of their own accord. He looks over to his savior."

    n "Until she spoke, he had no indication this powerful warrior was a woman."

    n "She eschews armor for green and brown traveler's leathers, adorned with protective talismans. Her longboots are characteristic of the locality."

    n "Her saw-toothed metal staff and iron mask strike Julian as distinct, but wracking his brain, he comes up with nothing for their origin."

    n "Whomever she is, she is a skilled warrior and healer."

    n "The warrior slips a bit made of hard rubber into Julian's mouth and prepares to set his leg."

    uw "Stay with me here..."

    uw "3..."

    uw "2..."

    uw "1..."

    n "An audible crunch disturbs the silence of the chamber as she sets the bone."

    n "Julian, despite his wounded and half-conscious state, lets out a muffled wail, biting down hard on the bit."

    uw "We're almost done. Hang in there. You're doing great."

    n "The warrior removes his plated leggings and rips his pant leg, using the material to bind the splint."

    uw "I'm going to pick you up. It's going to hurt a bit. You really shouldn't be moved in this condition, but we're not exactly swimming in options."

    uw "You're in good hands. You can leave as soon as you have recovered, but I'm going to have some questions for you first."

    uw "You can call me Tess. I think you're brave, for whatever that's worth."

    n "Tess carefully heaves Julian over her shoulder. Julian passes out shortly thereafter."
    $leftwithtess = True

    scene blackscreen
    with longdissolve

    stop music fadeout 15.0

    jump neutralend

label demonessresolution2:
    $ adessedead = True


    j "The deed is done. The demon is vanquished. Strange, it seems the foul harpy left a trinket among her remains. A soft, sulfurous stone - proof of my victory. It’s a shame to fell such a striking beauty. It invaded my mind… and seemed to know me."

    j "Perplexing, and dangerous. Why do I feel a sense of loss? An emptiness, left in the wake of my fallen foe? I had best put aside these thoughts. I should return promptly to the Archdruid, for he will want word of my success."

    scene blackscreen
    with longdissolve

    stop music fadeout 15.0

    jump neutralend

label questiondemoness1:

    hide adesse_neutral
    show adesse_angry:
        size (1240, 1754)
        xalign 0.5 yalign 0.0

    n "The demoness narrows her eyes and scowls."

    u "My nature dictates me to assume a form that resonates with the desires of those who behold me. Perhaps you would be best served reflecting on your own preferences..."

    u "This parley tires me - accept this small mercy before I reconsider."

    u "I have harmed none of the hapless fools who wandered into my domain, and I extend the same courtesy to you - in honor of the dead."

    u "This place is meant for the grieving, is it not? Leave me to grieve."

    label fightorquestiondemoness2:

    if havecoin:
        menu:
            "Fight the demoness":

                n "Drawing your blade, you steel yourself for battle."

                j "The Archdruid cautioned me against the lies of your kind. You’re afraid, monster - and I am no fool."

                j "If you have an ounce of honor, face me. I offer you a duel. Your life or mine. Let us settle this now."

                jump fightdemoness1

            "Question the demoness":

                n "Contemplating the small atrocities this fiend has personally wrought in this tomb, you withdraw the antique coin you collected on the upper levels."

                j "Your kind only sows grief with every new widow and orphan you leave to face this world alone. To grieve, you have to feel loss. What could you possibly know of grief?"

                jump questiondemoness2
    menu:
        "Fight the demoness":

            n "Drawing your blade, you steel yourself for battle."

            j "The Archdruid cautioned me against the lies of your kind. You’re afraid, monster - and I am no fool."

            j "If you have an ounce of honor, face me. I offer you a duel. Your life or mine. Let us settle this now."

            jump fightdemoness1


label questiondemoness2:

    hide adesse_angry
    show adesse_distant:
        size (1240, 1754)
        xalign 0.5 yalign 0.0

    n "The demoness's eyes look distant, and she appears forlorn."

    n "Her gaze drifts from the silver coin to the pit between you and her - this pit where the bodies of the destitute are unceremoniously thrown and left to rot."

    u "There was another mortal, not unlike yourself. We shared a bond, of sorts."

    u "Like you, she lived a fickle and fleeting life, and was taken from me - like you, she hesitated, and like you, she showed me mercy. She rests here, in this muck of unfortunates."

    $leftwithadesse = True

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

    u "You are most unusual and merciful for one who has lived such a dastardly life, Julian. Only an orphan such as yourself could truly understand that sting of loss…"

    u "The druids caution many against the worst atrocities of my kind, and they speak true…  We part, monster and murderer. We shall meet again."
    hide adesse_neutral with meddissolve
    n "The demoness vanishes, and the dancing shadows in the room stall to a halt."

    j "What an ordeal… Demons are both very like and very unlike how Archdruid described them. I couldn’t have possibly prepared for this."

    j "Even so… I can’t help but have my thoughts wander to that beshadowed beauty. It’s a pity I never learned her name - although I shudder at the thought of meeting again."

    j "She seemed quite confident we would… but if she knows the worst of my crimes, how could she see anything good in me?"

    j "Perhaps… I can only be my truest, deepest self with a demon. Nay, I should banish the thought."

    jump neutralend

label demonessresolution4:

    n "The dark energies dance in the room, possibly reflecting the demon’s state of mind. Her expression softens. She seems incapable of tears, perhaps due to her nature."

    u "I am called Adesse, mortal. You have given me much to consider - but I believe this encounter draws to an end."

    a "I shall say my final farewell and depart. You may tell your superiors whatever you choose - but this is not our last meeting, Julian."

    a "You're… intriguing - and you remind me of someone I once loved."

    hide adesse_distant
    show adesse_flirty:
        size (1240, 1754)
        xalign 0.5 yalign 0.0

    n "A bittersweet smile colors Adesse's ethereal features moments before she vanishes, and the dancing shadows in the room stall to a halt."

    hide adesse_flirty with meddissolve
    j "She just vanished. Well, that's great. Am I cursed now, haunted? I should be more worried about that, probably… but even though it has been but a moment, I can’t keep my thoughts off of her."

    j "I want to see her again. Adesse… such a peculiar name. I wonder if it was given to her."

    j "If I have been deceived, surely I will find the truth of things - for now, I shall report my success to the Archdruid."

    jump goodend

    label neutralend:

    #if the golem is been activated, then jump to golem waking up
    if golemactive:
        jump golemstart

    jump witchstart

label goodend:

    #if the golem is been activated, then jump to golem waking up
    if golemactive:
        jump golemstart

    jump witchstart

label golemstart:

    play music "Myst on the Moor.mp3"

    scene warehouse
    with pixellate

    gl "Sensation… A touch…"

    gl "The touch is familiar, but so distant…"

    gl "Distant like another life."

    gl "Sculpted from stone, was I. Once inert, once lifeless, but given life by my creator. Where is my creator? Who am I?"

    gl "The memories are dark, with spots of color - feelings, and meaning almost indecipherable in the static."

    gl "The music is gone. This one's creator is missing. There is nothing left. I must press on."

    label golemmirror:

    define golempulltogether = False
    define golembreakmirror = False

    menu:
        "Pull yourself together":

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

    $ golempulltogether = True

            
    menu:
        "Break the Mirror":

            #TODO: Add sfx of glass breaking, image of broken mirror, etc.

            gl "Memories of fury - of violence. I wish not to reflect. I wish not to suffer. I must not yearn."

            gl "… I press on."

            $ golembreakmirror = True

            jump golempresson

        "Leave Room":

            jump golempresson

label golempresson:

    #TODO: grayscale depiction of the cramped tunnel Julian passed through, with a trail of footprints / implied darkvision

    scene tunnel

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

    scene room1

    n "The Golem retraces Julian's steps to the crypt's atrium. It studies its surroundings - a sealed door to its left, unfamiliar stonework leading to an access tunnel of some kind dead ahead, and a path deeper into the crypt to its right."

    gl "It is now clear to this one a considerable amount of time has passed in this one's reverie. I must press on."

    menu:

        "Press on ahead":

            jump golemgoblin

        "Press on to the right":

            jump golemadesse

label golemgoblin:

    if leftwithgoblin:
        jump golemescape1

    elif goblindead:
        jump golemescape2
    jump golemescape3

label golemescape1:

    n "The footsteps continued in this direction. The Golem tirelessly pursues this interloper - and its objective, whenever it determines what its objective may be."
    scene goblinroom
    with pixellate

    gl "The interloper joined another. This one's senses indicate one is male - human. The other is . . . an unknown female."

    gl "What am I? What I was once is of little consequence - memories are no more."

    menu:
        "I am male.":
            gl "This one's creator sculpted this one in his perfect image. Like my creator, I am male."
            $pronoun = "He"
            $pronouns = "his"
        "I am female.":
            gl "This one's creator sculpted this one to serve as his counterpart and compliment. I am female."
            $pronoun = "She"
            $pronouns = "her"
        "I am something else.":
            gl "This one is… this one. I am neither male nor female. This one's identity is this one's. Flesh, I am not. Mortal, I am not. I have been created for a purpose. This purpose is undefined. This purpose must be defined."
            $pronoun = "It"
            $pronouns = "its"

    n "[pronoun] concentrates, divining information about 'the interloper' and his acquaintance using [pronouns] recalled latent magical ability to do so."

    "Skill recalled: Divination"

    gl ". . . The interloper is a human male named Julian. He is deeply conflicted. His life is unpredictable and dreary."

    gl "He has little trust. He was curious, cautiously hopeful and bemused."

    gl "His acquaintance is named Zanya, although she has assumed the alias 'Inya.' Undocumented species. Humanoid. Assessing . . ."

    gl "Likely an offshoot of humans engineered by sorcery to survive in inhospitable conditions. Slightly extended lifespan and hardiness."

    gl "Reduced temperament and intellect. She was excited, insecure, and infatuated. Strong counterpoint to general emotional state."

    scene blackscreen
    with longdissolve

    scene endingscreen
    with longdissolve

    gl "I have many questions. Perhaps this interloper will elucidate my purpose."

    n "[x] pursues Julian and Inya through the sewers, tirelessly. [pronoun] takes stock of Inya's deviation from Julian's path, but resolves to pursue Julian in the hopes of finding answers - and a purpose."
    jump witchstart

label golemescape2:

    n "The footsteps continued in this direction. The Golem tirelessly pursues this interloper - and its objective, whenever it determines what its objective may be."
    scene goblinroom
    with pixellate

    gl "The interloper joined another. This one's senses indicate one is male - human. His name is Julian Grymwald."
    gl "The other is . . . an unknown female. Deceased. The female was named Zanya, although she assumed the alias 'Inya.'"

    n "The Golem gingerly picks up the goblin's corpse, handling it with care. It inspects the wounds, then carefully deposits the goblin where it previously lied."

    n "Tenderly, the Golem closes the goblin's eyelids."

    n "The Golem concentrates, divining information about 'the interloper' and his acquaintance using their recalled latent magical ability to do so."

    "Skill recalled: Divination"
    #different text color maybe?
    gl "Fear was the last emotion she felt. A sting of betrayal - fading optimism and curiosity."

    gl "The interloper - the intruder in this one's master's domain fled. Senseless cowardice. Shame and guilt. The interloper has much to answer for. This is not the first murder he committed. He shall answer for his crimes."

    n "Using its recalled skill, the Golem pondered on what this information meant, and how it relates to it."

    gl "What am I? What I was once is of little consequence - memories are no more."

    menu:
        "I am male.":
            gl "This one's creator sculpted this one in his perfect image. Like my creator, I am male."
            $pronoun = "He"
            $pronouns = "his"
        "I am female.":
            gl "This one's creator sculpted this one to serve as his counterpart and compliment. I am female."
            $pronoun = "She"
            $pronouns = "her"
        "I am something else.":
            gl "This one is… this one. I am neither male nor female. This one's identity is this one's. Flesh, I am not. Mortal, I am not. I have been created for a purpose. This purpose is undefined. This purpose must be defined."
            $pronoun = "It"
            $pronouns = "its"

    scene blackscreen
    with longdissolve

    scene endingscreen
    with longdissolve

    n "The Golem followed Julian's trail through the sewers, exiting to the city streets. [pronoun] found [pronouns] purpose and [pronouns] objective."
    n "The conclusion and confrontation between the golem and Julian will play out, in time."

    jump witchstart

label golemescape3:
    n "The footsteps deviate to the left. This gives the Golem pause."

    menu:

        "Reconsider your pursuit, and investigate the access tunnel":
            gl "This merits a closer investigation. The interloper cannot elude this one forever."
            gl "This one does not sleep. This one does not eat. This one shall pursue this one's quarry tirelessly."

            jump golemescape4

        "Pursue the Interloper":

            jump golemadesse

label golemescape4:

    n "The way is blocked by iron bars. The Golem pauses, reflecting on the obstacle."

    "Skill recalled: Surge of Strength"
    #different text color maybe?

    n "Mere iron cannot stop the Golem. It snaps the bars like insignificant twigs."
    #bar breaking sfx

    scene goblinroom
    with pixellate

    g "Whoa! Hey! Don't hurt me!"

    play music "Inya Theme (First Encounter).mp3"
    
    show goblin at deadcenter:
        size (1500,1700)
        xalign 0.5 yalign 1.0
        linear 6.0 yalign 0.0
    pause 6.5
            
    hide goblin
    with dissolve
        

    show goblin at deadcenter:
        size (550,800)
    with dissolve
        
  
    n "A tiny form, compared to the Golem, stirs in the darkness. A moment of eye shine in the scant light betrays her position to the Golem."

    n "This development gives the Golem pause, who reflects on this development."

    "This creature presents me no threat. It appears to carry a blowgun, which fires darts traditionally bearing poisons harmful to organic creatures."

    "Flesh, I am not. Threatened, I am not. This unknown creature poses no threat to this one."

    gl "You pose no threat to this one. You shall not be harmed, if you remain pacified."

    g "Huh? Why do you talk like that? Who is that one?"

    gl "I am this one."

    g "Nobody talks like that. But um… You're really strong, that's so cool! What's your name?"

    $x = renpy.input("What is . . . my name?")
    $x = x.strip()

    if x == "":
        $x = "Golem"

    $gl = Character(x,color="0BC4ED")

    "I shall be [x]."

    "I am [x]."

    g "Okay, [x]. What are you? I've never seen anything like you, you're so cool."

    gl "I do not experience temperature as an organic creature - such as yourself does."

    gl "If I am too hot, I melt. If I am too cold, I can no longer move. There is no discomfort."

    g "Yeah… okay. I don't know why any of that matters, but you seem nice. I'm Inya."

    gl "Understood, Inya. Do you know the fate of my creator, or the interloper?"

    n "Inya laughs, caught off guard. She seems to find delight in verbally prodding this anomaly."

    i "I don't know what any of that means."

    i "Are you a boy or a girl, [x]?"
    "What am I? What I was once is of little consequence - memories are no more."

    menu:
        "I am male.":
            "This one's creator sculpted this one in his perfect image. Like my creator, I am male."
            $pronoun = "He"
            $pronouns = "his"
            $selection = "male"
        "I am female.":
            "This one's creator sculpted this one to serve as his counterpart and compliment. I am female."
            $pronoun = "She"
            $pronouns = "her"
            $selection = "female"
        "I am something else.":
            "This one is… this one. I am neither male nor female. This one's identity is this one's. Flesh, I am not. Mortal, I am not. I have been created for a purpose. This purpose is undefined. This purpose must be defined."
            $pronoun = "It"
            $pronouns = "its"
            $selection = "something else"

    "I am as I choose."

    n "Inya glances at [x] quizzically in its moment of introspection."

    i "I'm sorry… I guess you probably don't work like us?"

    gl "I have concluded I am [selection]."

    i "You take a while to think. Sometimes I do that too. What are you doing down here anyway? Where did you come from?"

    gl "Parameters unclear. My purpose is to find the interloper and my creator."

    i "Someone made you, and the interloper did something bad?"

    n "Inya appears genuinely puzzled."

    gl "Correct."

    n "She nods along, appearing perplexed for just a moment."

    i "We're both uh… fre- outcasts, right? Maybe we can be friends?"

    n "[x] takes a long time to consider this possibility. It knew what friendship is, in abstract, but never considered the possibility it could have a friend."

    menu:

        "Accept":
            gl " I find these terms acceptable."

            n "Inya appears positively delighted to have a new giant, powerful sidekick."

            i "Yay! Okay, there's something I've always wanted to do. Since we're friends, maybe you can help me."

            gl "State your request, creature of flesh."

            i "I was getting to that! So… for a while now, I've wanted to make a human friend."

            i "We could all be friends. They're afraid of me, and every time I've tried, well… it hasn't gone well."

            i "If I'm riding on your shoulders, they'd have to at least hear me out, right?"

            i "No more rocks, no more bows pointed at me… It could work!"

            gl "Your plan is ill conceived, creature of flesh. However, as your… friend… I shall humor it."

            i "Um… okay. Thanks I guess. Do you have a better idea?"

            gl "I do not."

            i "So you agree then, great! I'll lead you to the surface, and then we can… I don't know, we can figure it out."

            gl "I have professed my compliance, friend. We shall proceed."
            $golemleftwithgoblin = True

            scene endingscreen
            with longdissolve

            n "Inya nods, contextually learning new vocabulary words from [x] as they speak."
            n "She appears to be genuinely hopeful and excited for this new adventure."

            n "The pair leave immediately, heading through the sewers to the city as they prepare to execute Inya's ill-conceived scheme."
            $golemleftwithgoblin = True


            jump witchstart

        "Refuse":
            gl "There is no purpose in affecting 'friendship'. I am stone, and you are flesh."

            n "Inya looks genuinely hurt, and gravely disappointed. Her optimism was dashed away in an instant."

            i "I guess you've made up your mind then."

            gl "Indeed. It is not meant to be, creature of flesh. We must part ways."

            n "Tears well up in the goblin's tiny pink eyes."

            i "Okay… I'm leaving then. I don't care what you do."

            n "Inya walks off into the sewers she made her home, almost managing to sound sincere."
            n "Her quiet sobbing betrays her true emotions, however."

            "My purpose is undefined. I must not linger."

            scene endingscreen
            with longdissolve
            n "[x] proceeds through the sewer system into the city, ignoring the echoes of the sobbing heartbroken goblin as stoically as stone."

            n "[pronoun] knew not what awaited them in this cold world, but [pronoun] was prepared for it."

            n "[pronoun] knew not what awaited them in this cold world, but [pronoun] was prepared for it."

            jump witchstart

label golemadesse:
    if deadjulian:
        jump golemescape5

    elif leftwithgoblin or goblindead:
        jump golemescape6
    elif leftwithtess:
        scene wrathhall
        with longdissolve
        scene monument
        with longdissolve
        scene blackscreen
        with longdissolve
        scene room1
        with longdissolve
        gl "… Empty. The interloper has eluded this one. Pursuit, thwarted."
        n "Indeed, it seems the hydraulic lock previously sealing Julian in the tomb reset behind him."
        n "The Golem found itself ensnared in a trap, with only one way forward - the service entrance."
        jump golemescape4

    jump golemescape7

label golemescape5:
    "The interloper's footsteps are fresh. I proceed."

    n "The Golem follows Julian's tracks into the main vestibule."

    scene wrathhall
    with pixellate
    n "A massive subterranean corridor. Sarcophagi line each side of this room."
    show ghost at offright:
        alpha .3
    show dog at offleft:
        alpha .3
    n "Faint, indistinct, macabre wraithspawn lurk in the corners of this place. In the center of the room lies the face-down corpse of the Golem's foe - this interloper oozing blood from its many wounds."

    "I must neutralize these threats."

    "Skill recalled: Blinding Flash"
    #different text color maybe?
    n "The Golem emits a blinding pulse of radiance. The wraithspawn dissipate."

    hide ghost
    hide dog

    "The interloper is vanquished, and I have no answers. No purpose."
    n "The Golem, with a shred of hesitation, as if accepting the reality that this 'interloper' truly doesn't have any answers, tenderly flips over Julian's lifeless corpse."

    menu:
        "Express pity over the interloper's demise.":
            gl "A life taken prematurely. A senseless tragedy. The one responsible is nearby, and must pay."
            gl "Wraiths are never directionless. A flame casts a shadow. I must extinguish this flame. This one's purpose is clear."

            n "Purpose elucidated, the Golem proceeds through the crypt and glides down the vertical shaft into the Peasant's Graves."

            scene monument
            with fade

            n "A narrow walkway encircles an open pit full of decomposing bodies of the less fortunate. Tenebrous shapes skirt the edge of the Golem's vision. From the opposing side of the pit - it manifests!"

            jump golemtess
        "Express triumphant exultation over the interloper's demise.":
            gl "The interloper has been neutralized. Objective complete. The location of this one's creator remains unknown."
            gl "Perhaps the interloper's slayer shall know the location of this one's creator. I press on."

            n "Purpose elucidated, the Golem proceeds through the crypt and glides down the vertical shaft into the Peasant's Graves."

            scene monument
            with fade

            n "A narrow walkway encircles an open pit full of decomposing bodies of the less fortunate. Tenebrous shapes skirt the edge of the Golem's vision. From the opposing side of the pit - it manifests!"
            show adesse_neutral:
                size (1240, 1754)
                xalign 0.5 yalign 1.0
                linear 6.0 yalign 0.0

            u "Fascinating. An arcane anomaly."

            n "This gives the Golem pause. It resolves to show the enemy of its enemy respect."

            gl "The interloper perished to your spawn. You have this one's gratitude and admiration. I seek my creator."

            n "The demoness wickedly quirks an eyebrow - her lips curl into a mischievous smile."

            u "Oh, yes, yes, very good. And what are you? Who intrudes into my lair?"

            $x = renpy.input("What is . . . my name?")
            $x = x.strip()

            if x == "":
                $x = "Golem"

            $gl = Character(x,color="0BC4ED")

            "I shall be [x]."

            gl "I am [x]."

            u "I see. And what are you, [x]?"

            u "You look lost."

            u "Like a fly wandering into a web... but you are most certainly not harmless like a fly."

            u "You destroyed my spawn trivially, and I shant begrudge such an indulgence."

            u "Most certainly not when opportunity presents itself so… earnestly."

            u "You may know me as Adesse."

            n "Adesse floats down to where [x] stands, and grazes its unfeeling stone jaw with her bladed, beshadowed fingernail."

            n "[x] contemplates her inquiry."

            "What am I? What I was once is of little consequence - memories are no more."

    menu:
        "I am male.":
                "This one's creator sculpted this one in his perfect image. Like my creator, I am male."
                $pronoun = "He"
                $pronouns = "his"
                $selection = "male"
        "I am female.":
                "This one's creator sculpted this one to serve as his counterpart and compliment. I am female."
                $pronoun = "She"
                $pronouns = "her"
                $selection = "female"
        "I am something else.":
                "This one is… this one. I am neither male nor female. This one's identity is this one's. Flesh, I am not. Mortal, I am not."
                "I have been created for a purpose. This purpose is undefined. This purpose must be defined."
                $pronoun = "It"
                $pronouns = "its"
                $selection = "something else"

    "I am as I choose."

    gl "I have determined I am [selection]."

    a "Ah… of course. I have a proposition for you, [x]."

    a "My business here is concluded, and you've caught my eye…"

    a "I believe we can aid one another. Accompany me out of this crypt. I am marked by enemies of my kind, and many would seek your destruction for simply being what you are."

    a "We find ourselves alike. I can assist you in finding your creator, if you can assist me in… ensuring my safety."

    a "We both simply strive for survival, do we not?"

    n "[x] considers Adesse's proposal. A loneliness tugs from deep within."

    n "Was Adesse altogether candid? Or did she take note of [x]'s latent yearning? "

    n "he creator's absence was felt deeply. Could she fill that void? Did she intend to help [x] find [pronouns] creator earnestly?"

    gl "I… accept your accord. We shall assist one another."

    a "Marvelous. Firstly, let us escape this domain of death. Accompany me."
    $golemleftwithtess = True

    hide adesse_neutral
    scene endingscreen
    with longdissolve

    n "[x] and Adesse leave the crypt, accompanying each other - an unsteady accord cementing their tenuous bond."

    n "Adesse surely had foes to contend with - foes who placed a mark on her head."

    n "[x] sought [pronouns] creator."

    n "For now, their agreement was mutual. The future may have other plans. It remains to be seen."

    jump witchstart

    label golemtess:
    show adesse_neutral:
        size (1240, 1754)
        xalign 0.5 yalign 1.0
        linear 6.0 yalign 0.0

    gl "It is unavoidable. We must do battle."

    n "The demoness hesitates for but a moment, puzzled by the anomalous creature intruding into her domain. She grins an unnaturally wide grin."
    hide adesse_neutral
    with quickdissolve

    show adesse_distant:
        size (1240, 1754)
        xalign 0.5 yalign 0.0
    
    u "If we must. So be it."

    n "Seizing initiative, the Golem dashes forward, casting the chamber with a blue glow."

    n "The demoness, however, is prepared for this advance. A beshadowed hemisphere created by the demoness's sorcery separates her from the Golem - and swiftly envelops the Golem, halting its advance."

    n "The Golem remains held fast by the demoness's sorcery. She grins broadly in triumph."

    u "You thought it simple to vanquish me? You're trapped."

    u "You're mine for as long as I like. A plaything, should I choose. It's unavoidable."

    n "The demoness's monologue is cut short by a sturdy figure rappelling down the ladder leading to the depths of the crypt."
    # need tess image
    hide adesse_distant
    show tess:
        size (780, 1080)
        xalign 0.0 yalign 0.0


    n "The warrior eschews armor for green and brown traveler's leathers, adorned with protective talismans."

    n "Their longboots are characteristic of the locality."

    n "The saw-toothed metal staff wielded by the warrior and the iron mask strike the Golem as distinct, but mysterious in origin. Whomever this is, they strike an imposing form in the gray-hued darkness of the crypt."

    n "Without uttering a word, the warrior's talismans emit a bright glow, and they bound forth through the chamber, acrobatically and powerfully vaulting from the lip of the precipice transecting the room."
    #show talisman? with bright light?

    n "The demoness's eyes widen in shock when presented with this threat. She launches sorcerous bolts of solid darkness towards the charging warrior - to utterly no effect."

    n "Several of the countless protective talismans warding the warrior tremble and sunder, joining the human swamp below."

    n "Yet, the demoness's efforts are for naught. The warrior's weighted sawtoothed staff hurtles down at the end of the charge, pulping the demoness's skull with a sickening crunch."

    hide adesse_neutral

    n "The demoness discorporates, the look of revulsion and shock remaining the last features adorning her perfect face."

    n  "A smooth, sulfurous stone is all that remains of the pristine villainess."
    # picture of stone?

    n "The warrior heaves a deep breath, quickly recovering after clutching their chest in pain."

    n "They quickly filch up the stone with a handkerchief drawn from their pack. The warrior places the stone with great care into their pack and surveys the room."

    n "The Golem bears mute testament to this scene. The demoness's enveloping shadows wane, and reveal the Golem's form to the warrior."

    uw "Eh?!"

    n "A female voice, if low in pitch - accompanied by a startled gasp."

    uw "What in the world…? Who are you? What are you? Can you understand me?"

    ". . . "

    $x = renpy.input("What is . . . my name?")
    $x = x.strip()

    if x == "":
        $x = "Golem"

    $gl = Character(x,color="0BC4ED")

    "I shall be [x]."

    gl "I am [x]."

    "What am I? What I was once is of little consequence - memories are no more."

    menu:
        "I am male.":
            "This one's creator sculpted this one in his perfect image. Like my creator, I am male."
            $pronoun = "He"
            $pronouns = "his"
            $selection = "male"
        "I am female.":
            "This one's creator sculpted this one to serve as his counterpart and compliment. I am female."
            $pronoun = "She"
            $pronouns = "her"
            $selection = "female"
        "I am something else.":
            "This one is… this one. I am neither male nor female. This one's identity is this one's. Flesh, I am not. Mortal, I am not."
            "I have been created for a purpose. This purpose is undefined. This purpose must be defined."
            $pronoun = "It"
            $pronouns = "Its"
            $selection = "something else"

    "I am as I choose."

    gl "I understand you. I am [x]. I am [selection]."

    n "This pronouncement gives the warrior pause, who deigns not to question the strange behavior - produced by an even stranger creature."

    uw "Right then… I'm Tess, female."

    t "I don't know who or what you are, really and yes, I understand you just told me."

    t "I'm sure you have questions, and so do I. We can get them all answered once we're out of here."

    gl "I seek to elucidate the fate of my creator, and seek my purpose. If you can assist in this endeavor, so be it."

    n "Tess gapes at [x], staring in utter disbelief. Composing herself, she replies."

    t "... Let's be off then. Up the way we came."

    hide tess
    scene endingscreen
    with longdissolve

    n "Tess and [x] return through the unlocked crypt entrance, relatively unscathed."

    n "Their futures are murky, but for now, they have the dubious company of one another."

    $golemleftwithtess = True

    jump witchstart

label golemescape6:

gl "I must be thorough. The crypt must be searched for evidence of this one's creator's whereabouts."

n "The Golem proceeds into the main vestibule."

scene wrathhall
with pixellate
n "A massive subterranean corridor. Sarcophagi line each side of this room."
show ghost at offright:
    alpha .3
show dog at offleft:
    alpha .3

"The Golem emits a blinding pulse of radiance. The wraithspawn dissipate."

"Skill recalled Blinding Flash"

n "The Golem emits a blinding pulse of radiance. The wraithspawn dissipate."

". . . ."

"The threats are neutralized. I proceed."

". . . ."

menu:
    "These living shadows are aberrations.":
        gl "… And their creator is a monster. Intuitively, I know this to be a demon."
        gl "This one's creator opposed demons. This demon must be destroyed. This one's purpose is clear."

        n "Purpose elucidated, the Golem proceeds through the crypt and glides down the vertical shaft into the Peasant's Graves."

        scene monument
        with fade

        n "A narrow walkway encircles an open pit full of decomposing bodies of the less fortunate."
        n "Tenebrous shapes skirt the edge of the Golem's vision. From the opposing side of the pit - it manifests!"

        jump golemtess
    "The creator these creatures may eludicate the fate of {i}my{/i} creator.":
        gl "This one's purpose remains unclear. The creator of these creatures may elucidate the fate of my creator."
        gl "This one lacks a purpose. A flame casts shadows, and this one shall seek truth within the flame."

        n "Purpose elucidated, the Golem proceeds through the crypt and glides down the vertical shaft into the Peasant's Graves."

        scene monument
        with fade

        n "A narrow walkway encircles an open pit full of decomposing bodies of the less fortunate."

        n "Tenebrous shapes skirt the edge of the Golem's vision. From the opposing side of the pit - it manifests!"

        show adesse_neutral:
            size (1240, 1754)
            xalign 0.5 yalign 1.0
            linear 6.0 yalign 0.0

        u "Fascinating. An arcane anomaly."

        n "This gives the Golem pause. It resolves to show the enemy of its enemy respect."

        gl "I seek my creator."

        n "The demoness wickedly quirks an eyebrow - her lips curl into a mischievous smile."

        u "Oh, yes, yes, very good. And what are you? Who intrudes into my lair?"

        $x = renpy.input("What is . . . my name?")
        $x = x.strip()

        if x == "":
            $x = "Golem"

        $gl = Character(x,color="0BC4ED")

        "I shall be [x]."

        gl "I am [x]."

        u "I see. And what are you, [x].?"

        u "You look lost."

        u "Like a fly wandering into a web... but you are most certainly not harmless like a fly."

        u "You destroyed my spawn trivially, and I shant begrudge such an indulgence."

        u "Most certainly not when opportunity presents itself so… earnestly."

        u "You may know me as Adesse."

        n "Adesse floats down to where the [x] stands, and grazes its unfeeling stone jaw with her bladed, beshadowed fingernail."

        n "[x] contemplates her inquiry."

        "What am I? What I was once is of little consequence - memories are no more."

        menu:
            "I am male.":
                "This one's creator sculpted this one in his perfect image. Like my creator, I am male."
                $pronoun = "He"
                $pronouns = "his"
                $selection = "male"
            "I am female.":
                "This one's creator sculpted this one to serve as his counterpart and compliment. I am female."
                $pronoun = "She"
                $pronouns = "her"
                $selection = "female"
            "I am something else.":
                "This one is… this one. I am neither male nor female. This one's identity is this one's. Flesh, I am not. Mortal, I am not."
                "I have been created for a purpose. This purpose is undefined. This purpose must be defined."
                $pronoun = "It"
                $pronouns = "its"
                $selection = "something else"

        "I am as I choose."

        gl "I have determined I am [selection]."

        a "Ah… of course. I have a proposition for you, [x]. My business here is concluded, and you've caught my eye…"

        a "I believe we can aid one another. Accompany me out of this crypt. I am marked by enemies of my kind, and many would seek your destruction for simply being what you are."

        a "We find ourselves alike. I can assist you in finding your creator, if you can assist me in… ensuring my safety."

        a "We both simply strive for survival, do we not?"

        n "[x] considers Adesse's proposal. A loneliness tugs from deep within. Was Adesse altogether candid?"

        n "Or did she take note of [x]'s latent yearning? The creator's absence was felt deeply."

        n "Could she fill that void? Did she intend to help [x] find [pronouns] creator earnestly?"

        gl "I… accept your accord. We shall assist one another."

        a "Marvelous. Firstly, let us escape this domain of death. Accompany me."

        hide adesse_neutral
        scene endingscreen
        with longdissolve

        n "[x] and Adesse leave the crypt, accompanying each other - an unsteady accord cementing their tenuous bond."

        n "Adesse surely had foes to contend with - foes who placed a mark on her head. [x] sought [pronouns] creator."

        n "For now, their agreement was mutual. The future may have other plans. It remains to be seen."

        jump witchstart

label golemescape7:

    scene wrathhall
    with pixellate

    "The interloper's footsteps are fresh. I proceed."

    n "The Golem pauses, closely examining the single set of footprints entering and leaving the crypt."

    if leftwithadesse:
        n "Waning daylight intrudes upon this place of rest. The Golem contemplates the sequence of events, and is hit with a sudden realization - the interloper has fled with an accomplice."

    n "Waning daylight intrudes upon this place of rest. The Golem contemplates the sequence of events, and is hit with a sudden realization - the interloper has fled."

    "Skill Recalled: Moment of Prescience"

    n "A mental flash - the spark of prescience. The Golem realized it would be soon met by another - a friend, perhaps."

    n "A warrior, a healer, and a former druidess. The Golem's form would startle her, and she would elucidate much about the Golem's purpose… and their ultimate destiny."

    n "A burly form lumbers into the crypt - just as the Golem foresaw."

    show tess

    n "The warrior eschews armor for green and brown traveler's leathers, adorned with protective talismans. Their longboots are characteristic of the locality."

    n "The saw-toothed metal staff wielded by the warrior and the iron mask strike the Golem as distinct, but mysterious in origin."

    n "Whomever this is, they strike an imposing form in the twilit hues of the crypt entrance."

    n "The warrior pauses, stock still at the sight of the Golem mutely studying them."

    uw "Shit. I'm too late. . . . "

    uw "Eh?!"

    n "A female voice, if low in pitch - accompanied by a startled gasp."

    uw "What in the world…?"

    uw "Who are you? What are you? Can you understand me?"

    $x = renpy.input("What is . . . my name?")
    $x = x.strip()

    if x == "":
        $x = "Golem"

    $gl = Character(x,color="0BC4ED")

    "I shall be [x]."

    gl "I am [x]."

    ". . . ."

    "What am I? What I was once is of little consequence - memories are no more."

    menu:
        "I am male.":
            "This one's creator sculpted this one in his perfect image. Like my creator, I am male."
            $pronoun = "He"
            $pronouns = "his"
            $selection = "male"
        "I am female.":
            "This one's creator sculpted this one to serve as his counterpart and compliment. I am female."
            $pronoun = "She"
            $pronouns = "her"
            $selection = "female"
        "I am something else.":
            "This one is… this one. I am neither male nor female. This one's identity is this one's. Flesh, I am not. Mortal, I am not."
            "I have been created for a purpose. This purpose is undefined. This purpose must be defined."
            $pronoun = "It"
            $pronouns = "its"
            $selection = "something else"

    "I am as I choose."

    gl "I understand you. I am [x]. I am [selection]."

    n "This pronouncement gives the warrior pause, who deigns not to question the strange behavior - produced by an even stranger creature."

    uw "Right, then… I'm Tess, female."

    t "I don't know who or what you are, really - and yes, I understand you just told me."

    t "I'm sure you have questions, and so do I."

    t "We can get them all answered soon. It seems as if I'm just a bit late, and you're… well…"

    gl "I seek to elucidate the fate of my creator, and seek my purpose. If you can assist in this endeavor, so be it."

    n "Tess gapes at [x], staring in utter disbelief. Composing herself, she replies."

    t "... Let's be off then. Up the way we came. I'm going to have some choice words with Nikolai."

    scene endingscreen
    with longdissolve

    n "Tess and [x] promptly exit the crypt."
    n "Their futures are murky, but for now, they have the dubious company of one another."
    $golemleftwithtess = True

    jump witchstart

label witchstart:

scene darkcrypt
with longdissolve

play music "Oppressive Gloom.mp3"

n "The night watchman's body drops with a thunk presaging Dahlia's arrival."

n "The pressure on the hydraulics of the crypt's door is released with a gesture and a tug of the witch's hand - a subtle thaumaturgical manipulation."

# add sound effect

dh "It will do."

dh  "The anomaly, and the demon."

dh "One to be harvested, one to be bound. Good help is so very hard to find."

n "Confidently, the witch struts into the crypt."

scene room1
with pixellate

n "She follows the path in her divination - first, to the arcane anomaly."

if not barricade:
    n "Ancient, crumbling boards practically hang from the nails they were fixed to many decades ago."

    n "Even so, they do the trick. The way is blocked."

    dh "A trifle."
    #add spelleffect

    n "A deadly gesture - moderate necromancy."

    n "The boards wither and crumble before Dahlia's eyes, collapsing in a parched pile at her feet."

    n "She proceeds down the narrow tunnel to her first destination."

    jump golemnotactived

n "Boards, once comprising a barricade, lie in a disassembled heap at Dahlia's feet."

dh "My, my. Unsavory complications."

dh "They will be managed."

n "Despite her confidence, Dahlia scowls."

n "She hated complications."

n "She proceeds down the narrow tunnel to her first destination."
if golemactive:
    jump golemactived

label golemnotactived:

scene warehouse
with fade

n "A room full of detritus. A disused artificer's lab, surely, by Dahlia's estimation."

n "Her eyes settle on her prize."

show golem:
    alpha .3

dh "My dear, sweet thing. I've traveled leagues for you."

n "Mustering her magical might, the room glows alight with a fel crimson bloom."

#more spell effects

hide golem

n "The dismembered torso of the Golem rises in rhythm with the malevolent pulse."

n "Dahlia gestures sharply, and the Golem's stone torso is violently torn asunder - revealing a pristine core, alight with a blue glow."

# add core item

n "The neutral blue of its light is drowned in Dahlia's sea of crimson."

dh "Marvelous! And now for my sweet…"

n "Dahlia unclasps her pack, retrieving a silvered bird cage like receptacle for the Golem's heart."

n "Using minor telekinesis, she hefts the Golem's heart - ablaze with raw magic as it is, into the receptacle, and shuts it."

#mooooorreee spell effects

n "The witch breathes a self-satisfied sigh of contentment and beams."

n "Dahlia hastens to her task, returning to the Atrium."

jump backtoatrium

label golemactived:

scene warehouse
with fade

n "A room full of detritus. A disused artificer's lab, surely, by Dahlia's estimation."

n "She peers carefully through the mess, coming up empty."

if golembreakmirror:

    n "Broken shards of glass litter the floor."

    n "Dahlia spots the source - a broken mirror from across the room. Whatever impacted the mirror struck it hard."

    dh "A temper tantrum… not entirely unexpected."

dh "Disappointing, but not the end of the road."

dh "It seems another has hastened to the prize."

dh "I have a competitor. No sense in wasting precious time."

n "Dahlia hastens to her task, returning to the Atrium."

label backtoatrium:

scene room1
with pixellate

if golemleftwithtess and leftwithgoblin:
    jump witchsolo

if golemleftwithtess and goblindead:
    jump witchsolo

elif golemleftwithgoblin and leftwithtess:
    jump witchsolo

elif deadjulian:
        jump raisejulian

elif leftwithadesse or adessedead:
        jump witchtess

elif leftwithtess or golemleftwithtess:
        jump witchgoblin

jump witchadesse

label raisejulian:
n "Dahlia proceeds through the crypt."

n "Her enhanced senses give her warning - wraithspawn ahead, and a fresh body."

n "She casts a spell, concealing her presence completely from the mindless undead creatures roaming the crypt."

scene wrathhall
with quickdissolve

n "Entering the room, she examines the corpse with a malevolent smirk."

#insert image of julian

show julian

dh "Delightfully fresh… and bearing the stench of transgression."

n "The witch inhales deeply, stifling a chortle."

dh "Awash with blood heavy with guilt. It isn't often I can reanimate a vampire."

n "Dahlia takes a moment to clear her head and muster her might."

n "She casts a powerful hex, utilizing the latent remnants of guilt Julian's soul possessed."

n "Binding the weight of his guilt to the blood remaining in his body, her spell concludes."

n "A stirring digit."

n "A trembling limb."

n "Julian's eyes go wide."

dh "You may move when I permit."

dh "Nikolai sent you, I presume? That doddering old fool."

vj "... Yes."

dh "Hm. Responsive to commands."

dh "I may keep you."

n "Dahlia's malice softens, and a small wicked smile graces her black lips."

dh "Your new existence will be confusing, but you may take my lead."

dh "Call me Dahlia. Provide me with your name, if you please."

n "The witch's politeness belied the bidding of a magical pact binding her now to Julian - she did not offer a polite suggestion."

n "She issued a command."

n "Julian coughs, nearly vomiting, sputtering out the remaining blood in his esophagus and lungs."

n "Rising to his feet, he marveled at his healed wounds, newfound vitality, and ability to see in the overbearing, oppressive darkness of the crypt."

n "Yet, a gnawing, unfamiliar hunger brewed in his gut - mingled with dread. He did as he was bidden by Dahlia."

vj "Julian… Grymwald."

dh "You have the look of a town guard, Mr. Grymwald, or a mercenary."

dh "Oh, please tell me you were a druid. That would truly tickle me."

n "Still recovering from his ordeal, Julian stammers out a response."

vj "M-mercenary."

dh "Mm, I see. Await me outside."

dh "I shan't be long now. You may go."

hide julian

n "Julian's limbs carried him to the entrance of the crypt, bidden by Dahlia's command."

label witchadesse:

n "Dahlia hastens to the depths of the crypt with supernatural speed."

scene monument
with fastdissolve

n "Silently, she lands in the depths of the place overlooking a bit transecting the center of the room."

n "The pit is filled with the decaying remains of the less fortunate - a particularly putrid soup, of sorts."

n "The shadows dance, indicating the presence of a Demon of Shadow."

n "Dahlia grins, and sharply gestures."

show adesse_hurt:
    size (1240, 1754)
    xalign 0.5 yalign 1.0
    linear 6.0 yalign 0.0

dh "You're {i}mine{/i}. Did you think you could hide from me, my sweet?"

a "A demonologist. No… I suppose I couldn't."

a "You're quite competent, aren't you?"

dh "Spare me the pillow talk."

dh "The king's circle binds you, demon. You are mine to command."

a "As you wish."

a "You… seem to know what you're doing. A woman with experience."

hide adesse_hurt
with fastdissolve

show adesse_flirty
with fastdissolve

a "How endearing."

n "The demoness's flirtation briefly catches Dahlia off guard."

n "She narrows her eyes, focusing her magical senses to probe the fiend's mind."

dh "Right this way, Adesse. You may refer to me as Dahlia."

a "So it shall be."

n "Regaining her composure, Adesse politely curtseys to the witch."

hide adesse_flirty
with fastdissolve

scene endingscreen

if deadjulian:

    n "The trio departed the crypt."
    n "A witch, a demon, and a newly awakened vampire."
    n "Dahlia's designs for them are yet unclear, but the hands of the malevolent are rarely still."
    jump endofprologue

n "The pair departed the crypt."

n "A witch and a demon."

n "A likely pair, perhaps, but the future remains uncertain."

n "Dahlia's designs for Adesse are yet unclear - surely a sorceress as powerful as she would not travel such a great distance and go to such lengths to entrap a specific demon for naught."

jump endofprologue

label witchtess:

if golemleftwithtess:
    jump witchgoblin

n "Dahlia hastens to the depths of the crypt with supernatural speed."

scene monument
with fastdissolve

n "Silently, she lands in the depths of the place overlooking a bit transecting the center of the room."

n "The pit is filled with the decaying remains of the less fortunate - a particularly putrid soup, of sorts."

dh "… I'm too late."

n "Indeed, the absence of animate shadows indicates the witch's estimation is correct. Dahlia is disappointed, but just for mere moments."

n "A sturdy figure rappels down the ladder leading to the depths of the crypt."

show tess

n "The warrior eschews armor for green and brown traveler's leathers, adorned with protective talismans."

n "Their longboots are characteristic of the locality."

n "The saw-toothed metal staff wielded by the warrior and the iron mask strike Dahlia as distinct, but mysterious in origin."

n "Whomever this is, they strike an imposing form in the gray-hued darkness of the crypt."

dh "Not so fast."

n "The witch gestures dramatically, buckling the warrior's knees."

n "She wails in pain, dry heaving as the intense pain topples her."

dh "The pain shall pass."

dh "You should know better than to barrel into rooms like that. You'll upset people."

dh "Perhaps… honey would be a better approach."

n "Dahlia, continuing the momentum established with her sorcery, gestures a charm, and a mental probe."

dh "Tessanrae. A beautiful name for a beautiful woman."

dh "It's a pity you hide your beauty behind a mask of iron - and the beauty of your name behind a base alias like 'Tess'."

dh "The world should behold the beauty you possess, my 'Tess' and tremble."

n "Dahlia's slight sardonic bite seems to fall on deaf ears, to her slight displeasure."

dh "Druidic wards may protect against demonic magic, but not all of mine."

dh "Demonology… necromancy… thaumaturgy… conjuration… enchantment… I have so many to choose from."

n "Tess catches her breath, managing not to vomit in her helmet."

n "She places a hand on her knee and forces herself to rise, reaching for her weapon."

n "Dahlia mimes a gesture and locks eyes with the larger woman."

dh "I wouldn't. Don't you recall moments ago, my dear?"

dh "Can't we just have a peaceful chat?"

n "Tess grunts, eschewing her weapon despite her better judgement."

n "Dimly, she screams at herself, realizing on some distant level she is subject to this witch's charm hex."

t "We can parley. Who are you and what do you want?"

dh "That's better. You may call me Dahlia."

dh "My goal appears to be misplaced… but you're interesting."

dh "What business do you have in an old dusty tomb, my Tessie?"

t "I really don't like being called Tessie. But… I'll forgive you."

t "This time."

t "I learned Nikolai is sending mercenaries to handle stray demons. That old fool has really lost the plot."

n "The witch grins as her charm bears fruit - the moments of agony so easily forgotten and forgiven."

dh "It would seem our common goal is absent. It's a pity, isn't it?"

t "A pity? Well, it worries me."

dh "Cast aside your doubts."

dh "Look into my eyes."

n "Tess obliges, despite a subconscious realization she is being magically manipulated."

n "As she meets Dahlia's eyes, the witch's charm truly bears fruit - and allows her to leave a lasting imprint in the warden's mind."

dh "You're interesting. I want to see you again."

dh "I will call to you, and you will come, unarmed."

dh "We will next meet in your dreams. I ever so look forward to it."

n "Tess's slight alarm is concealed by her mask."

t "That sounds unlikely, but if you say so."

dh "I do, I do. Wait five minutes in this place, standing still, then you may leave."

dh "It's been fascinating, my dear."

t "That seems reasonable enough, you need to escape, and you'd prefer if I wasn't able to trail you."

dh "Precisely. You're quite perceptive. I'll be off, then."

n "Tess does as directed, allowing Dahlia to escape."

hide tess
scene endingscreen
with longdissolve

n "Frustrated at the fruits of her labor going unrealized, but tantalized by the mirth tormenting a warden will bring, Dahlia departs."

n "Tess obediently waits five minutes, precisely as directed."

n "Both Dahlia and Tess have a feeling they will see each other again - perhaps sooner than expected."

jump endofprologue

label witchgoblin:

scene blackscreen
with longdissolve

scene room1
with longdissolve

n "Dahlia's search of the crypt was futile. She walked back to the entrance, in defeat."

dh "What a waste of time. Dreadful."

n "Utilizing her keen senses, Dahlia spots the glimmer of eye shine from the corner of her eye."

n "A scheming, curious smile creeps across her black lips."

dh "What do we have here? Oh, how I love surprise visitors."

n "A flick of the wrist, a draw on the latent thaumaturgical current."

n "The bars blocking the path to the service entrance turn red, then white, then pool as a liquid on the ground."

n "As a bit of flair, Dahlia makes a show of exhaling in the direction of the molten metal, while concealing her gestures, freezing it."

scene goblinroom
with pixellate

play music "Inya Theme (First Encounter).mp3"

show goblin at deadcenter:
    size (1500,1700)
    xalign 0.5 yalign 1.0
    linear 6.0 yalign 0.0
pause 6.5
            
hide goblin
with dissolve
        

show goblin at deadcenter:
    size (550,800)
with dissolve

g "Wooooooow! You're a magician!"

dh "A goblin so close to the surface? Bless your heart, you're deformed… but alive."

n "Dahlia appears genuinely impressed, realizing the implications of the goblin's predicament quickly."

g "Are all magicians so rude? You're tall like a man and really creepy."

n "Dahlia chuckles darkly."

dh "My dear, pardon my disrespect. You have done well for yourself."

dh "You're a survivor, and you've taught yourself our language."

dh "You've triumphed over your impediments, and for that, you have my ardent admiration."

g "I…"

n "The goblin is momentarily stunned by Dahlia's words."

g "..I'm Inya."

dh "Zanya. You are Zanya."

dh "Inya is a cute name, but it draws too many unfortunate comparisons…"

dh "…but it may be as you wish."

dh "I am Dahlia. It is a pleasure to meet you."

n "Inya blinks, processing the fact Dahlia somehow knew her birth name. The realization hits her."

i "Oh… you figured out my goblin name with your magic."

i "I wish you wouldn't do things like that. I like 'Inya'. It sounds so much more refined."

n "Inya pouts, to Dahlia's muted amusement."

dh "It shan't happen again, my little morsel."

dh "I have divined all I need to know about you, and I find you starkly unique, and simply fascinating."

i "Y-you do?"

dh "I do."

i "It's a little creepy when you call people things like 'morsel'. Just call me Inya."

n "Dahlia frowns."

dh "You would begrudge an artful turn of phrase? Very well, my Inya."

dh "It seems my quarry in this dreadful hole has eluded me. I must retire to my lair. Perhaps you would accompany me?"

i "Um, things are moving a little fast, don't you think? We only just met."

dh "You're lonely. You've been seeking a human friend for fourteen years since your cruel abandonment by your tribe."

dh "I'm offering you a home, and a human companion."

dh "I am the answer to your deepest desires."

dh "I know everything about you, my Inya, and I find you worthy and fascinating."

n "Inya blushes a deep red and nearly faints. Meekly, she replies."

i "That's a lot to think over, ma'am. I suppose you're right though. You seem like you're always right."

dh "Yes, my dear, I am. "

dh "You may ask your questions on the way. The front door will do."

dh "You're coming with me - if that is your wish."

n "As with anything Dahlia says, her suggestions are almost always demands."

i "I have so many questions. But uh, I'll ask them on our way, like you said. Looks like you're right again, Ms. D."

n "Dahlia smiles affirmingly."

hide goblin

scene endingscreen
with longdissolve

n "Guiding her by her hand, Dahlia leads Inya out of the crypt."

n "En route to Dahlia's lair, Inya incessantly prattled on about each and every thing that whizzed through her mind, and Dahlia patiently obliged her."

n "In truth, Dahlia saw a bit of herself in the goblin, and more importantly, had plans for her."

n "Plans take time to cultivate, and Dahlia was nothing, if not patient."

jump endofprologue

label witchsolo:

scene blackscreen
with longdissolve

scene room1
with longdissolve

n "Dahlia's search of the crypt was futile. She walked back to the entrance, in defeat."

dh "What a waste of time. Dreadful."

n "Dahlia sighs deeply and focuses her mind. Her magical senses probe her surroundings and detect the presence of recent creatures."

dh "… But the trails are fresh. I cannot possibly pursue them all."

dh "Who shall it be, hm? It would be a pity for my time to be wasted."

menu:
    "The Mercenary":
        dh "Nikolai's lapdog."
        dh "It would be suitable to wrap him around my finger, whether he is willing or not, and use this… distasteful attempt to thwart me against that pest."

        scene endingscreen
        with longdissolve

        n "Motivated foremost by spite, Dahlia resolved to pursue the gnat Nikolai flung in her direction - successfully disrupting her effort."

        n "Dahlia was irritated, and an avid enjoyer of irony. She simply couldn't pass up this opportunity to harass Nikolai with his pawn."

        n "Perhaps she could make this mercenary a better offer - whether that be gold, or whatever else enticed him."

        n "If he proved unyielding, well, Dahlia always had her way."
        jump endofprologue
    "The Arcane Anomaly":
        dh "My goal has not changed, despite this… unprecedented setback."

        dh "Foremost, the arcane core is my quarry. I shan't tarry."

        scene endingscreen
        with longdissolve

        n "Resolved and focused, and with a fresh lead, Dahlia decided to pursue the Arcane Anomaly."

        n " She would harvest its arcane core and latent power. It was, after all, the first step in creating a golem of her own."

        n "She couldn't pass up just a juicy offer. These cores are artifacts, and their personalities were ever so malleable."

        n "How could she waste such an enticing opportunity?"
        jump endofprologue
    "The Unusual Goblin":
        dh "An albino. An outcast."

        dh "She hasn't perished, despite her deformity."

        dh "Marvelous - it speaks to her ingenuity. I can use that."

        scene endingscreen
        with longdissolve

        n "Interest piqued at the novelty of this goblin, Dahlia resolved to pursue her."

        n "She would handle her with care, for she saw potential… and a bit of herself in what she could divine about the small creature."

        n "Dahlia departed to her lair to plan the pursuit and her strategy."
        jump endofprologue
    "The Warden":
        dh "A warden… and a traitor to her kind. How unique."
        dh "The roots of this conspiracy go deep."
        dh "Perhaps if she were under my thumb I could root out the core of this wart, and collect a novel plaything."
        dh "'Tessanrae'... Few of her kind survive."
        dh "She shall be the crowning jewel of my collection."

        scene endingscreen
        with longdissolve

        n "Dahlia resolved to pursue Tessanrae, wherever she may flee."

        n "Her unique quirks interested Dahlia even more than the allure of an arcane anomaly."

        n "Dahlia got what she wanted - always."
        jump endofprologue
    "It is time to confront Nikolai once and for all.":
        n "Dahlia takes a deep breath, and lets out a long, irritated sigh."
        dh "Nikolai has thwarted me at every turn."
        dh "His lairs are hidden, but not inaccessible…"
        dh "It is long overdue to pay him a friendly visit."

        scene endingscreen
        with longdissolve

        n "Dahlia left the crypt, returning to her lair to scheme."

        n "This was not the first time Nikolai attempted to thwart her, but it was the first time he had found success."

        n "Dahlia had never been one to forgive or forget. She was planning something, as she always was."

        n "She would have the last word… as always."
        jump endofprologue
    "My efforts are best actualized elsewhere…":
        n "This is a waste of time."
        dh "These fools are beneath me."
        dh "I shall return to my lair."
        dh "The fruits of my labor shall be actualized… elsewhere."

        scene endingscreen
        with longdissolve

        n "Failures upset Dahlia, but she was never one to truly rest."

        n "She knew it was best to move on to the next project or scheme."

        n "She departed the crypt, returning to her reclusive lair."
        jump endofprologue

label endofprologue:

"To be continued..."

play music "Casa Bossa Nova.mp3"

centered "{size=+75}{cps=8}{color=000000} Credits {/cps}{/size}{p=5.0}{nw}"

$ renpy.pause(1.5)

centered "{size=+75}{cps=8}{color=000000} Narrative / Project Manager: \nBarry Weber{/cps}{/size}{p=5.0}{nw}"

centered "{size=+75}{cps=8}{color=000000} Code/Script: \nRachel 'Des' Marzzarella\nLake Watkins\nDeniz Balik{/cps}{/size}{p=5.0}{nw}"

$ renpy.pause(1.5)

centered "{size=+40}{cps=8}{color=000000} Editing/Revisions/Special Thanks:\nLake Watkins\nJesse Bohnet\n'Scoot Gygax'\nMiriam Bates\nWill Watkins\nNicholas 'Evő Kolbász' Tolga Balik{/cps}{/size}{p=5.0}{nw}"

centered "{size=+40}{cps=8}{color=000000} Deniz Balik\n Nick Vitale\nRachel 'Des' Marzzarella\nJude Bigboy\nJennifer Svensson\nJay Brinkman\nDoug 'Dr. Wasteland' Watkins\nSarah Caldwell {/cps}{/size}{p=5.0}{nw}"

$ renpy.pause(1.5)

centered "{size=+75}{cps=8}{color=000000} Art:\nRihards Kurts\nOndrej Svinčiak{/cps}{/size}{p=5.0}{nw}"

$ renpy.pause(1.5)

centered "{size=+40}{cps=8}{color=000000}  Music:\n'Wholesome', 'Darkest Child', 'Midnight Tale', 'Deep Haze', 'Floating Cities', 'Myst on the Floor', 'Impact Prelude', 'Casa Bossa Nova' by Kevin MacLeod (incompetech.com). \n\nLicensed under Creative Commons: By Attribution 4.0 License http://creativecommons.org/licenses/by/4.0/{/cps}{/size}{p=5.0}{nw}"

centered "{size=+40}{cps=8}{color=000000} \n 'Inya's Theme (First Encounter) by Taylor Perfater"

$ renpy.pause(1.5)

centered "{size=+75}{cps=8}{color=000000}  Sound effects provided by https://pixabay.com/sound-effects/ {/cps}{/size}{p=5.0}{nw}"

$ renpy.pause(1.5)

centered "{size=+75}{cps=8}{color=000000} Thanks for playing! We hope to see you in chapter 1!{/cps}{/size}{p=5.0}{nw}"

$ renpy.pause(1.5)

return
