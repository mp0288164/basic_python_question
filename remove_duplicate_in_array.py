def myfunc(a1):
    a2=[]
    for i in a1:
        if i not in a2 :
            a2.append(i)
    return a2 
arr=[1,4,45,7,7,9,0,9,5,4,56,9,4,67,9,67,98,4,]
print(arr)
print("array:-",myfunc(arr))