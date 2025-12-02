if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    ar = list(arr)
    ar = list(set(ar))
    m = max(ar)
    ar.remove(m)
    l = []
    for i in range(len(ar)):
        l.append(m-ar[i])
    least_dif = min(l)
    for i in range(len(l)):
        if(l[i] == least_dif):
            print (ar[i])



# OR -------------------------------------


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr = list(set(arr))       # remove duplicates
    arr.sort()                 # sort ascending
    
    print(arr[-2])             # second largest
