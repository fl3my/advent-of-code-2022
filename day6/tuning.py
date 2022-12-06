def has_unique_chars(string):  
    
    # Use a set to reture all unique characters
    unique_char_count = len(set(string))
    string_length = len(string)

    if unique_char_count == string_length:
        return True
    return False
    

def get_start_of_packet_marker(signal, packet_length):

    start_index = 0

    # Loop in sections of 4
    for end_index in range(packet_length, len(signal)):

        signal_line_section = signal[start_index:end_index]

        # Return the last index position of the first unique section
        if has_unique_chars(signal_line_section):
            return end_index

        # Move the section up by one
        start_index += 1 

    return -1

def main():
    # Read signal line from file
    with open('input.txt') as f:
        signal = f.readline()
    
    # Get the packet position
    packet_pos = get_start_of_packet_marker(signal, 4)

    print("The start position is {0}.".format(str(packet_pos)))

if __name__ == "__main__":
    main()