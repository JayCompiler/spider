# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 12:57:39 2018

@author: zhang_yu

"""
import re
def inputLexicon():
    lexicon=[]
    pos=[]
    with open('hujiang.txt',encoding = 'gb2312') as f1:#打开'weibo_train_data.txt'文件
        for line in f1:  
            tmp=re.split(' |\n',line)
            lexicon.append(str.lower(tmp[0]))
            pos.append(str.lower(tmp[1]))
#    lexicon=[k for k in lexicon if not sw.hasSpecialchar(k)  and not sw.hasNumbers(k)]  
    return lexicon,pos

lexicon,pos=inputLexicon()
file=open('word.txt','w')
for i in range(len(lexicon)):
#        print(result[i])
    file.write(lexicon[i])
    file.write('\n')
file.close()
file=open('pos.txt','w')
for i in range(len(pos)):
#        print(result[i])
    file.write(pos[i])
    file.write('\n')
file.close()

