def remove_frequent_element(list,k):

    size_of_list=len(list)

    record_dict={}

    temp=0
    for i in range(0,size_of_list-1):
        
        list_element=list[i]
        for j in range(1,size_of_list):

            if i!=j and list[i]==list[j]:
                
                temp=temp+1+1

        if k>temp:
            temp=0
        record_dict[list_element]=temp
        temp=0


    max_value=max(record_dict.keys())

    for i in range(0,size_of_list):

        if max_value == list[i]:
            list.remove(max_value)
    
    return list


k=int(input('Enter k:'))

size_of_list=int(input("input list's size:"))

list=[]
for i in range (0,size_of_list):
    element=int(input("enter list element: "))
    list.append(element)

print("list before removing k most frequently occuring element")
print(list)
remove_frequent_element(list,k)
print(list)

