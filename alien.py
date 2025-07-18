import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_sitting,screen):
        super(Alien,self).__init__()
        self.screen=screen
        self.ai_setting=ai_sitting
        #加载外星人图形并设置rect
        self.image=pygame.image.load('images/alien.png')
        self.rect=self.image.get_rect()
        #每个外星人最初都在左上角
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height
        #准确位置
        self.x=float(self.rect.x)
    def blitme(self):
        self.screen.blit(self.image,self.rect)
        
    def update(self):
        self.x += (self.ai_setting.alien_speed_factor * self.ai_setting.fleet_direction)
        self.rect.x=self.x





    def check_edges(self): 
        """如果外星人位于屏幕边缘，就返回True""" 
        screen_rect = self.screen.get_rect() 
        if self.rect.right >= screen_rect.right: 
            return True 
        elif self.rect.left <= 0: 
            return True 