def ins_sort(lst: list):
    """insertion sort: takes one element out of the list
    and finds it correct place. Only works, because a area
    of the list is sorted. In this area, the programm
    finds the correct place for the element.
    Args:
        lst(list): the list to sort
    Returnes:
        list: the sorted list
    """

    try:
        for c in range(1, len(lst)):

            temp = lst[c]

            # Move elements of list, that are
            # bigger than temp, to one position ahead
            # of their current position
            j = c - 1
            while j >= 0 and temp < lst[j]:
                lst[j + 1] = lst[j]
                j -= 1
            # then fills the empty spot
            # with temp
            lst[j + 1] = temp

        return lst

    except TypeError:
        return None