# Задание B
def transpose(lst):
    m = 0 # счетчик кол-ва столбцов
    ans = []
    for i in lst:
        m = max(m, len(i))
    for j in range(m):
        a =[]
        for k in lst:
            a.append(k[j])
        ans.append(a)
    return ans
#print(transpose([[1, 2, 5], [3, 4]]))

def row_sums(lst):
    ans = []
    m = len(lst)
    for j in range(m):
        ans.append(sum(lst[j]))
    return ans
#print(row_sums([[1, 2, 3], [4, 5, 6]]))

def col_sums(lst):
    ans = []
    new_lst = transpose(lst)
    return(row_sums(new_lst))
#print(col_sums([[-1, 1], [10, -10]]))