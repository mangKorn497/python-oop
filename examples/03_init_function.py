"""
หัวข้อ: ฟังก์ชัน __init__() (The __init__() Function)
อ้างอิงแนวคิดจาก: https://www.w3schools.com/python/python_oop.asp

__init__() คือ constructor ที่ถูกเรียกอัตโนมัติทุกครั้งที่สร้างอ็อบเจกต์
ใช้กำหนดค่าเริ่มต้นให้กับ property ของอ็อบเจกต์แต่ละตัว
"""


class Robot:
    def __init__(self, name, power):
        self.name = name    # กำหนดชื่อให้อ็อบเจกต์แต่ละตัว
        self.power = power   # กำหนดพลังงานเฉพาะตัว


# ส่งค่าตอนสร้างอ็อบเจกต์ ค่าจะถูกส่งเข้า __init__()
r1 = Robot("Astro", 90)
r2 = Robot("Nova", 75)

print(f"{r1.name} มีพลังงาน {r1.power}")
print(f"{r2.name} มีพลังงาน {r2.power}")
