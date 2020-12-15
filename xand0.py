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
    print(board[0],"|",board[1],"|",board[2])
    print(board[3],"|",board[4],"|",board[5])
    print(board[6],"|",board[7],"|",board[8])
    print('\n')
    void_places()
    win(board,choice)

    if choice=="x":
        playerx(board)
    if choice=="0":
        player0(board)
    if choice=="q":
        print('[THANK YOUR FOR PLAYING]')
        exit()
    else:
        print("invalid choice")



def win(board,choice):
    #CHECKING ALL POSSIBILITES OF WINNERS
    if (board[0] == choice and board[1] == choice and board[2] == choice):
        winner(choice)
    if (board[3] == choice and board[4] == choice and board[5] == choice):
        winner(choice)
    if (board[6] == choice and board[7] == choice and board[8] == choice):
        winner(choice)
    if (board[0] == choice and board[4] == choice and board[8] == choice):
        winner(choice)
    if (board[0] == choice and board[3] == choice and board[6] == choice):
        winner(choice)
    if (board[1] == choice and board[4] == choice and board[8] == choice):
        winner(choice)
    if (board[2] == choice and board[5] == choice and board[8] == choice):
        winner(choice)
    if (board[2] == choice and board[5] == choice and board[8] == choice):
        winner(choice)

    if board.count('-') <=0 :
        print("Tie!") 
        xand0(True , True)


def playerx(board):
    #PLAYING X
    try:
        print("enter the position for x:")
        position=int(input())
        position=position-1
        print(f'{player_1} plays {position+1}')
        if board[position]=="0":
            print("0 already exists")
            choice="x"
            main(choice,board)
        board[position]='x'
        choice="0"
        remaining_places = []
        main(choice,board)
    except:
        print('ENTER A VALID NUMBER BETWEEN 1-9')
        playerx(board)

def second_player_move(position):
    if board[position]=="x":
        print("x already exists")
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
                exit()
            if play_again=="c":
                 xand0(True,False)

        no_of_players = input("[HOW MANY PLAYERS ARE PLAYING?]:")
        player_1 = input('[ENTER THE NAME OF FIRST PLAYER]:')

        
        if no_of_players == '2':
            player_2 = input('[ENTER THE NAME OF SECOND PLAYER]:')
        
        elif no_of_players == '1' :
            player_2 = 'Computer'
        
        choice = 'x'

        player_data[player_1] = 'x'
        player_data[player_2] = '0'
        
        for key , value in player_data.items():
            print(f'{key} plays {value}')

        print('\n')
        main(choice,board)


if __name__== "__main__":
    remaining_places = []
    player_data = dict()
    game=True
    loop=False
    xand0(game,loop)
