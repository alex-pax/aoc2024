import re

# open() creates a TextIOWrapper object
# methods of TextIOWrapper are used to read data from the connection
file_con = open('09/input.txt')


cur_char = ""
data = []
while cur_char != "\n":
    # get one char at a time, will be useful later
    
    data.append(file_con.read(1))
    cur_char = data[-1]
    if cur_char == '\n':
        data.pop()
    else:
        data[-1] = int(data[-1])



# apply the "every-other" character represents number of file elements
# or empty memory elements.  None will represent empty, and file
# numbers will increment.
file_switch = True
file_counter = 0
data_struct = []
for i in range(len(data)):
    if file_switch:
        for j in range(data[i]):
            data_struct.append(file_counter)
        file_switch = False
        file_counter += 1
    else:
        for j in range(data[i]):
            data_struct.append(None)
        file_switch = True

        
# swap the last non-None element with the first None element and
# iterate until the last non-None element has a higher index than the
# first None element.
masked_list = []
# True if digit, False if None
for x in data_struct:
    if x == None:
        masked_list.append(False)
    else:
        masked_list.append(True)
        
index_overlapped_yet = False
while not index_overlapped_yet:
    first_none_index = masked_list.index(False)
    last_num_index = len(masked_list) -1 - masked_list[::-1].index(True)

    index_overlapped_yet = first_none_index > last_num_index
    if index_overlapped_yet:
        continue
    
    # pop and lock:
    data_struct.insert(first_none_index, data_struct.pop(last_num_index))
    data_struct.append(data_struct.pop(first_none_index + 1))
    
    # switch flags after swapping values:
    masked_list[first_none_index] = True
    masked_list[last_num_index] = False

    


check_sum = 0
for i in range(len(data_struct)):
    if data_struct[i] is None:
        continue
    else:
        check_sum += i * data_struct[i]

print(check_sum)
