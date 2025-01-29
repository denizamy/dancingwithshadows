# it's a me, mario


# characters
define n = Character("Narrator")
define j = Character("Julian")
define a = Character("Adesse")



#images

image background = "background.png"
image atrium = "atrium.png"
image shadow = "shadow.png"


# other definitions
transform deadcenter:
    xalign 0.5
    yalign 0.5

transform topright:
    xalign .9
    yalign 1



define fastdissolve = Dissolve(.3)

define quickdissolve = Dissolve(.2)




# The game starts here.

label start:


    show background at deadcenter


    n "You are Julian Grymwald, a rough and tumble mercenary."

    # character pic of julian evench

    n "Recently, you have accepted a contract from the Archdruid to investigate the local crypt."
    n "As of late, locals have been harassed when mourning their dead..."
    n "Statues and monuments have been toppled, and unsettling shadows have darted around the crypt, irrespective of the lack of wind and torch"
    
    # i want a thing that indicates julian thinking to himself like a differnt textbox
    # maybe even just a different font but idk yet fam
    
    "The Archdruid told me my quarry is a Demon of Shadow - not a trivial, nor a major demon. I should be on my guard."

    # You have: Contract, Demonslaying Blade, Blessed Shield
    # Contract: Slay and banish the presence, whatever it may be, from this formerly sanctified place of rest.
    # Demonslaying Blade - A steel arming sword plated with silver along the edge - said to scourge demons. The druids placed a blessing on it. Normal weapons cant even scratch their flesh. I might stand a chance with this blade, if Im lucky.
    # Blessed Shield - The sheen on this steel heater is phenomenal, and as long as there is even a scant amount of light, the Archdruid reassured me none of the demons shadow magic can harm me.
    # Hardtack - I dont even want to think about hardtack if I cant soften it up first. Its about as hard and appetizing as a brick
    # Waterskin - Its filled with three-day old small beer. Smells sour. I probably shouldnt, unless I really need to.

    hide background with dissolve
    scene atrium at deadcenter
    
    j "A large stone room, far underground. As you enter, you hear hydraulic mechanisms automatically shut the large steel gate behind you."
    j "A security measure by the townsfolk, surely. You are trapped down here with the demon, and it with you, until one of you perishes."
    j "Torchlight glints off of brass embellishments on the sarcophagi populating this moderately impressive tomb."
    
    
    show shadow at top
    hide shadow with quickdissolve 


    show shadow at topright
    hide shadow with quickdissolve

    show shadow at right 
    hide shadow with quickdissolve


    n "On the periphery of your vision, you notice unusual fleeting shadows"
    
    n "The demon must not be far off, and it has nowhere to run. One of you must perish today." 
    
    n "A great stone arch allows passage further in this dark place. It seems the druids left a torch here for your use."
    
    j "Torch - A sturdy branch topped with dry cloth soaked in pitch and an alchemical mixture. I can ignite it by striking it against the wall. These dont last forever..."
    
    ################################################################

    n "A massive subterranean corridor. Sarcophagi line each side of this room."
    
    j "The rooms ahead are shrouded in oppressive darkness - likely the work of this demon"

    j "I should be well prepared for the push ahead - at the very least, I should have a light source."
    
    j "If I squint, I can see solid silhouettes deeper in this place."





































































    # The end little bitch

    return
