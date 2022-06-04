import os
os.system('CLS')

# برنامه ای بنویسید که نام و نمره تعداد دانشجو را دریافت کرده
# نام و نمره شاگرد اول کلاس را چاپ نماید

count_of_students = int(input('> enter the count of students : '))
myDict = {}
for _ in range(count_of_students):
    name, glare = input('> ').split()
    myDict[name] = float(glare)

max_name = ''
max_glare = 0

for name, glare in myDict.items():
    if glare > max_glare:
        max_glare = glare
        max_name = name

print(f'Best Student Name Is : {max_name} and his Galre Is {max_glare}')
