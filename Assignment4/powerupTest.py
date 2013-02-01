""" Author: James McColl
   
   Create power-ups and add scrolling
"""
    
import pygame, random
pygame.init()

screen = pygame.display.set_mode((640, 480))

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ship.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.center = (65, mousey)
        
        
class Powerup(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("powerup.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dx = 5
    
    def update(self):
        self.rect.right -= self.dx
        if self.rect.left < -20:
            self.reset()
            
    def reset(self):
        self.rect.right = 660
        self.rect.centery = random.randrange(0, screen.get_height())
    
    
def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Gradius-esque - Adding the powerups!")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 255))
    screen.blit(background, (0, 0))
    ship = Ship()
    powerup = Powerup()
    
    allSprites = pygame.sprite.Group(powerup, ship)
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        pygame.display.flip()
    
    #return mouse cursor
    pygame.mouse.set_visible(True) 
if __name__ == "__main__":
    main()
            
