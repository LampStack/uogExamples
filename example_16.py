import os
os.system('CLS')


# ۱۳۹۸ لامپ خاموش داریم؛
# مدار لامپ ها به گونه ای طراحی شده که با روشن یا خاموش کردن یک لامپ، لامپ های مضارب اون لامپ هم تغییر وضعیت میدن!

# اگر وضعیت تمامی لامپ هارا به ترتیب از ۱ تا ۱۳۹۸ تغییر بدیم، در پایان عملیات چند لامپ روشن باقی میمونه ؟!


def ChangeStatus(n):
    for i in range(n, 1399, n):
        Lamps[i] = not Lamps[i]

Lamps = [False] * 1399
for i in range(1, 1399):
    ChangeStatus(i)

counter = 0
for i in range(1, 1399):
    if Lamps[i]:
        counter += 1
print(counter) # 37
