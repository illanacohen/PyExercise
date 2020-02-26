#gives back the times a word apears in a text
#does not make diference with capital letters


def popular_words(text: str, words: list) -> dict:

    dicc = {}
    leveledText = text.lower()
    listText = leveledText.split()
    
    for key in words:
        dicc[key] = 0
        
    for word in words:
        word = word.lower() 
        
    for n in words:
        for m in listText:
            if n == m:
                dicc[n] = dicc.get(n) + 1     
      
    return dicc


#tests



if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
