import pygame
import sys
import random
import math
import numpy as np

pygame.init()

black = [0, 0, 0]
white = [255, 255, 255]

size = (800, 800)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()


'''Coordenadas'''
# creamos 100 coordenadas aleatorias para las estrellas
n_robots = 110
D = 250
step = 0.01
#sep = math.pi*D/(n_robots-20)
sep = D/2*math.sqrt(2)*4/(n_robots-10)
robots_pos = np.random.randint(-200, 1000, (n_robots, 2))
robots_pos = robots_pos.astype('float64') 

def update_robots_position(n_robots, D, step, sep, robots_pos):
    
    for i in range(0, n_robots):
        
        r = robots_pos[i]
        
        v = robots_pos - r
        dist = [np.linalg.norm(i) for i in v]
        F = robots_pos[np.argmax(dist)]  
        dist[i] = 10
        N = robots_pos[np.argmin(dist)]
        
        midpoint = (N + F)/2        
        v_midpoint = midpoint - r
        
        if np.linalg.norm(v_midpoint, ord = 1) >= D/2:
            robots_pos[i] += step*v_midpoint
        else:
            robots_pos[i] -= step*v_midpoint
        
        v_nearestpoint = N - r
        
        if np.linalg.norm(v_nearestpoint, ord = 1) >= sep:
            robots_pos[i] += step*v_nearestpoint
        else:
            robots_pos[i] -= step*v_nearestpoint
            
    return robots_pos  

'''Mouse'''
frec=30 
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    screen.fill(black)

    
    for coord in robots_pos:
        pygame.draw.circle(screen, white, coord, 2)
    
    robots_pos = update_robots_position(n_robots, D, step, sep, robots_pos)  
    
    if frec<=1000:
        frec += 0.1
    else: frec = 1000
    pygame.display.flip()
    clock.tick(frec)
