"""
หัวข้อ: ฟังก์ชัน __str__() (The __str__() Function)
อ้างอิงแนวคิดจาก: https://www.w3schools.com/python/python_oop.asp

__str__() ควบคุมว่าเมื่อ print อ็อบเจกต์แล้วจะแสดงข้อความอะไร
ถ้าไม่กำหนด __str__() การ print จะได้ข้อความแบบ <__main__.Robot object at 0x...>
"""


class Robot:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __str__(self):
        return f"Robot(name={self.name}, power={self.power})"


r1 = Robot("Astro", 90)

# เมื่อ print อ็อบเจกต์ Python จะเรียก __str__() ให้เอง
print(r1)
