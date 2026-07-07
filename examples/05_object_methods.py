"""
หัวข้อ: เมธอดของอ็อบเจกต์ (Object Methods)
อ้างอิงแนวคิดจาก: https://www.w3schools.com/python/python_oop.asp

method คือฟังก์ชันที่อยู่ภายในคลาส ใช้กำหนด "พฤติกรรม" ของอ็อบเจกต์
เรียกใช้ผ่านตัวอ็อบเจกต์ด้วยรูปแบบ object.method()
"""


class Robot:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def greet(self):
        # method สามารถอ่านค่า property ของตัวเองผ่าน self ได้
        print(f"สวัสดี ฉันคือ {self.name} พลังงาน {self.power}")

    def work(self, hours):
        # method รับพารามิเตอร์เพิ่มเติมได้เหมือนฟังก์ชันทั่วไป
        self.power -= hours * 5
        print(f"{self.name} ทำงาน {hours} ชม. เหลือพลังงาน {self.power}")


r1 = Robot("Astro", 90)
r1.greet()
r1.work(3)
