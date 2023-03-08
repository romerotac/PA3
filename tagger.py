from sys import argv
from nltk.tokenize import word_tokenize
import pandas as pd
import re

"""
Author: Christian Romero Taipe
Date: 3/8/2023
"""


"""
create_before_after is a function that is used to create 
a file that shows a bigram count for each tag (used to determine rules)
"""
def create_before_after(lines):
    for i in range(len(lines)):
        if i != 1:
            before_words = lines[i-1].split('/')
            after_words = lines[i].split('/')
            if (len(after_words) > 1) and (len(before_words) > 1):
                before = before.append({'Before':before_words[1],'After':after_words[1]}, ignore_index = True)

    tot_before = pd.crosstab(index= [before['Before'], before['After']], columns = 'count')
    
    f = open("before_after.txt", "w")
    f.write(tot_before)
    f.close()

def rule_0():

    entire_text = ""
    
    for w in lines_test:
        testo = ""
        words = w.split()
        for i in words:
            if i in pos_dic:
                new_d = df.loc[df['Word'] == i]
                count_type = new_d['Type'].value_counts().index
                testo = testo + i + "/" + count_type[0] + " "
            elif i == "[":
                testo = testo + i + " "
            elif i == "]":
                testo = testo + i
            else:
                testo = testo + i +  "/" + "NN " 
        entire_text = entire_text + testo + "\n"
    
    return entire_text


def rules(testo):

    # RULE1: check if it's numeric, then tag it CD
    def rule1(words, text):
        if (bool(re.match("[0-9]+",words[0])) == True):
            return text + words[0] + "/" + "CD" + " "
        return text + words[0] + "/" + words[1] + " "

    # RULE2: check if the sequence is all NN/PRP + all the VB then the following is a JJ (adjective)
    # NN NNP NNPS NNS PRP + VB + the targetted word predicted to be NN then is a JJ
    def rule2(words, testo_dic, text):
        if words[1] == 'NN':
            if ((bool(re.match("([NN])\w+",testo_dic[len(testo_dic)-3])) == True) or (testo_dic[len(testo_dic)-3] == 'PRP')) :
                if (bool(re.match("([VB])\w+",testo_dic[len(testo_dic)-2])) == True):
                    return text + words[0] + "/" + "JJ "
        return text + words[0] + "/" + words[1] + " "

    #RULE3: check when having NN tagged if the initial of the word has an upper case, if it has than it's a NNP
    def rule3(words, text):
        if words[1] == 'NN':
            if bool((re.match("([A-Z])\w+", words[0]))):
                return text + words[0] + "/" + "NNP "
        return text + words[0] + "/" + words[1] + " "

    #RULE4: if PRP or all NN check if the next word ends with -d -> if it does than the word tag is VBD
    def rule4(words,flag,text):
        if flag == True:
            # check if the word ends with -ed
            if bool(re.match("\w*ed\b", words[0]) == True):
                return False, text + words[0] + "/" + "VBD" + " "
            else:
                return False, text + words[0] + "/" +  words[1] + " "
        elif((bool(re.match("([NN])\w+",words[1])) == True) or (words[1] == 'PRP')) :
            return True, text + words[0] + "/" +  words[1] + " "                       

        return flag, text + words[0] + "/" +  words[1] + " "

    # RULE5: WDT check if the word is what, which, who, whoever  and is not at the begining of a sentece
    # check if starts with wh- and there is not a uppercase, if there is then is a WP 
    def rule5(words, text):
        if (words[0] == 'which') or (words[0] == 'what') or (words[0] == 'who') or (words[0] == 'whoever'):
            if bool((re.match("([A-Z])\w+", words[0]))):
                return text + words[0] + "/" + "WDT" + " "
        return text + words[0] + "/" + words[1] + " "     
    
    lines_test = testo.split("\n")
    testo_dic = []
    final_testo = ""
    flag = False
    for w in lines_test:
        change_testo = w.split()
        text = ""
        for i in range(len(change_testo)):
            words = change_testo[i].split('/')
            if len(words) > 1:
                testo_dic.append(words[1])
                if len(change_testo) > 2:
                    """ Choose your rule:"""
                    text = rule1(words,text)
                    #text = rule2(words, testo_dic,text)
                    #text = rule3(words, text)
                    #flag, text = rule4(words, flag, text)
                    #text = rule5(words, text)
                else:
                    text = text + words[0] + "/" + words[1] + " "
            else:
                text = text + words[0] + " "
    
        final_testo = final_testo + text + "\n"

    return final_testo


pos_train = argv[1] 
pos_test = argv[2]

pos_dic = {}

pd.set_option('display.max_row',None)

#dictionary of all the tag associated with the word based on the testset
df = pd.DataFrame.from_dict({
    'Word':[],
    'Type':[],
})

# panda dic to know what there is before the next word
before = pd.DataFrame.from_dict({
    'Before':[],
    'After' :[]
})

# creating pos_dic based on the pos-train.txt
train_file = open(pos_train, encoding = "utf8")
lines = train_file.read().split()

""" -- helping tool to create rules --"""
#create_before_after(lines)

for i in lines:
    words = i.split('/')
    if len(words) > 1:
        #used for words with two tags ex JJ|NN
        type = words[1].split('|')
        df = df.append({'Word': words[0], 'Type': type[0]}, ignore_index= True)
        if words[0] not in pos_dic:
            pos_dic[words[0]] = pos_dic.setdefault(words[0],[type[0]]) 

        elif words[1] not in pos_dic[words[0]]:
            pos_dic[words[0]].append(type[0])



test_file = open(pos_test, encoding = "utf8")
lines_test = test_file.read().split("\n")

testo = rule_0()

print(rules(testo))
