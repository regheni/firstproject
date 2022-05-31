def get_sorted_lists(list_of_numbers):
    data = []
    # create a list with all elements from line1 and line 2
    with open(list_of_numbers, "r") as f_content:
        for line in f_content:
            for char in line.split():
                char = char.strip(',][')
                if char.isdigit():
                    data.append(char)
    data.sort(key=int)
    return data