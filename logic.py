def start():
    global grid
    global x_rows
    global y_colums
    global turn
    global win
    x_rows = 7
    y_colums = 6
    win = False
    turn = "R"
    grid = []

    for y in range(y_colums):
        grid.append([])
        for x in range(x_rows):
            grid[y].append(" ")

    return grid



def drop(x_pos,turn):
    y_drop = 0
    valid = False
    if grid[y_drop][x_pos] != " ":
        return None
    while y_drop != 5 and not valid:
        if grid[y_drop + 1][x_pos] == " ":
            y_drop += 1
        else:
            valid = True
            grid[y_drop][x_pos] = turn
    if not valid:
        grid[y_drop][x_pos] = turn
    return [x_pos,y_drop]

def detect_wins():
    global win
    for y in range(len(grid)):
        same = 0
        type = " "
        for x in range(len(grid[y])):
            if grid[y][x] == type and grid[y][x] != " ":
                same += 1
                if same == 3:
                    print("WIN PLAYER",type)
                    return True
            else:
                same = 0
                type = grid[y][x]

    for x in range(len(grid[0])):
        same = 0
        type = " "
        for y in range(len(grid)):
            if grid[y][x] == type and grid[y][x] != " ":
                same += 1
                if same == 3:
                    return True
            else:
                same = 0
                type = grid[y][x]

    for i in [[0,2],[0,1],[0,0],[1,0],[2,0],[3,0]]:
        same = 0
        type = " "
        pos = i
        while pos[0] < x_rows and pos[1] < y_colums:
            x = pos[0]
            y = pos[1]
            if grid[y][x] == type and grid[y][x] != " ":
                same += 1
                if same == 3:
                    return True
            else:
                same = 0
                type = grid[y][x]
            pos[0] += 1
            pos[1] += 1

    for i in [[6,0],[6,1],[6,2],[5,0],[4,0],[3,0]]:
        same = 0
        type = " "
        pos = i
        while 0 <= pos[0] < x_rows and 0 <= pos[1] < y_colums:
            x = pos[0]
            y = pos[1]
            if grid[y][x] == type and grid[y][x] != " ":
                same += 1
                if same == 3:
                    return True
            else:
                same = 0
                type = grid[y][x]
            pos[0] -= 1
            pos[1] += 1
    return False
        
def do_turn(drop_point):
    global turn
    global win
    if drop_point == None:
        pass
    else:
        drop_point = drop(drop_point,turn)
        win = detect_wins()
        if drop_point == None:
            return None
        if win:
            return "WIN", drop_point
        if turn == "R":
            turn = "Y"
        elif turn == "Y":
            turn = "R"
        return drop_point 

