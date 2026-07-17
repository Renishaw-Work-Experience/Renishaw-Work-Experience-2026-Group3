from email.mime import text
from tkinter import font

import random
import pygame
import logic
grid = []
turn = "R"

def draw_sprite(pos,image,size):
    global surface
    surface.blit(image,(pos[0] - size[0]//2,pos[1] - size[1]//2),(0,0,size[0],size[1]))

def drop_update():
    global surface
    global grid
    global rendered_grid
    global turn
    pygame.init()
    WIDTH = 1000
    HEIGHT = 1800
    font = pygame.font.Font("freesansbold.ttf", 128)
    add_pos = [-1,-1]
    surface = pygame.display.set_mode((WIDTH,HEIGHT))
    pos = (WIDTH//2,HEIGHT//2 - 75 * 3 - 25)
    fall_pos = (WIDTH//2,HEIGHT//2 - 75 * 3 - 25)
    fall_velocity = (0,0)
    falling = False
    result = 3
    running = True
    direction = [0,0]
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    BLACK = (0, 25, 0)
    clock = pygame.time.Clock()
    wait_till_win = -1
    move_time = 0
    bounces = 0
    particles = []
    particle_velocity = []
    red_counter = pygame.image.load("sprites/counter_red.png")
    red_counter = pygame.transform.scale(red_counter,(75,75))
    board_sprite = pygame.image.load("sprites/Board.png")
    new_size = (board_sprite.size[0]//2, board_sprite.size[1]//2)
    board_sprite = pygame.transform.scale(board_sprite,(1050//2,900//2))

    yellow_counter = pygame.image.load("sprites/counter_yellow.png")
    new_size = (yellow_counter.size[0]//2, yellow_counter.size[1]//2)
    yellow_counter = pygame.transform.scale(yellow_counter,new_size)
    background_sound = pygame.mixer.Sound("sound/Quiet_glade.mp3")
    background_sound.set_volume(1)
    background_sound.play(-1)
    while running:
        surface.fill(BLACK)
        if turn == "R":
            draw_sprite(pos,red_counter,(75,75))
        elif turn == "Y":
            draw_sprite(pos,yellow_counter,(75,75))
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                x_pos = (x-3) * 75 + WIDTH//2
                y_pos = (y-2) * 75 + HEIGHT//2 
                if add_pos == [x,y] and falling:
                    pygame.draw.circle(surface,BLACK,(x_pos,y_pos),37.5,0)
                elif grid[y][x] == "R" :
                    draw_sprite((x_pos,y_pos),red_counter,(75,75))  
                elif grid[y][x] == "Y":
                    draw_sprite((x_pos,y_pos),yellow_counter,(75,75))        
                else:
                    pygame.draw.circle(surface,BLACK,(x_pos,y_pos),37.5,0)
        
        if falling:
            x_pos = (add_pos[0]-3) * 75 + WIDTH//2
            y_pos = (add_pos[1]-2) * 75 + HEIGHT//2 
            if turn == "R":
                draw_sprite(fall_pos,yellow_counter,(75,75))
            elif turn == "Y":
                draw_sprite(fall_pos,red_counter,(75,75))
            fall_pos = (fall_pos[0] + fall_velocity[0],fall_pos[1] + fall_velocity[1])
            fall_velocity = (fall_velocity[0],fall_velocity[1] + 0.2)
            if fall_pos[1] > y_pos:
                bounces += 1
                for i in range(10 - bounces * 2):
                    particles.append((fall_pos[0],fall_pos[1]+37.5))
                    particle_velocity.append((random.uniform(-5,5),random.uniform(-5,-1)))
                fall_velocity = (fall_velocity[0],fall_velocity[1] * -0.4)
                fall_pos = (fall_pos[0],y_pos)
                print("FALL VELOCITY",fall_velocity[1])
                sound = pygame.mixer.Sound("sound/freesound_community-stone-dropping-6843.mp3")
                sound.set_volume(1-(0.3 * bounces))
                sound.play()
                if bounces == 3:
                    falling = False
        for i in range(len(particles)):
            particles[i] = (particles[i][0] + particle_velocity[i][0],particles[i][1] + particle_velocity[i][1])
            particle_velocity[i] = (particle_velocity[i][0],particle_velocity[i][1] + 0.2)
            pygame.draw.circle(surface,RED if turn == "Y" else YELLOW,particles[i],4,0)
        if direction != [0,0]:
            pos = (pos[0] + direction[0] * 15,pos[1] + direction[1] * 15)
            move_time -= 1
        if move_time == 0:
            direction = [0,0]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and direction == [0,0]:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if turn == "R":
                    left_press = event.key == pygame.K_a
                    right_press = event.key == pygame.K_d
                    key_pressed = event.key in [pygame.K_s, pygame.K_w]
                elif turn == "Y":
                    left_press = event.key == pygame.K_LEFT
                    right_press = event.key == pygame.K_RIGHT
                    key_pressed = event.key in [pygame.K_DOWN, pygame.K_UP] 
                if left_press and 0 < result:
                    direction = [-1,0]
                    result -= 1
                    move_time = 5
                if right_press and result < 6:
                    direction = [1,0]
                    result += 1
                    move_time = 5
                if key_pressed and not falling and wait_till_win < 0:
                    add_pos = logic.do_turn(result)
                    if add_pos == None:
                        add_pos = [-1,-1]
                    elif add_pos[0] == "WIN":
                        win_sound = pygame.mixer.Sound("sound/Winning.mp3")
                        win_sound.set_volume(0.5)
                        win_sound.play()
                        print(add_pos[1])
                        add_pos = add_pos[1]
                        print("WINNER IS",turn)
                        winner = "RED" if turn == "R" else "YELLOW"
                        text = font.render(winner + " WINS!", True, RED if turn == "R" else YELLOW)
                        shadow = font.render(winner + " WINS!", True, WHITE)
                        wait_till_win = 200    
                    if not (add_pos == [-1,-1]) or add_pos == None:
                        falling = True
                        grid[add_pos[1]][add_pos[0]] = turn
                        fall_pos = pos
                        bounces = 0
                        fall_velocity = (0,-5)
                        if turn == "R":
                            turn = "Y"
                        elif turn == "Y":
                            turn = "R"
                    if all(grid[0][x] != " " for x in range(7)):
                        draw = True
                        text = font.render("DRAW!", True, WHITE)
                        shadow = font.render("DRAW!", True, BLACK)
                        wait_till_win = 100
                if event.key == pygame.K_r:
                    grid = logic.start()
                    turn = "R"
                    
        surface.blit(board_sprite,(WIDTH//2 - board_sprite.size[0]//2 + 2,HEIGHT//2 - board_sprite.size[1]//2 + 40))   
        if wait_till_win >= 0:
            wait_till_win -= 1
            surface.blit(shadow, (WIDTH//2 - text.get_width()//2 - 5, HEIGHT//2 - text.get_height()//2 - 5))
            surface.blit(shadow, (WIDTH//2 - text.get_width()//2 + 5, HEIGHT//2 - text.get_height()//2 + 5))
            surface.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
        if wait_till_win == 0:
            grid = logic.start()
            turn = "R"
        
        pygame.display.flip()
        clock.tick(120)
    
    
if __name__ == "__main__":
    grid = logic.start()
    drop_update()
    
    