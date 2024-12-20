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


similarity_list = []
# this is basically the question AoC is asking us to solve.
#  the built-in .count() method for lists does pretty much
#  all of the work here.
# Take each number in left_list, multiply it by the
#  number of times it appears in right_list, and
#  append to similarity_list.
for num in left_list:
    similarity_list.append(num * right_list.count(num))

answer = 0
# Add up all the similarity scores:
for num in similarity_list:
    answer += num

print(answer)    
