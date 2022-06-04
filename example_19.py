import os
os.system('CLS')

# برنامه ای بنویسید که یک عدد از کاربر دریافت کرده و آنرا در یک لیست مرتب شده درج نماید
# تابع insert

myList = [1, 5, 7, 8, 9, 12, 15, 25]
user_input = int(input('> '))

for i in range(len(myList)):
    if myList[i] >= user_input:
        myList.insert(i, user_input)
        break

print(myList)
