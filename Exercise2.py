def index_power(lst, n):
    if n >= len(lst):
        return -1
    else:
        answer = lst[n]**n
        return answer


lst = [1, 2, 3, 4]
n = 2
num = index_power(lst, n)
print(num)
