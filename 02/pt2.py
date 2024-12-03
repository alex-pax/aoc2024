import re

# open() creates a TextIOWrapper object
# methods of TextIOWrapper are used to read data from the connection
file_con = open('02/input.txt')

# .readlines() - list of characters; one per line
# are all various ways 
lines = file_con.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

# convert lines to lists of number strings:
levels = []
for line in lines:
    levels.append(re.findall(r"\d+", line))

# convert from string to int:
for i in range(len(levels)):
    for j in range(len(levels[i])):
        levels[i][j] = int(levels[i][j])

################################################################################
## Create helper functions to handle problem's logical comparisons
################################################################################
        
# Helper function to check one of the two criteria:        
def incr_decr_check(x):
    # From the problem statement:
    # The levels are either all increasing or all decreasing.
    #
    # We will check both in this function and return True/False
    #  depending on whether the level meets the criteria
    incr_check = []
    decr_check = []

    # check if all values are increasing:
    for i in range(1, len(x)):
        incr_check.append(x[i] > x[i-1])

    # check if all value are decreasing:
    for i in range(1, len(x)):
        decr_check.append(x[i] < x[i-1])
       
    return (all(incr_check) or all(decr_check))


# Helper function to check the other criteria:
def check_distance(x):
    # From the problem statement:
    #
    # Any two adjacent levels differ by at least one and at most
    # three.

    dist_check = []
    for i in range(1, len(x)):
        dist_check.append(abs(x[i] - x[i-1]) >= 1 and abs(x[i] - x[i-1]) <= 3)

    return all(dist_check)

def check_both(x):
    # combine the helpers
    return all([incr_decr_check(x), check_distance(x)])

# new for part 2: remove each element of a level incrementally and
#  re-check if the level is safe
def check_dampened_levels(x):
    if check_both(x):
        return True
    else:
        incremental_checks = []
        for i in range(len(x)):
            # pop off element at index i, store in val
            val = x.pop(i)
            # check if levels is safe without popped element
            incremental_checks.append(check_both(x))
            # push element back into it's previous position
            x.insert(i, val)
        return any(incremental_checks)

    
################################################################################
## Apply helpers to the data and get our answer
################################################################################

safe_levels = []
for level in levels:
    safe_levels.append(check_dampened_levels(level))

answer = 0
for safe_level in safe_levels:
    answer += safe_level

print(answer)
