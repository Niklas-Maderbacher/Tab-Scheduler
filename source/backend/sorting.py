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
        for element in range(1, len(lst)):

            temp = lst[element]

            # Move elements of list, that are
            # bigger than temp, to one position ahead
            # of their current position
            element_before = element - 1
            while element_before >= 0 and temp < lst[element_before]:
                lst[element_before + 1] = lst[element_before]
                element_before -= 1
            # then fills the empty spot
            # with temp
            lst[element_before + 1] = temp

        return lst

    except TypeError:
        return None
