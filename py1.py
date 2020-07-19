#TODO #1@henryho8012
def qsort(alist):
    print(alist)
    if len(alist)<=1:
        return(alist)
    else:
        pivot = alist[0]
        return qsort([x for x in alist[1:] if x<pivot]) + \
                [pivot] + qsort([x for x in alist[1:] if x>=pivot])

alist = [1,6,6,3,6,2,5,3,6]
print(qsort(alist))
