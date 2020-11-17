import pygame, sys, os, pnj, menu
from pygame.locals import *

class MainApp():
    __screenSize = (1400, 800)
    
    def __init__(self):
        pygame.init()
        self.__screen = pygame.display.set_mode(self.__screenSize)#pygame.RESIZABLE
        pygame.FULLSCREEN
        pygame.display.set_caption("Contra-Tiburones")
        self.__screen.fill((0, 0, 150))
        self.__margin = self.__screen.get_rect()
        
        self.__enemy = []
        self.__enemy.append(pnj.Stripe())
        self.__enemy.append(pnj.Stripe())
        self.__enemy.append(pnj.Stripe())
        self.__enemy.append(pnj.Turtle())
        self.__player = pnj.Shark()
        self.__player.setPlayer()
        
        self.__player.pos(int((self.__margin[0] + self.__margin[2]) / 2), (self.__margin[1] + self.__margin[3]) - self.__player.getRect()[3])
        self.__enemy[0].pos(500, 100)
        
        self.__menu = menu.Menu(self.__margin)
        self.__menu.menu('playing')
        
        
    def __str__(self):
        return 'player: {}'.format(self.__player.name())
        
        
    def close(self):
        pygame.quit()
        sys.exit()
        
        
    def getCollision(self):
        count = 0
        collision = {'margin': {'up': False, 'down': False, 'left': False, 'right': False}}
        
        if self.__player.getRect()[0] <= self.__margin[0]:
            collision['margin']['left'] = True
        if self.__player.getRect()[0] + self.__player.getRect()[2] >= self.__margin[0] + self.__margin[2]:
            collision['margin']['right'] = True
        if self.__player.getRect()[1] <= self.__margin[1]:
            collision['margin']['up'] = True
        if self.__player.getRect()[1] + self.__player.getRect()[3] >= self.__margin[1] + self.__margin[3]:
            collision['margin']['down'] = True
            
        for enemy in self.__enemy:
            collision['enemy' + str(count)] = self.__getCollisionObject(self.__player, enemy)
            count += 1
            
        return collision
    
    
    def __getCollisionObject(self, object1, object2):
        axisX = False
        axisY = False
        rect1 = object1.getRect()
        rect2 = object2.getRect()
        obj1 = {'up': rect1[1], 'down': rect1[1] + rect1[3], 'left': rect1[0], 'right': rect1[0] + rect1[2]}
        obj2 = {'up': rect2[1], 'down': rect2[1] + rect2[3], 'left': rect2[0], 'right': rect2[0] + rect2[2]}
        collision = {'up': False, 'down': False, 'left': False, 'right': False}
        
        axisX = self.__collisionPart('left', obj1, obj2)
        axisY = self.__collisionPart('up', obj1, obj2)
        
        if obj1['up'] < obj2['down'] and obj1['up'] > obj2['up'] and axisY:
            collision['up'] = True
        if obj1['down'] > obj2['up'] and obj1['down'] < obj2['down'] and axisY:
            collision['down'] = True
        if obj1['left'] < obj2['right'] and obj1['left'] > obj2['left'] and axisX:
            collision['left'] = True
        if obj1['right'] > obj2['left'] and obj1['right'] < obj2['right'] and axisX:
            collision['right'] = True
        
        return collision
    
    
    def __collisionPart(self, part, object1, object2):
        parm1 = ''
        parm2 = ''
        if part == 'up' or part == 'down':
            parm1 = 'left'
            parm2 = 'right'
        elif part == 'left' or part == 'right':
            parm1 = 'up'
            parm2 = 'down'
        else:
            return None

        if (object1[parm1] > object2[parm1] and object1[parm1] < object2[parm2])\
           or (object1[parm2] < object2[parm2] and object1[parm2] > object2[parm1])\
           or (object1[parm1] < object2[parm1] and object1[parm2] > object2[parm2])\
           or (object1[parm1] > object2[parm1] and object1[parm2] < object2[parm2]):
            return True
        else:
            return False
        
        
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
                            
            if collision['margin']['up'] and move['y'] < 0:#comprove if player collision with margin
                move['y'] = 0
            if collision['margin']['down'] and move['y'] > 0:
                move['y'] = 0
            if collision['margin']['left'] and move['x'] < 0:
                move['x'] = 0
            if collision['margin']['right'] and move['x'] > 0:
                move['x'] = 0
                
            if collision['enemy0']['left'] \
               or collision['enemy0']['right']\
               or collision['enemy0']['up']\
               or collision['enemy0']['down']:#comprove if player collision of enemy
                #print(collision)
                self.__menu.addScore(10)
                print(self.__menu.data)
                
            self.__player.move(move['x'], move['y'])#move the player
                    
            self.__screen.fill((0,0,200))#color of background
            
            for enemy in self.__enemy:
                enemy.move()
                self.__screen.blit(enemy.getImage(), enemy.pos())#enemy image
                
            self.__screen.blit(self.__player.getImage(), self.__player.pos())#player image
            
            self.__menu.draw(self.__screen)
                    
            pygame.display.flip()#refresh screen
            
            
if __name__ == '__main__':
    game = MainApp()
    game.start()