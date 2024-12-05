import re

# open() creates a TextIOWrapper object
# methods of TextIOWrapper are used to read data from the connection
file_con = open('04/input.txt')

# .readlines() - list of characters; one per line
# are all various ways 
lines = file_con.readlines()

# found that I was using this number a lot, make it a variable:
matrix_size = len(lines)

for i in range(len(lines)):
    lines[i] = lines[i].strip()

# Using regex for part 2 is much less convenient.  will use a helper
#  function to extract the relevant 3x3 grid from the matrix and check
#  it for an "X-MAS"
    
line_chars = []
for line in lines:
    line_chars.append(re.findall("[A-Z]", line))

def xmas_checker(letter_matrix, i, j):
    """
    with index (i,j) representing the upper-left hand corner of the
    3x3 submatrix to check, return True if "X-MAS" is
    present; return False otherwise

    i is the row
    j is the column
    """
    edge = len(letter_matrix) - 1
    
    ## Check simple edge cases first that cannot possible return an X-MAS.
    if (i >= edge - 1) or (j >= edge - 1):
        return False

    ## Generate 3x3 submatrix:
    sub = [[0 for _ in range(3)] for _ in range(3)]
    for x in range(3):
        for y in range(3):
            sub[x][y] = letter_matrix[i + x][j + y]

    # To save on time, check that the middle character is an 'A'
    # before proceeding:
    if sub[1][1] != 'A':
        return False

    
    # Each MAS can be forward or backward
    # check both diagonals
    case_one_check = ((sub[0][0] == 'M' and
                       sub[2][2] == 'S') or
                      (sub[0][0] == 'S' and
                       sub[2][2] == 'M'))

    case_two_check = ((sub[0][2] == 'S' and
                       sub[2][0] == 'M') or
                      (sub[0][2] == 'M' and
                       sub[2][0] == 'S'))

    ## both cases need to be True for it to be an X-MAS:
    return case_one_check and case_two_check

# testing xmas_checker
test_mat = [['S', 'X', 'S'],
            ['K', 'A', 'K'],
            ['M', 'D', 'M']]
xmas_checker(test_mat, 0, 0)

    
check_list = []
for i in range(matrix_size):
    for j in range(matrix_size):
        check_list.append(xmas_checker(line_chars, i, j))

answer = 0
for check in check_list:
    answer += check

print(answer)    
