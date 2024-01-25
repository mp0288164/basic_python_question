def list_reverse():
    input_list_size=int(input("please enter the size of list:-"))
    my_list=[]
    while (input_list_size>0):
        list_element=input("please enter the element:-")
        #append method for add element in list 
        my_list.append(list_element)
        #decrese list_size by one
        input_list_size=input_list_size-1
    #print list    
    print("list is:-",my_list)
    #reverse list by  list slicing method
    print("reverse list is:-",my_list[-1: :-1])
    #reverse list by list reversing method
    my_list.reverse()
    print("reverse list is:-",my_list)
list_reverse()
