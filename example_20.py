import os
os.system('CLS')

# برنامه ای بنویسید که یک فایل متنی باز کرده و تعداد خط ها, کلمات و کارکتر های اون فایل رو مشخص کنه

myFile = open('myfile.txt', 'r').read()

lines = 0
words = 0
chars = 0

# 1nd algorithm
for myLine in myFile.split('\n'):
    lines += 1
    myLine = myLine.strip()
    for myWord in myLine.split():
        words += 1
        for char in myWord:
            chars += 1

# 2st algorithm
lines = len(myFile.split('\n'))
words = len(myFile.split())
chars = len(myFile.replace(' ', '').replace('\n', ''))


print(f'{lines} - {words} - {chars}')
