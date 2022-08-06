"""Sorts list of tuples by first element"""

def tuple_sort(lst: list):
    """sorts list of tuples by first element in tuple

    Args:
        lst(list): list to sort

    Returns:
        list: sorted list
    """

    new_ele = 0
    new_lis_len = len(lst)
    for ele in range(0, new_lis_len):
        for elem in range(0, new_lis_len-ele-1):
            if lst[elem][new_ele] > lst[elem + 1][new_ele]:
                new_tem = lst[elem]
                lst[elem]= lst[elem + 1]
                lst[elem + 1]= new_tem

    return lst
