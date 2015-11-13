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
        self.carrying = []
        self.stage = 1
        self.death = Death()    

    def do(self,command):
        if self.stage == 1:
            if 'back door' in command:
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
            if 'room' in command :
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

    box = Object("match box","some one forgot to take after smoking")
    scene_one = "Bike parking area"
    des_one = "full of bikes\n two way fron door or back door"
    bike_parking = Scene(scene_one ,des_one,[box])
    
    scene_two = "back room"
    des_two = "naroow varantha , toilet on the left side, \n OMG manger is coming ...you will loos your halfday sallry if she see you "
    back_room = Scene ( scene_two , des_two)
    
    scene_tree = "toilet "
    des_tree = " fire alarm  triger or open door"
    toilet = Scene (scene_tree, des_tree)

    scene_four = "alarm "
    des_four = "go to manager room or runn to ground "
    alarm = Scene(scene_four, des_four)

    bike_parking.out = back_room
    back_room.out = toilet
    toilet.out = alarm

    start = Engine(bike_parking)
    return start



if __name__ == '__main__':
    print " Welcome to mission msp "
    print "*" * 20
    start = start()

    while True:
        print """"""
        start.current.describe()
        print """"""
        command = raw_input (" what you gonna do ?")
        start.do(command)









