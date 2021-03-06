#says true if there are three consecutive words in a string

def checkio(words: str) -> bool:

    word = words
    array = list()
    res = False
    count = 0
    
    #todo el sig for se puede resumir en str.split()
    for i in range(len(words)):
        dif = len(words) - len(word)
        if words[i] == " ":
            array.append(word[:i-dif])
            word = words[i+1:]
        else:
            if i == len(words)-1:
                array.append(word[:i-dif+1])
                
    for elem in array:
        if elem.isalpha():
            count += 1
        else:
            count = 0
        if count == 3:
            res = True
            break
   
    return res
    
    
    
    
 #tests   
    
    

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))
    
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
