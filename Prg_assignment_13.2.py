"Paul Yang M06 Prg Assignment 13.2"
"This program will read the text file today.txt into the string today_string"

read = open('today.txt','r')
texts = read.readlines()
read.close()
print(len(texts), 'text read')

for text in texts:
    print(text, end='')