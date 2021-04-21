def ArrayChunk(M: list) -> int:    N = M[len(M) // 2]    N_index = len(M) // 2    i1 = 0    i2 = len(M) - 1    while True:        if M[i1] < N:            i1 += 1        if M[i2] > N:            i2 -= 1        if i1 == i2 - 1 and M[i1] > M[i2]:            inter_el = M[i1]            M[i1] = M[i2]            M[i2] = inter_el            N = M[len(M) // 2]            N_index = len(M) // 2            i1 = 0            i2 = len(M) - 1            continue        if i1 == i2 or i1 == i2 - 1 and M[i1] < M[i2]:            return N_index        if M[i1] >= N and M[i2] <= N:            if M[i1] == N:                N_index = i2            if M[i2] == N:                N_index = i1            inter_el = M[i1]            M[i1] = M[i2]            M[i2] = inter_eldef QuickSort(array: list, left: int, right: int):    if len(array[left:right]) < 2:        return None    arr = array[left:right + 1]    index = ArrayChunk(arr)    array[left:right + 1] = arr    QuickSort(array, left, left + index)    QuickSort(array, left + index, right)def QuickSortTailOptimization(array: list, left: int, right: int):    if len(array[left:right]) < 2:        return None    arr = array[left:right + 1]    index = ArrayChunk(arr)    array[left:right + 1] = arr    QuickSort(array, left, left + index)    QuickSort(array, left + index, right)def KthOrderStatisticsStep(Array: list, L: int, R: int, k: int) -> list:    arr = Array[L:R + 1]    i = ArrayChunk(arr) + L    Array[L:R + 1] = arr    if i == k:        return [i, i]    if i > k:        return [L, i - 1]    if i < k:        return [i + 1, R]def split(input_list):    """    Splits a list into two pieces    :param input_list: list    :return: left and right lists (list, list)    """    input_list_len = len(input_list)    midpoint = input_list_len // 2    return input_list[:midpoint], input_list[midpoint:]def merge_sorted_lists(list_left, list_right):    # Особый случай: один или два списка пусты    if len(list_left) == 0:        return list_right    elif len(list_right) == 0:        return list_left    index_left = index_right = 0    list_merged = []  # list to build and return    list_len_target = len(list_left) + len(list_right)    while len(list_merged) < list_len_target:        if list_left[index_left] <= list_right[index_right]:            # Значение левого списка меньше            list_merged.append(list_left[index_left])            index_left += 1        else:            # Значение правого списка меньше            list_merged.append(list_right[index_right])            index_right += 1        # Проверяем на конец списка        if index_right == len(list_right):            # Достигнут конец справа            list_merged += list_left[index_left:]            break        elif index_left == len(list_left):            # Достигнут конец слева            list_merged += list_right[index_right:]            break    return list_mergeddef MergeSort(array: list):    if len(array) <= 1:        return array    else:        left, right = split(array)        # Следующая строка является наиболее важной        return merge_sorted_lists(MergeSort(left), MergeSort(right))if __name__ == '__main__':    l = MergeSort([9,2,5,7,8,2,5,9,4,7])    print(l)