import pygame
from datetime import datetime
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

DIGITAL_H = 100 # height of digital clock
W = 700 # screen width
H = W + DIGITAL_H # screen height
CLOCK_W = W # analog clock width
CLOCK_H = 700 # analog clock height
MARGIN_H = MARGIN_W = 5 # margin of analog clock from window border
CLOCK_R = (W - MARGIN_W) / 2 # clock radius
HOUR_R = CLOCK_R / 2 # hour hand length
MINUTE_R = CLOCK_R * 7 / 10 # minute hand length
SECOND_R = CLOCK_R * 8 / 10 # second hand length
TEXT_R = CLOCK_R * 9 / 10 # distance of hour markings from center
TICK_R = 2 # stroke width of minute markings
TICK_LENGTH = 5 # stroke length of minute markings
HOUR_STROKE = 5 # hour hand stroke width
MINUTE_STROKE = 2 # minute hand stroke width
SECOND_STROKE = 2 # second hand stroke width
CLOCK_STROKE = 2 # clock circle stroke width
CENTER_W = 10 # clock center mount width
CENTER_H = 10 # clock center mount height
HOURS_IN_CLOCK = 12
MINUTES_IN_HOUR = 60
SECONDS_IN_MINUTE = 60
SIZE = (W, H)

def circle_point(center, radius, theta):
    """Calculates the location of a point of a circle given the circle's
       center and radius as well as the point's angle from the xx' axis"""

    return (center[0] + radius * math.cos(theta),
            center[1] + radius * math.sin(theta))

def line_at_angle(screen, center, radius, theta, color, width):
    """Draws a line from a center towards an angle. The angle is given in
       radians."""
    point = circle_point(center, radius, theta)
    pygame.draw.line(screen, color, center, point, width)

def get_angle(unit, total):
    """Calculates the angle, in radians, corresponding to a portion of the clock
       counting using the given units up to a given total and starting from 12
       o'clock and moving clock-wise."""
    return 2 * math.pi * unit / total - math.pi / 2

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Clock')
digital_font = pygame.font.SysFont('Calibri', 32, False, False)

clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    now = datetime.now()


    # draw digital clock
    digital_text = now.strftime('%H:%M:%S')
    text = digital_font.render(digital_text, True, BLACK)
    screen.blit(
        text,
        [
            W / 2 - digital_font.size(digital_text)[0] / 2,
            H - DIGITAL_H / 2 - digital_font.size(digital_text)[1] / 2
        ]
    )
    pygame.display.flip()
    clock.tick(60)

pygame.quit()