from sys import exit
class Object(object):
    def __init__(self,thing,description):
        self.thing = thing
        self.description = description


    def describe(self):
        return "%s %s "%(self.name,self.description)



class Scene(object):
    def __init__(self,name,description,objects=None):
        self.name = name
        self.des = description
        if objects == None:
            objects = []
        self.objects = objects
        
            
    def describe(self):
        print self.name
        print self.des
        for i in self.objects:
            print i
    


class Engine(object):
    def __init__(self,scene):
        self.current=scene
        self.carrying = []
        self.death = Death()
        self.stage = 1
    
    def do(self,command):
        if self.stage == 1:
            if 'back door' in command:
                print " WAW.....Nice Decision"
                self.stage=2
            elif "matchbox" in command:
                self.carrying.append("matchbox")
                print "Now you got matchbox"
            else:
                self.death.message(1)
        elif self.stage == 2:
            if 'hide' in command:
                print "shittty smell better than half day leave "
                self.stage = 3
            else:
                self.death.message(2)

        elif self.stage == 3:
            if ' fire alarm ' in command:
                print " mind blowing idea ..but watch ur dress "
                self.stage = 4
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
    def message(stage):
        if stage == 1 :
            print " You r A LOOOOOOOSER ,\n GO and learn how to bunk  class "





def start():
    pass




if __name__ == '__main__':
    pass




