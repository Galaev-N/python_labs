# Задание A

def min_max(lst):
    if lst == []:
        return 'ValueError'
    else:
        return min(lst), max(lst)
#print(min_max([1.5,2, 2.0, -3.1]))

def unique_sorted(lst):
    lst = set(lst)
    return sorted(lst)
#print(unique_sorted((1, 2, 3, 2, 1)))

def flatten(lst):
    for k in lst:
        if isinstance(k, list) == 0 and isinstance(k, tuple) == 0:
            return 'TypeError'
    ans = []
    for i in lst:
        for j in i:
            ans.append(j)
    return ans
print(flatten([[1, 2], [], [3, 4, 5]]))