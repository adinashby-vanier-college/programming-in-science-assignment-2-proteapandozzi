list1 = [1,16,7,4,21]

def max_val(list1):
    
    if len(list1) == 0:
        return (None, None)
    elif len(list1) == 1:
        return (list1[0], None)
    
    if list1[0] > list1[1]:
        max_value = list1[0] 
        second_max = list1[1]
    else:
        second_max = list1[0]
        max_value = list1[1]

    for i in list1[2:]:
        if i > max_value:
            second_max = max_value
            max_value = i
        elif i > second_max:
            second_max = i
    


    return (max_value, second_max)

#print(max_val(list1))

list = [1,2,3]

def sum(list):
    sum_list = 0
    new_list = []
    for i in list:
        sum_list += i
        new_list.append(sum_list)      

    return new_list
print(sum(list))

