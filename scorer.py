from sys import argv
import re
import pandas as pd
pos_test_result = argv[1]
pos_test_key = argv[2]

test_result_file = open(pos_test_result, encoding= "utf16")
test_key_file = open(pos_test_key, encoding="utf8")

word_test_result = test_result_file.read().split()
word_key_result = test_key_file.read().split()

# actual =  the total number of word that have been used
# predicted = the number that it was correct

pd.set_option('display.max_row',None)
df = pd.DataFrame.from_dict({
    'perd_Tag':[],
    'actual_Tag':[],
    'prediction':[],
})

tot_comp = 0
correct = 0

for i in range(len(word_test_result)):
    if ((bool(re.match("\[",str(word_key_result[i])))) != True):
        if ((bool(re.match("\]",str(word_key_result[i])))) != True):
            tot_comp += 1
            w2 = word_key_result[i].split("/")
            #used for words with two tags ex JJ|NN
            type = w2[1].split("|")
            w1 = word_test_result[i].split("/")

            try:
                if w1[1] == type[0]:
                    df = df.append({'perd_Tag': w1[1],'actual_Tag': type[0], 'prediction': 'correct'}, ignore_index = True)
                    correct += 1
                else:
                    df = df.append({'perd_Tag': w1[1],'actual_Tag': type[0], 'prediction': 'incorrect'}, ignore_index = True)
            except:
                print("error in " + str(i))
                print(w1)
                print(w2)
                break
prob = (correct/tot_comp) * 100

count_prediction = pd.crosstab(index= [df['actual_Tag'],df['perd_Tag'], df['prediction']], columns= 'count' )
print("The total number of correct value was: " + str(correct))
print("The total number of words is: " + str(tot_comp))
print("The percetange of accuracy was: " + str(prob))
print(count_prediction)