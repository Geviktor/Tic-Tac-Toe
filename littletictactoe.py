#Imports
from os import system
from random import randint


#Take one list and print it 3 row and 3 colm
def printBoard(board):
   for i in range(len(board)):
        print("    " + board[i][0] +"  "+ board[i][1] +"  "+ board[i][2])
        print("")


# If x's and o's are crosswise or straight, return False else return True.
def gameOver(board,draw):
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != "~":
            return False
        elif board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] != "~":
            return False
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != "~":
        return False
    elif board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] != "~":
        return False
    elif draw(board):
        return False
    else:
        return True


#If the ~'s over return True, else return False
def drawChecker(board):
    draw = 0
    for i in range(3):
        if board[i][0] != "~" and board[i][1] != "~" and board[i][2] != "~":
            draw += 1
    if draw == 3:
        return True
    else:
        return False

#check board straight for computer play
def checkStraight(board,symbol,control,c1):
    for i in range(3):
        if board[i][0] == c1 and board[i][1] == c1 and board[i][2] == "~":
            board[i][2] = symbol
            control +=1
            return board, control
        elif board[i][2] == c1 and board[i][1] == c1 and board[i][0] == "~":
            board[i][0] = symbol
            control +=1
            return board, control
        elif board[i][0] == c1 and board[i][2] == c1 and board[i][1] == "~":
            board[i][1] = symbol
            control +=1
            return board, control
        elif board[0][i] == c1 and board[1][i] == c1 and board[2][i] == "~":
            board[2][i] = symbol
            control +=1
            return board, control
        elif board[2][i] == c1 and board[1][i] == c1 and board[0][i] == "~":
            board[0][i] = symbol          
            control +=1
            return board, control
        elif board[2][i] == c1 and board[0][i] == c1 and board[1][i] == "~":
            board[1][i] = symbol
            control +=1
            return board, control
    return False, False


#check board cross for computer play
def checkCross(board,symbol,control,c1):
    if board[0][0] == c1 and board[1][1] == c1 and board[2][2] == "~":
        board[2][2] = symbol
        control +=1
        return board, control
    elif board[2][2] == c1 and board[1][1] == c1 and board[0][0] == "~":
        board[0][0] = symbol
        control +=1
        return board, control
    elif board[0][0] == c1 and board[2][2] == c1 and board[1][1] == "~":
        board[1][1] = symbol
        control +=1
        return board, control
    elif board[0][2] == c1 and board[1][1] == c1 and board[2][0] == "~":
        board[2][0] = symbol
        control +=1
        return board, control
    elif board[2][0] == c1 and board[1][1] == c1 and board[0][2] == "~":
        board[0][2] = symbol
        control +=1
        return board, control
    elif board[0][2] == c1 and board[2][0] == c1 and board[1][1] == "~":
        board[1][1] = symbol
        control +=1
        return board, control
    else:
        return False, False
 

#Main function for player. control rows, colms, fix game and play it.
def playerPlay(board,row,colm,symbol,control):
    if row > 2 or  colm > 2 or row < 0 or colm < 0:
        input("Row or column cannot be larger than 3 and less than 1! Press Enter.")
    elif board[row][colm] == "X" or board[row][colm] == "O":
        input("This field is full! Press Enter. ")
    else:
        board[row][colm] = symbol
        control += 1
    return board, control


#Main function for computer
def compPlay(board,symbol,control):
    tour = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "~":
                tour += 1

    if tour == 8:
        row = randint(0,2)
        colm = randint(0,2)
        if board[row][colm] != "~":
            if row != 2:
                row += 1
            else:
                row -= 1
        board[row][colm] = symbol
        control += 1
        return board, control
    else:
        board1, control1 = checkStraight(board,symbol,control,"O")
        if control1:
            return board1, control1
        board2, control2 = checkCross(board,symbol,control,"O")
        if control2:
            return board2, control2
        board3, control3 = checkStraight(board,symbol,control,"X")
        if control3:
            return board3, control3
        board4, control4 = checkCross(board,symbol,control,"X")
        if control4:
            return board4, control4
        else:
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "~":
                        board[i][j] = symbol
                        control += 1
                        return board, control


#For two people
def multiPlayer(): 
    board = []
    for i in range(3):
        board.append(["~"]*3)

    system("clear")
    printBoard(board)
    control = 0
    
    while gameOver(board,drawChecker):
        if control % 2 == 0:
            symbol = "X"
        else:
            symbol = "O"

        try:
            row = int(input("Row: ")) - 1
            colm = int(input("Colm: ")) - 1
            board, control = playerPlay(board,row,colm,symbol,control)
        
        except ValueError:
            input("Row or column connot be string! Press Enter.")
    
        system("clear")

        printBoard(board)
    
    if drawChecker(board):
        input("GAME OVER! DRAW! Press Enter.")
    else:
        input(f"GAME OVER! WINNER IS {symbol}! Press Enter.")



#For play with computer
def singlePlayer():
    board = []
    for i in range(3):
        board.append(["~"]*3)

    system("clear")
    printBoard(board)
    control = 0

    while gameOver(board,drawChecker):
        if control % 2 == 0:
            symbol = "X"
            try:
                row = int(input("Row: ")) - 1
                colm = int(input("Colm: ")) - 1
                board, control = playerPlay(board,row,colm,symbol,control)

            except ValueError:
                input("Row or column connot be string! Press Enter.")
  
        else:
            symbol = "O"
            board, control = compPlay(board,symbol,control)


        system("clear")

        printBoard(board)

    if drawChecker(board):
        input("GAME OVER! DRAW! Press Enter.")
    else:
        input(f"GAME OVER! WINNER IS {symbol}! Press Enter.")


#The main function
def main():
    while True:
        system("clear")
        print("""
                        Welcome to Tic-Tac-Toe Game!

                        [1] Play With A Friend
                        [2] Play With Computer
                        [Q] Quit

        """)
        choice = input("Enter choice: ")
        choice = choice.lower()
        
        if choice == "1":
            multiPlayer()
        elif choice == "2":
            singlePlayer()
        elif choice == "q":
            print("See you later! :)")
            break
        else:
            input("Invalid value! Just you can type: 1, 2, Q. Press Enter.")


if __name__ == "__main__":
    main()
