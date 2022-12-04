def clean_line(line):
    clean_line = line.split()
    sections = clean_line[0].split(',')
    return sections

def get_range_as_dict(string):
    range_min, range_max = string.split('-')
    return {"min": int(range_min),"max": int(range_max)}

def compare_range(dict_1, dict_2):
    if (dict_1["min"] >= dict_2["min"]):
        if(dict_1["max"] <= dict_2["max"]):
            return True
    return False

def compare_range_both_ways(dict_1, dict_2):
    compare_1 = compare_range(dict_1, dict_2)
    compare_2 = compare_range(dict_2, dict_1)
    if compare_1 or compare_2:
        return True
    return False

def does_fully_contain(line):
    range_str_1, range_str_2 = clean_line(line)
    range_1 = get_range_as_dict(range_str_1)
    range_2 = get_range_as_dict(range_str_2)
    fully_contain = compare_range_both_ways(range_1, range_2)
    return fully_contain


def main():
    fully_contains_count = 0
    with open('input.txt') as f:
        for line in f:
            if(does_fully_contain(line)): 
                fully_contains_count += 1

    print(fully_contains_count)
    
if __name__ == "__main__":
    main()


