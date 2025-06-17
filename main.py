import pygame
import math

pygame.init()
window = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True
bg_color = (40, 42, 54)
GridColor = (128, 128, 128)
pygame.display.set_caption("Grid")

def rotate_point(x, y, angle_deg, origin):
    angle_rad = math.radians(angle_deg)
    ox, oy = origin
    dx = x - ox
    dy = y - oy
    qx = ox + math.cos(angle_rad) * dx - math.sin(angle_rad) * dy
    qy = oy + math.sin(angle_rad) * dx + math.cos(angle_rad) * dy
    return qx, qy

def squash_y(y, squash_factor, origin_y):
    return origin_y + (y - origin_y) * squash_factor



def drawGrid():
    blockSize = 50 
    center = (300, 300)
    squash_factor = 0.5
    for x in range(0, 600, blockSize):
        for y in range(0, 600, blockSize):
            
            points = [
                (x, y),
                (x + blockSize, y),
                (x + blockSize, y + blockSize),
                (x, y + blockSize)
            ]
            rotated = [rotate_point(px, py, 45, center) for (px, py) in points]
            pygame.draw.polygon(window, GridColor, rotated, 1)

            squashed = [(px, squash_y(py, squash_factor, center[1])) for (px, py) in rotated]

            
            pygame.draw.polygon(window, GridColor, squashed, 1)

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False

    window.fill(bg_color)
    drawGrid()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

