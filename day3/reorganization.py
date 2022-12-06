
# Split an even string in half
def split_in_half(string):
    return string[:len(string)//2], string[len(string)//2:]

# Find the common letter in two strings
def get_common_letter(string_1, string_2):
    for letter in string_1:
        if letter in string_2:
            return letter

def get_common_letter_group(strings):
    common = set.intersection(*map(set, strings))
    return str(list(common)[0])

def get_prority_value(letter):
    ascii_value = ord(letter)

    if (ascii_value > 96):
        # is lowercase
        return ascii_value - 96
    else:
        # is uppercase
        return ascii_value - 38

def sum_bag_priority():
    priority_sum = 0

    with open('input.txt') as f:
        for line in f:
            compartment_1, compartment_2 = split_in_half(line)
            common_item = get_common_letter(compartment_1, compartment_2)
            priority_sum += get_prority_value(common_item)    
    
    return priority_sum

def sum_badge_priority():
    priority_sum = 0
    group = []
    with open('input.txt') as f:
        for line in f:
            
            group.append(line.strip())

            # Create a group every three lines
            if (len(group) == 3):
                common_item = get_common_letter_group(group)
                priority_sum += get_prority_value(common_item) 
                group.clear()
    
    return priority_sum

def main():
    print(sum_badge_priority())
    #print(sum_bag_priority())
    
if __name__ == "__main__":
    main()