""" Author: James McColl

    Create enemies and enable movement of varying degrees
    Also add sound effects
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
        
        if not pygame.mixer:
            print("problem with sound")
        else:
            pygame.mixer.init()
            self.sndPowerup = pygame.mixer.Sound("powerup.ogg")
            self.sndDeath = pygame.mixer.Sound("death.ogg")
            self.sndMusic = pygame.mixer.Sound("background_music.ogg")
            self.sndGameOver = pygame.mixer.Sound("game_over.ogg")
            self.sndMusic.play(-1)
        
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
    
      
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("enemy.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()

    def update(self):
        self.rect.right -= self.dx
        self.rect.right -= self.dy
        if self.rect.left < -20:
            self.reset()
    
    def reset(self):
        self.rect.right = 660
        self.rect.centery = random.randrange(0, screen.get_height())
        self.dy = random.randrange(5, 10)
        self.dx = random.randrange(-2, 2)
    
class Ocean(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ocean.gif")
        self.rect = self.image.get_rect()
        self.dy = 5
        self.reset()
        
    def update(self):
        self.rect.bottom += self.dy
        if self.rect.bottom >= 1440:
            self.reset() 
    
    def reset(self):
        self.rect.top = -960
        
    
def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Gradius-esque - Creating the enemies")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    ship = Ship()
    powerup = Powerup()
    enemy1 = Enemy()
    enemy2 = Enemy()
    enemy3 = Enemy()
    ocean = Ocean()
    
    friendSprites = pygame.sprite.OrderedUpdates(ocean, powerup, ship)
    enemySprites = pygame.sprite.Group(enemy1, enemy2, enemy3)
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        #check collisions
        
        if ship.rect.colliderect(powerup.rect):
            ship.sndYay.play()
            powerup.reset()

        hitEnemy = pygame.sprite.spritecollide(ship, enemySprites, False)
        
        if hitEnemy:
            ship.sndThunder.play()
            for theEnemy in hitEnemy:
                theEnemy.reset()

        #friendSprites.clear(screen, background)
        #cloudSprites.clear(screen, background)
        friendSprites.update()
        enemySprites.update()
        friendSprites.draw(screen)
        enemySprites.draw(screen)
        
        pygame.display.flip()
    
    #return mouse cursor
    pygame.mouse.set_visible(True) 
if __name__ == "__main__":
    main()
            
