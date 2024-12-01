import re

# open() creates a TextIOWrapper object
# methods of TextIOWrapper are used to read data from the connection
file_con = open('input.txt')


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
for pair in line_nums:
    left_list.append(int(pair[0]))
    right_list.append(int(pair[1]))


similarity_list = []
for num in left_list:
    similarity_list.append(num * right_list.count(num))

answer = 0
for num in similarity_list:
    answer += num

print(answer)    
