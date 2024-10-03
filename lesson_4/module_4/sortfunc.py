def bubble_sort(ls):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i+1]:
                ls[i], ls[i+1] = ls[i+1], ls[i]
                swapped = True
    return ls


def selection_sort(ls):
    for i in range(len(ls)):
        lowist = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[lowist]:
                lowist = j
        if lowist > i:
            ls[i], ls[lowist] = ls[lowist], ls[i]
    return ls

def insertion_sort(ls):
    for i in range(1, len(ls)):
        key = ls[i]
        j = i - 1
        while ls[j] > key and j >= 0:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = key
    return ls
