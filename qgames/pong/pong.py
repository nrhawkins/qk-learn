
import pygame
# from random import choice

from pygame.time import Clock

fps = 80

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 255, 0)

x_ball = 500
y_ball = 300

horizontal_dir = "left"
vertical_dir = "down"

score = 0
step = 2

clock: Clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Pong")

pygame.init()


def draw_ball():
    pygame.draw.circle(screen, red, (x_ball, y_ball), 10, 10)


def draw_paddle(x_pos, y_pos):
    pygame.draw.rect(screen, black, (x_pos, y_pos, 80, 10))


def move_ball():
    global x_ball, y_ball, horizontal_dir, vertical_dir

    if horizontal_dir == "left":
        x_ball -= step
        if x_ball < 10:
            horizontal_dir = "right"

    if horizontal_dir == "right":
        x_ball += step
        if x_ball > 400:
            horizontal_dir = "left"

    if vertical_dir == "up":
        y_ball -= step
        if y_ball < 10:
            vertical_dir = "down"

    if vertical_dir == "down":
        y_ball += step


def served():
    global x_ball, y_ball
    global x, y
    global horizontal_dir, vertical_dir, step
    global score

    if horizontal_dir == "left":

        if y_ball > 400:

            # ball is touching the paddle
            if x <= x_ball < x + 50:
                print("Good Job")
                score += 1
                vertical_dir = "up"
                step = 1

            # if ball missed, reset ball coordinates and decrement score
            else:
                pygame.draw.circle(screen, black, (x_ball, y_ball), 10, 10)
                pygame.display.update()
                x_ball, y_ball = 500, 300
                score -= 1

        pygame.display.set_caption(f"Your score is: {score}")


loop = True
while loop:

    # detect pressed keys
    keys = pygame.key.get_pressed()

    # if quit button press event quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = 0

    # get mouse pointer coordinates
    x, y = pygame.mouse.get_pos()

    # move the ball by a step
    move_ball()
    draw_ball()
    draw_paddle(x, 490)
    served()
    pygame.display.update()
    screen.fill(white)
    clock.tick(fps)

pygame.quit()
