def myfunc():
    input_list=(input('enter the element for list with some space:-'))
    my_list=list(input_list.split())
    print("original list is:-",my_list)
    my_list.reverse()
    print("reverse list is:-",my_list)
myfunc()