# Задание A

def min_max(lst):
    if lst == []:
        return 'ValueError'
    else:
        return min(lst), max(lst)
print(min_max([1.5,2, 2.0, -3.1]))

def unique_sorted(lst):
    lst = set(lst)
    return sorted(lst)
#print(unique_sorted((1, 2, 3, 2, 1)))

def flatten(lst):
    ans = []
    for i in lst:
        if type(i) != list:
            return 'TypeError'
        else:
            for j in i:
                ans.append(j)
    return ans
#print(flatten([[1, 2], (3, 4, 5)]))