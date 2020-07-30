import pygame
from pygame.locals import *

class Menu:
    def __init__(self):
        self.__mode = {}
        self.__actual = 'initial'
        self.element = []
        
        
    def __str__(self):
        return self.__actual
        
        
    def mode(self, value = None):
        if value == None:
            return self.__mode[self.__actual]
    
    
    def __charge(self, mode = None):
        if mode == None:
            return None
        
        for menu in self.__mode[mode]:
            pass
        
        
    def addButton(self):
        button = Button()
        self.__element.append(button)
        
        
    def addLabel(self):
        label = Label()
        self.__element.append(label)
        
        

class Button:
    def __init__(self):
        self.__colorBackground = ''
        self.__colorMerge = ''
        self.__label = None
        self.__image = []
        self.__position = {'x': 0, 'y': 0}
        
        
    def setLabel(self, text = None, size = None, font = None):
        self.__label = Label(text, size, font)
            
            
    def colorBackground(self, color = None):
        if color == None:
            return self.__colorBackground
        else:
            self.__colorBackground = color
            
            
    def colorMerge(self, color = None):
        if color == None:
            return self.__colorMerge
        else:
            self.__colorMerge = color
            
            
    def getRect(self):
        return self.__image[self.__state].get_rect(topleft = (self.__position['x'], self.__position['y']))
    
    

class Label:
    def __init__(self, text = None, size = None, font = None):
        if text == None:
            self.__text = ''
        else:
            self.__text = text
        if size == None:
            self.__size = 12
        else:
            self.__size = size
        if font == None:
            self.__font = 'arial'
        else:
            self.__font = font
            
        self.__position = {'x': 0, 'y': 0}
            
        self.__tFont = pygame.font.SysFont(self.__font, self.__size)
        
        
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
            
        
    
if __name__ == '__main__':
    menu = Menu()
    print(menu)