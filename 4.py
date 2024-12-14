from typing import List 

def count_xmas(board:List[str]) -> int:
    # Find every XMAS on the board written forward, backward, up, down or diagonally
    # Get strings by reading the board horizontaly, verticaly and diagonally 
    # Then search for the word in the strings

    strings = []
    row_count = len(board)
    col_count = len(board[0])
    verticals = [[None] * col_count for i in range(0,row_count)]
    
    for row in range(0,row_count):
        for col in range(col_count):
            verticals[col][row] = board[row][col]


    top_right = [[] for i in range(0,len(board))]
    for start_col in range(0,col_count):
        col = start_col
        row = 0
        while row < row_count and col < col_count:
            top_right[start_col].append(board[row][col])
            row +=1
            col +=1

    bottom_left = [[] for i in range(0,len(board))]
    for start_row in range(1,row_count):
        row = start_row
        col = 0
        while row < row_count and col < col_count:
            bottom_left[start_row].append(board[row][col])
            row +=1
            col +=1

    top_left = [[] for i in range(0,len(board))]
    for start_col in range(col_count -1, -1, -1):
        col = start_col
        row = 0
        while row < row_count and col >= 0:
            top_left[start_col].append(board[row][col])
            row +=1
            col -=1


    bottom_right = [[] for i in range(0,len(board))]
    for start_row in range(1, row_count):
        col = col_count - 1
        row = start_row
        while row < row_count and col >= 0:
            bottom_right[start_row].append(board[row][col])
            row +=1
            col -=1

    for l in board:
        strings.append(l)
    
    for l in verticals:
        strings.append("".join(l))
    
    for l in top_right:
        strings.append("".join(l))
    for l in bottom_left:
        strings.append("".join(l))
    for l in top_left:
        strings.append("".join(l))
    for l in bottom_right:
        strings.append("".join(l))
    
    result = 0
    for s in strings:
        result += s.count('XMAS')
        result += s.count('SAMX')   # read it backwards too
    return result

def x_mas(board:List[str]) -> int:
    result = 0 
    row_count = len(board)
    col_count = len(board[0])
    for row in range(1, row_count - 1):
        for col in range(1, col_count -1):
            a = set(['M','S'])
            b = set(['M','S'])
            if 'A' == board[row][col]:
                tl = board[row-1][col-1]
                br = board[row+1][col+1]
                a.discard(tl)
                a.discard(br)
                tr = board[row-1][col+1]
                bl = board[row+1][col-1]
                b.discard(tr)
                b.discard(bl)
                if (len(a) == 0 and len(b) == 0):
                    result += 1
            

    return result

test = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
test_board = test.split('\n')
print(f"Test: XMAS Count {count_xmas(test_board)}")
print(f"Test: X-MAS Count {x_mas(test_board)}")

board = []
with open('./4.txt') as f:
    input = f.readlines()

for i in input:
    board.append(i.replace("\n",""))

print(f"XMAS Count {count_xmas(board)}")
print(f"X-MAS Count {x_mas(board)}")