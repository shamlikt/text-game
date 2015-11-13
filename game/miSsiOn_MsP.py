from sys import exit


class Object(object):
    def __init__(self,thing,description):
        self.thing = thing
        self.description = description

    def describe(self):
        return "%s %s "%(self.thing,self.description)


class Scene(object):
    def __init__(self,name,description,objects=None):
        self.name = name
        self.des = description
        if objects == None:
            objects = []
        self.objects = objects
        self.out = None
    
    def describe(self):
        print self.name
        print self.des
        if self.objects:
            for i in self.objects:
                print i.describe()
            
    
class Engine(object):
    def __init__(self,scene):
        self.current=scene        
        self.carrying = self.current.objects
        self.stage = 1
        self.death = Death()    

    def do(self,command):
        if self.stage == 1:
            if 'back' in command:
                print " WAW.....Nice Decision"
                self.current=self.current.out
                self.stage=2
            elif "matchbox" in command:
                print "Now you got matchbox"
                self.current.objects.pop()
            else:
                self.death.message(1)
        elif self.stage == 2:
            if 'hide' in command:
                print "shittty smell better than half day leave "
                self.current=self.current.out
                self.stage = 3
            else:
                self.death.message(2)
        elif self.stage == 3:
            if 'fire' in command and self.carrying:
                print " mind blowing idea ..but watch ur dress "
                self.current=self.current.out
                self.stage = 4
            elif 'fire' in command and not self.carrying:
                self.death.message('3a')
            else:
                self.death.message(3)
        elif self.stage == 4 : 
            if 'manager' in command :
                print '*' * 20
                print " MISSION  ACCOMPLISHED YOU GOT FULL DAY SALLARY " 
                print '*' * 20
                exit()
            else:
                self.death.message(4)


class Death(object):
    def message(self,stage):
        if stage == 1 :
            print " You r A LOOOOOOOSER ,\n GO and learn how to bunk  class "
            exit()
        elif stage == 2:
            print "Are MAD....? \n she will kick you out...."
            print "you lost your half day sallary..."
            exit()
        elif stage == '3a':
            print "How can you triger alarm without fire....."
            print "Remember that matchbox"
            print "Now stuck here...LOOSER"
            exit()
        elif stage == 3:
            print " OMG caught Red handed Now make some excuse"
            exit()
        else:
            print " Good news You lost ua job"
            


def start():

    box = Object("matchbox","some one forgot to take after smoking")
    scene_one = "\n\t\tBike Parking area"
    des_one = "In front of office building , old economy vehicles ,No super bike with 900 cc  ..Roof may collapse at any moment ,Two way to office , front door which straight leads to managers room , back door which leads to Narrow Passage anyone noticing that passage *  "
    bike_parking = Scene(scene_one ,des_one,[box])
    
    scene_two = "\n\t\tNarrow Passage"
    des_two = "Narrow passage which reaches to staff room. old files are kept in corners .. just like a usual government office . ..just remember 1960 Bollywood films. toilet is in the Left side.Be careful about your shoes so that its sound won't cheat u  ..look at your watch.time is running such a fast ... Oooff . aaaah .that mouse may destroy my life . god !I am just escaped. OMG......! Managers coming toward me from opposite side , you have two option Just say 'Hello good morning' with a Closeup Smile to manager or HIDE in the toilet .......|"
    back_room = Scene ( scene_two , des_two)
    
    scene_tree = "\n\t\tToilet "
    des_tree = " Awful smell , creepy spiders i hate them most  :(.. where are these  sweepers ? Next day must complaint about them . Fire alarm on the top left corner ...how can i escape from here ..yaaaa... Got an idea 'TRIGGER FIRE ALARM'  every one will run towards ground and I can easily put sign in register"
    toilet = Scene (scene_tree, des_tree)

    scene_four = "\n\t\tAlarm Running"
    des_four = "[keeeeeyeeee..keeeeeyeeeeee......] ... sound is not too loud ..curruption in alarm also.. Any way plan worked .. every one running from building ...Now got to 'MANAGER'/' room or stay in toilet  and loose half day Sallary "
    alarm = Scene(scene_four, des_four)

    bike_parking.out = back_room
    back_room.out = toilet
    toilet.out = alarm

    start = Engine(bike_parking)
    return start



if __name__ == '__main__':
    print "\t\t Welcome to miSsiOn MsP "
    print "*" * 60
    print  ''' No hero with Bazuka, no villain with neutron emitter , only  AleX with a matchBox.Alex Lazy Government Employe with Zero casual leave in his  credit , As usual  reached office at 10.30 AM .. of course 30 mnt late .. Now oua mission is to save his Half day salary by signing in attendance register without noticing no one .  Activate ua stealth mode and go trough back door hide in toilet , trigger the fire alarm using matchbox and go to manager's room '''

    print "\n\t\tSTART GAME"
    print "*" * 60


    start = start()

    while True:
        print """"""
        start.current.describe()
        print """"""
        command = raw_input (" what you gonna do ?")
        start.do(command)






