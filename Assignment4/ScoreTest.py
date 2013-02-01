""" Author: James McColl

    Add the scoring and lives system
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
    
class Space(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("space.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.dx = 5
        self.reset()
        
    def update(self):
        self.rect.right -= self.dx
        if self.rect.right < 640:
            self.reset() 
    
    def reset(self):
        self.rect.centerx = 640
        

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 5
        self.score = 0
        self.font = pygame.font.SysFont("Arial", 30)
        
    def update(self):
        self.text = "lives: %d, score: %d" % (self.lives, self.score)
        self.image = self.font.render(self.text, 1, (0, 150, 255))
        self.rect = self.image.get_rect()
    
def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Gradius-esque - Adding the score and lives")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    ship = Ship()
    powerup = Powerup()
    enemy1 = Enemy()
    enemy2 = Enemy()
    enemy3 = Enemy()
    enemy4 = Enemy()
    enemy5 = Enemy()
    space = Space()
    scoreboard = Scoreboard()

    friendSprites = pygame.sprite.OrderedUpdates(space, powerup, ship)
    enemySprites = pygame.sprite.Group(enemy1, enemy2, enemy3, enemy4, enemy5)
    scoreSprite = pygame.sprite.Group(scoreboard)

    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        #check collisions
        #TODO: change to sprite.collideany
        
        #check collisions
        
        if ship.rect.colliderect(powerup.rect):
            ship.sndPowerup.play()
            powerup.reset()
            scoreboard.score += 100

        hitEnemy = pygame.sprite.spritecollide(ship, enemySprites, False)
        if hitEnemy:
            ship.sndDeath.play()
            scoreboard.lives -= 1
            if scoreboard.lives <= 0:
                print("Game over!")
                ship.sndMusic.stop()
                ship.sndGameOver.play()
                scoreboard.lives = 5
                scoreboard.score = 0
            for theEnemy in hitEnemy:
                theEnemy.reset()
        
        #friendSprites.clear(screen, background)
        #cloudSprites.clear(screen, background)
        #scoreSprite.clear(screen, background)
        
        friendSprites.update()
        enemySprites.update()
        scoreSprite.update()
        
        friendSprites.draw(screen)
        enemySprites.draw(screen)
        scoreSprite.draw(screen)
        
        pygame.display.flip()
    
    #return mouse cursor
    pygame.mouse.set_visible(True)
    ship.sndMusic.stop() 

    
if __name__ == "__main__":
    main()
            
