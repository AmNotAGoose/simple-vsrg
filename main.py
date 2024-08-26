import pygame
import sys

# USER PREFERENCE
UPSCROLL = False # no plans to implement upscroll
JUDGEMENT_LINE = 900
NOTE_HEIGHT = 60

# LANES
LANE_1 = 100
LANE_2 = 200
LANE_3 = 300
LANE_4 = 400

pygame.init()

screen = pygame.display.set_mode((1000, 1000))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    judgement_line = pygame.draw.line(screen, (255, 0, 0), (0, JUDGEMENT_LINE), (1000, JUDGEMENT_LINE), 5)
    lane_1 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(LANE_1, JUDGEMENT_LINE - NOTE_HEIGHT / 2, 60, NOTE_HEIGHT),
                              2)
    lane_2 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(LANE_2, JUDGEMENT_LINE - NOTE_HEIGHT / 2, 60, NOTE_HEIGHT),
                              2)
    lane_3 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(LANE_3, JUDGEMENT_LINE - NOTE_HEIGHT / 2, 60, NOTE_HEIGHT),
                              2)
    lane_4 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(LANE_4, JUDGEMENT_LINE - NOTE_HEIGHT / 2, 60, NOTE_HEIGHT),
                              2)


    pygame.display.flip()

pygame.quit()
sys.exit()
