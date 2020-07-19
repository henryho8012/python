def qsort1(alist):
    print(alist)
    if len(alist)<=1:
        return(alist)
    else:
        pivot = alist[0]
        return qsort1([x for x in alist[1:] if x<pivot]) + [pivot] + qsort1([x for x in alist[1:] if x>=pivot])

def qsort2(alist,l,u):
    print(alist)
    if l>=u:
        return (alist)
    
    m=l
    for i in range(l+1,u+1):
        if alist[i]<alist[l]:
            m +=1
            if i!=m:
                alist[i],alist[m] = alist[m],alist[i]
    
    alist[l],alist[m] = alist[m],alist[i]
    qsort2(alist,l,m-1)
    qsort2(alist,m+1,u)



test =[6,3,1,8,4,7,2]
#print(qsort1(test))
print(test)
print('')
print(qsort2(test,0,len(test)-1))