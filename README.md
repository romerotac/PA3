# PA3
Report Project:

The first part of the project make use of tagger.py program and 2 text file.
The programm should be run like this:

python tagger.py pos-train.txt pos-test.txt > pos-test-with-tags.txt

Where pos-train.txt is the text file on which we train the model to recognize specifc word|tag associations, and pos-test.txt is the text document containing the words without any tags. when running the program it will output a text file  called pos-test-with-tags.txt to which results in pos-test file but this time with the supposedly apporprite tag been associated.

Note --Rules--:
During this part of the program is being selected to use the first rule. There is a total of 5 rules which can be modified hard-coding inside the function rules. Each rule can increase or decrese the precision of the model.

Note --create_before_after:
This function is used to create a table with the total of number of times where one tag is followed up by another, this can be usufull when creating rules 

the second and last part of the project consist on evaluating the efficiency of the model created.
The program should run like this:

python scorer.py pos-test-with-tags.txt pos-test-key.txt > pos-tagging-report.txt

Where we use the prevously text result and we compare with another text file but with the correct tag associated. When running the program will compare each word with the tag associated, and will give as a result a message with the total of correct tag associated compared with the number of word, as well as, the percentage of accuracy and a table corresponding the number of correct and incorrect tag association for each tag in the text file

P.S By rules we mean all the solutions to make the program more accurate, thus can be based on the regex or the dependecies between tags
