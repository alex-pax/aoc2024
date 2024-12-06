import re

# open() creates a TextIOWrapper object
# methods of TextIOWrapper are used to read data from the connection
file_con = open('05/input.txt')

# .readlines() - list of characters; one per line
# are all various ways 
lines = file_con.readlines()

# Split lines into rules and updates based on weather they occur
# before or after the single new line character
rules = lines[0:lines.index("\n")]
updates = lines[(lines.index("\n")+1):(len(lines)+1)]

# strip whitespace:
for i in range(len(rules)):
    rules[i] = rules[i].strip()

for i in range(len(updates)):
    updates[i] = updates[i].strip()

# Convert strings to integer information.  rules will contain a list
# of list pairs where the rule is that element 0 must appear before
# element 1 in the update.  updates will contain a list of lists where
# the order of the elements of the sublists will be checked for
# adhering to all of the rules.

for i in range(len(rules)):
    rules[i] = re.findall(r"\d+", rules[i])
    for j in range(len(rules[i])):
        rules[i][j] = int(rules[i][j])

for i in range(len(updates)):
    updates[i] = re.findall(r"\d+", updates[i])
    for j in range(len(updates[i])):
        updates[i][j] = int(updates[i][j])

        
def find_relevant_rules(update, rule_set):
    """
    for each rule in 'rule', check that both numbers that define the
    rule appear in update.  If they don't, exclude them from the
    result.  Return a sublist of 'rule' with only the rules that need
    apply to update
    """
    out = []
    for rule in rule_set:
        if(rule[0] in update and rule[1] in update):
            out.append(rule)

    return out

incorrect_updates = []
for update in updates:
    # get only the relevant rules:
    checks = find_relevant_rules(update, rules)
    checks_followed = []
    # Boolean list describing whether each rules was met:
    for check in checks:
        checks_followed.append(update.index(check[0]) < update.index(check[1]))

    # if not all rules were met, then add to list of "incorrect updates"
    # this is the first change since part 1.
    if not all(checks_followed):
        incorrect_updates.append(update)

def apply_rules_sort(rule_set):
    """

    Return a function of (x) that returns the number of times x
    appears in rule_set.

    """
    
    # rule_set needs to be pre-process to be a list of the first
    # (lowest) number in each binary rule pair.  The number that shows
    # up first on this list the most is less than all the other
    # numbers, etc...
    def custom_key(x):
        return(rule_set.count(x))
    return custom_key

corrected_updates = []
for i in range(len(incorrect_updates)):
    ## shallow copy to prevent altering original incorrect_update
    ## element:
    temp = incorrect_updates[i][:]
    # get the relevant rules:
    checks = find_relevant_rules(temp, rules)
    lowest_num = []
    # get the first (lowest) number from each rule:
    for check in checks:
        lowest_num.append(check[0])
    # lock in the list of lowest numbers as the sorting rule for a
    # custom sort key function:
    loop_key_fun = apply_rules_sort(rule_set = lowest_num)
    # sort the numbers in the correct order:
    temp.sort(key=loop_key_fun, reverse=True)
    corrected_updates.append(temp)
        
middle_numbers = []
for update in corrected_updates:
    # is there a better way to get the middle element of an odd-length
    # list?
    middle_numbers.append(update[int((len(update) - 1) / 2)])

# add 'em all up:    
answer = 0
for num in middle_numbers:
    answer += num

print(answer)
