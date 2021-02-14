'''
 @Author: Ritika Patidar
 @Date: 2021-02-13 11:28:29
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-14 15:15:29 
 @Title : Cross game problem
 '''
import random

#function for create board
def create_board(user_input):
    return [[0 for r in range(user_input)]for r in range(user_input)]

#check who have first turn
def choose_player():
    if(random.randint(1,2)==1):
        return [1,2]
    else:
        return [2,1]

#function for see empty move on board
def random_space(board):
    available_move=[]
    for r in range(len(board)):
        for c in range(len(board)):
            if(board[r][c]==0):
                available_move.append((r,c))
    return available_move

#function for computer move 
def computer_move(board):
    if(len(random_space(board))>0):
        selection=random.choice(random_space(board))
        board[selection[0]][selection[1]]=1
    return board

#function for user move
def user_move(board):
    while True:
        empty_space=random_space(board)
        print("{0} spaces are available".format(empty_space))
        user_row=int(input("enter row value in available spaces: "))
        user_column=int(input("enter column value in available spaces: "))
        if((user_row,user_column) in empty_space):
            board[user_row][user_column]=2
            break

#function for player move
def move(player,board):
    global counter
    if(player==1):
        move_com=computer_move(board)
        print("computer move {0}".format(counter))
        print(board)
        counter+=1
    else:
        try:
            move_user=user_move(board)
            print("user move {0}".format(counter))
            print(board)
            counter+=1
        except ValueError:
            print("give only int value")
            move(player,board)

#function for check the winning row
def win_row(board,player):
    for r in range(len(board)):
        win=True
        for c in range(len(board)):
            if(board[r][c]!=player):
                win=False
                continue
        if(win==True):
            return win
    return win

#function for check the winning column
def win_col(board,player):
    for r in range(len(board)):
        win=True
        for c in range(len(board)):
            if(board[c][r]!=player):
                win=False
                continue
        if(win==True):
            return win
    return win

#function for check winning digonal 
def win_digon(board,player):
    win=True
    for r in range(len(board)):
        if(board[r][r]!=player):
            win=False
    if(win==False):
        win=True
        for r in range(len(board)):
            if(board[r][len(board)-1-r]!=player):
                win=False
    return win

#function for check winner or tie
def evaluate_game(board,player):
    winner=0
    if(win_row(board,player) or win_col(board,player) or win_digon(board,player)):
        winner=player
    if(winner==0 and len(random_space(board))==0):
        return -1
    return winner

#function for result of game
def result(winner):
    if(winner==1):
        return "computer is winner"
    elif(winner==2):
        return "user is winner"
    else:
        return "game is tie"

#main program for play game
def play_game():
    try:
        winner=0
        global counter
        counter=1
        while True:
            user_input=int(input("enter board size greater or equal to 3: "))
            if(user_input>=3):
                break
        board=create_board(user_input)
        player_seq=choose_player()
        while(len(random_space(board))>0 and winner==0):
            for player in player_seq:
                move(player,board)
                winner=evaluate_game(board,player)
                if(winner!=0):
                    break
        print(result(winner))
    except Exception as error:
        print("give input integer only")
        play_game()

if __name__ == "__main__":
    play_game()
