import pygame
from pygame.locals import *

class Menu:
    def __init__(self):
        self.__mode = {}
        self.__actual = 'initial'
        
        
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
        
        
    
if __name__ == '__main__':
    menu = Menu()
    print(menu)