from turtle import position
import random

board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

board1 = {1: '   ', 2: '   ', 3: '   ',
          4: '   ', 5: '   ', 6: '   ',
          7: '   ', 8: '   ', 9: '   '}

a = 0

# Print the board


def printBoard(board):
    print(" ")
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("---+---+---")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("---+---+---")
    print(board[7] + "|" + board[8] + "|" + board[9])
    print(" ")

# Check for free spaces


def isSpaceFree(position):
    global board
    if(board[position] == ' '):
        return True
    else:
        return False


def checkDraw():
    # Check for any empty spaces
    for key in board.keys():
        if board[key] == ' ':
            return False

    return True


def checkForWin():

    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

# This for the AI playing the Virtual game !


def checkWhichMarkWon(mark):

    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False

# Enter letter at the desired potion


def enterLetterAtPosition(letter, position):
    global board
    global board1

    if(isSpaceFree(position)):
        board[position] = letter
        for k in board.keys():
            board1[k] = " " + board[k] + " "
        printBoard(board1)
        if(checkDraw()):
            print("Draw !")
            exit()

        if(checkForWin()):
            if(letter == 'X'):
                print("Bot Wins !")
                exit()
            else:
                print("Player Wins !")
                exit()

    else:
        print("Cant insert there !")
        position = int(input("Enter a new position : "))
        enterLetterAtPosition(letter, position)
        return


player = 'O'
bot = 'X'


def playerMove():
    global player
    position = int(input("Enter the position for 'O' : "))
    enterLetterAtPosition(player, position)
    return


def compMove():
    global bot
    global board
    # we set bestmove = -1 to assume that bot will LOOSE
    bestScore = -800
    # we set the best move = 0 so that if there is no solution we aim for a DRAW
    bestMove = 0
    # looping through every possible empty spaces in the BOARD
    for key in board.keys():
        if (board[key] == ' '):
            # Player a bot move at the current postion in the loop
            board[key] = bot
            # Maximizing is BOT so this move is for the PLAYER
            score = minimax(board, 0, False)
            # reset the board because that move was a trial and not mean to be played !
            board[key] = ' '
            # Remember the bestScore is the desired score and its the winning score for the enemy (PLAYER) AND we want anything that is more than that.
            if (score > bestScore):
                # we set the highest number as the best score because we want to MAXIMIZE
                bestScore = score
                # we use the bestScore as our move in the REAL WORLD game
                bestMove = key
    # We play the calculated best move in the real world game
    enterLetterAtPosition(bot, bestMove)
    return


# When this function is called then we check the possiblity that can player can play and we choose the most suitable** move
# suitalbe** : that is in which of the moves we have the most chances of WINNING or atleast DRAW

# This function will be called by thr real game once !
# The this function will call itself recursively till we reach the best score desired
def minimax(board, depth, isMaximizing):

    global player
    global bot

    # check for the winning BOT in the virtual game
    if (checkWhichMarkWon(bot)):
        return 1
    # check for the winning PLAYER in the virtual game
    elif (checkWhichMarkWon(player)):
        return -1
    # check for the DRAW in the virtual game
    elif (checkDraw()):
        return 0

    # This is for the virtual game
    if (isMaximizing):
        # at the begining we assume that we are loosing so we set the best score to -1 = LOOSE
        bestScore = -800
        # we loop through every possible empty spaces in the virtual board
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                # same as explained above just we change the is MAXIMIZING depending weather its a PLAYER or BOT
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        # at the begining we assume that BOT is WINNING so we set the best score to +1 = LOOSE FOR PLAYER
        bestScore = 800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                # isMaximizing = True = we want the BOT to win
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore


for k in board.keys():
    board1[k] = " " + board[k] + " "
printBoard(board)


print("Positions are as follow:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("\n")

global firstComputerMove
firstComputerMove = True

print("Computer goes first! Good luck.")
while not checkForWin():
    compMove()
    playerMove()

print("Finished Execution !")
