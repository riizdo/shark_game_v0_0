import pygame
from pygame.locals import *


#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 50, 255)


class TMenu:
    __mode = ('initial', 'playing')
    __actual = __mode[0]
    def __init__(self):
        self.__mode = ('initial', 'playing')
        self.actual = self.__mode[0]
        self.element = {'button': {}, 'label': []}
        self.level = 1
        self.player = ''
        self.score = 0
        self.data = [self.level, self.player, self.score]
        
        
    def __str__(self):
        return self.__actual
    
    
    def player(self, player = None):
        if player == None:
            return self.data[1]
        else:
            self.data[1] = player
            
            
    def addScore(self, value = 1):
        self.data[2] += value
        
        
    def mode(self, value = None):
        if value == None:
            return self.actual
        else:
            self.actual = value
    
        
    def addButton(self, text1 = None, text2 = None, rect = None):
        self.element['button'][text1] = Button(text1, text2)
        if rect != None:
            print(self.element)
            self.element['button'][text1].setRect(rect)
        
        
    def addLabel(self):
        label = Label()
        self.element['label'].append(label)
        
        
        
    def draw(self, surface):
        for list in self.element:
            count = 0
            for element in self.element[list]:
                self.element[list][element].draw(surface, element + '{}'.format(self.data[count]))
                count += 1
        
        
        
        
class Menu(TMenu):
    def __init__(self, margin):#constructor of class
        TMenu.__init__(self)
        self.__margin = margin
        
        self.menu(self.actual)
        

        
    def menu(self, menu = None):
        if menu == None:
            return self.actual
        else:
            if self.actual != menu:
                self.actual = menu
                if self.actual == 'initial':
                    self.__initial()
                elif self.actual == 'playing':
                    self.__playing()
        
            
            
    def __clear(self):
        self.element['button'].clear()
        self.element['label'].clear()
            
            
    def __initial(self):
        pass
    
    
    def __playing(self):#menu of screen of the game
        self.__clear()
        
        sizeButton = (400, 60)
        rectButton = (self.__margin[0], self.__margin[1] + self.__margin[3] - sizeButton[1], sizeButton[0], sizeButton[1])
        self.addButton('NIVEL: ', '{}'.format(self.level), rectButton)
        
        rectButton = (sizeButton[0], self.__margin[1] + self.__margin[3] - sizeButton[1], sizeButton[0], sizeButton[1])
        self.addButton('JUGADOR: ', '{}'.format(self.player), rectButton)
        
        rectButton = (sizeButton[0] * 2, self.__margin[1] + self.__margin[3] - sizeButton[1],\
                      (self.__margin[0] + self.__margin[2]) - (sizeButton[0] * 2), sizeButton[1])
        self.addButton('PUNTOS: ', '{}'.format(self.score), rectButton)
        
        

class Button:
    def __init__(self, text1 = None, text2 = None):
        self.__tSize = ('personalized', 'little', 'medium', 'big')
        self.__size = self.__tSize[2]
        
        self.__type = 'button'
        self.__color = BLUE
        self.__colorMargin = ''
        self.__label = None
        self.__image = []
        self.__current = 0
        self.__position = {'x': 0, 'y': 0}
        
        if text1 == None:
            self.__label = None
        elif text1 != None and text2 == None:
            self.__label = Label(text1)
            self.__label.center(self.getRect())
        elif text1 != None and text2 != None:
            self.__label = Label(text1 + text2)
            self.__label.center(self.getRect())
        
        self.__rect = self.getRect()
        #self.__chargeImage()
        
    def __str__(self):
        return 'button, label: {}'.format(self.__label)
    
    
    def setRect(self, rect):
        self.__size = 'personalized'
        self.__rect = rect
        self.pos(rect[0], rect[1])
        if self.__label != None:
            self.__label.center(rect)
    
    
    def __chargeImage(self):
        exist = True
        
        while exist:
            try:
                self.__image.append(pygame.image.load('images/' + self.__type + '_' + self.__size + '.png'))
            except:
                exist = False
    
    
    def pos(self, x = None, y = None):
        if x == None and y == None:
            pos = (self.__position['x'], self.__position['y'])
            return pos
        elif x != None and y != None:
            self.__position['x'] = x
            self.__position['y'] = y
            if self.__label != None:
                self.__label.pos(x, y)
    
    
    def draw(self, surface, data):
        if len(self.__image) > 0:
            pass
        else:
            pygame.draw.rect(surface, self.__color, self.getRect())
            print('draw button and label {}'.format(self.__label))
            if self.__label != None:
                self.__label.draw(surface, data)
    
    
    def getType(self):
        return self.__type
        
        
    def setLabel(self, text = None, size = None, font = None):
        self.__label = Label(text, size, font)
        self.__label.pos(self.__position['x'], self.__position['y'])
        self.__label.center(self.getRect())
            
            
    def color(self, color = None):
        if color == None:
            return self.__color
        else:
            self.__color = color
            
            
    def colorMargin(self, color = None):
        if color == None:
            return self.__colorMargin
        else:
            self.__colorMargin = color
            
            
    def getRect(self):
        if self.__size == self.__tSize[1]:
            return (self.__position['x'], self.__position['y'], 75, 30)
        elif self.__size == self.__tSize[2]:
            return (self.__position['x'], self.__position['y'], 125, 60)
        elif self.__size == self.__tSize[0]:
            return self.__rect
    

 
    

class Label:
    def __init__(self, text = None, size = None, font = None):
        if text == None:
            self.__text = 'label'
        else:
            self.__text = text
        if size == None:
            self.__size = 25
        else:
            self.__size = size
        if font == None:
            self.__font = 'arial'
        else:
            self.__font = font
            
        self.__position = {'x': 0, 'y': 0}
        self.__type = 'label'
            
        self.__tFont = pygame.font.SysFont(self.__font, self.__size)
        
        self.__textSurface = self.__tFont.render(self.__text, True, WHITE)
        
        
    def __str__(self):
        return 'label rect {}'.format(self.getRect())
    
    
    def draw(self, surface, data):
        self.__text = data
        self.__textSurface = self.__tFont.render(self.__text, True, WHITE)
        surface.blit(self.__textSurface, self.pos())
        
        
    def center(self, surface):
        surfaceCenterX = int((surface[0] + surface[2]) / 2)
        surfaceCenterY = int((surface[1] + surface[3]) / 2)
        labelCenterX = int((self.getRect()[0] + self.getRect()[2]) /2)
        labelCenterY = int((self.getRect()[1] + self.getRect()[3]) /2)
        distanceX = surfaceCenterX - labelCenterX
        distanceY = surfaceCenterY - labelCenterY
        self.pos(self.__position['x'] + distanceX, self.__position['y'] + distanceY)
        
        
    def getRect(self):
        return self.__textSurface.get_rect(topleft = (self.__position['x'], self.__position['y']))
        
        
    def pos(self, x = None, y = None):
        if x == None and y == None:
            pos = (self.__position['x'], self.__position['y'])
            return pos
        elif x != None and y != None:
            self.__position['x'] = x
            self.__position['y'] = y
    
    
    def getType(self):
        return self.__type
        
        
    def text(self, text = None):
        if text == None:
            return self.__text
        else:
            self.__text = text
        
        
    def size(self, size = None):
        if size == None:
            return self.__size
        else:
            self.__size = size
            
            
    def font(self, font = None):
        if font == None:
            return self.__font
        else:
            self.__font = font
            
            
            
            
class Level(TMenu):
    def __init__(self):
        TMenu.__init__(self)
        
        self.__score = 0
        self.__level = 1
        
        
    
if __name__ == '__main__':
    menu = Menu()
    print(menu)