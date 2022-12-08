from collections import defaultdict


def get_stripped_lines(filename):
    # Read the file, stip and return as a list
    lines = []
    with open(filename) as f:
        for line in f:
            if line != "$ ls\n":
                lines.append(line.strip())
    return lines


def convert_to_dir_dict(lines):

    size_dict = defaultdict(int)
    current_directory = []

    for line in lines:
        line = line.split(" ")
        if line[1] == "cd":
            string_after_cd = line[2]
            if string_after_cd == "..":
                # Go up a directory
                current_directory.pop()
            else:
                # Set the current directory
                current_directory.append(string_after_cd)
        else:
            # Add the filename and filesize to the dictionary
            file_size = line[0]
            if file_size.isdigit():
                file_size = int(file_size)

                # Get the total sum on the current directory
                for i in range(len(current_directory)):
                    size_dict['/'.join(current_directory[:i+1])] += file_size

    return size_dict


def sum_of_directories(directory, max_size):
    total_sum = 0
    for key, value in directory.items():
        if value <= max_size:
            total_sum += value
    return total_sum


def main():
    lines = get_stripped_lines('input.txt')
    directory = convert_to_dir_dict(lines)
    print(sum_of_directories(directory, 100000))

    free = 70000000 - directory['/']
    need = 30000000 - free

    for size in sorted(directory.values()):
        if size >= need:
            print(size)
            break


if __name__ == "__main__":
    main()
