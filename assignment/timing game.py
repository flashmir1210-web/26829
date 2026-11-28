import sys
import pygame

WIDTH, HEIGHT = 640, 480
FPS = 60

def print_menu(screen, font):
    # 게임 이름 출력
    # 메뉴 "TYPING GAME", "CALCULATOR GAME", "EXIT"
    # 초기 선택된 값 표시 -> 현재는 TYPING GAME
    text_surf = font.render("Game Start", True, (255, 255, 255))
    screen.blit(text_surf, (100, 100))
    text_surf = font.render("ssssssss", True, (255, 255, 255))
    screen.blit(text_surf, (100, 200))


def main():
    font = pygame.font.SysFont(None, 50)
    pygame.display.set_caption("Blank Window")
    clock = pygame.time.Clock()

    running = True
    mode = "wait"

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # press mode : press 시작 후 누른 시점까지의 시간을 경과
                    # wait mode : 잘못조작됨.
                    # 다시시작(R)
                    # 종료(E)

        screen.fill((30, 32, 40))

        if random.randint(0, 100) == 0:
            mode = "press"

        if mode == "press":
            screen.blit(font.render("PRESS BUTTON!", True, (255, 255, 255)), (200, 200))
        else:
            screen.blit(font.render("WAIT!", True, (255, 255, 255)), (200, 200))

        pygame.display.flip()