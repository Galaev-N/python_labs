# Задание B


def transpose(lst):
    if lst == []:
        return []
    count_table = len(lst[0])
    for k in lst:
        if len(k) != count_table:
            return "ValueError"
    ans = []
    m = len(lst[0])
    for j in range(m):
        a = []
        for k in lst:
            a.append(k[j])
        ans.append(a)
    return ans


# print(transpose([[1, 2], [3,4]]))


def row_sums(lst):
    ans = []
    count_table = len(lst[0])
    for k in lst:
        if len(k) != count_table:
            return "ValueError"
    m = len(lst)
    for j in lst:
        ans.append(sum(j))
    return ans


print(row_sums([[1, 2, 3], [4, 5, 6]]))


def col_sums(lst):
    ans = []
    count_table = len(lst[0])
    for k in lst:
        if len(k) != count_table:
            return "ValueError"
    new_lst = transpose(lst)
    return row_sums(new_lst)


# print(col_sums([[1, 2, 3], [4, 5, 6]]))
