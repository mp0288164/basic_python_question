def myfunc(a1):
    max=a1[0]
    for i in range(1,len(a1)):
        if a1[i]>max:
            max=a1[i]
    return max

def myfunc1(a1):
    min=a1[0]
    for i in range(1,len(a1)):
        if a1[i] < min :
            min=a1[i]
    return min


arr=[76,942,233,876687,12,43345]
print(arr)
print("maximum or largest element in an array:-",myfunc(arr))
print('minimum or smallest element in an  array:-',myfunc1(arr))
