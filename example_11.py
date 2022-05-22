import os
os.system('CLS')

# برنامه ای بنویسید که عددی را در ورودی خوانده و به حروف تبدیل نماید

def numbersToWords(number):
    numbers=['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    return numbers[number]

number = input('> ')
print(numbersToWords(number))
