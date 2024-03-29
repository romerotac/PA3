# PA3/Pos Tagging program
<p align = "center">
  <span>English</span> |
  <a href = "https://github.com/romerotac/PA3/tree/master/languages/Italian"> Italian </a>
</*>

Report Project:

The first part of the project makes use of the tagger.py program and 2 text files.
The program should be run like this:

python tagger.py pos-train.txt pos-test.txt > pos-test-with-tags.txt

Where pos-train.txt is the text file on which we train the model to recognize specific word|tag associations, and pos-test.txt is the text document containing the words without any tags. With the execution of the program will get a text file called pos-test-with-tags.txt to which results in a pos-test file but this time with the supposedly appropriate tag being associated.

Note --Rules--:
During this part of the program is being selected to use the first rule. There are a total of 5 rules which can be modified hard-coding inside the function rules. Each rule can increase or decrease the precision of the model.

Note --create_before_after:
This function is used to create a text file containing a table with the total of number of times (frequency distribution) where one tag is followed up by another, this can be useful when creating rules 

The second and last part of the project consists of evaluating the efficiency of the model created.
The program should run like this:

python scorer.py pos-test-with-tags.txt pos-test-key.txt > pos-tagging-report.txt

Where we use the previous text result and we compare with another text file but with the correct tag associated. With the execution of the program will get a new text file containing the total number of correct tag associated compared with the number of word, as well as, the percentage of accuracy and a table corresponding the number of correct and incorrect tag association for each tag in the text file

P.S By rules we mean all the solutions to make the program more accurate, thus can be based on the regex or the dependencies between tags

"***Example of the ouput files can be found in <a href = "https://github.com/romerotac/PA3/tree/master/file_report"> file_report <a> and under tag_with_rules you can find also the otuput example for the first part***"
