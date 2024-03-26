import random

matrix = ["x", "o", "x", "o", "o", "x", "o", "x", "x"]
winning_tuple = ([0, 1, 2], [0, 3, 6], [0, 4, 8],
                 [1, 4, 7], [2, 5, 8], [2, 4, 6],
                 [3, 4, 5], [6, 7, 8])

TURN = '1'


def matrix_clean():
    for n in range(0, 9):
        matrix[n] = " "


def update(index):
    row = int(index[0])
    column = int(index[1])
    if row < 3 and column < 3:
        # for matrix index into row index conversion
        indices = column
        if row == 1:
            indices = column + 3
        if row == 2:
            indices = column + 6

        # check for given index is empty or not
        if matrix[indices] != " ":
            print("please enter valid index")
            userinput()

        # set which value to be set in matrix
        value = ""
        if TURN == "1":
            value = player1_choice
        if TURN == "2":
            value = player2_choice
        matrix[indices] = value
    else:
        print("please enter valid index")
        userinput()


def display():
    for n in range(1, 10):
        if n % 3 == 0:
            temp = "\n"
        else:
            temp = "|"
        print(matrix[n-1], end=f"{temp}")


def cpu_update():
    vacant_places = []
    for i in range(0, 9):
        if matrix[i] == " ":
            vacant_places.append(i)
    cpu_choice = random.choice(vacant_places)
    matrix[cpu_choice] = player2_choice


def userinput():
    global TURN
    player = input(f"Player{TURN} your turn: ")
    update(player)
    if play_with_computer == "yes":
        cpu_update()
    else:
        if TURN == '1':
            TURN = "2"
        else:
            TURN = '1'


def check():
    global game_is_on
    for i in winning_tuple:
        if matrix[i[0]] == 'x':
            if matrix[i[1]] == 'x':
                if matrix[i[2]] == 'x':
                    game_is_on = False
                    print("X is The winner")
        if matrix[i[0]] == 'o':
            if matrix[i[1]] == 'o':
                if matrix[i[2]] == 'o':
                    game_is_on = False
                    print("O is The winner")


print("Tic Tac Toe")
display()
print("Instruction:\nfor changing element use '02' \n\t0->for row and \n\t2->for column")
play_with_computer = input("Want to play with CPU? YES or NO: ").lower()
player1_choice = input("Player1 choose 'x' or 'o': ").lower()
if player1_choice == 'x':
    player2_choice = 'o'
else:
    player2_choice = 'x'
matrix_clean()
game_is_on = True
while game_is_on:
    userinput()
    display()
    check()
