"""
หัวข้อ: การสร้างคลาส (Create a Class)
อ้างอิงแนวคิดจาก: https://www.w3schools.com/python/python_oop.asp

คลาส (class) เปรียบเสมือนพิมพ์เขียว (blueprint) สำหรับสร้างอ็อบเจกต์
ใช้คีย์เวิร์ด `class` ในการประกาศ ภายในคลาสสามารถมี property และ method ได้
"""


class Robot:
    # property ระดับคลาส (class attribute) ทุกอ็อบเจกต์ใช้ค่าร่วมกัน
    power = 100


# เข้าถึง property ของคลาสได้โดยตรงผ่านชื่อคลาส
print("พลังงานเริ่มต้นของหุ่นยนต์:", Robot.power)
