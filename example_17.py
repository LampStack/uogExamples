import os
os.system('CLS')

# برنامه ای بنویسید که لیستی از کاربر دریافت کرده و اعضای تکراری را با استفاده از متود پاپ حذف نماید

count_of_numbers = int(input('> enter the count of numbers : '))
myList = list()
for _ in range(count_of_numbers):
    myList.append(int(input('> ')))

# [1, 4, 3, 4, 5]
for i in range(len(myList)):
    j = i+1
    while j < len(myList):
        if myList[i] == myList[j]:
            myList.pop(j)
        else:
            j += 1
print(myList)
