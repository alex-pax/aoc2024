import re

# open() creates a TextIOWrapper object
# methods of TextIOWrapper are used to read data from the connection
file_con = open('03/input.txt')

# .readlines() - list of characters; one per line
# are all various ways 
lines = file_con.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

# Find the uncorrupted lines of multiplication, which
#  look exactly like:
#   mul(X,Y)
#  where X and Y are between 1 and 3 digits
# Can achieve this very quickly with regex:
uncorrupted_lines = []
for line in lines:
    uncorrupted_lines.append(re.findall(r"mul\(\d{1,3},\d{1,3}\)", line))

# Could have combined the lines into one string earlier, but we'll do
# it now:
collated_operations = []
for i in range(len(uncorrupted_lines)):
    for j in range(len(uncorrupted_lines[i])):
        collated_operations.append(uncorrupted_lines[i][j])

# extract just the pair of numbers from each operation:        
num_list = []        
for item in collated_operations:
    num_list.append(re.findall(r"\d+", item))

# Split pairs into list of operands    
lhs = []
rhs = []
for num in num_list:
    lhs.append(int(num[0]))
    rhs.append(int(num[1]))

# Perform the sum of the product of all the pairs:    
output = 0
for i in range(len(lhs)):
    output += lhs[i] * rhs[i]

print(output)    
