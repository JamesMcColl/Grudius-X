""" Author: James McColl
    
    Creating the ship sprite and ensuring proper movement.
    
"""
    
import pygame
pygame.init()

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ship.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.center = (65, mousey)
        
def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Gradius-esque Ship test code")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 255))
    screen.blit(background, (0, 0))
    ship = Ship()
    
    allSprites = pygame.sprite.Group(ship)
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
            
