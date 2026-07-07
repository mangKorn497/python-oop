"""
หัวข้อ (เสริม): อิเทอเรเตอร์ (Iterators)
อ้างอิงแนวคิดจาก: https://www.w3schools.com/python/python_iterators.asp

อ็อบเจกต์ที่เป็น iterator ต้องมี method __iter__() และ __next__()
__iter__() คืนค่าตัว iterator เอง ส่วน __next__() คืนค่าถัดไปทีละตัว
เมื่อหมดค่าให้ raise StopIteration เพื่อจบการวนลูป
"""


class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


# ใช้ใน for loop ได้เพราะเป็น iterator
for n in Countdown(5):
    print(n)
