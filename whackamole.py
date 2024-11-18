import pygame
import random

def main():
    
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        molX = 0
        molY = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clickX, clickY = event.pos
                    if clickX//32 == molX and clickY//32 == molY:
                        molX = random.randrange(0, 20)
                        molY = random.randrange(0, 16)
            screen.fill("light green")
            screen.blit(mole_image, mole_image.get_rect(topleft=(molX * 32, molY * 32)))
            for i in range(20):
                pygame.draw.line(screen, (255,255,255), (32*i,0), (32*i,512))
            for i in range(16):
                pygame.draw.line(screen, (255,255,255), (0,32*i), (640,32*i))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
