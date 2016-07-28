import sys
import unicodedata as ud
import codecs
import os
import re

from nltk.tree import sinica_parse
from nltk.tag import map_tag

from nltk.corpus.reader.util import *
from nltk.corpus.reader.api import *

print(sys.platform)
 

'''Choose source file'''

with open('Tom_kevin_convo_2.txt',encoding="utf-8-sig") as f:
    for line in f:
        scriptline = f.readline()
        scriptline.rstrip('\r\n')
        '''print (scriptline + "END") '''

        if (scriptline == ""):
            break
   	
    '''  To remove learner sentences: if scriptline contains "T:" string then continue'''
          
        scriptline = ud.normalize('NFC', scriptline)

        '''print all characters'''
        print(scriptline)
        lineLength=len(scriptline)-2  '''Remove CR and full stop '''

	''' tokenize'''
	''' map chars to words'''


	''' map words to clauses + author '''
	
	''' deal with duplicate two-char words'''

	''' tokenize'''

        with open('tomsvocab.txt','a',encoding="utf-8-sig") as wf:

	    
	    ''' write chars to words '''
	    ''' search for duplicate char-to-word mappings in this file '''
	    ''' Better to add new words to the top of the list so that they show up first (presumably)'''
	    ''' extract author name from filename: authorName = ''' 
	    ''' write words to clauses-author '''
	   	
            for hanzi in range(0, lineLength ):
                '''print (scriptline[hanzi])'''
                wf.write(scriptline[hanzi] + '\t' + "shi" + '\t' + "("+ authorName + ") " + scriptline )
            print ("done")

            

                   
                    
            
        





     

