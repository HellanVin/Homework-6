
#Exercise 3
def remove_all_after(lst, n):
    list = []
    for i in lst:
        if i <= n:
            list.append(i)
        else:
            break
    return list


lst = [1, 1, 2, 2, 3, 3]
n = 2
answer = remove_all_after(lst, n)
if answer[-1] == answer[-2]:
    answer.pop(-1)
    print(answer)
else:
    print(answer)
