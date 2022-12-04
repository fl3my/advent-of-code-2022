def clean_line(line):
    clean_line = line.split()
    sections = clean_line[0].split(',')
    return sections

def get_range_as_dict(string):
    range_min, range_max = string.split('-')
    return {"min": int(range_min),"max": int(range_max)}

def get_both_range_to_dict(line):
    range_str_1, range_str_2 = clean_line(line)
    range_1 = get_range_as_dict(range_str_1)
    range_2 = get_range_as_dict(range_str_2)
    return range_1, range_2
    
def compare_range(dict_to_fit, dict):
    if (dict_to_fit["min"] >= dict["min"]):
        if(dict_to_fit["max"] <= dict["max"]):
            return True
    return False

def compare_range_overlap(dict_to_check, dict):
    if(dict_to_check["max"] >= dict["min"]):
        return True
    return False

def does_range_overlap(dict_1, dict_2):
    compare_1 = compare_range_overlap(dict_1, dict_2)
    compare_2 = compare_range_overlap(dict_2, dict_1)
    if (compare_1 and compare_2):
        return True
    return False

def does_fully_contain(dict_1, dict_2):
    compare_1 = compare_range(dict_1, dict_2)
    compare_2 = compare_range(dict_2, dict_1)
    if compare_1 or compare_2:
        return True
    return False


def main():
    fully_contains_count = 0
    any_overlap_count = 0

    with open('input.txt') as f:
        for line in f:

            range_1, range_2 = get_both_range_to_dict(line)

            if(does_fully_contain(range_1, range_2)): 
                fully_contains_count += 1

            if(does_range_overlap(range_1, range_2)):
                any_overlap_count += 1

    print("Fully overlap: " + str(fully_contains_count))
    print("Any overlap: " + str(any_overlap_count))

if __name__ == "__main__":
    main()


