import sys
import unicodedata as ud
import codecs

print(sys.platform)
successCounter = 0
failureCounter = 0
grade = 0 

with open('emissions_shorter.txt',encoding="utf-8-sig") as f:
    for line in f:
        scriptline = f.readline()
        scriptline.rstrip('\r\n')
        '''print (scriptline + "END") '''
        if (ord(scriptline[0]) < 500):   
            continue
        '''scriptline = ud.normalize('NFC', scriptline)'''

        inputline = input("Please type what you hear: ")
        inputline.rstrip('\r\n')
        inputline = inputline + '\n'

        scriptline = ud.normalize('NFC', scriptline)
        inputline = ud.normalize('NFC', inputline)

        if(inputline == scriptline):
            print("This sentence is correct!")
            successCounter +=1
        else:
            print ("Incorrect.. check the differences below:")
            print (scriptline)
            print ("Length of the string: ", len(scriptline))
            print (inputline)
            print ("Length of the string: ", len(inputline))
            failureCounter += 1
            
print("Correct sentences:", successCounter)
print("INcorrect sentences:", failureCounter)
grade = successCounter / (successCounter+failureCounter) *100                 

print("Your grade:", grade, "%")






     

