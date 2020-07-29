import pygame, timeit
from pygame.locals import *


class Pnj:
    
    def __init__(self, type = None):#constructor of superclass
        self.__controlTime = pygame.time.get_ticks()
        self.__image = []
        self.__mask = []
        self.__position = {'x': 0, 'y': 0}
        self.seconds = 60
        self.__change = False
        self.__armor = 0
        self.__speed = 0
        self.__type = ''
        self.__name = ''
        self.__previusPose = 0
        self.__currentPose = 0
        self.__colour = ''
        self.__controlTime = float(self.__controlTime)
        
        if type != None:
            self.__type = type
            self.chargeImages(self.__type)
            
            
    def __str__(self):#method of string output
        return 'name: {}, type: {}, position: {}x, {}y, armor: {}, speed: {}'.format(self.__name,
                                                                                     self.__type,
                                                                                     self.__position['x'],
                                                                                     self.__position['y'],
                                                                                     self.__armor,
                                                                                     self.__speed)
            
            
    def getRect(self):
        return self.__image[self.__currentPose].get_rect(topleft = (self.__position['x'], self.__position['y']))
        
        
    def name(self, name = None):
        if name == None:
            return name
        else:
            self.__name = name
            
            
    def seconds(self, seconds = None):
        if seconds == None:
            return self.seconds
        else:
            self.seconds = seconds
            
            
    def pos(self, x = None, y = None):
        if x == None and y == None:
            pos = (self.__position['x'], self.__position['y'])
            return pos
        else:
            self.__position['x'] = x
            self.__position['y'] = y
            
            
    def move(self, x, y):
        self.__position['x'] += x
        self.__position['y'] += y
            
            
    def __selectPose(self):
        qImages = len(self.__image)
        timer = self.__timer()
        
        if self.__previusPose == self.__currentPose:
            if qImages % 2 == 0:
                self.__currentPose = qImages / 2
                self.__currentPose = int(self.__currentPose)
                self.__previusPose = self.__currentPose - 1
            else:
                self.__currentPose = ((qImages + 1) / 2) - 1
                self.__currentPose = int(self.__currentPose)
                if qImages > 1:
                    self.__previusPose = self.__currentPose - 1
                else:
                    self.__previusPose = self.__currentPose
        elif timer and self.__currentPose == 0:
            self.__previusPose = self.__currentPose
            self.__currentPose = 1
        elif timer and self.__currentPose == qImages - 1:
            self.__previusPose = self.__currentPose
            self.__currentPose = qImages - 2
        elif timer and self.__currentPose != 0 and self.__currentPose != qImages - 1:
            if self.__previusPose < self.__currentPose:
                self.__previusPose = self.__currentPose
                self.__currentPose += 1
            else:
                self.__previusPose = self.__currentPose
                self.__currentPose -= 1
                
                
    def __timer(self):
            t = pygame.time.get_ticks()
            t = float(t)
            if ((self.__controlTime < t and t >= self.__controlTime + self.seconds) or
                (self.__controlTime > t and t + 60 >= self.__controlTime + self.seconds)):
                self.__controlTime = pygame.time.get_ticks()
                self.__controlTime = float(self.__controlTime)
                return True
            else:
                return False
        
            
    def getImage(self):
        self.__selectPose()
        return self.__image[self.__currentPose]
            
            
    def chargeImages(self, type):
        count = 0
        exist = True
        
        while exist:
            
            path = 'images/' + str(type) + str(count) + '.png'
            try:
                self.__image.append(pygame.image.load(path))
                count += 1
            except:
                exist = False
                
            
    
    
class Shark(Pnj):
    def __init__(self):#constructor of subclass
        Pnj.__init__(self)
        self.__type = 'shark'
        self.seconds = 80
        
        self.chargeImages(self.__type)
    
    
class Turtle(Pnj):
    def __init__(self):#constructor of subclass
        Pnj.__init__(self)
        self.__type = 'turtle'
        
        self.chargeImages(self.__type)
        
        
class Stripe(Pnj):
    def __init__(self):#constructor of subclass
        Pnj.__init__(self)
        self.__type = 'stripe'
        self.seconds = 250
        
        self.chargeImages(self.__type)
        
        
        
if __name__ == '__main__':
    shark = Shark()
    turtle = Turtle()
    stripe = Stripe()
    print(shark)
    print(turtle)
    print(stripe)