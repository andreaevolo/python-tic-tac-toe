gameStatus = True
switchPlayer = True

print("Welcome to the game Tic Tac Toe! \n The rules are simple:"
      " choose a number between 0 and 2 to select the row/column in wich you want to place your symbol. \n NOTICE: 0 is equal to the first row and column")

grid = [
    [" ", " " ," "],
    [" ", " " ," "],
    [" ", " ", " "]]

def printRow():
    for row in grid:
        print(row)
printRow()

def displayPlayerMove(row, col):
    playerOne = "X"
    playerTwo = "O"
    grid[row][col] =  playerOne if switchPlayer else playerTwo
    printRow()

def diagonalsSolutionPlayer1():

    if grid[0][0] == "O" and grid[1][1] == "O" and grid[2][2] == "O":
        print("Player One is the winner!")

    if grid[0][2] == "O" and grid[1][1] == "O" and grid[2][0] == "O":
        print("Player One is the winner!")

def diagonalsSolutionPlayer2():

    if grid[0][0] == "X" and grid[1][1] == "X" and grid[2][2] == "X":
        print("Player Two is the winner!")

    if grid[0][2] == "X" and grid[1][1] == "X" and grid[2][0] == "X":
        print("Player Two is the winner!")

def checkDiagonalSolutions():
    diagonalsSolutionPlayer1()
    diagonalsSolutionPlayer2()

def horizintalSolutionPlayer1():

    if grid[0][0] == "O" and grid[0][1] == "O" and grid[0][2] == "O":
        print("Player One is the winner")
    if grid[1][0] == "O" and grid[1][1] == "O" and grid[1][2] == "O":
        print("Player One is the winner")
    if grid[2][0] == "O" and grid[2][1] == "O" and grid[2][2] == "O":
        print("Player One is the winner")

def horizontalSolutionPlayer2():
    if grid[0][0] == "X" and grid[0][1] == "X" and grid[0][2] == "X":
        print("Player One is the winner")
    if grid[1][0] == "X" and grid[1][1] == "X" and grid[1][2] == "X":
        print("Player One is the winner")
    if grid[2][0] == "X" and grid[2][1] == "X" and grid[2][2] == "X":
        print("Player One is the winner")

def checkHorizontalSolutions():
    horizintalSolutionPlayer1()
    horizontalSolutionPlayer2()

def verticalSolutionsPlayer1():

    if grid[0][0] == "O" and grid[1][0] == "O" and grid[2][0] == "O":
        print("Player One is the winner!")
    if grid[0][1] == "O" and grid[1][1] == "O" and grid[2][1] == "O":
        print("Player One is the winner!")
    if grid[0][2] == "O" and grid[1][2] == "O" and grid[2][2] == "O":
        print("Player One is the winner!")

def verticalSolutionsPlayer2():

    if grid[0][0] == "X" and grid[1][0] == "X" and grid[2][0] == "X":
        print("Player One is the winner!")
    if grid[0][1] == "X" and grid[1][1] == "X" and grid[2][1] == "X":
        print("Player One is the winner!")
    if grid[0][2] == "X" and grid[1][2] == "X" and grid[2][2] == "X":
        print("Player One is the winner!")

def checkVerticalSolutions():
    verticalSolutionsPlayer1()
    verticalSolutionsPlayer2()


def checkAllSolutions():
    checkDiagonalSolutions()
    checkHorizontalSolutions()
    checkVerticalSolutions()

for totalMoves in range(0, 9):
    switchPlayer = not(switchPlayer)
    try:
        rowChoosed = int(input("Select a row on the X axis: "))
        colChoosed = int(input("Select column on the Y axis: "))
        displayPlayerMove(rowChoosed, colChoosed)
    except  ValueError:
        print("Error,Please enter a valid number between 0 and 2.")
    except IndexError:
        print("Ops! You select something that doesn't exist. Please enter a valid number between 0 and 2.")
    checkAllSolutions()

