"""
CSE 210 W02 Ari-John Katia
tic-tac-toe thing!
"""
#some variables since I don't really know much about inbuilt functions
numbers = [1,2,3,4,5,6,7,8,9]
player1 = "x"
player2 = "o"
phrase = ""
winner = ""

#the main program
def main():
    player = next("")
    while not (win(numbers) or tie(numbers)):
        area_of_play(numbers)
        move(player)
        player = next(player)
    area_of_play(numbers)
    has_win(numbers)
    print(phrase)
    print()

#not gonna lie, I almost gave up... and so did my bones

#the first three functions are just from me messing around
def area_of_play(numbers):
    print(f"{numbers[0]}|{numbers[1]}|{numbers[2]}\n"
    "-+-+-\n"
    f"{numbers[3]}|{numbers[4]}|{numbers[5]}\n"
    "-+-+-\n"
    f"{numbers[6]}|{numbers[7]}|{numbers[8]}\n"
    )
    #nice!

def x_select(numbers):
    selection = False
    while selection != True:
        select = int(input("x's turn to choose a square (1-9): "))
        if select >= 1 and select <= 9 and numbers[select-1] == select:
            numbers[select-1] = player1
            selection = True
        else:
            print("Please enter a valid number")
            selection = False

#why do I get the feeling that this specific function will come in handy during a certain week?
def o_select(numbers):
    selection = False
    while selection != True:
        select = int(input("o's turn to choose a square (1-9): "))
        if select >= 1 and select <= 9 and numbers[select-1] == select:
            numbers[select-1] = player2
            selection = True
        else:
            print("Please enter a valid number")
            selection = False

#next and move are from both a video and solution after giving up after 3 hours of headache
def next(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"
        
def move(player):
    if player == "x":
        return x_select(numbers)
    elif player == "o":
        return o_select(numbers)

#hori, verti, diag are from going through a video and trying to understand what in the world a "return True" even means, dear lord was it a nightmare
def hori(board):
    global winner
    if board[0] == board[1] == board[2]:
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5]:
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8]:
        winner = board[6]
        return True

def verti(board):
    global winner
    if board[0] == board[3] == board[6]:
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7]:
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8]:
        winner = board[2]
        return True

def diag(board):
    global winner
    if board[0] == board[4] == board[8]:
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6]:
        winner = board[2]
        return True

#took what I learned from the video and solution to try and make this work to the best that I can think of
def has_win(numbers):
    global winner
    global phrase
    if hori(numbers) or verti(numbers) or diag(numbers):
        phrase = (f"Congratulations!\nThe winner is '{winner}'")

#win and tie are basically from the solution since the way I did it was absolutely terrible and I had no idea what I was doing
def win(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def tie(numbers):
    global phrase
    for i in range(9):
        if numbers[i] != "x" and numbers[i] != "o":
            return False
    phrase = "Good Game!\nIt's a tie"
    return True

if __name__ == "__main__":
    main()
