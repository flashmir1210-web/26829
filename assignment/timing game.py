
import sys
import random
import pygame

WIDTH, HEIGHT = 640, 480
FPS = 60

def main():
    pygame.init()

    font = pygame.font.SysFont(None, 50)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Blank Window")
    clock = pygame.time.Clock()

    running = True
    mode = "wait"
    result = ""

    press_time = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if mode == "press":
                        reaction_time = pygame.time.get_ticks() - press_time
                        result = "Reaction: " + str(reaction_time) + " ms"
                        mode = "result"
                    elif mode == "wait":
                        result = "Game Over!"
                        mode = "result"

                elif event.key == pygame.K_r:
                    mode = "wait"
                    result = ""

                elif event.key == pygame.K_e:
                    mode = "exit"
                    running = False

        screen.fill((30, 32, 40))

        if mode == "wait" and random.randint(0, 100) == 0:
            mode = "press"
            press_time = pygame.time.get_ticks()

        if mode == "press":
            screen.blit(
                font.render("PRESS BUTTON!", True, (255, 255, 255)),
                (200, 200)
            )

        elif mode == "wait":
            screen.blit(
                font.render("WAIT!", True, (255, 255, 255)),
                (260, 200)
            )

        elif mode == "exit":
            screen.blit(
                font.render("BYE BYE!", True, (255, 255, 255)),
                (260, 200)
            )

        else:
            screen.blit(
                font.render(result, True, (255, 255, 255)),
                (150, 200)
            )
            screen.blit(
                font.render("PRESS R TO RESTART", True, (255, 255, 255)),
                (120, 280)
            )
            screen.blit(
                font.render("PRESS E TO ESCAPE", True, (255, 255, 255)),
                (120, 330)
            )

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
