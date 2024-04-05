#TIC-TAC_TOE
#Plays tic-tac-toe against a cpu, where you are X and O is the CPU
#Keeps track of points and asks to play again once a round has been finished
#Checks for errors in case user has submitted an incorrect input

import  random
oWins = 0
xWins = 0

def printboard(board):
    count = 0
    global oWins
    global xWins

    print("You: " + str(xWins) +" Wins")
    print("Comp: " + str(oWins) +" Wins")
    for i in range(3):
        for j in range(5):
            if j%2 ==0:
                print(board[count],end =" ")
                count=count + 1 #count+=1
            else:
                print("|",end =" ")

        print("")
        


def askandupdateX(board):
    try:
        inputXO= input("What position do you want your X to be?(0-9)")
        int(inputXO)
        if ord(inputXO)>=49 and ord(inputXO)<=57 and board[int(inputXO)-1] != 'O' and board[int(inputXO)-1] != 'X':
            board[int(inputXO)-1] = 'X'
        else:
            print("The Spot is taken!")
            printboard(board)
            askandupdateX(board)
    except TypeError:
        print("You didn't enter a number between 0 and 9! Try again")
        printboard(board)
        askandupdateX(board)
    except ValueError:
        print("You entered a letter/phrase! Try again")
        printboard(board)
        askandupdateX(board)



def updatecomputerboardO(board):#MAKE O choice smart when there are two in a row
    oSpots =[]
    spotCount = 0
    chosenSpot = 0


    for i in range(9):
        if board[i] == ' ':
            oSpots.append(i)
            spotCount+=1

    if spotCount == 0:
        return
    chosenSpot = random.randint(0,len(oSpots)-1)
    board[oSpots[chosenSpot]] = "O"
            



def endcheck(board):
    global oWins
    global xWins
    xPos=[0,0,0,0,0,0,0,0,0]
    oPos=[0,0,0,0,0,0,0,0,0]
    xCount=0
    oCount=0

    for i in range(9):
        if board[i]=='X':
            xPos[xCount]= i+1
            xCount+=1
        if board[i]=='O':
            oPos[oCount]= i+1
            oCount+=1
    
    if xCount<=2:
        return False
    else:#8 ways to win, check 3 horizontal, 3 vertical, 2 diagonal WIN Checker
        for i in range(3):
            if board[3*i] == board[3*i +1] == board[3*i +2] and board[3*i] != ' ':#ROWS
                if board[3*i] == 'X':
                    xWins+=1
                    printboard(board)
                    print("X Wins!")
                    return True
                elif board[3*i] == 'O':
                    oWins+=1
                    printboard(board)
                    print("O Wins!")
                    return True
            if board[i] == board[i+3] == board[i+6] and board[i] != ' ':#COLS
                if board[i] == 'X':
                    xWins+=1                    
                    printboard(board)
                    print("X Wins!")
                    return True
                elif board[i] == 'O':
                    oWins+=1
                    printboard(board)
                    print("O Wins!")
                    return True
            if board[i] == board[4] == board[8-i] and board[4] != ' ':#CROSS
                if board[i] == 'X':
                    xWins+=1
                    printboard(board)
                    print("X Wins!")
                    return True
                elif board[i] == 'O':
                    oWins+=1
                    printboard(board)
                    print("O Wins!")
                    return True

    #TIE Checker
    blankCount = 0
    for i in board:
        if i == ' ':
            blankCount+=1
    if blankCount == 0:
        printboard(board)
        print("Its a Tie!")
        return True
    else:
        return False





def main():
    
    gameEnd = False
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

    while not gameEnd:
        printboard(board)
        askandupdateX(board)
        gameEnd = endcheck(board)
        if not gameEnd:
            updatecomputerboardO(board)#Glitch where it shows O placed even after you've won
            gameEnd = endcheck(board)

    playAgain = input("Do you want to play again? y/n ")

    if playAgain == 'y' or playAgain == 'Y':
        main()


main()