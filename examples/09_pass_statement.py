"""
หัวข้อ: คำสั่ง pass ในคลาส (The pass Statement)
อ้างอิงแนวคิดจาก: https://www.w3schools.com/python/python_oop.asp

นิยามคลาสไม่สามารถเว้นว่างได้ หากต้องการคลาสเปล่า ๆ ไว้ก่อน
ให้ใส่คำสั่ง `pass` เพื่อไม่ให้เกิดข้อผิดพลาด
"""


class Placeholder:
    pass


# สร้างอ็อบเจกต์จากคลาสเปล่าได้ตามปกติ แล้วค่อยเพิ่ม property ทีหลัง
obj = Placeholder()
obj.note = "เดี๋ยวมาเติมรายละเอียดภายหลัง"
print(obj.note)
