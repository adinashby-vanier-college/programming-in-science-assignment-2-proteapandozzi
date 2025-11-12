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
#print(sum(list))

list2 = [1,16,7,4,21,45,14,20]

list3 = [2,5,1]
list4 = [10,1,3]

#Question 5 -> attempt #1
lst = [1,2,3,4,5,6,7,8]
def slice_every_nth(lst, step):
    step_list = []
    
    for i in lst:
        if lst[i] % step == 0: 
            step_list.append(i)

    return step_list
#print(slice_every_nth(lst, 2))

#Question 5 -> attempt #2

L = [[1,2], [4,5], [7,8]]
L2 = [[1, 2, 3], [4, 5, 6]]
def transpose(matrix):
    full_transposed = []
    rows = len(matrix)
    column = len(matrix[0])

    for i in range (column):
        mini_transpose = []
        for j in range(rows):
            mini_transpose.append(matrix[j][i])
        full_transposed.append(mini_transpose)
    
    return full_transposed
print(transpose(L2))