# Python OOP — ตัวอย่างการเขียนโปรแกรมเชิงวัตถุด้วย Python

โปรเจกต์นี้รวบรวมตัวอย่างโค้ด **Object-Oriented Programming (OOP)** ในภาษา Python
โดยเรียบเรียงและเขียนโค้ดขึ้นใหม่เอง อ้างอิงหัวข้อ/แนวคิดจากบทเรียนของ W3Schools:

- Python Classes/Objects — https://www.w3schools.com/python/python_oop.asp
- Python Inheritance — https://www.w3schools.com/python/python_inheritance.asp
- Python Polymorphism — https://www.w3schools.com/python/python_polymorphism.asp
- Python Iterators — https://www.w3schools.com/python/python_iterators.asp

> หมายเหตุ: โค้ดและคำอธิบายทั้งหมดในรีโพนี้เขียนขึ้นใหม่เพื่อการเรียนรู้
> เป็นเพียงการอ้างอิง "หัวข้อ/แนวคิด" จาก W3Schools ไม่ได้คัดลอกข้อความต้นฉบับ

## OOP คืออะไร?

OOP (การเขียนโปรแกรมเชิงวัตถุ) คือแนวคิดที่จัดกลุ่ม **ข้อมูล (property)** และ
**พฤติกรรม (method)** ไว้ด้วยกันในรูปของ "อ็อบเจกต์" ทำให้โค้ดเป็นระเบียบ
นำกลับมาใช้ซ้ำได้ และดูแลรักษาง่าย โดยมี **คลาส (class)** เป็นพิมพ์เขียว
สำหรับสร้าง **อ็อบเจกต์ (object)**

## โครงสร้างโปรเจกต์

```
python-oop/
├── README.md
└── examples/
    ├── 01_create_class.py             # การสร้างคลาส
    ├── 02_create_object.py            # การสร้างอ็อบเจกต์
    ├── 03_init_function.py            # ฟังก์ชัน __init__() (constructor)
    ├── 04_str_function.py             # ฟังก์ชัน __str__()
    ├── 05_object_methods.py           # เมธอดของอ็อบเจกต์
    ├── 06_self_parameter.py           # พารามิเตอร์ self
    ├── 07_modify_properties.py        # การแก้ไข property
    ├── 08_delete_properties_objects.py# การลบ property / อ็อบเจกต์
    ├── 09_pass_statement.py           # คำสั่ง pass ในคลาส
    ├── 10_inheritance.py              # การสืบทอด (เสริม)
    ├── 11_polymorphism.py             # พหุสัณฐาน (เสริม)
    └── 12_iterators.py                # อิเทอเรเตอร์ (เสริม)
```

## หัวข้อที่ครอบคลุม

| ไฟล์ | หัวข้อ | สรุปแนวคิด |
|------|--------|-----------|
| `01_create_class.py` | Create a Class | ใช้คีย์เวิร์ด `class` ประกาศคลาสซึ่งเป็นพิมพ์เขียวของอ็อบเจกต์ |
| `02_create_object.py` | Create Object | สร้างอ็อบเจกต์โดยเรียกใช้คลาสเหมือนฟังก์ชัน |
| `03_init_function.py` | `__init__()` | constructor ที่ถูกเรียกอัตโนมัติเพื่อกำหนดค่าเริ่มต้น |
| `04_str_function.py` | `__str__()` | กำหนดข้อความที่แสดงเมื่อ `print` อ็อบเจกต์ |
| `05_object_methods.py` | Object Methods | ฟังก์ชันภายในคลาสที่กำหนดพฤติกรรมของอ็อบเจกต์ |
| `06_self_parameter.py` | The self Parameter | ตัวอ้างอิงถึงอ็อบเจกต์ปัจจุบัน |
| `07_modify_properties.py` | Modify Properties | เปลี่ยนค่า property หลังสร้างอ็อบเจกต์ |
| `08_delete_properties_objects.py` | Delete Properties/Objects | ใช้ `del` ลบ property หรือลบอ็อบเจกต์ |
| `09_pass_statement.py` | The pass Statement | ใช้ `pass` เมื่อต้องการคลาสเปล่า |
| `10_inheritance.py` | Inheritance | คลาสลูกรับคุณสมบัติจากคลาสแม่ด้วย `super()` |
| `11_polymorphism.py` | Polymorphism | method ชื่อเดียวกันทำงานต่างกันในแต่ละคลาส |
| `12_iterators.py` | Iterators | อ็อบเจกต์ที่มี `__iter__()` และ `__next__()` |

## วิธีรัน

ต้องมี Python 3 ติดตั้งไว้ (แนะนำ 3.8 ขึ้นไป)

รันทีละไฟล์:

```bash
python3 examples/03_init_function.py
```

รันทุกไฟล์ในครั้งเดียว:

```bash
for f in examples/*.py; do echo "=== $f ==="; python3 "$f"; done
```

## จัดทำผ่าน VS Code

ทุกไฟล์ในโปรเจกต์นี้สร้างและจัดการผ่าน Visual Studio Code สามารถเปิดโฟลเดอร์
ทั้งโปรเจกต์ด้วยคำสั่ง:

```bash
code python-oop
```

แล้วกดปุ่ม ▶ (Run Python File) ที่มุมขวาบน หรือรันผ่าน Terminal ที่ฝังใน VS Code ได้เลย

## License

MIT
