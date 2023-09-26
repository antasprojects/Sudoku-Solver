## Sudoku Solver with back tracking algorithm



Board = [
    [7, 5, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 8, 6, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 4, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 5, 0, 9, 0, 0],
    [0, 0, 0, 0, 0, 0, 8, 0, 6],
    [6, 0, 9, 8, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 5, 0],
    [3, 0, 0, 0, 0, 0, 0, 0, 0]
]


# Board = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]




def show_board(B):

    for y in range(len(B)):
        if y % 3 == 0 and y != 0:
            print("- - - - - - - - - - - - - - - - ")
        for x in range(len(B[0])):
            if x % 3 == 0 and x != 0:
                print("| ", end=" ")

            if x == 8:
                print(B[y][x])
            else:
                print(str(B[y][x]) + " ", end=" ")



def find_zero(Board):
    for y in range(len(Board)):
        for x in range(len(Board[0])):
            if Board[y][x] == 0:
                i = x
                j = y
                return i, j


    return None




def check_posibilities(i,j):

    # all posibilities
    posibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # checking the vertical line
    for y in range(len(Board)):
        if Board[y][i] != 0 and Board[y][i] in posibilities:
            posibilities.remove(Board[y][i])

    # checking the horizontal line
    for x in range(len(Board[i])):
        if Board[j][x] != 0 and Board[j][x] in posibilities:
            posibilities.remove(Board[j][x])


    # checking the small square

    square_x = int(i // 3)
    square_y = int(j // 3)

    for x in range(square_x*3, square_x*3 + 3):
        for y in range(square_y*3, square_y*3 + 3):
            if Board[y][x] != 0 and Board[y][x] in posibilities:
                posibilities.remove(Board[y][x])


    return posibilities


def solve(Board):

    zero = find_zero(Board)
    if not zero:
        return True
    else:
        i, j = zero
        for posibility in check_posibilities(i, j):
            Board[j][i] = posibility


            if solve(Board):
                return True

            Board[j][i] = 0

        return False


show_board(Board)
solve(Board)
print()
show_board(Board)







