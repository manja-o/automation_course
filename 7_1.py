numbers_list = [5, -12, 17, -18, 24, -32, 0, -3, -5, 6, 31]

# task_1.a - manual map function


def absolute_value_number(number):
    return abs(number)


def map_function(func, list_for_map):
    list_after_map = []
    for i in list_for_map:
        list_after_map.append(func(i))
    return list_after_map


print('list after map:', map_function(absolute_value_number, numbers_list))

# task_1.b - manual filter function


def if_positive_number(number):
    if number >= 0:
        return True
    else:
        return False


def filter_function(func, list_for_filtering):
    list_after_filtering = []
    for i in list_for_filtering:
        if func(i):
            list_after_filtering.append(i)
        else:
            continue
    return list_after_filtering


print('list after filter:', filter_function(if_positive_number, numbers_list))










