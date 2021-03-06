#gives the first word over a string that can start with space comma and dots

def first_word(text: str) -> str:

    string = ""

    lista = list()

    text = text.replace(","," ")

    text = text.replace("."," ")

    for i in range(len(text)):

        if text[i] != " ":

            string += text[i]

        else:

            lista.append(string)

            string = ""

    for j in range(len(lista)):

        if lista[j] != "":

            string = lista[j]

            break

    return string



#tests



if __name__ == '__main__':

    print("Example:")

    print(first_word("Hello world"))

    

    # These "asserts" are used for self-checking and not for an auto-testing

    assert first_word("Hello world") == "Hello"

    assert first_word(" a word ") == "a"

    assert first_word("don't touch it") == "don't"

    assert first_word("greetings, friends") == "greetings"

    assert first_word("... and so on ...") == "and"

    assert first_word("hi") == "hi"

    assert first_word("Hello.World") == "Hello"

    print("Coding complete? Click 'Check' to earn cool rewards!")

