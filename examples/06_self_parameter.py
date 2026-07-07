"""
หัวข้อ: พารามิเตอร์ self (The self Parameter)
อ้างอิงแนวคิดจาก: https://www.w3schools.com/python/python_oop.asp

self คือตัวอ้างอิงถึงอ็อบเจกต์ปัจจุบัน ใช้เข้าถึง property และ method ของตัวเอง
self ต้องเป็นพารามิเตอร์ตัวแรกของทุก method แต่ตอนเรียกไม่ต้องส่งเอง
ชื่อ self เป็นเพียงธรรมเนียมนิยม จะตั้งชื่ออื่นก็ได้ (แต่ไม่แนะนำ)
"""


class Robot:
    def __init__(self, name):
        self.name = name

    # ใช้ชื่ออื่นแทน self ก็ทำงานได้ แต่เพื่อความชัดเจนควรใช้ self
    def whoami(this):
        print("ฉันคือ", this.name)


r1 = Robot("Astro")
r1.whoami()   # ไม่ต้องส่ง self เอง Python ส่งตัวอ็อบเจกต์ให้อัตโนมัติ
