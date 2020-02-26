#The function should recognise if a subject line is stressful.
#stresfull letters:
#all in uppercase
#ends by 3 exc
#contains 3 red words: help asap or urgent
     
   
def is_stressful(subj):
     
    newsubj = subj.lower()
    finalsubj = newsubj[0]
    alert = False

    #get rid of symbols and extra letter
    for i in range(len(newsubj)-1):
        if newsubj[i+1] != newsubj[i] and newsubj[i+1] != "." and newsubj[i+1] != "," and newsubj[i+1] != "!" and newsubj[i+1] != "-":
            finalsubj = finalsubj + newsubj[i+1]
            print(finalsubj)
               
    #see if red words happens in the new text
    if ("help" in finalsubj) or ("asap" in finalsubj) or ("urgent" in finalsubj):
            alert = True      
         
    #build new text with '!!!'
    for i in range(len(newsubj)-1):
        if newsubj[i+1] != "." and newsubj[i+1] != "," and newsubj[i+1] != "-":
            finalsubj = finalsubj + newsubj[i+1]
               
    #check !!! and capital
    if "!!!" in finalsubj[-3:]:
        alert = True
    if alert == False:
        alert = True
        for letter in subj:
            if letter.islower():
                alert = False
                
    return alert

if __name__ == '__main__':
    #These "asserts" are only for self-checking and not necessarily for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    assert is_stressful("ah!!!,") == True, "exclamation"
    assert is_stressful("HE.lP,") == True, "dot in it"
    assert is_stressful("HEEEeeelPPPP,") == True, "chaos"
    assert is_stressful("Heeeeeey!!! I’m having so much fun!”") == False, "so much fun ha"
    print('Done! Go Check it!')
