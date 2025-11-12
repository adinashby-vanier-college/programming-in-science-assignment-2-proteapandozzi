# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
list1 = [ 10,66,9,66,5,87,67,66,66,100,5]
def max_two_in_list(numbers):

    ndup = [] #[10,20]
    for i in numbers:
        if i not in ndup:
            ndup.append(i)
    
    list1 = ndup

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
    
    




# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
    
    remove_duplicates = []
    for i in numbers:
        if i not in remove_duplicates:
            remove_duplicates.append(i)

    sorted_list = sorted(remove_duplicates)

    return sorted_list

    
# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    sum_list = 0
    new_list = []
    for i in arr:
        sum_list += i
        new_list.append(sum_list)      

    return new_list
#print(sum(list))
    



# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    return [[]]
# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.

lst = [1,2,3,4,5,6,7,8]
def slice_every_nth(lst, step):
    step_list = []
    j = 0

    for i in lst:
        if j % step == 0:
            step_list.append(i)
        j += 1

    return step_list
print(slice_every_nth(lst,2))
    
    
    
    
    
    
    
    


# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    return 0

# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    return [[0, 0], [0, 0]]