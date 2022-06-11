'''This is the function to run the game'''


def rules():
    print("player 1--->X")
    print("player 2--->Y")
    print("Enter the number written in each position to mark it with your symbol")
    layer = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    for i in layer:
        print("   |   ".join(i))
        print("----|-------|---")
    print("The first one to get three in a line wins!!!")


pos_sol = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]


def checker(xp, yp):
    ''' this checks for the result in each step of the game'''
    xc=[]
    yc=[]
    for sol in pos_sol:
        xc.append(len(xp.intersection(sol)))
        yc.append(len(yp.intersection(sol)))
        if(max(xc))>2:
            return 1
        elif(max(yc))>2:
            return 2
        else:
            continue
    return 0





def prt_game(board):
    print()
    print()
    print()
    for i in board.values():
        print("   |   ".join(i.values()))
        print("----|-------|---")


def adder(p1, p2, i):
    if i in range(1, 10):
        if i in p1:
            print("You have already picked the position, choose again")
            return 0
        elif i in p2:
            print("Your opponent has picked that position pick the right one")
            return 0
        else:
            p1.add(i)
            return 1
    else:
        print("Hehe nice joke")
        return 0


def inserter(i, board, char):
    if i in range(1, 4):
        board['row1'][i] = char
    elif i in range(4, 7):
        board['row2'][i] = char
    elif i in range(7, 10):
        board['row3'][i] = char
    else:
        raise Exception("Program should not reach this stage as if i is not valid it should have asked again")


rules()
xp = set()
yp = set()
count = 1
decision = 0
board = {'row1': {1: ' ', 2: ' ', 3: ' '}, "row2": {4: ' ', 5: ' ', 6: ' '}, "row3": {7: ' ', 8: ' ', 9: ' '}}
while count < 10 and decision == 0:
    if count % 2 != 0:
        print("player 1 turn")
        i = int(input("Enter the position"))
        breaker = adder(xp, yp, i)
        if breaker == 0:
            continue
        inserter(i, board, 'X')
        # print(xp)
        count += 1
    else:
        print("player 2 turn")
        i = int(input("Enter the position"))
        breaker = adder(yp, xp, i)
        if breaker == 0:
            continue
        inserter(i, board, 'O')
        # print(yp)
        count += 1
    prt_game(board)
    decision = checker(xp, yp)


else:
    pass

if decision == 1:
    print("congratulations player 1!!! You won")
elif decision == 2:
    print("Congatulations player 2!!! You won")
elif decision == 0:
    print("It's a tie!")
else:
    raise Exception("WHAT")
