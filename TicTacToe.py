#Function to choose the game mode. Either single player or multiplayer
def choice():
    try:
        mode=int(input('Choice: '))
        print()
        if mode not in range(1,3):
            print('You\'ve entered an invalid option. PLease try again')
            choice()
        else:
            start(mode)
    except(ValueError):
        print('You\'ve entered an invalid option. Please try again')
        print()
        choice()

def start(mode):
    #Initialise (3x3)board
    board=[
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
    ]
    win=False
    draw=False
    PC=0

    if mode==2:
        print('Player 1 is O')
        print('Player 2 is X')
    else:
        PC=int(input('Play first(1) or second(2): '))

        #display empty board
    grid(board)
    print('Example of input: C3')

    while win==False and draw==False:
        PC=inpt(board,PC,mode)
        grid(board)
        win=check(win,board)
        #check to see if the outcome was a draw for the grid is full and no winner was found
        if PC==9 and win==False:
            print('DRAW')
            draw=True

def inpt(board,PC,mode):
#sym means symbol(X or O)
    turn=False
    sym,PC,turn=playa(PC,turn)
    free=False
    if mode ==2:
        while free==False:
            #decide who's turn it is
            if turn == False:
                print("Player 2's turn")
            else:
                print("Player 1's turn")

            #input playing position then check if it is free or occupied
            pos=inptpos()
            free=posverify(pos,board)
            if free==False:
                print('Desired position is already occupied. Please choose another')
    else:
        while free==False:
            if PC%2==0:
                print("Player's turn:")
                pos=inptpos()
                free=posverify(pos,board)
                if free==False:
                    print('Input position is not empty')
            else:
                print("Computer's turn:")
                pos=com()
                free=posverify(pos,board)
    position(pos,board,sym)
    return PC

#function to check whether position on grid is free then place symbol if it is the case
def position(pos,board,sym):
    x=y(pos)
    if pos[0]=='A' and board[0][x]==' ':
        board[0][x]=sym
    elif pos[0]=='B' and board[1][x]==' ':
        board[1][x]=sym
    elif pos[0]=='C' and board[2][x]==' ':
        board[2][x]=sym

#for single player mode only. Will play in a random position when it is the computer's turn
def com():
    import random
    x=random.choice(['A','B','C'])
    y=random.choice(['1','2','3'])
    return x+y

#function to alternate between players
def playa(PC,turn):
    PC+=1
    if PC % 2==0:
        turn = not turn
        return 'X',PC, turn
    elif PC % 2 !=0:
        turn = not turn
        return 'O',PC, turn

#function to ind winning conditions
def check(win,board):
#DIAGONALS
    if board[0][0] == board[1][1] == board[2][2] and board[1][1] !=' ' or board[0][2] == board[1][1] == board[2][0] and board[1][1] !=' ':
        print(board[1][1],' wins')
        return True
    for i in range(0,3):
#HORIZONTALS
        if board[i][0] !=' ' and board[i][1] == board[i][2] == board[i][0]:
            print(board[i][0],' Wins')
            return True
#VERTICALS
        if board[0][i] !=' ' and board[1][i] == board[2][i] == board[0][i]:
            print(board[0][i],' Wins')
            return True
    else:
        return False

#displaying the current state of the board
def grid(board):
    print()
    print('    1  2  3')
    print()
    print('A ', ' | '.join(board[0]))
    print('   ---------')
    print('B ',' | '.join(board[1]))
    print('   ---------')
    print('C ',' | '.join(board[2]))
    print()
    print()

#to check whether incorrect position has been input
def inptpos():
    comb=['A1','A2','A3','B1','B2','B3','C1','C2','C3']
    valid = False
    while valid==False:
        pos=input('Position: ').upper()
        if pos in comb:
            valid = True
        else:
            print('Wrong format. Example of a correct input is "A1"')
    return pos


def posverify(pos,board):
    x=y(pos)
    if pos[0]=='A' and board[0][x]==' ' or pos[0]=='B' and board[1][x]==' ' or pos[0]=='C' and board[2][x]==' ':
        return True
    else:
        return False

def y(pos):
    return int(pos[1])-1

#initial interface
def game():
    play=True
    while play==True:
        print("""1) Singleplayer mode
2) Multiplayer mode
        """)
        choice()
        play = again()

#post game interface
def again():
        print('Keep on playing?(yes/no)')
        a = input('--->').upper()
        opshuns=['YES','NO']
        if a not in opshuns:
            again()
        else:
            if a=='YES':
                return True
            else:
                return False

game()
