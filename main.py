import random

def create_array():
    '''
    This function creates a sorted array containing 300 random integers between 1 and 1000.

    Returns:
    --------
    ar : List
    '''
    ar = []
    for i in range(300):
        a = random.randint(1,1000)
        ar.append(a)
    ar.sort()
    return ar

def Binary_search1(sor_arr, Low,High,searched_value):
    '''
    This function will perform the binary search algorith recursively.
    There is a condition first where we will check if the length of the searched part of the
    algorithm is bigger then 0. If it is not then that means that the searched number could not be 
    found in the arrray.
    The array is then cut in the middle, while checking if the value in the middle is equal to the searched value.
    if it is higher, then we will check in the right half of the array.
    If it is lower, then we will check in the lower half of the array.

    Parameters:
    -----------
    sor_arr: List
    The sorted array, to search in.
    Low: Integer
    The low part of the array.
    Hight: Integer
    The high part of the array.
    searched_value: Int
    our target search

    Returns:
    --------
    mid: Integer
    The index of the middle of the array.

    Binary_search1(sor_arr,mid+1,High, searched_value): Function
    The same function where we chose the right of the array.

    return Binary_search1(sor_arr,Low,mid-1, searched_value): Function
    The same function where we chose the left of the array.

    -1: float
    When our search range is 0. It means we did not find the searched value

    '''
    if High >= Low: 
        
        mid = (High + Low)//2

        if searched_value == sor_arr[mid]:
            return mid
        elif searched_value > sor_arr[mid]:
            return Binary_search1(sor_arr,mid+1,High, searched_value)
        elif searched_value < sor_arr[mid]:  
            return Binary_search1(sor_arr,Low,mid-1, searched_value)
    else:
        return -1

if __name__ == '__main__':
    sorted_array = create_array()
    searched = input("Input the value You want to search for: ")
    if searched.isdigit() and int(searched)<=1000:
        a = Binary_search1(sorted_array,0,len(sorted_array),int(searched))
        if a == -1:
            print("It is not present in the array!")
        else:
            print("its position is: ",a)
    else:
        print("Enter a number between 1 and 1000!")
    
    

