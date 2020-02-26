#gives back the word in between two symbols

def between_markers(text: str, begin: str, end: str) -> str:
    word = ""
    for i in range(len(text)):
        if text[i] == begin:
            for j in range(i,len(text)):
                if text[j] == end:
                    word = text[i+1:j]                
    return word


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')
