from sys import exit

def forest():
    print "You enter a dark forest."
    print "You hear strange sounds, screams of terror and red, glowing eyes follow your steps."
    print "Do you start to run?"

    choice = raw_input ("> ")

    if "yes" in choice:
        print "You run for your life."
        print "Suddenly you hear heavy steps behind you."
        print "The footsteps are approaching you very fast."
        print "You increase your pace and the footsteps fade away."
        print "The surrounding area gets brighter and you reach the outskirts of the forest."
        kingdom()

    elif "no" in choice:
        print "You slowly walk through the forest, admiring the beauty of the knaggy trees and creepy creatures around you."
        print "Suddenly you hear a sound behind you, left, right - you are surrounded."
        print "Dark creatures descend upon you and tear you apart."
    else:
        dead ("You stumble bewildered trough the wilderness and will probably die a cruel death.")


def duel():
    print "You both draw your swords and start duelling."
    print "You're opponent has got a pretty good cover, you better not underestimate him!"
    print "What are you going to do?"
    cover_down = False

    while True:
        choice = raw_input("> ")

        if choice == "run":
            print "You fool are no knight! Go and work on the fields!"


        elif choice == "strike" and not cover_down:
            print "You strike a strong blow, your opponent blocks your sword but stumbles and loses his cover."
            cover_down = True
        elif choice == "strike" and cover_down:
            print "Your opponent's cover is not up and you hit him in the chest!"
            print "He stumbles and goes down, you are free to pass the bridge!"
        elif choice == "pass" and cover_down:
            print "You pass the bridge."
            print "After a short while fields, forests and nature get replaced by cottages, forges and mills."
            print "You are now in the outskirts of King Jamies kingdom."
            print "Shortly after you pass the gatehouse of King Jamies castle."
            print "Suddenly a hand touches your arm and an old, wrinkled woman shouts at you: 'YOU! You look like a brave knight looking for adventures. My sweet daughter got lost in the mountains, please go and find here!'"
            choice = raw_input("> ")

            if "yes" in choice:
                print "You turn around and start your way back to the mountains."
                mountain()

            if "no" in choice:
                print "Really? Do you even want to win this game?"


        else:
            print "You should rethink your life, man."


def kingdom():
    print "After you left the forest you quickly arrive at a bridge across a stream."
    print "As you start passing the bridge a voice shouts at you: 'Halt you fool. You cannot pass the bridge to the kingdom of King Jamie without paying a toll!'"
    print "Do you pay the toll or ask for alternatives?"

    choice = raw_input("> ")

    if "pay" in choice:
        print "You pay the toll and pass the bridge."
        print "After a short while fields, forests and nature get replaced by cottages, forges and mills."
        print "You are now in the outskirts of King Jamies kingdom."
        print "Shortly after you pass the gatehouse of King Jamies castle."
        print "Suddenly a hand touches your arm and an old, wrinkled woman shouts at you: 'YOU! You look like a brave knight looking for adventures. My sweet daughter got lost in the mountains, please go and find her!'"

        choice = raw_input("> ")

        if "yes" in choice:
            print "You turn around and start your way back to the mountains."
            mountain()

        if "no" in choice:
            print "Really? Do you even want to win this game?"


        else:
            dead ("Really? Do you even want to win this game?")


    if "alternatives" in choice:
        print "Oh, if you don't want to pay, you could also fight me, you wimp!"
        duel()

def fight():
    print "You step out of your cover and approach the wolves."
    print "Do you draw your sword?"

    choice = raw_input("> ")

    if "yes" in choice:
            print "You draw your sword and show the maid your fighting skills."
            print "After a short and bloody fight the surviving wolves flee."
            print "Congrats you just swept the maiden off her feet."
            print "Both of you return to King Jamies castle and you receive the title:"
            choice = raw_input("Enter your name > ")
            print "%s the wolfshunter" % choice
            exit(0)

    elif "no" in choice:
            print "You descend upon the wolves, screaming and waving your bare hands."
            print "The wolves snap at your arms and start tearing you apart."


    else:
        dead("You leave the scenery and continue your life living as a coward.")


def mountain():
    print "You hike to the top of a mountain"
    print "suddenly you hear screaming and shouting."
    print "What will you do?"

    choice = raw_input("> ")

    if "ignore" in choice:
        print "You coward! Rethink your life and decide if brave knight is the right job for you!"


    elif "approach" in choice:
        print "You sneak to the direction of the noise."
        print "You discover a maid, surrounded by a pack of wolves."
        fight()
    else:
        dead("*programmer shakes head*")


def dead(why):
    print why, "Shame on you!"
    #exit(0)

def start():
    print "You are a brave knight."
    print "You strive for glory."
    print "You left your hometown to experience glorious adventures"
    print "After a short hike you arrive at a fork."
    print "Do you walk through the forest or do you take the way across the mountain?"

    choice = raw_input("> ")

    if choice == "forest":
        forest()
    elif choice == "mountain":
        mountain()
    else:
      dead("You scaredy cat are no knight! You continue to live your life in shame.")
      

start()
