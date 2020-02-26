#gives the limit's higher prices over a list of dictionaries

def bigger_price(limit: int, data: list) -> list:
    array = list()
    count = 0
    maxVal = 0
    maxDicc = {}
    maxPos = 0
    while count != limit:
        for i in range(len(data)):
            dicc = data[i]
            if maxVal < dicc.get("price"):
                maxVal = dicc.get("price")
                maxDicc = dicc
                maxPos = i
        array.append(maxDicc)
        data.pop(maxPos)
        maxDicc = {}
        maxVal = 0
        count += 1        
            
    return array


if __name__ == '__main__':
    from pprint import pprint
    print('Example:')
    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

    # These "asserts" using for self-checking and not for auto-testing
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"

    print('Done! Looks like it is fine. Go and check it')
