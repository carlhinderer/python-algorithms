def unordered_sequential_search(a_list, item):
    for i in range(len(a_list)):
        if a_list[i] == item:
            return True

    return False


def ordered_sequential_search(a_list, item):
    for i in range(len(a_list)):
        if a_list[i] == item:
            return True
        elif a_list[i] > item:
            return False

    return False
