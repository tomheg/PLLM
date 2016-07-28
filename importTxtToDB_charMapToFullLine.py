import sys
import unicodedata as ud
import codecs
import os
import re

print(sys.platform)

successCounter = 0
failureCounter = 0
grade = 0 

'''Choose source file'''

with open('emissions_shorter.txt',encoding="utf-8-sig") as f:
    for line in f:
        scriptline = f.readline()
        scriptline.rstrip('\r\n')
        '''print (scriptline + "END") '''

        if (scriptline == ""):
            break

        ''' assume anything above 500 is Chinese'''
        if (ord(scriptline[0]) < 500):   
            continue
        '''scriptline = ud.normalize('NFC', scriptline)'''

        scriptline = ud.normalize('NFC', scriptline)

        '''print all characters'''
        print(scriptline)
        lineLength=len(scriptline)-2  

        with open('tomsvocab.txt','a',encoding="utf-8-sig") as wf:

            for hanzi in range(0, lineLength ):
                '''print (scriptline[hanzi])'''
                wf.write(scriptline[hanzi] + '\t' + "shi" + '\t' + "(CP) " + scriptline )
            print ("done")    
            

                    
                    
            
        





     

