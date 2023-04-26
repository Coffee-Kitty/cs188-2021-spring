
def quickSort(lis):
    if len(lis) <= 1:
        return  lis
    
    smaller = [x for x in lis[1:] if x < lis[0]]
    bigger = [x for x in lis[1:] if x >= lis[0]]
    return quickSort(smaller) + [lis[0]] + quickSort(bigger)



if __name__ == '__main__':
    lst = [2, 4, 5, 1]
    print(quickSort(lst))
