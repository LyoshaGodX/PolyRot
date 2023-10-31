import pygame
import numpy as np


def scale_object(original_points, scaling_factor):
    scaling_matrix = np.array([[scaling_factor, 0], [0, scaling_factor]])
    scaled_points = [np.dot(scaling_matrix, np.array([point[0], point[1]])) for point in original_points]
    return scaled_points


def rotate_object(original_points, angle_degrees):
    angle_radians = np.radians(angle_degrees)
    rotation_matrix = np.array([[np.cos(angle_radians), -np.sin(angle_radians)],
                                [np.sin(angle_radians), np.cos(angle_radians)]])
    rotated_points = [np.dot(rotation_matrix, np.array([point[0], point[1]])) for point in original_points]
    return rotated_points


def visualize_objects(screen, *args):
    screen.fill((255, 255, 255))

    for obj in args:
        object_points, object_color = obj

        pygame.draw.lines(screen, object_color, True, object_points, 2)

    pygame.display.flip()

def shift_polygon(polygon, canvas_size):
    max_x = max(point[0] for point in polygon)
    min_x = min(point[0] for point in polygon)
    max_y = max(point[1] for point in polygon)
    min_y = min(point[1] for point in polygon)

    offset_x = canvas_size[0] / 2 - (max_x + min_x) / 2
    offset_y = canvas_size[1] / 2 - (max_y + min_y) / 2

    shifted_polygon = [[point[0] + offset_x, point[1] + offset_y] for point in polygon]

    return shifted_polygon


if __name__ == '__main__':
    pygame.init()

    canvas_size = (500, 500)
    screen = pygame.display.set_mode(canvas_size)
    pygame.display.set_caption('Квадратовращение')

    # Создание изначального квадрата
    initial_square = ([[200, 200], [-200, 200], [-200, -200], [200, -200]], (0, 0, 0))
    objects_to_visualize = [(shift_polygon(initial_square[0], canvas_size), (0, 0, 0))]

    for _ in range(20):
        current_square = objects_to_visualize[-1][0]  # Берем последний добавленный квадрат
        scaled_square = scale_object(current_square, 0.9)
        rotated_square = rotate_object(scaled_square, 5.625)

        shifted_square = shift_polygon(rotated_square, canvas_size)

        objects_to_visualize.append((shifted_square, (0, 0, 0)))  # Добавляем новый квадрат в objects_to_visualize

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        visualize_objects(screen, *objects_to_visualize)

    pygame.quit()


