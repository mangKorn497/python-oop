"""
หัวข้อ: การแก้ไข property ของอ็อบเจกต์ (Modify Object Properties)
อ้างอิงแนวคิดจาก: https://www.w3schools.com/python/python_oop.asp

เราสามารถเปลี่ยนค่า property ของอ็อบเจกต์ได้โดยตรงหลังจากสร้างแล้ว
"""


class Robot:
    def __init__(self, name, power):
        self.name = name
        self.power = power


r1 = Robot("Astro", 90)
print("ก่อนแก้ไข:", r1.power)

# แก้ไขค่า property โดยตรง
r1.power = 50
print("หลังแก้ไข:", r1.power)
