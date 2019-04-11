

def max_list_iter(int_list):  # must use iteration not recursion
    if int_list is None:
        raise ValueError
    elif len(int_list) == 0:
        return None
    else:
        total = int_list[0]
        for i in int_list:
            if(i > total):
                total = i
        return total


def reverse_rec(int_list):   # must use recursion
    if int_list is None:
        raise ValueError
    elif len(int_list) == 0:
        return []
    else:
        return (reverse_rec(int_list[1:])) + int_list[0:1]


def bin_search(target, low, high, int_list):
    midpoint = (low + high) // 2
    if int_list == None:
        raise ValueError
    if(low > high):
        return None
    if int_list[midpoint] == target:
        return midpoint
    if target > int_list[midpoint]:
        return bin_search(target, midpoint + 1, high, int_list)
    if target < int_list[midpoint]:
        return bin_search(target, low, midpoint - 1, int_list)
