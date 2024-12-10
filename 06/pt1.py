import re

# open() creates a TextIOWrapper object
# methods of TextIOWrapper are used to read data from the connection
file_con = open('06/input.txt')

# .readlines() - list of characters; one per line
# are all various ways 
lines = file_con.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()
    lines[i] = re.findall(r".", lines[i])

def get_start_index(mat):
    # return the row, col, and character of the starting location in a
    # list:
    for row in range(len(mat)):
        for col in range(len(mat[row])):
            if mat[row][col] in ['<', '^', '>', 'v']:
                return [row, col, mat[row][col]]

get_start_index(lines)            

# ^: move up be decrementing row
# >: move right by increasing col
# v: move down by increasing row
# <: move left by decreasing col

# rotate 90 degrees:
rotate_char = {"^": ">",
               ">": "v",
               "v": "<",
               "<": "^"}

def look_ahead(x):
    """
    char_info is a 3-element list with the following elements in this order:
      - [row, col, character symbol]
    
    returns the next row and col that the character /should/ move to
    regardless of whether that move is valid as well as the current
    character.  A different function will check for valid moves

    # ^: move up be decrementing row
    # >: move right by increasing col
    # v: move down by increasing row
    # <: move left by decreasing col
    """
    char_info = x[:]
    
    char_to_check = char_info[2]
    
    if char_to_check == "^":
        char_info[0] += -1
    elif char_to_check == ">":
        char_info[1] += 1
    elif char_to_check == "v":
        char_info[0] += 1
    elif char_to_check == "<":
        char_info[1] += -1
    else:
        raise ValueError("Invalid character type: " + char_to_check)

    return char_info

def apply_next_move(cur, proposed, mat):
    """
    cur_info is a list of the current location and character

    proposed_move is a list of the proposed next location for the
    current character before factoring in collision rules (to be
    applied here)

    mat is the matrix representing the puzzle maze

    identify if the row/col from char_info contain the "#" character,
    which means the charater needs to rotate 90 degrees before moving.

    identify if the next move is outside the range of the map.
    
    """

    cur_info = cur[:]
    proposed_move = proposed[:]
    
    mat_dim = {"rows": len(mat),
               "cols": len(mat[0])}
    
    if (proposed_move[0] < 0 or
        proposed_move[1] < 0 or
        # offset for 0-based indexing:
        proposed_move[0] > (mat_dim["rows"] - 1) or
        proposed_move[1] > (mat_dim["cols"] - 1)):
        return "Done"
    else:
        next_char = mat[proposed_move[0]][proposed_move[1]]
        if next_char != "#":
            return proposed_move
        else:
            # apply rotation:
            cur_info[2] = rotate_char[cur_info[2]]
            # apply movement rule for new character recursively:
            return apply_next_move(cur_info, look_ahead(cur_info), mat)
    

# get the starting location:
location_info = get_start_index(lines)
visited_locations = [location_info]
end = ""
while end != "Done":
    location_info = apply_next_move(location_info, look_ahead(location_info), lines)
    # keep track of all the locations that 
    visited_locations.append(location_info)
    if location_info == "Done":
        end = "Done"


# Since the character potentially retraces it's steps, we need to plug
# in where the X's go, then count up all the X's:
traced_path = lines[:]
for location in visited_locations:
    if location != "Done":
        traced_path[location[0]][location[1]] = "X"



count = 0
for line in traced_path:
    for i in range(len(line)):
        if line[i] == "X":
            count += 1

print(count)            
