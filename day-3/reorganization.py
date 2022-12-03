
# Split an even string in half
def split_in_half(string):
    return string[:len(string)//2], string[len(string)//2:]

# Find the common letter in two strings
def get_common_letter(string_1, string_2):
    for letter in string_1:
        if letter in string_2:
            return letter

def get_prority(letter):
    ascii_value = ord(letter)
    if (ascii_value > 96):
        # is lowercase
        return ascii_value - 96
    else:
        # is uppercase
        return ascii_value - 38

def main():
    priority_sum = 0
    with open('input.txt') as f:
        for line in f:
            bag_1, bag_2 = split_in_half(line)
            common_item = get_common_letter(bag_1, bag_2)
            priority_sum += get_prority(common_item)
    
    print(priority_sum)

if __name__ == "__main__":
    main()