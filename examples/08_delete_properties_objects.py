"""
หัวข้อ: การลบ property และการลบอ็อบเจกต์ (Delete Properties / Delete Objects)
อ้างอิงแนวคิดจาก: https://www.w3schools.com/python/python_oop.asp

ใช้คีย์เวิร์ด `del` เพื่อลบ property เฉพาะตัว หรือลบทั้งอ็อบเจกต์
หลังลบแล้ว หากพยายามเรียกใช้อีกจะเกิดข้อผิดพลาด
"""


class Robot:
    def __init__(self, name, power):
        self.name = name
        self.power = power


r1 = Robot("Astro", 90)

# ลบ property เฉพาะตัวออกจากอ็อบเจกต์
del r1.power
try:
    print(r1.power)
except AttributeError:
    print("property 'power' ถูกลบไปแล้ว")

# ลบทั้งอ็อบเจกต์
del r1
try:
    print(r1.name)
except NameError:
    print("อ็อบเจกต์ r1 ถูกลบไปแล้ว")
