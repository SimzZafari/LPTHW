from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This is a blueprint of a scene construction"
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

            current_scene.enter()

class Cave(Scene):
    def enter(self):
      print "Your head hurts. You must have hit a rock or something."
      print "You open your eyes and see nothing, but darkness."
      print "Where are you and where are your friends?"
      print "Slowly you get onto your feet.."
      print "and promptly hit your head again."
      print "You stand on a rocky ground and just hit your head
      print "at the hard stone ceiling above you."
      print "It has to be a cave...but how did you get here?!"
      print "The last thing you remember is sitting at a camp fire with your friends."
      print "Spending the last warm days of the year in the wild..."
      print "seemed like the perfect idea back then."
      print "Thinking about what happened you stumble forward and hit something with your foot."
      print "Do you get on your knees and search the ground for the object?"

      action = raw_input("> ")

      if action == "Yes":
        print "You get on your knees and slide across the rocky surface."
        print "Suddenly your hands touch something hairy."
        print "Your heart stops for a second and you quickly crawl backwards."
        print "Your left hand touches something, which does not feel like a rock."
        print "It feels like a backpack!"
        print "You open the hatch and find something that feels like a flashlight."
        return 'LitCave'

      elif action == "No":
        print "You do not care about anything on the ground of this dark, deadly cave."
        print "Sightless you start your way into any direction."
        print "After a few minutes it seems like your eyes get used to the darkness."
        print "Just in the moment you feel like you can see a few meters you stumble over a little rock."
        print "While falling you stretch your arms and try to safe you from a nasty fall."
        print "But you grab into nothing!"
        print "While walking through the darkness you came to a pretty deep crack."
        print "You start screaming, while you fall into the darkness - but nobody will hear your voice, which slowly dies away..."
        return 'Cave'

      else:
        print "You have to decide!"
        print "Try again!"
        return 'Cave'

class LitCave(Scene):
    def enter(self):
      print "Now you have a fleshlight in your hand."
      print "Do you activate the flashlight?"

      action = raw_input("> ")
      if action == "Yes":
          print "You activate your flashlight and inspect the surrounding area."
          print "It seems like you are in a deep cave, the ceiling is damp and water drops fall to the ground."
          print "You follow the drops and turn the light onto the floor."
          print "You burst out in fear - next to you in a big puddle of blood lies a corpse."
          print "Its head is bashed in and you recognize its figure...It is one of your friends!"
          print "Fear and anger grab your mind - you have to calm down quickly."
          print "To calm down you deactivate your flashlight, lean against the wall and start to count until 3."
          print "Write 1,2,3 to calm down"

          action = raw_input("> ")



          if action == "1,2,3":
                print "Surrounded by complete darkness you slowly start counting from 1 to 3."
                print "You feel a little bit better and start over again."
                print "1...2...3..."
                print "1...2...3..."
                return 'NotAlone'

          else:
            print "You can't manage to calm down and lose your mind - GAME OVER"
            Cave()

      elif action == "NO":
            print "You can't manage to calm down and lose your mind - GAME OVER"
            return 'Cave'

      else:
        print "You can't manage to calm down and lose your mind - GAME OVER"
        return 'Cave'

class NotAlone(Scene):

    def enter(self):
        print "1...2..Wait, what was that?!"
        print "To your left you hear something."
        print "You try to merge into the wall and hold your breath."
        print "You hear rattling breathing and long claws scratching across the walls."
        print "You look to the left and see two huge, yellow glowing eyes in the darkness."
        print "What do you want to do?"

        action = raw_input("> ")

        if action == "Stay":
            print "You pray to good that the creature won't notice your presence."
            print "You hold your breath."
            print "Suddenly a bloodcurdling scream grows from your left."
            print "Whimpering you sink to the ground and wrap your arms around you."
            print "Slowly, out of the darkness a shadow approaches you..."
            print "GAME OVER"
            return 'NotAlone'


        elif action == "Run":
            print "You activate your flesh light and point at the huge eyes of the creature."
            print "Immediately its eyes start to fume and it starts screaming in pain."
            print "You turn around and notice a corridor on the right, leading upwards."
            print "Without looking back you start your way upwards."
            return 'GetOut'

    #else:
    #    print "You are not alone in front of your PC...turn around!"
    #    print "GAME OVER"
    #    Cave()

class GetOut(Scene):

    def enter(self):
        print "You run for your life."
        print "Far behind you you hear the strange creature shouting in pain and agony."
        print "You look over your shoulder and suddenly a glowing light approaches with a fast pace."
        print "You speed up your pace."
        print "The corridor you are running through leads you into a huge cavern."
        print "It is covered with glowing lichen."
        print "In the dim light you can see three corridors descending into the darkness."
        print "Behind you the scratching and screaming gets louder and you can smell a sour stench."
        print "Which corridor do you take?"

        good_corridor = randint(1,3)
        guess = raw_input("[corridor #]> ")

        if int(guess) != good_corridor:
            print "You descend into corridor %s and speed up your pace again." % guess
            print "You totally forgot to turn on your flashlight again."
            print "With a click its light cone appears and you can finally see something."
            print "You stop in shock and stand still..."
            print "As your glance reaches the ceiling of the corridor you notice the egg-like things growing over your head."
            print "You straight on ran into the nest of whatever is hunting you."
            print "You realize that you are doomed..."
            print "GAME OVER!"
            return 'Cave'

        else:
            print "You descend into corridor %s and speed up your pace again." % guess
            print "The thick, damp air suddenly gets better and you hear a waterfall."
            print "You run around a corner and see the falling water, you rush in its direction."
            print "You burst through the wall of water and stand at the corner of a huge lake."
            return 'finished'


class Finished(Scene):

    def enter(self):
            print "You are free, you escaped the cave."
            print "You get on your knees and start to realize what kind of scary experience you just escaped."
            print "As you sit there, organizing your thoughts, a shadow slowly descends out of the waterfall at your back..."
            print "The end..."
            return 'finished'

class Map(object):

    scenes = {
        'Cave': Cave(),
        'LitCave': LitCave(),
        'NotAlone': NotAlone(),
        'GetOut': GetOut(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):

        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('Cave')
a_game = Engine(a_map)
a_game.play()
