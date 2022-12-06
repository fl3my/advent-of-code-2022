# Remove new line and split into two lists
def clean_input_data(file_data):

    lines = file_data.split('\n')
    graph = lines[:lines.index('') - 1]

    # Remove the last item in the procedure as its whitespace
    procedure = lines[lines.index('') + 1:-1]

    return [graph, procedure]

# Return a list of all occurences of a character in a list
def find_indices(list, char_to_find):

    indices = []

    for idx, value in enumerate(list):
        if value ==  char_to_find:
            indices.append(idx)

    return indices

# Return a 2D array that contains nested lists that represent
# a stack.
def get_stacks(graph):

    # Get the postions of each column
    base_layer = graph[-1]
    col_position_list = find_indices(base_layer, '[')

    # Initiate an array for each column
    stacks = [[] for _ in range(len(col_position_list))]

    # Loop through each layer, bottom up
    for layer in reversed(graph):

        # Get the postions of all columns in layer
        columns_found = find_indices(layer, '[')

        # iterate over each found column postion
        for col in columns_found:

            col_position = col_position_list.index(col)
            col_letter = layer[col + 1]

            stacks[col_position].append(col_letter)

    return stacks

# move x amount of crates from one stack to another sequentially
def move_crates_one_by_one(stacks, count, last_pos, new_pos):

    last_pos -= 1
    new_pos -= 1

    new_stacks = stacks

    # Take off the old stack and add to the new stack
    for i in range(count):
        crate = new_stacks[last_pos].pop()
        new_stacks[new_pos].append(crate)

    return new_stacks

# Move crates in same order to another stack
def move_crates_bulk(stacks, count, last_pos, new_pos):

    last_pos -= 1
    new_pos -= 1

    new_stacks = stacks

    # Take off the old stack
    crates = new_stacks[last_pos][-count:]

    # Delete the last items on the stack
    del new_stacks[last_pos][-count:]

    # Add the items onto the new stack
    new_stacks[new_pos].extend(crates)

    return new_stacks

# print a string with top item in stack
def get_top_crates(stacks):

    top_stack_string = ""

    for stack in stacks:
        top_stack_string += stack[-1]

    return top_stack_string

# Parse the procedure string to a dictionary
def read_procedure(procedure_line):
    numbers = [int(x) for x in procedure_line.split() if x.isdigit()]
    procedure_dict = { 'count': numbers[0], 'last_pos': numbers[1], 'new_pos': numbers[2]}
    return procedure_dict

def main():
    # Read from the file
    with open('input.txt') as f:
        input = f.read()

    graph, procedures = clean_input_data(input)
    stacks = get_stacks(graph)

    # for each line in the procedure list
    for line in procedures:
        
        procedure = read_procedure(line)

        stacks = move_crates_bulk(stacks, procedure['count'], procedure['last_pos'], procedure['new_pos'])
        # stacks = move_crates_one_by_one(stacks, procedure['count'], procedure['last_pos'], procedure['new_pos'])


    print(get_top_crates(stacks))

if __name__ == "__main__":
    main()