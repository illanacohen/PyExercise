
#ordena unatupla por valores absolutos:



def checkio(numbers_array: tuple) -> list:
    listArray = list(numbers_array)
    for i in range(len(listArray)):
        min = listArray[i]
        for j in range(i+1,len(listArray)):
            if abs(min) > abs(listArray[j]):     
                min = listArray[j]
                listArray[j] = listArray[i]
                listArray[i] = min    
        min = abs(numbers_array[0])
    return listArray



#tests:



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(list(checkio((-20, -5, 10, 15))))

    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)

    assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
