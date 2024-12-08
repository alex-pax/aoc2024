import re

# open() creates a TextIOWrapper object
# methods of TextIOWrapper are used to read data from the connection
file_con = open('07/input.txt')

# .readlines() - list of characters; one per line
# are all various ways 
lines = file_con.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()
    lines[i] = lines[i].split(":")
    ## convert string of operands to list of character operands:
    lines[i][1] = re.findall(r"\d+", lines[i][1])
    ## convert result of operation to int:
    lines[i][0] = int(lines[i][0])
    ## convert list of operand characters to int:
    for n in range(len(lines[i][1])):
        lines[i][1][n] = int(lines[i][1][n])

test_values = []
opperands = []
for line in lines:
    test_values.append(line[0])
    opperands.append(line[1])


def generate_permutations(elements, length):
    if length == 0:
        return [()]
    smaller_permutations = generate_permutations(elements, length - 1)
    return [(e,) + p for e in elements for p in smaller_permutations]
    
def new_add(a, b):
    return a + b

def new_mult(a, b):
    return a * b

def int_concat(a, b):
    return int(str(a) + str(b))

def create_possible_vals(ops, funs):
    # ops is the list of opperands (integers)
    # funs is the set of possible functions to apply
    
    function_orders = generate_permutations(funs, len(ops) - 1)

    vals = []

    for fun in function_orders:
        temp = ops[0]
        for i in range(len(ops) - 1):
            temp = fun[i](temp, ops[i+1])
        vals.append(temp)

    return vals
            
            
check_list = []

for op in opperands:
    check_list.append(create_possible_vals(op, {new_add, new_mult, int_concat}))

result = 0    
for i in range(len(test_values)):
    if test_values[i] in check_list[i]:
        result += test_values[i]

print(result)
