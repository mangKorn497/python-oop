"""
หัวข้อ (เสริม): การสืบทอด (Inheritance)
อ้างอิงแนวคิดจาก: https://www.w3schools.com/python/python_inheritance.asp

การสืบทอดช่วยให้คลาสลูก (child) รับ property และ method จากคลาสแม่ (parent) มาใช้ต่อ
ใช้ super() เพื่อเรียก constructor ของคลาสแม่ และ override method เพื่อปรับพฤติกรรม
"""


class Robot:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"ฉันคือหุ่นยนต์ชื่อ {self.name}")


# FlyingRobot สืบทอดจาก Robot
class FlyingRobot(Robot):
    def __init__(self, name, altitude):
        super().__init__(name)   # เรียก constructor ของคลาสแม่
        self.altitude = altitude

    # override เมธอด greet เพื่อเพิ่มความสามารถบิน
    def greet(self):
        super().greet()
        print(f"และฉันบินได้สูงถึง {self.altitude} เมตร")


f1 = FlyingRobot("Sky", 1200)
f1.greet()
