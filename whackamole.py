import pygame
import random

def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        line_color=(0,0,0)
        running = True
        x, y = 0, 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[0] >=x and event.pos[0]<=x+32 and event.pos[1] >= y and event.pos[1] <=y+32 :
                        x=random.randrange(0,640,32)
                        y=random.randrange(0,512,32)
            screen.fill("light green")
            clock.tick(60)
            for i in range(32, 640, 32):
                pygame.draw.line(screen, line_color, (i, 0), (i, 512), 1)
            for i in range(32, 512, 32):
                pygame.draw.line(screen, line_color, (0, i), (640, i), 1)
            screen.blit(mole_image, (x,y))
            pygame.display.update()
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
