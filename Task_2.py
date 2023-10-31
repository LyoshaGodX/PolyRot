import numpy as np
import pygame
import math


def calculate_pascal_spiral(a, b, theta_increment, num_iterations):
    points = []
    theta = 0.0
    for i in range(1, num_iterations + 1):
        r = b + 2 * a * math.cos(theta)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        points.append((x, y))
        theta += theta_increment

    return points


def visualize_pascal_spiral(screen, points):
    screen.fill((255, 255, 255))
    pygame.draw.lines(screen, (0, 0, 0), False, points, 3)
    pygame.display.update()


if __name__ == '__main__':
    pygame.init()

    canvas_size = (900, 900)
    screen = pygame.display.set_mode(canvas_size)
    pygame.display.set_caption('Улитка Паскаля')

    a = 10
    b = 10
    theta_increment = math.pi/32

    pascal_points = calculate_pascal_spiral(a, b, theta_increment, 65)
    points = np.array(pascal_points) * 20 + np.array([canvas_size[0]/2 - 250, canvas_size[0]/2])

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        visualize_pascal_spiral(screen, points)

    pygame.quit()
