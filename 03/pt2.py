import re

# open() creates a TextIOWrapper object
# methods of TextIOWrapper are used to read data from the connection
file_con = open('03/input.txt')

# .readlines() - list of characters; one per line
# are all various ways 
lines = file_con.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

# Since the program starts with multiplication enabled
#  we'll just add a 'do()' instruction to the start
#  of it.  Then we don't need a seperate special case
lines[0] = "do()" + lines[0]

# Find the uncorrupted lines of multiplication, which
#  look exactly like:
#   mul(X,Y)
#  where X and Y are between 1 and 3 digits
# For part 2, add do() and don't() to pattern matching.
# Can achieve this very quickly with regex:
uncorrupted_lines = []
for line in lines:
    uncorrupted_lines.append(re.findall(r"(do\(\)|don\'t\(\)|mul\(\d{1,3},\d{1,3}\))", line))

    
# Could have combined the lines into one string earlier, but we'll do
# it now:
collated_operations = []
for i in range(len(uncorrupted_lines)):
    for j in range(len(uncorrupted_lines[i])):
        collated_operations.append(uncorrupted_lines[i][j])

# Perform part 2's switching logic.
# When we encounter a do()/don't() operation,
#  turn the switch on/off then go to the next item.
# When we don't encounter a do()/don't() operation:
#  if the switch is on, add the operation to the stack
#  otherwise, if it's off, go to next item.
op_switch = True
filtered_operations = []
for op in collated_operations:
    if op == 'do()':
        op_switch = True
        continue
    else:
        if op == "don't()":
            op_switch = False
            continue
        else:
            if op_switch:
                filtered_operations.append(op)


################################################################################
## The rest is the same as from part 1, the loop above to filter for
##  only do() operations and the regex to include the do() and don't()
##  strings are the only significant additions to solve part 2.
################################################################################


# extract just the pair of numbers from each operation:        
num_list = []        
for item in filtered_operations:
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
