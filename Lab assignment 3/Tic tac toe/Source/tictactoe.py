import random  #Random function has been called
def tic_tac_toe():  #defined tic tac toe as function
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]  #Total numbers of board places has been assigned starting from 1 to 9 otherwise it will generate output as false
    end = False
    win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
                    #These are the possible winning combinations has been assigned in input
    def draw():
        print(board[0], board[1], board[2]) #These are the possible draw combination which has been assigned in inout side
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])
        print()

    def p1():
        n = choose_number()         #Place of the mark A or B
        if board[n] == "X" or board[n] == "O":     #"X' and 'O' will be used by either user
            print("\nCan't choose that place. Try again") #If number assigned is other than defined in inout side then it will print following message, otherwise 'X' as default
            p1()
        else:
            board[n] = "X"

    def p2():
        n = choose_number()
        if board[n] == "X" or board[n] == "O":
            print("\nCan't choose that place. Try again")  #Same will be in this case as above where if player choose different place other what defined in input side then it will print as following message, otherwise it will print 'O' by default for player 2
            p2()
        else:
            board[n] = "O"

    def choose_number():      #This function is used to accept number from input(Player)
        while True:
            while True:
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(0, 9):     #The range of board index value has been assigned
                        return a
                    else:
                        print("\nNot on the board. Try again")   #If player enters value other than index value assigned on board then following message will display
                        continue
                except ValueError:        #If in case entered input is not a number i. e. letter, then it will print error message as mentioned
                   print("\nNot a number. Try again")
                   continue

    def check_board():
        count = 0
        for a in win_commbinations:        #Here i have used 0,1,2 combination for example to show win condition
            if board[a[0]] == board[a[1]] == board[a[2]] == "X":
                print("Angie Won!\n")
                print("Congratulations!\n")
                return True

            if board[a[0]] == board[a[1]] == board[a[2]] == "O":
                print("Jeremy Won!\n")
                print("Congratulations!\n")
                return True

        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                count += 1
            if count == 9:
                print("The game has been tied\n")
                return True

    while not end:

        end = check_board()
        if end == True:
            break
        print("Angie will choose where to place a cross")
        p1()
        print()

        end = check_board()
        if end == True:
            break
        print("jeremy will choose where to place a nought")
        p2()
        print()

    if input("Want to play again? (y/n)\n") == "y":     #If user wants to restart the game then press 'y', otherwise 'n' to terminate
        print()
        tic_tac_toe()

tic_tac_toe()