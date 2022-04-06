# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define jul = Character("Jul")
define arnav = Character("Arnav")
define nate = Character("Nate")
define TSK = Character("TSK")
define mc = Character("Me")
define slowdissolve = Dissolve(1.0)

image donutgold1 = "Donutgold1.png"


# The game starts here.

label start:

    #####SCENE 1
    scene upperhallway:
        size (1920, 1080)
    with slowdissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show donutgold1

    play music "<from 0 to 7>audio/red_sun_in_the_sky.mp3" volume 0.1 noloop

    # These display lines of dialogue.

    arnav "BOOM WADDUP ARNAV BACK HERE"

    mc "This man..."

    "Once again I am greeted by my friend arnav. He has been my friend since we were in kindergarten together"

    arnav "Coming to class?"

    mc "yea.. sure..."

    "As we walk I think about my life choices and feel that something very interesting is about to happen to me today"

    arnav "I hope teacher curves the next test my parents aren't so happy about me having a F in prealgebra"

    "Arnav has always been someone who saves his homework till the last minute. Nothing gets between him and his League of Legends games."

    mc "Maybe if you studied more your parents wouldn't be so mad at you"

    arnav "Yeah.. I guess.."

    scene staircase:
        size (1920, 1080)
    with slowdissolve

    show donutgold2

    arnav "By the way... Clubs start today and I am in the best club at BCA called BCA Esports club. You should join we need another member"

    mc "Nahh... I'm not really a gamer to be honest. Besides I have a lot of work to do anyway."

    arnav "Come on! it will be fun! And its really easy to learn. BCA esports is filled with a lot of cool kids you'll make so many friends too!"

    mc "It sounds fun, but I'd rather just go home- sorry"

    arnav "... That sounds so lame"

    mc "Says the person who plays League of Legends"


    #####SCENE 3
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene transition:
        size (1920, 1080)
    with slowdissolve

    scene lowerhallway:
        zoom 2.0
    with dissolve
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show cellphone

    # These display lines of dialogue.

    play music "audio/CellPhoneRing.mp3" noloop
    "Rrrrrrrrrring. Rrrrrrrrrring."

    "Mom" "Hi honey"

    mc "Hi mom. Are you almost here to pick me up?"

    "Mom" "About that..."

    mc "Don't even tell me this is about you and dad again-"

    "Mom" "Listen, sweetie, your dad and I have been talking and... we think it's time for you to know."

    mc "What?"

    "This can't be good."

    "Mom" "Your father and I have been making sects."

    mc "???"

    "Mom" "Anyway, you'll have to stay late after school today until we can come pick you up in the cope-mobile. Cya."

    "Click."

    scene
    scene lowerhallway:
        zoom 2.0

    "As I put my phone back into my pockets filled with pringles cans, I check my hello-kitty watch for the time."

    mc "Damn.. already 16 O'clock. Guess I might as well check out that BCA Esports club."

    ############# Scene 4

    scene transition:
        size (1920, 1080)
    with slowdissolve

    scene compsci1:
        zoom 2.0
    with dissolve

    show julian1

    jul "Who's this noob? You know this club is only for diamond plus players right? You look like you've touched grass AND talked to women recently.\
    There's no way you're above bronze."

    mc "My bad?"

    hide julian1

    show julian2:
        zoom 4.0
        ypos 0
        xpos 400

    jul "Well, as long as you agree..."

    hide julian2

    show donutgold2

    arnav "WASSUP BlGBol, UWU!"

    mc "Hello arnav."

    "Wait"

    scene transition:
        size (1920, 1080)
    with slowdissolve

    scene compsci1:
        zoom 2.0
    with dissolve

    show donutgold3:
        zoom 1.5
        xpos 500

    "HE'S HOT!??!?!?"

    mc "Uhh.. h- hi arnav"

    arnav "Anyway, jul, this is the guy I was telling you about. I think he'd be really good for our team for the tournament!"

    hide donutgold3

    show julian2:
        zoom 4.0
        ypos 0
        xpos 400

    jul "Really? Him?"

    hide julian2

    show donutgold1

    arnav "Yeah, he's super cool and awesome! NYYAAA!!"

    mc "Please stop that"

    hide donutgold1

    show julian2:
        zoom 4.0
        ypos 0
        xpos 400

    jul "Well, I guess its ok then..."

    hide julian2

    mc "What was this about a tournament?"

    show tsk2

    TSK "What's up gamers. What's going on over here?"

    hide tsk2

    show nate1

    nate "Uhhh Hii."

    mc "Hi i guess"

    nate "I go play val. bye"

    hide nate1

    show julian1

    jul "So this is our team. Because you're new, you're gonna need some practice games before the big tournament."

    mc "What tournament!??!?!?!?"

    jul "Pick idiot."



    #####SCENE 5


    scene lowerhallway:
        size (1920,1080)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    menu:
        "Duo with TSK.":
            jump choiceTSK
        "Duo with Julian":
            jump choiceJulian
        "Duo with Nate":
            jump choiceNate
        "Duo with Arnav":
            jump choiceArnav

    label choiceTSK:
        scene transition:
            size (1920, 1080)
        with slowdissolve
        scene compsci1:
            size (1920,1080)
        show tsk3:
            ypos 300
            xpos 700
        TSK "Would you like to play one for all?"
        menu:
            "I would love to!":
                jump oneforall
            "no we're playing ranked >:(":
                jump ranked
        label ranked:
            TSK ":(, alright we're gonna lose so much LP not my LP :(("
            "I queue up for a ranked solo/duo invite TSK23, I go adc and TSK goes support"
            TSK "I hate playing support though"
            mc "I don't care"
            "The game goes fine but suddenly you notice TSK go silent and his character in game stops moving"
            mc "what are you doing?????"
            "I start to spam missing pings"
            "After I get blocked from pings I turn around and find TSK ASLEEP!!!!"
            hide tsk3
            show tsk2:
                ypos 350
                xpos 800
            pause(1.0)
            mc "WHAT THE HECK!!!!! IM DONE"
            "I get up and leave the school never to talk to TSK ever again"
            jump end
        label oneforall:
            TSK "YAYYYYY we should play GRAGAS my main"
            mc "sureee ig"
            "the game goes smoothly with lots of belly bumping and barrel smashing"
            TSK "WE WON LETS GOOOO"
            mc "yea because of me"
            "you press tab and see that you are 21/0 while TSK is 1/15"
            mc "are you good at any game I just started playing this and you did worse than me!"
            mc "oh wait I think I heard you were good a pulsus"
            TSK "DID SOMEONE SAY PULSUS?????!?!?!??!?!?!??!??!??!"
            TSK "DID YOU KNOW I AM RANK 86 IN PULSUS LIKE DOUBLE DIGIT TOP 100!!!!!!"
            TSK "to be fair, you have to have a very high IQ to understand technical mapping. The SV changes are extremely subtle, and without a solid grasp of music theory most of the quality will go over a typical players head. Theres also Monstratas triangular outlook, which is deftly woven into his mapping - his personal philosophy"
            pause (1.0)
            TSK "draws heavily from Pishifat literature, for instance. The fans understand this stuff; they have the intellectual capacity to truly appreciate the Depths of these patterns, to realize that they're not just high quality- they say something deep about MAPPING. As a consequence people who dislike technical maps truly ARE idiots-"
            menu:
                "pls be quiet":
                    jump nothingmatters
                "...":
                    jump nothingmatters
            label nothingmatters:
                TSK "of course they wouldn't appreciate, for instance, the quality in Sotarks existencial catchphrase this needs more overdone jumps, which itself is a Cryptic reference to Monstratas map quaver. Im smirking right now just imagining one of those addlepated simpletons scratching their heads in confusion as Natsus genius unfolds"
                TSK "itself on their computer screens. What fools... how I pity them. :joy: And yes by the way, I DO have a Monstrata slider butterfly tattoo. And no, you cannot see it. It's for the ladies eyes only- And even they have to demonstrate that they're within 5 PP points of my own (preferably lower) beforehand."
                "you get fed up and leave the man rambling on and on about a game noone even knows"
                jump end

    label choiceJulian:
        scene transition:
            size (1920, 1080)
        with slowdissolve
        scene hallway1:
            size (1920,1080)
        Julian ""
        jump end

    label choiceNate:
        scene transition:
            size (1920, 1080)
        with slowdissolve
        scene lowerhallway:
            size (1920,1080)
        Nate ""
        jump end

    label choiceArnav:
        scene transition:
            size (1920, 1080)
        with slowdissolve
        scene hallway1:
            size (1920,1080)
        Arnav ""
        jump end

    label end:
        hide tsk2
        hide tsk3
        show greygirl1:
            size (290,433)
            ypos 350
            xpos 800
        "forever I will be alone"

    # This ends the game.

    return
