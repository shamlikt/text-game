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
        pass



class Engine(object):
    def __init__(self):
        pass



class Death(object):
    def __init__(self):
        pass

def start():
    pass




if __name__ == '__main__':
    pass




