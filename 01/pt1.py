import re

# open() creates a TextIOWrapper object
# methods of TextIOWrapper are used to read data from the connection
file_con = open('01/input.txt')


# .read() - a character string containing the entire contents of the file
# .readline() - a character string containing the first line of the file
# .readlines() - list of characters; one per line
# are all various ways 
lines = file_con.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

line_nums = []
# convert each line into a list of the pairs of numbers on
#  those lines.
# numbers will still be strings after this step
for line in lines:
    line_nums.append(re.findall(r"\d+", line))

left_list = []
right_list = []
# split line pairs into column lists and convert to integer:
for pair in line_nums:
    left_list.append(int(pair[0]))
    right_list.append(int(pair[1]))

# sort both lists from small to large:
left_list.sort()
right_list.sort()

diff_list = []
# calc absolute value of difference between
#  pairwise elements of sorted lists:
for i in range(len(left_list)):
    diff_list.append(abs(left_list[i] - right_list[i]))

# add 'em all up:    
answer = 0
for diff in diff_list:
    answer += diff

print(answer)    
