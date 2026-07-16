import logic

def print_grid(x_rows, y_colums, grid):
    print(" 0123456")
    for y in range(y_colums):
        print("|" + "".join(grid[y]) + "|")
    print("+-------+")

def get_drop_point(grid):
    valid = False
    while not valid:
        try:
            drop_point = int(input("Drop: "))
            while drop_point <0 or drop_point > 6:
                print("Number is out of range. Please enter a number between 0 and 6.")
                drop_point = int(input("Drop: "))
        except ValueError:
            print("Please enter a number between 0 and 6.")
            continue
        if grid[0][drop_point] == " ":
            valid = True
    return drop_point

grid = logic.start()
while True:
    print_grid(logic.x_rows, logic.y_colums, grid)
    drop_point = get_drop_point(grid)
    add_pos = logic.do_turn(drop_point)
    if add_pos == None:
        print("Column is full. Please choose another column.")
    if add_pos[0] == "WIN":
        break