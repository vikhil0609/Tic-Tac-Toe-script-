import random

def winner(player):
    #DECLARING WINNERS
    for k,v in player_data.items():
        if v == player:
            print(f'[{k}] has won the match')
    xand0(True,True)

def void_places():
    #TO CHECK VOID PLACES IN THE BOARD
    for spaces in range(len(board)):
        if board[spaces] == "-":
            remaining_places.append(spaces+1)

    return remaining_places


def main(choice,board):
    '''operates each an every function of
        games either it may be for checking the winner
        or playing playerx or playery.
        This is kind of gateway to pass through the set of rules of games to played'''

    print(board[0],"|",board[1],"|",board[2])
    print("--|---|--")
    print(board[3],"|",board[4],"|",board[5])
    print("--|---|--")
    print(board[6],"|",board[7],"|",board[8])
    print('\n')


    if choice=="x":
        if win(board,"0"):
            playerx(board)
    if choice=="0":
        if win(board,"x"):
            player0(board)
    else:
        print("invalid choice")



def win(board,choice):
    #CHECKING ALL POSSIBILITES OF WINNERS
    if (board[0] == choice and board[1] == choice and board[2] == choice):
        winner(choice)
        return False
    if (board[3] == choice and board[4] == choice and board[5] == choice):
        winner(choice)
        return False
    if (board[6] == choice and board[7] == choice and board[8] == choice):
        winner(choice)
        return False
    if (board[0] == choice and board[4] == choice and board[8] == choice):
        winner(choice)
        return False
    if (board[0] == choice and board[3] == choice and board[6] == choice):
        winner(choice)
        return False
    if (board[1] == choice and board[4] == choice and board[8] == choice):
        winner(choice)
        return False
    if (board[2] == choice and board[5] == choice and board[8] == choice):
        winner(choice)
        return False
    if (board[2] == choice and board[4] == choice and board[6] == choice):
        winner(choice)
        return False

    if board.count('-') <=0 :
        #CHECKS FOR TIE
        print("Tie!")
        xand0(True , True)

    else:
        return True

def playerx(board):
    #PLAYING X
    try:
        print("enter the position for x:")
        position=int(input())
        position=position-1
        print(f'{player_1} plays {position+1}')
        if board[position]=="0" or board[position]=="x"  :
            print("[PLACE ALREADY OCCUPIED]")
            choice="x"
            main(choice,board)
        board[position]='x'
        choice="0"
        main(choice,board)
    except:
        print('ENTER A VALID NUMBER BETWEEN 1-9')
        playerx(board)

def second_player_move(position):
    if board[position]=="x" or board[position]=='0':
        print("[PLACE ALREADY OCCUPIED]")
        choice="0"
        main(choice,board)
    board[position]='0'
    choice="x"
    main(choice,board)

def player0(board):
    #PLAYING 0
    if player_2 == 'Computer':
        void_places()
        position = int(random.choice(remaining_places))
        position = position -1
        print(f'Computer playes {position +1}')
        remaining_places.clear() #REMOVES ALL ITEMS FROM LIST SO THAT REDUNDENCY WILL NOT BE THERE
        second_player_move(position)

    else:
        try:
            print("enter position for 0:")
            position=int(input())
            position=position-1
            print(f'{player_2} plays {position+1} ')
            second_player_move(position)
        except:
            print('ENTER A VALID NUUMBER BETWEEN 1-9')
            player0(board)


def xand0(game,loop):
    #MAIN GAME LOOP
    global player_1
    global player_2
    global board
    while  game:
        board=["-","-","-",
               "-","-","-",
               "-","-","-",]
        while loop:

            play_again=input("press q to quit or c to play again:")
            if play_again =="q" :
                print('[THANK YOUR FOR PLAYING]')
                quit()
                xand0(True,False)
            if play_again=="c":
                 xand0(True,False)


        try:
            no_of_players = int(input("[HOW MANY PLAYERS ARE PLAYING?]:"))
            player_1 = input('[ENTER THE NAME OF FIRST PLAYER]:')


            if (no_of_players) == 2:
                player_2 = input('[ENTER THE NAME OF SECOND PLAYER]:')

            elif no_of_players == 1 :
                player_2 = 'Computer'

            choice = 'x'

            player_data[player_1] = 'x'
            player_data[player_2] = '0'

            for key , value in player_data.items():
                print(f'{key} plays {value}')

            print('\n')
            main(choice,board)

        except:
            print("[WRONG INPUT]")
            print("[CHOOSE NO OF PLAYERS IN NUMBERS EITHER 1 OR 2]")
            xand0(True,False)

if __name__== "__main__":
    remaining_places = []
    player_data = dict()
    game=True
    loop=False
    xand0(game,loop)
