'''
 @Author: Ritika Patidar
 @Date: 2021-02-13 11:28:29
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-17 8:19:29 
 @Title : Cross game problem
 '''
#importing module 
import logging 
import random

#function for create board
def create_board(user_input):
    return [[' ' for r in range(user_input)]for r in range(user_input)]
def draw_board(board):
    print(board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("--|---|--")
    print(board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("--|---|--")
    print(board[2][0] + " | " + board[2][1] + " | " + board[2][2])


#check who have first turn
def choose_player():
    if(random.randint(1,2)==1):
        return ["0","X"]
    else:
        return ["X","0"]

#function for see empty move on board
def random_space(board):
    available_move={}
    possible_move={(0,0):1, (0,1):2, (0,2):3, (1,0):4, (1,1):5, (1,2):6, (2,0):7, (2,1):8, (2,2):9}
    for r in range(len(board)):
        for c in range(len(board)):
            if(board[r][c]==" "):
                available_move[possible_move[(r,c)]]=(r,c)
    return available_move

#function for computer move 
def computer_move(board):
    select=random_space(board)
    if(len(list(select.values()))>0):
        selection=random.choice(list(select.values()))
        board[selection[0]][selection[1]]="0"
    return board

#function for user move
def user_move(board):
    while True:
        empty_space=random_space(board)
        print("available move: {0}".format(list(empty_space.keys())))
        user_turn=int(input("it's your turn enter: "))
        try:
            if(empty_space[user_turn] in list(empty_space.values())):
                board[empty_space[user_turn][0]][empty_space[user_turn][1]]="X"
                break
        except KeyError:
            print("this move is not available please try again!!")
#function for player move
def move(player,board):
    global counter
    if(player=="0"):
        move_com=computer_move(board)
        print("computer move {0}".format(counter))
        draw_board(board)
        counter+=1
    else:
        try:
            move_user=user_move(board)
            print("user move {0}".format(counter))
            draw_board(board)
            counter+=1
        except ValueError as error:
            print("give only int value")
            move(player,board)

#function for check the winning row
def evaluate_game(board,player):
    winner=0
    for r in range(len(board)):
        win=True
        for c in range(len(board)):
            if(board[r][c]!=player):
                win=False
                continue
        if(win==True):
            winner=player
    if win==False:
        for r in range(len(board)):
            win=True
            for c in range(len(board)):
                if(board[c][r]!=player):
                    win=False
                    continue
            if(win==True):
                winner=player
    if win==False:
        win=True
        for r in range(len(board)):
            if(board[r][r]!=player):
                win=False
        if(win==False):
            win=True
            for r in range(len(board)):
                if(board[r][len(board)-1-r]!=player):
                    win=False
    if(win==True):
        winner=player
    if(winner==0 and len(random_space(board))==0):
        return -1
    return winner
    
#function for result of game
def result(winner):
    print(winner)
    if(winner=="0"):
        return "computer is winner"
    elif(winner=="X"):
        return "user is winner"
    else:
        return "game is tie"

#main program for play game
def play_game():
    try:
        winner=0
        global counter
        counter=1
        user_input=3
        board=create_board(user_input)
        player_seq=choose_player()
        while(len(random_space(board))>0 and winner==0):
            for player in player_seq:
                move(player,board)
                winner=evaluate_game(board,player)
                if(winner!=0):
                    break
        print(result(winner))
    except ValueError as error:
        print("give input integer only")
        play_game()

if __name__ == "__main__":
    play_game()
