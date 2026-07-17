import logic

def test_start_test(): 
    logic.start()
    assert logic.x_rows == 7
    assert logic.y_colums == 6
    assert logic.turn == "R"
    assert logic.win == False
    assert logic.grid == [[" ", " ", " ", " ", " ", " ", " "],
                          [" ", " ", " ", " ", " ", " ", " "],
                          [" ", " ", " ", " ", " ", " ", " "],
                          [" ", " ", " ", " ", " ", " ", " "],
                          [" ", " ", " ", " ", " ", " ", " "],
                          [" ", " ", " ", " ", " ", " ", " "]]
    
def test_turn_test(): 
    logic.do_turn(0)
    assert logic.win == False
    assert logic.turn == "Y"

def test_drop_full_column_test(): 
    logic.start()
    logic.drop(0, "R")
    assert logic.grid[5][0] == "R"
    logic.drop(0, "Y")
    assert logic.grid[4][0] == "Y"
    logic.drop(0, "R")  
    assert logic.grid[3][0] == "R"
    logic.drop(0, "Y")
    assert logic.grid[2][0] == "Y"
    logic.drop(0, "R")
    assert logic.grid[1][0] == "R"
    logic.drop(0, "Y")
    assert logic.grid[0][0] == "Y"  
    logic.drop(0, "R")
    assert logic.drop(0, "R") == None

def test_drop_invalid_column_test(): 
    logic.start()
    assert logic.drop(-1, "R") == None
    assert logic.drop(7, "Y") == None

def test_four_horizontal_test(): 
    logic.start()
    logic.drop(0, "R")
    logic.drop(1, "R")
    logic.drop(2, "R")
    logic.drop(3, "R")
    assert logic.detect_wins() == True

def test_four_vertical_test(): 
    logic.start()
    logic.drop(0, "R")
    logic.drop(0, "R")
    logic.drop(0, "R")
    logic.drop(0, "R")
    assert logic.detect_wins() == True

def test_four_diagonal_test(): 
    logic.start()
    logic.drop(0, "R")
    logic.drop(1, "Y")
    logic.drop(1, "R")
    logic.drop(2, "Y")
    logic.drop(2, "Y")
    logic.drop(2, "R")
    logic.drop(3, "Y")
    logic.drop(3, "Y")
    logic.drop(3, "Y")
    logic.drop(3, "R")
    assert logic.detect_wins() == True

def test_full_grid_test(): 
    logic.start()
    for i in range(3):
        logic.drop(0, "R")
        logic.drop(1, "Y")
        logic.drop(2, "R")
        logic.drop(3, "Y")
        logic.drop(4, "R")
        logic.drop(5, "Y")
    for i in range(3):
        logic.drop(0, "Y")
        logic.drop(1, "R")
        logic.drop(2, "Y")
        logic.drop(3, "R")
        logic.drop(4, "Y")
        logic.drop(5, "R")
    assert logic.detect_wins() == False

def test_false_win_test():
    logic.start()
    logic.drop(0, "R")
    logic.drop(1, "R")
    logic.drop(5, "R")
    logic.drop(6, "R")
    assert logic.win == False

def test_after_win_move_test():
    logic.start()
    logic.win = True
    logic.drop(0, "R")
    assert logic.valid == False