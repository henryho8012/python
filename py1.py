def qsort(alist):
    print(alist)
    if len(alist)<=1:
        return(alist)
    else:
        pivot = alist[0]
        return qsort([x for x in alist[1:] if x<pivot]) + [pivot] + qsort([x for x in alist[1:] if x>=pivot])


test =['z','b','c','a']
print(qsort(test))