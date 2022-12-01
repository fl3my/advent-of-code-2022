
elf_list = []

puzzleInput = open('input.txt', 'r')

total = 0

while True:
    line = puzzleInput.readline()

    # Loop until end of file
    if not line:
        break

    # Strip new line and add to running total
    if line != '\n':
        total += int(line.strip())
    else:
        elf_list.append(total)

        # Reset the total when a new line is reached
        total = 0

puzzleInput.close()

print("The top elf is carrying " + str(max(elf_list)) + " calories.")
print("The top 3 elves are carrying " + str(sum(sorted(elf_list)[-3:])))