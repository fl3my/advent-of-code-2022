loses_to = {
    "rock": {"scissors"},
    "paper": {"rock"},
    "scissors": {"paper"},
}

# Decrypt the input values
def decrypt(letter):
    if letter in ["A", "X"]: return "rock"
    elif letter in ["B","Y"]: return "paper"
    elif letter in ["C", "Z"]: return "scissors"

def getScore(choice):
    if choice == "rock": return 1
    elif choice == "paper": return 2
    elif choice == "scissors": return 3

def play(choice_1, choice_2):

    choice_1 = decrypt(choice_1)
    choice_2 = decrypt(choice_2)

    # Get the shapes default score
    score = getScore(choice_2)

    # Get the outcome score
    if choice_2 in loses_to[choice_1]:
        return score
    elif choice_1 in loses_to[choice_2]:
        score += 6
    else:
        score += 3

    return score

def main():
    puzzleInput = open('input.txt', 'r')

    total = 0

    while True:
        line = puzzleInput.readline()

        # Loop until end of file
        if not line:
            break

        line = line.split("\n")
        letters = line[0].split(" ")
        total += play(letters[0], letters[1])

    puzzleInput.close()

    print(total)

if __name__ == "__main__":
    main()
