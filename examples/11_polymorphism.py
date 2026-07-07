"""
หัวข้อ (เสริม): พหุสัณฐาน (Polymorphism)
อ้างอิงแนวคิดจาก: https://www.w3schools.com/python/python_polymorphism.asp

พหุสัณฐานหมายถึง "รูปแบบหลากหลาย" คลาสต่างกันสามารถมี method ชื่อเดียวกัน
แต่ทำงานต่างกันได้ เราจึงเรียก method เดิมกับอ็อบเจกต์หลายชนิดได้โดยไม่ต้องสนใจชนิด
"""


class Dog:
    def sound(self):
        return "โฮ่ง โฮ่ง"


class Cat:
    def sound(self):
        return "เมี้ยว"


class Cow:
    def sound(self):
        return "มอ~"


# วนเรียก method sound() เดียวกันกับอ็อบเจกต์ต่างชนิด
for animal in (Dog(), Cat(), Cow()):
    print(animal.sound())
