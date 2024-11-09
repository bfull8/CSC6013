def stringMatch(substring,text):
    for i in range(len(text) - len(substring) + 1):
        count = 0
        for j in range(len(substring)):
            if text[i + j] == substring[j]:
                count +=1
            if count == len(substring):
                print(i)




stringMatch("RIT",'ALGORITHM')
