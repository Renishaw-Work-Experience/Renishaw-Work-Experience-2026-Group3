import pygame
import logic
grid = []
turn = "R"

def drop_update():
    global grid
    global turn
    pygame.init()
    WIDTH = 1000
    HEIGHT = 1800

    surface = pygame.display.set_mode((WIDTH,HEIGHT))
    pos = (WIDTH//2,HEIGHT//2 - 75 * 3 - 25)
    result = 3
    running = True
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    clock = pygame.time.Clock()
    while running:
        surface.fill(WHITE)
        pygame.draw.circle(surface,RED,pos,37.5,0)
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                x_pos = x * 75
                y_pos = y * 75
                pygame.draw.circle(surface,RED,(x_pos,y_pos),37.5,0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_LEFT and 0 < result:
                    pos = (pos[0] - 75,pos[1])
                    result -= 1
                if event.key == pygame.K_RIGHT and result < 6:
                    pos = (pos[0] + 75,pos[1])
                    result += 1
                if event.key == pygame.K_z:
                    add_pos = logic.do_turn(result)
                    grid[add_pos[1]][add_pos[0]] = turn
                    if turn == "R":
                        turn = "Y"
                    elif turn == "Y":
                        turn = "R"
        
        clock.tick(120)
        pygame.display.flip()

grid = logic.start()
drop_update()
    
    