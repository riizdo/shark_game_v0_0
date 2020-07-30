import pygame, sys, os, pnj, menu
from pygame.locals import *

class MainApp():
    __screenSize = (1500, 700)
    
    def __init__(self):
        pygame.init()
        self.__screen = pygame.display.set_mode(self.__screenSize)
        pygame.display.set_caption("Contra-Tiburones")
        self.__screen.fill((0, 0, 150))
        self.__merge = self.__screen.get_rect()
        
        self.__enemy = []
        self.__enemy.append(pnj.Stripe())
        self.__enemy.append(pnj.Stripe())
        self.__enemy.append(pnj.Stripe())
        self.__enemy.append(pnj.Turtle())
        self.__player = pnj.Shark()
        self.__player.setPlayer()
        
        self.__player.pos(int((self.__merge[0] + self.__merge[2]) / 2), (self.__merge[1] + self.__merge[3]) - self.__player.getRect()[3])
        self.__enemy[0].pos(500, 100)
        
        self.__menu = menu.Menu()
        
        
    def __str__(self):
        return 'player: {}'.format(self.__player.name())
        
        
    def close(self):
        pygame.quit()
        sys.exit()
        
        
    def getCollision(self):
        count = 0
        collision = {'merge': {'up': False, 'down': False, 'left': False, 'right': False}}
        
        if self.__player.getRect()[0] <= self.__merge[0]:
            collision['merge']['left'] = True
        if self.__player.getRect()[0] + self.__player.getRect()[2] >= self.__merge[0] + self.__merge[2]:
            collision['merge']['right'] = True
        if self.__player.getRect()[1] <= self.__merge[1]:
            collision['merge']['up'] = True
        if self.__player.getRect()[1] + self.__player.getRect()[3] >= self.__merge[1] + self.__merge[3]:
            collision['merge']['down'] = True
            
        for enemy in self.__enemy:
            collision['enemy' + str(count)] = self.__getCollisionObject(self.__player, enemy)
            count += 1
            
        return collision
    
    
    def __getCollisionObject(self, object1, object2):
        rect1 = object1.getRect()
        rect2 = object2.getRect()
        obj1 = {'up': rect1[1], 'down': rect1[1] + rect1[3], 'left': rect1[0], 'right': rect1[0] + rect1[2]}
        obj2 = {'up': rect2[1], 'down': rect2[1] + rect2[3], 'left': rect2[0], 'right': rect2[0] + rect2[2]}
        
        collision = {'up': False, 'down': False, 'left': False, 'right': False}
        
        if obj1['up'] < obj2['down'] and obj1['up'] > obj2['up'] and self.__collisionPart('up', obj1, obj2):
            collision['up'] = True
           
        
        return collision
    
    
    def __collisionPart(self, part, object1, object2):
        if part == 'up' or part == 'down':
            if (object1['left'] > object2['left'] and object1['left'] < object2['right'])\
               or (object1['right'] < object2['right'] and object1['right'] > object2['left'])\
               or (object1['left'] < object2['left'] and object1['right'] > object2['right'])\
               or (object1['left'] > object2['left'] and object1['right'] < object2['right']):
                return True
        if part == 'left' or part == 'right':
            pass
            
        
        
    def start(self):
        state = True
        move = {'x': 0, 'y': 0}
        collision = {}
        up = False
        down = False
        right = False
        left = False
        
        while state:
            collision = self.getCollision()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:#event for quit game
                    pygame.quit()
                    state = False
                    self.close()
                if event.type == pygame.KEYDOWN:#key press events
                    if event.key == K_UP:
                        move['y'] = -1
                        up = True
                    elif event.key == K_DOWN:
                        move['y'] = 1
                        down = True
                    elif event.key == K_RIGHT:
                        move['x'] = 1
                        right = True
                    elif event.key == K_LEFT:
                        move['x'] = -1
                        left = True
                    elif event.key == K_SPACE:
                        print('shark rect {}, enemy rect {} collision {}'.format(self.__player.getRect(),
                                                                                  self.__enemy[0].getRect(), collision))
                if event.type == pygame.KEYUP:#key release events
                    if event.key == K_UP:
                        up = False
                        if down:
                            move['y'] = 1
                        else:
                            move['y'] = 0
                    elif event.key == K_DOWN:
                        down = False
                        if up:
                            move['y'] = -1
                        else:
                            move['y'] = 0
                    elif event.key == K_RIGHT:
                        right = False
                        if left:
                            move['x'] = -1
                        else:
                            move['x'] = 0
                    elif event.key == K_LEFT:
                        left = False
                        if right:
                            move['x'] = 1
                        else:
                            move['x'] = 0
                            
            if collision['merge']['up'] and move['y'] < 0:#comprove if player collision with merge
                move['y'] = 0
            if collision['merge']['down'] and move['y'] > 0:
                move['y'] = 0
            if collision['merge']['left'] and move['x'] < 0:
                move['x'] = 0
            if collision['merge']['right'] and move['x'] > 0:
                move['x'] = 0
                
            if collision['enemy0']['left'] \
               or collision['enemy0']['right']\
               or collision['enemy0']['up']\
               or collision['enemy0']['down']:#comprove if player collision of enemy
                #print(collision)
                pass
                
            self.__player.move(move['x'], move['y'])#move the player
                    
            self.__screen.fill((0,0,200))#color of background
            
            for enemy in self.__enemy:
                enemy.move()
                self.__screen.blit(enemy.getImage(), enemy.pos())#enemy image
                
            self.__screen.blit(self.__player.getImage(), self.__player.pos())#player image
                    
            pygame.display.flip()#refresh screen
            
            
if __name__ == '__main__':
    game = MainApp()
    game.start()