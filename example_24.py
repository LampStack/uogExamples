import os
os.system('CLS')

# کلاسی برای دایره طراحی کنید که متود های زیر را داشته باشد
# محاسبه مساحت دایره
# محاسبه محیط دایره

class circle:
    r = 0
    def __init__(self, r):
        self.r = r
    def primeter(self):
        return 2 * 3.14 * self.r
    def area(self):
        return 3.14 * self.r * self.r



mtObject = circle(9.33)
area = mtObject.area()
print(area)
