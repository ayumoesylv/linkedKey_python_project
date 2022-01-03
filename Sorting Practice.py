# Bubble sort
def bubble_sort(lst):
    n = len(lst)
    while n > 0:
        for i in range(0, n - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        n -= 1

    return lst



# driver
list1 = [1, 3, 8, 2, 9, 2, 5, 6]
print(bubble_sort(list1))