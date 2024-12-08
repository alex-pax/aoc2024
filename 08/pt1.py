import re

# open() creates a TextIOWrapper object
# methods of TextIOWrapper are used to read data from the connection
file_con = open('08/input.txt')

# .readlines() - list of characters; one per line
# are all various ways 
lines = file_con.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()
    lines[i] = re.findall(r".", lines[i])

map_size = [len(lines)-1, len(lines[0]) -1]
    
# modified function from day 07 to generate combindations instead of perumtations:
def generate_combinations(elements, length, start=0):
    if length == 0:
        return [()]
    combinations = []
    for i in range(start, len(elements)):
        smaller_combinations = generate_combinations(elements, length - 1, i + 1)
        for comb in smaller_combinations:
            combinations.append((elements[i],) + comb)
    return combinations

def find_unique_chars(x):
    # x is a list of lists, all items are strings
    #  looking for unique elements that match the regex [A-Za-z/d]

    chars = []
    for line in x:
        for item in line:
            # is item one of the characters we're looking for?
            if (len(re.findall(r"[A-Za-z\d]", item)) != 0 and
                item not in chars):
                chars.append(item)

    return(chars)

unique_chars = find_unique_chars(lines)

location_info = dict.fromkeys(unique_chars, [])

# Populate the dictionary with the list of coordinate pairs for all
# keys (the unique, valid characters found above):
for i in range(len(lines)):
    for j in range(len(lines[i])):
        char = lines[i][j]
        if char in unique_chars:
            # don't know the better python way to update a dictionary.
            # This hack seems to be fit for purpose
            temp = location_info[char][:]
            temp.append([i, j])
            location_info[char] = temp

# will be populated with the list of lists of all unique coordinate pairs            
connection_info = dict.fromkeys(unique_chars, [])

for key in connection_info.keys():
    connection_info[key] = generate_combinations(location_info[key], 2)

def create_freq_loc(loc_pair):
    # creates the frequency location at both ends of the pair.  need
    # to check later whether these are valid locations or note (i.e.,
    # not falling over the edge of the map)
    x_dist = loc_pair[0][0] - loc_pair[1][0]
    y_dist = loc_pair[0][1] - loc_pair[1][1]
    
    out1 = [loc_pair[0][0] + x_dist,
            loc_pair[0][1] + y_dist]

    out2 = [loc_pair[1][0] - x_dist,
            loc_pair[1][1] - y_dist]
    
    
    return [out1, out2]


# frequency_info = dict.fromkeys(unique_chars, [])
# for key in frequency_info.keys():
#     temp = []
#     for pair in connection_info[key]:
#         temp.append(create_freq_loc(pair))
#     frequency_info[key] = temp

# don't need this to be a dictionary, because at the moment, we don't
# care which antenna generates the frequencies:
frequency_info = []
for char in unique_chars:
    for pair in connection_info[char]:
        temp = create_freq_loc(pair)
        frequency_info.append(temp[0])
        frequency_info.append(temp[1])

def is_on_map(loc, size):
    # loc is a [x,y] cord pair    
    # size is the max x and y value in the matrix representing the map

    x = loc[0]
    y = loc[1]
    return (x >= 0 and
            x <= size[0] and
            y >= 0 and
            y <= size[1])

valid_locs = []
for loc in frequency_info:
    if (is_on_map(loc, map_size) and
        # preserve uniqueness of frequency locations:
        loc not in valid_locs):
        valid_locs.append(loc)

# answser is the number of valid locations:        
print(len(valid_locs))
