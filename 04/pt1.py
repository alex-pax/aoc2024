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

# the lines list contains all left-right and right-left info we need
# for 1/4 of the puzzle

# Pivot this info 90 degrees to extract another 1/4 for the top-bottom
# and bottom-top info:
line_chars = []
for line in lines:
    line_chars.append(re.findall("[A-Z]", line))

vert_lines = []
for i in range(matrix_size):
    temp = ""
    for j in range(matrix_size):
        # j then i does the trick
        temp += line_chars[j][i]
    vert_lines.append(temp)

# Abuse the fact that problem input is square to get diagonal line
# info for another two more 1/4ths of puzzle info.
#
# There are N x 2 - 1 many diagonals in an NxN matrix:
diag_lines_one = [[] for _ in range(matrix_size * 2 - 1)]
diag_lines_two = [[] for _ in range(matrix_size * 2 - 1)]

# outer loop goes across lines to extract diagonals:
for i in range(matrix_size):
    for j in range(matrix_size):
        diag_lines_one[i+j].append(line_chars[i][j])
        diag_lines_two[i-j + matrix_size - 1].append(line_chars[i][j])

# Concatenate back into strings:        
for i in range(len(diag_lines_one)):
    diag_lines_one[i] = "".join(diag_lines_one[i])
for i in range(len(diag_lines_two)):
    diag_lines_two[i] = "".join(diag_lines_two[i])    

# Ok, so now lines, vert_lines, diag_lines_one, and diag_lines_two
#  contain all the information we need to count matches of "XMAS" or "SAMX":
xmas_count = 0
for line in lines:
    xmas_count += len(re.findall("XMAS", line))
    xmas_count += len(re.findall("SAMX", line))

for line in vert_lines:
    xmas_count += len(re.findall("XMAS", line))
    xmas_count += len(re.findall("SAMX", line))

for line in diag_lines_one:
    xmas_count += len(re.findall("XMAS", line))
    xmas_count += len(re.findall("SAMX", line))

for line in diag_lines_two:
    xmas_count += len(re.findall("XMAS", line))
    xmas_count += len(re.findall("SAMX", line))

print(xmas_count)
