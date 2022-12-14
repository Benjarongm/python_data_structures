# -*- coding: utf-8 -*-
"""Python Data Structures.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1K9ZVOXKPtuCwyIRoOzIKNkzyWbmKaDoR
"""

print('hello')

print("Hello")

print('Hello word')

print("Hello World")

print('Hello_python')

print("Hello_python")

print("Merry X'mas")

print('Merry X\'mas')

print('I want to ask you "Why don\'t you drive to work ?"')

print("I want to ask you \"Why don't you drive to work ?\"")

print('"I don\'t have a car\"')

print("\"I don 't have a car\"")

print("You got a new job !? That's so exciting !")

print('You got a new job !? That\'s so exciting')

print('สวัสดีวันจันทร์')

print("สวัสดีวันจันทร์")

print('ความแตกต่างระหว่างคนเก่งกับคนไม่เก่ง คือ "การใช้เวลาว่างให้เป็นประโยชน์"')

print("ความแตกต่างกับคนเก่งกับคนไม่เก่ง คือ การใช้เวลาว่างให้เป็นประโยชน์")

print('/\\/\\/\\')

print("/\\/\\/\\")

print('''a
an
ant''')

print("""a
an
ant""")

print('''\t*
*\t*\t*
\t*''')

print("""\t*
*\t*\t*
\t*""")

print('''*\t+\t*
+\t*\t+
*\t+\t*''')

print("""*\t+\t*
+\t*\t+
*\t+\t*""")

print("""Just because something
thinks differently from you,
does that mean it's not thinking ?""")

print('''Just becauhse somthing
thinks differently from you,
does that mean it's not thinking ?''')

print('''\\\t\t/
\tx
/\t\t\\''')

print("""\\\t\t/
\tx
/\t\t\\""")

"""# Print Numeric"""

print(25)

print('%d' %25)

print('%f' %100)

print('%.6f' %100)

from math import pi
print('%.15f' %pi)

import math
print('%.15f' %math.pi)

a = 2
print(a)

a = 12.5
print('%.1f' %a)

"""# Print String+Numeric"""

a = 2
b = 3
print(a,'x',b,'=',a*b)

a = 2
b = 3
print('%d x %d = %d' %(a,b, a*b))

a = 2
b = 3
c = 5
print('%d*(%d + %d) = %d*%d + %d*%d' %(a,b,c,a,b,a,c))

a = 2
b = 3
c = 5
print("%d*(%d+%d) = %d*%d + %d*%d" %(a,b,c,a,b,a,c))

a = 2.4
b = 2.5
print('%.1f + %.1f = %.4f' %(a,b, a+b))

a = 2.4
b = 2.5
print("%.1f + %.1f = %.4f" %(a,b,a+b))

a = 5
b = 2
print('%.1f - %.2f = %.4f' %(a,b,a-b))

a = 5
b = 2
print('%.1f - %.2f = %.4f' %(a,b,a-b))

a = 5
b = 2
print("%.1f - %.2f = %.4f" %(a,b, a-b))

birthday = 25
print('ฉันเกิดวันที่', birthday, 'ธันวาคม')

birthday = 25
print("ฉันเกิดวันที่",birthday, "ธันวาคม")

a = 5
b = 100
print('%d เท่าของ %d มีค่าเท่ากับ %d' %(a, b, a*b))

a = 3.5
print('เขามีเงินเยอะกว่าฉัน %.2f บาท' %a)

a = 3.5
print("เขามีเงินเยอะกว่าฉัน %.2f บาท" %a)

a = 5
print('ฉันมีกำไร',a,'%')

a = 5
print('ฉันได้กำไร %d %%' %a)

a = 2
b = 3.5
print('เมื่อวานฉันขาดทุน %d %% วันนี้ฉันได้กำไร %.2f %%' %(a,b))

a = 2
b = 3.5
print("เมื่อวานฉันขาดทุน %d %% วันนี้ฉันได้กำไร %.2f %%" %(a,b))

"""เขียนโปรแกรมสร้างตัวแปรชื่อ numeric1 และกำหนดค่าให้เท่ากับ 5 หลังจากนั้นให้ทำารพิมพ์ค่าและชนิดข้อมูลของ numeric1 ออกมา"""

numeric1 = 5
print (numeric1)
print(type(numeric1))

"""เขียนโปรแกรมสร้างตัวแปรชื่อ numeric2 และกำหนดค่าให้เท่ากับ -3 หลังจากนั้นให้ทำารพิมพ์ค่าและชนิดข้อมูลของ numeric2 ออกมา"""

numeric2 = -3
print (numeric2)
print(type(numeric2))

numeric3 = 0
print(numeric3)
print(type(numeric3))

numeric4 = int(input('Please insert integer:'))
print(numeric4)
print(type(numeric4))

"""เขียนโปรแกรมสร้างตัวแปรชื่อ Numeric1 และกำหนดค่าให้เท่ากับ 5 หลังจากนั้นให้พิมพ์ค่า และชนิดของ Numeric1 ออกมา"""

numeric1 = 5.0
print(numeric1)
print(type(numeric1))

"""เขียนโปรแกรมสร้างตัวแปรชื่อ Numeric2 และกำหนดค่าให้เท่ากับ -3.1 หลังจากนั้นให้พิมพ์ค่า และชนิดของ Numeric2 ออกมา"""

numeric2 = -3.1
print(numeric2)
print(type(numeric2))

"""เขียนโปรแกรมสร้างตัวแปรชื่อ Numeric3 และกำหนดค่าให้เท่ากับ 0.0 หลังจากนั้นให้พิมพ์ค่า และชนิดของ Numeric3 ออกมา"""

numeric3 = 0.0
print(numeric3)
print(type(numeric3))

"""เขียนโปรแกรมรับอินพุต 1 ตัวที่เป้นจำนวจริง หลังจากนั้นให้ทำการพิมพ์ค่าและชนิดข้อมูลของจำนวนที่รับออกมา:


"""

numeric1 = int(input('please input:'))
print(numeric1)
print(type(numeric1))

เขียนโปรแกรมรับอินพุต 2 ตัวที่เป็นจำนวนต็ม(int1,int2) ให้คำนวณผลบวก,ผลลบ,ผลคูณ และผลหารของจำนวนที่รับมา หลังจากนั้นให้พิมพ์ค่าและชนิดข้อมูลของทุกผลลัพธ์ออกมา

numeric1 = int(input('int1:'))
numeric2 = int(input('int2:'))
print('numeric1 =',numeric1,(type(numeric1)))
print('numeric2 =',numeric2,(type(numeric2)))
print('คำนวณผลบวก =',(numeric1+numeric2),(type(numeric1+numeric2)))
print('ผลลบ =',(numeric1-numeric2),(type(numeric1-numeric2)))
print('ผลคูณ =',(numeric1*numeric2),(type(numeric1*numeric2)))
print('ผลคูณ =',(numeric1/numeric2),(type(numeric1/numeric2)))

"""เขียนโปรแกรมรับอินพุต 2 ตัวที่เป็นจำนวนต็ม(float1,float2) ให้คำนวณผลบวก,ผลลบ,ผลคูณ และผลหารของจำนวนที่รับมา หลังจากนั้นให้พิมพ์ค่าและชนิดข้อมูลของทุกผลลัพธ์ออกมา"""

numeric1 = float(input('float1:'))
numeric2 = float(input('float2:'))
print('numeric1 =',numeric1,(type(numeric1)))
print('numeric2 =',numeric2,(type(numeric2)))
print('คำนวณผลบวก =',(numeric1+numeric2),(type(numeric1+numeric2)))
print('ผลลบ =',(numeric1-numeric2),(type(numeric1-numeric2)))
print('ผลคูณ =',(numeric1*numeric2),(type(numeric1*numeric2)))
print('ผลคูณ =',(numeric1/numeric2),(type(numeric1/numeric2)))

"""เขียนโปรแกรมรับอินพุต 2 ตัวที่เป็นจำนวนต็ม(float1,int1) ให้คำนวณผลบวก,ผลลบ,ผลคูณ และผลหารของจำนวนที่รับมา หลังจากนั้นให้พิมพ์ค่าและชนิดข้อมูลของทุกผลลัพธ์ออกมา"""

numeric1 = float(input('float1:'))
numeric2 = int(input('int1:'))
print('numeric1 =',numeric1,(type(numeric1)))
print('numeric2 =',numeric2,(type(numeric2)))
print('คำนวณผลบวก =',(numeric1+numeric2),(type(numeric1+numeric2)))
print('ผลลบ =',(numeric1-numeric2),(type(numeric1-numeric2)))
print('ผลคูณ =',(numeric1*numeric2),(type(numeric1*numeric2)))
print('ผลคูณ =',(numeric1/numeric2),(type(numeric1/numeric2)))

"""เขียนโปรแกรมสร้่างตัวแปรชื่อ Logic1 และกำหนดค่าให้เท่ากับ true หลังจากนั้นให้ทำการพิมพืค่าและชนิดข้อมูลของ Logic1 ออกมา"""

logic1 = True
print(logic1)
print(type(logic1))

"""เขียนโปรแกรมสร้างตัวแปรชื่อ logic2 และกำหนดค่าให้เท่ากับ false หลังจากนั้นให้พิมพ์ค่าและชนิดข้อมุลของ logic2 ออกมา"""

logic2 = False
print(logic2)
print(type(logic2))

logic1 = True
logic2 = False
print(logic1 and logic2)

logic1 = True
logic2 = False
print(logic1 or logic2)

complex1 = 1+2j
print(complex1,type(complex1))

complex1 = 1+2j
print(complex1.real)

complex1 = 1+2j
print(complex1.imag)

"""## `06-07-2022` 50 ข้อ

# String

19.เขียนโปรแกรมสร้างตัวแปรชื่อ String1 และกำหนดค่าให้เท่ากับ 'Python' หลังจากนั้นให้ทำการพิมพ์ค่าและชนิดข้อมูลของ string1 ออกมา
"""

string1 = 'Python'
print(string1,(type(string1)))

"""20.เขียนโปรแกรมสร้างตัวแปรชื่อ string1 และกำหนดค่าให้เท่ากับ 'Python' หลังจากนั้นให้ทำการพิมพ์อักขระที่ index เป็น 0 ออกมา"""

string1 = 'Python'
print(string1[0])

"""21.เขียนโปรแกรมสร้างตัวแปรชื่อ string1 และกำหนดค่าให้เท่ากับ 'Python' หลังจากนั้นให้ทำการพิมพ์อักขระที่ index เป็น 1 ออกมา"""

string1 = 'Python'
print(string1[1])

"""22.เขียนโปรแกรมสร้างตัวแปรชื่อ string1 และกำหนดค่าให้เท่ากับ 'Python' หลังจากนั้นให้ทำการพิมพ์อักขระที่ index เป็น -1 ออกมา"""

string1 = 'Python'
print(string1[-1])

"""23.เขียนโปรแกรมสร้างตัวแปรชื่อ string1 และกำหนดค่าให้เท่ากับ 'Python' หลังจากนั้นให้ทำการพิมพ์อักขระที่ index เป็น -2 ออกมา"""

string1 = 'Python'
print(string1[-2])

"""24.เขียนโปรแกรมสร้างตัวแปรชื่อ string1 และกำหนดค่าให้เท่ากับ 'Python' หลังจากนั้นให้ทำการพิมพ์อักขระ 't' ออกมา โดยอ้างอิงตำแหน่งจาก string1"""

string1 = 'Python'
print(string1[2])

"""25.เขียนโปรแกรมสร้างตัวแปรชื่อ string1 และกำหนดค่าให้เท่ากับ 'Python' หลังจากนั้นให้ทำการพิมพ์อักขระ 'h' ออกมา โดยอ้างอิงตำแหน่งจาก string1"""

string1 = 'Python'
print(string1[3])

"""26.เขียนโปรแกรมสร้างตัวแปรชื่อ string1 และกำหนดค่าให้เท่ากับ 'Python' หลังจากนั้นให้ทำการพิมพ์สายอักขระตั้งแต่ index ที่ 1 จนถึง index ที่ 4 ออกมา"""

string1 = 'Python'
print(string1[1:4])

"""27.เขียนโปรแกรมสร้างตัวแปรชื่อ string1 และกำหนดค่าให้เท่ากับ 'Python' หลังจากนั้นให้ทำการพิมพ์สายอักขระตั้งแต่ index ที่ 2 จนถึง index ที่ -1 ออกมา"""

string1 = 'Python'
print(string1[2:-1])

"""28.เขียนโปรแกรมสร้างตัวแปรชื่อ string1 และกำหนดค่าให้เท่ากับ 'Python' หลังจากนั้นให้ทำการพิมพ์สายอักขระตั้งแต่ index ที่ 2 จนถึง index ที่ -1 ออกมา"""

string1 = 'Python'
print(string1[2:])

"""29.เขียนโปรแกรมสร้างตัวแปรชื่อ string1 และกำหนดค่าให้เท่ากับ 'Python' หลังจากนั้นให้ทำการพิมพ์สายอักขระตั้งแต่ index ที่ -4 จนถึง index ที่ 5 ออกมา"""

string1 = 'Python'
print(string1[-4:5])

"""30.เขียนโปรแกรมสร้างตัวแปรชื่อ string1 และกำหนดค่าให้เท่ากับ 'Python' หลังจากนั้นให้ทำการพิมพ์สายอักขระตั้งแต่ index ที่ -6 จนถึง index ที่ 5 ออกมา"""

string1 = 'Python'
print(string1[-6:5])

string1 = 'Python'
print(string1[:5])

"""31.เขียนโปรแกรมสร้างตัวแปรชื่อ String1 และกำหนดค่าให้เท่ากับ 'Python' หลังจากนั้นให้ทำการพิมพ์สายอักขระตั้งแต่ index ที่ -4 จนถึง Index ที่ -2"""

string1 = 'Python'
print(string1[-4:-1])

"""32.เขียนโปรแกรมรับอินพุต 1 ตัวที่เป็นสายอักขระ จากนั้นให้ทำการพิมพ์ความยาวของสายอักขระ"""

string = input('Please insert string:')
print(len(string1))

"""33.เขียนโปรแกรมรับอินพุต 1 ตัวที่เป็นสายอักขระ ให้ทำการตรวจสอบสายอักขระที่รับว่า 'ก' หรือไม่ จากนั้นให้พิมพ์ค่าความจริงออกมา"""

string = input('Please insert string:')
print('ก' in string)

"""34.เขียนโปรแกรมรับอินพุต 2 ตัวที่เป็นสายอักขระ (string1,string2)ให้ทำการตรวจ  String1 ที่รับมาว่ามี String2 ในนั้นหรือไม่ จากนั้นให้พิมพ์ค่าความจริงออกมา


> ตัวอย่างที่1:สมมติให้ string1 = 'happy',string2 = 'app' ผลลัพธ์ที่จะพิมพ์ออกมาคือ True


"""

string1 = input('Text1:')
string2 = input('Text2:')
print(string2 in string1
      )

"""35.เขียนโปรแกรมรับอินพุต 1 ตัวที่เป็นสายอักขระ ให้ทำการแทนที่อักขระ 'a' ด้วย 'A' จากนั้นให้พิมพ์สายอักขระที่ผ่านดำเนินการแล้วออกมา"""

string1 = input('Please insert string1:')
print(string1.replace('a','A'))

"""36.เขียนโปรแกรมรับอินพุต 1 ตัวที่เป็นสายอักขระ ให้ทำการแทนที่อักขระ 'a' ด้วย 'A'และกำหนดที่ผ่านการดำเนินการใส่ตัวแปรชื่อ string2 จากนั้นให้พิมพ์ string2 ออกมา"""

string1 = input('Please insert string1:')
string2 = string1.replace('a','A')
print(string2)

"""37.เขียนโปรแกรมรับอินพุต 1 ตัวที่เป็นสายอักขระ (sentence) ให้ทำการตัดคำในสายอักขระโดยใช้ '' เป็นตัวตัดคำ หลังจากนั้นให้พิมพ์ผลลัพธ์จากการตัดคำออกมา


>ตัวอย่างที่ 1: สมมติให้ sentence = 'We love Python' ผลลัพธ์ที่จะพิมพ์ออกมาคือ['We','love','Python']


"""

sentence = input('Please insert sentence:')
print(sentence.split(' '))

"""38.เขียนโปรแกรมรับอินพุต 2 ตัวที่เป็นสายอักขระ (sentence, c) ให้ทำการตัดคำใน sentence โดยใช้ c เป็นตัวตัดคำ หลังจากนั้นให้พิมพ์ผลลัพธ์จากการการตัดคำออกมา


> ตัวอย่างที่1: สมมติให้ sentence = 'Py-thon',c = '-' ผลลัพธ์ที่จะพิมพ์ออกมาคือ ['Py','thon']


"""

string1 = input('Please insert string1:')
string2 = input('Please insert string2:')
print(string1.split(string2))

"""39.เขียนโปรแกรมรับอินพุต 2 ตัวที่เป็นสายอักขระ (str1, str2) ให้ทำการต่อสายอักขระทั้งสอง (โดยนำ str2 ไปต่อหลัง str1) หลังจากนั้นให้พิมพ์ผลลัพธ์ออกมา


> ตัวอย่างที่ 1:สมมติให้ str1 = 'Fri',str2 ='day' ผลลัพธ์ที่จะพิมพ์ออกมาคือ 'friday'


"""

string1 = input('Please insert string1:')
string2 = input('Please insert string2:')
print(string1+string2)

"""# List

40.เขียนโปรแกรมสร้าง List ที่มีสมาชิก 0,1,2,'a','b','c' ตามลำดับ จากนั้นให้ทำการพิมพ์ค่าและชนิดข้อมูลของ List ที่สร้างออกมา
"""

list1 = [0,1,2,'a','b','c']
print(list1)
print(type(list1))



"""41.กำหนดให้ list1 =[0,1,2,'a','b','c'] เขียนโปรแกรมเพื่อพิมพ์สมาชิกที่ inndex เป็น 2 ออกมา"""

list1 =[0,1,2,'a','b','c']
print(list1[2])



"""42.กำหนดให้ list1 =[0,1,2,'a','b','c'] เขียนโปรแกรมเพื่อพิมพ์สมาชิกที่ inndex เป็น -3 ออกมา"""

list1 =[0,1,2,'a','b','c']
print(list1[-3])



"""43.กำหนดให้ list1 =[0,1,2,'a','b','c'] เขียนโปรแกรมเพื่อพิมพ์ 0 ออกมาโดยอ้างอิงตำแหน่งจาก list1"""

list1 =[0,1,2,'a','b','c']

print(list1[0])

"""44.กำหนดให้ list1 =[0,1,2,'a','b','c'] เขียนโปรแกรมเพื่อพิมพ์ 'b'ออกมาโดยอ้างอิงตำแหน่งจาก list1"""

list1 =[0,1,2,'a','b','c']
print(list1[4])

list1 =[0,1,2,'a','b','c']
print(list1[-2])

"""45.กำหนดให้ list1 =[0,1,2,'a','b','c'] เขียนโปรแกรมเพื่อพิมพ์ list ที่มีสมาชิกตั้งแต่ index ที่ 2 จนถึง index ที่ 3 ของ list1 ออกมา"""

list1 =[0,1,2,'a','b','c']
print(list1[2:4])



"""46.กำหนดให้ list1 =[0,1,2,'a','b','c'] เขียนโปรแกรมเพื่อพิมพ์ list ที่มีสมาชิกตั้งแต่ index ที่ 1 จนถึง index ที่ -2 ของ list1 ออกมา"""

list1 =[0,1,2,'a','b','c']
print(list1[1:-1])

"""47.กำหนดให้ list1 =[0,1,2,'a','b','c'] เขียนโปรแกรมเพื่อพิมพ์[1,2,'a','b'] โดยอ้างอิงตำแหน่งจาก list1"""

list1 =[0,1,2,'a','b','c']
print(list1[1:5])

list1 =[0,1,2,'a','b','c']
print(list1[1:-1])

list1 =[0,1,2,'a','b','c']
print(list1[-5:5])

list1 =[0,1,2,'a','b','c']
print(list1[-5:-1])

"""48.กำหนดให้ list1 =[0,1,2,'a','b','c'] เขียนโปรแกรมเพื่อพิมพ์['a','b','c'] โดยอ้างอิงตำแหน่งจาก list1"""

list1 =[0,1,2,'a','b','c']
print(list1[3:])

list1 =[0,1,2,'a','b','c']
print(list1[-3:])



"""49.กำหนดให้ list1 =[0,1,2,'a','b','c'] เขียนโปรแกรมเพื่อพิมพ์[0,1,2] โดยอ้างอิงตำแหน่งจาก list1"""

list1 =[0,1,2,'a','b','c']
print(list1[:3])

list1 =[0,1,2,'a','b','c']
print(list1[:-3])

"""50.กำหนดให้ list2 =['ant','bird','cat','dog','eagle'] เขียนโปรแกรมเพื่อเปลี่ยนค่าสมาชิกใน index ที่ 3 เป็น 'duck' หลังจากนั้นให้พิมพ์ list2 ออกมา"""

list2 =['ant','bird','cat','dog','eagle']
 list2[3]= 'duck'
 print(list2)

"""51.กำหนดให้ list2 =['ant','bird','cat','dog','eagle'] เขียนโปรแกรมเพื่อเปลี่ยน  'ant'เป็น 'ape' หลังจากนั้นให้พิมพ์ list2 ออกมา"""

list2 =['ant','bird','cat','dog','eagle']
 list2[0]= 'ape'
 print(list2)

list2 =['ant','bird','cat','dog','eagle']
 list2[-5]= 'ape'
 print(list2)

"""52.กำหนดให้ list2 =['ant','bird','cat','dog','eagle']เขียนโปรแกรมเพื่อเพิ่ม 'fish' ไปเป้นสมาชิกตัวสุดท้ายของ list2 หลังจากนั้นให้่พิมพ์ list2 ออกมา"""

list2 =['ant','bird','cat','dog','eagle']
 list2[4]= 'fish'
 print(list2)

list2 =['ant','bird','cat','dog','eagle']
 list2[-1]= 'fish'
 print(list2)

"""53.เขียนโปรแกรมสร้าง empty list และรับอินพุฒ 3 ตัวที่เป็นสายอักขระ(str1,str2,str3) จากนั้นให้ทำการเพิ่มสายอักขระทั้ง 3 ไปเป็นสมาชิกใน list โดยใช้เมธอด append สุดท้ายให้พิมพ์ list ออกมา"""

list2 = []
str1 = input('Please insert first element:')
str2 = input('Please insert second element:')
str3 = input('Please insert third element:')
list2.append(str1)
list2.append(str2)
list2.append(str3)
print(list2)

"""54.กำหนดให้ list3 =['apple','cherry','eggfruit'] เขียนโปรแกรมเพื่อแทรก 'ba-nana' ไปเป็นสมชิกใน index ที่1 ของ list3 หลังจากนั้นให้พิมพ์ list3 ออกมา"""

list3 =['apple','cherry','eggfruit']
list3.insert(1,'banana')
print(list3)



"""55.กำหนดให้ list3 =['apple','banana',''cherry','eggfruit'] เขียนโปรแกรมเพื่อแทรก 'kiwi' ไปเป็นสมชิกใน index ที่-2 ของ list3 หลังจากนั้นให้พิมพ์ list3 ออกมา

"""

list3 =['apple','cherry','eggfruit']
list3.insert(-1,'kiwi')
print(list3)

"""56.กำหนดให้ list4=[0,4,2,3,1] เขียนโปรแกรมเพื่อเรียงลำดับข้อมูลใน list4 จากน้อยไปมาก หลังจากนั้นให้พิมพ์ list4 ออกมา"""

list4=[0,4,2,3,1] 
list4.sort()
print(list4)

"""57.กำหนดให้ list4=[0,4,2,3,1] เขียนโปรแกรมเพื่อเรียงลำดับข้อมูลใน list4 จากมากไปน้อย หลังจากนั้นให้พิมพ์ list4 ออกมา"""

list4=[0,4,2,3,1] 
list4.sort(reverse=True)
print(list4)

"""58.กำหนดให้ list4=[0,4,2,3,1] เขียนโปรแกรมเพื่อเรียงลำดับข้อมูลใน list4 จากน้อยไปมาก และเก็บค่าไว้ในตัวแปรชื่อ sorted_list4 หลังจากนั้นให้พิมพ์ sorted_list4 ออกมา"""

list4=[0,4,2,3,1]
sort_list4 = sorted(list4)
print(sort_list4)



"""59.กำหนดให้ list4=[0,4,2,3,1] เขียนโปรแกรมเพื่อเรียงลำดับข้อมูลใน list4 จากมากไปน้อย และเก็บค่าไว้ในตัวแปรชื่อ sorted_list4 หลังจากนั้นให้พิมพ์ sorted_list4 ออกมา"""

list4=[0,4,2,3,1]
sort_list4 = sorted(list4,reverse=True)
print(sort_list4)

"""60.กำหนดให้ list5=['d','a','c','b','e'] เขียนโปรแกรมเพื่อเรียงลำดับข้อมูลใน list5 ตามตัวอักษร หล้ังจากนั้นให้พิมพ์ list5 ออกมา"""

list5=['d','a','c','b','e'] 
 list5.sort()
 print(list5)

"""61.กำหนดให้ list5=['d','a','c','b','e'] เขียนโปรแกรมเพื่อเรียงลำดับข้อมูลใน List5 ตามตัวอักษรแบบถอยหลัง และเก็บค่าไว้ในตัวแปรชื่อ sorted_list5 หลังจากนั้นให้พิมพ์ sorted_list5 ออกมา"""

list5 = ['d','a','c','b','e']
sorted_list5 = sorted(list5, reverse = True)
print(sorted_list5
      )



"""62.กำหนดให้ list1 =['a','b','c'] และ list2 = [0,1,2] เขียนโปรแกรมเพื่อนำสมาชิกทั้งหมดของ list2 ไปต่อท้าย list1 จากนั้นให้พิมพ์ list1 และ list2 ออกมา"""

list1 =['a','b','c']
list2 = [0,1,2]
list1.extend(list2)
print(list1,list2)



"""63.กำหนดให้ list1 =['a','b','c'] และ list2 = [0,1,2] เขียนโปรแกรมเพื่อนำสมาชิกทั้งหมดของ list2 ไปต่อท้าย list1 และเก็บ list ที่ได้จากการดำเนินการไว้ในตัวแปรชื่อ list3 จากนั้นให้พิมพ์ list1,list2 และ list3 ออกมา"""

list1 =['a','b','c']
list2 = [0,1,2] 
list3 =list1+list2
print(list1)
print(list2)
print(list3)



"""64.กำหนดให้ list1 =[1,2,3,1,2,3] เขียนโปรแกรมลบสมาชิกใน index ที่ 1 ออกจาก list1 โดยใช้คำสั่ง del หลังจากนั้นให้พิมพ์ list1 ออกมา"""

list1 =[1,2,3,1,2,3]
del list1[1]
print(list1)

"""65.กำหนดให้ list1 = [1,2,3,1,2,3]  เขียนโปรแกรมลบ 3 ทั้งหมดออกจาก list1 โดยใช้คำสั่ง Del หลังจากนั้นให้พิมพ์ list1 ออกมา"""

list1 =[1,2,3,1,2,3]
del list1[-1]
del list1[2]
print(list1)

"""66.กำหนดให้ list1 = [1,2,3,1,2,3]  เขียนโปรแกรมลบ 1 ออกจาก list1 โดยใช้เมธอด Remove หลังจากนั้นให้พิมพ์ list1 ออกมา"""

list1 = [1,2,3,1,2,3] 
list1.remove(1)
print(list1)

"""67.กำหนดให้ list1 = [1,2,3,1,2,3]  เขียนโปรแกรมลบ 1 ทั้งหมดออกจาก list1 โดยใช้เมธอด Remove หลังจากนั้นให้พิมพ์ list1 ออกมา

"""

list1 = [1,2,3,1,2,3] 
list1.remove(1)
list1.remove(1)
print(list1)

"""68.กำหนดให้ list1 = [1,2,3,1,2,3]  เขียนโปรแกรมลบสมาชิกทุกตัวออกจาก list1 หลังจากนั้นให้พิมพ์ list1 ออกมา"""

list1 = [1,2,3,1,2,3] 
list1.clear()
print(list1)

"""## `07-07-2022` 50 ข้อ

69.กำหนดให้ list1 =[1,2,3,'a','b','c'] เขียนโปรแกรมหาความยาวของ list1 และพิมพ์ออกมา
"""

list1 =[1,2,3,'a','b','c']
print(len(list1))

"""70.กำหนดให้ list1 = [1,2,3,4,5] เขียนโปรแกรมรับอินพุต 1 ตัวที่เป็นจำนวนเต็ม(numeric1) ให้ทำการตรวจว่า numeric1 เป็นสมาชิกใน list1 หรือไม่ จากนั้นให้พิมพ์ค่าความจริงออกมา"""

list1 = [1,2,3,4,5] 
numeric1 = int(input('Please insert numeric1:'))
print(numeric1 in list1)

"""# **Tuple**

71. เขียนโปรแกรมสร้าง tuple ที่มีสมาชิกเป็น 'America','Brazil','China',Do-minican','Egypt' ตามลำกดับจากนั้นให้ทำการพิมพ์ค่า และชนิดข้อมูลของ tuple ที่สร้างออกมา
"""

tuple1=( 'America','Brazil','China','Do-minican','Egypt')
print(tuple1)
print(type(tuple1))

"""72.กำหนดให้ tuple1 =('America','Brazil','China','Do-minican','Egypt') เขียนโปรแกรมเพื่อพิมพ์สมาชิกที่ Index เป็น 1 ออกมา"""

tuple1 =('America','Brazil','China','Do-minican','Egypt') 
print(tuple1[1])

"""73.กำหนดให้ tuple1 =('America','Brazil','China','Do-minican','Egypt') เขียนโปรแกรมเพื่อพิมพ์สมาชิกที่ Index เป็น -2 ออกมา"""

tuple1 =('America','Brazil','China','Do-minican','Egypt')
print(tuple1[-2])

"""74.กำหนดให้ tuple1 =('America','Brazil','China','Do-minican','Egypt')เขียนโปรแกรมเพื่อพิมพ์ 'China'ออกมาโดยอิ้างอิงตำแหน่งจาก tuple1"""

tuple1 =('America','Brazil','China','Do-minican','Egypt')
print(tuple1[2])

tuple1 =('America','Brazil','China','Do-minican','Egypt')
print(tuple1[-3])

"""75.กำหนดให้ tuple1 =('America','Brazil','China','Do-minican','Egypt')เขียนโปรแกรมเพื่อพิมพ์ 'Egypt'ออกมาโดยอิ้างอิงตำแหน่งจาก tuple1"""

tuple1 =('America','Brazil','China','Do-minican','Egypt')
print(tuple1[-1])

tuple1 =('America','Brazil','China','Do-minican','Egypt')
print(tuple1[4])

"""76.กำหนดให้ tuple2 =('one','two','three','1','2','3') เขียนโปรแกรมเพื่อพิมพ์ tuple ที่มีสมาชิกตั้งแต่ Index ที่ 1 จนถึง Index ที่3 ของ tuple2 ออกมา"""

tuple2 =('one','two','three','1','2','3')
print(tuple2[1:4])

"""77.กำหนดให้ tuple2 =('one','two','three','1','2','3')เขียนโปรแกรมเพื่อพิมพ์ tuple ที่มีสมาชิกตั้งแต่ Index ที่ 2 จนถึง Index ที่-2 ของ tuple2 ออกมา"""

tuple2 =('one','two','three','1','2','3')
print(tuple2[2:-1])

"""78.กำหนดให้ tuple2 =('one','two','three','1','2','3')เขียนโปรแกรมเพื่อพิมพ์ ('three',1) โดยอ้างอิงตำแหน่งจาก tuple2"""

tuple2 =('one','two','three','1','2','3')
print(tuple2[2:4])

tuple2 =('one','two','three','1','2','3')
print(tuple2[-4:-2])

tuple2 =('one','two','three','1','2','3')
print(tuple2[2:-2])

tuple2 =('one','two','three','1','2','3')
print(tuple2[-4:-2])

"""79.กำหนดให้ tuple2 =('one','two','three','1','2','3')เขียนโปรแกรมเพื่อพิมพ์ ('one','two','three') โดยอ้างอิงตำแหน่งจาก tuple2"""

tuple2 =('one','two','three','1','2','3')
print(tuple2[:3])

tuple2 =('one','two','three','1','2','3')
print(tuple2[:-3])

tuple2 =('one','two','three','1','2','3')
print(tuple2[0:3])

tuple2 =('one','two','three','1','2','3')
print(tuple2[-6:-3])

"""80.กำหนดให้ tuple2 =('one','two','three','1','2','3')เขียนโปรแกรมเพื่อพิมพ์ (1,2,3) โดยอ้างอิงตำแหน่งจาก tuple2"""

tuple2 =('one','two','three','1','2','3')
print(tuple2[3:])

tuple2 =('one','two','three','1','2','3')
print(tuple2[-3:])

"""81.กำหนดให้ tuple3 =('one','two','three','four','five')เขียนโปรแกรมหาความยาวของ tuple3 และพิมพ์ออกมา"""

tuple3 =('one','two','three','four','five')
print(len(tuple3))



"""82.กำหนดให้ tuple3 =('one','two','three','four','five')เขียนโปรแกรมรับอินพุต 1 ตัวที่เป็นสายอักขระ(str1) ให้ทำการตรวจว่า str1 เป็นสมาชิกใย tuple3 หรือไม่ จากนั้นให้พิมพ์ค่าความจริงออกมา"""

tuple3 =('one','two','three','four','five')
str1 = str(input('Please insert str:'))
print(str1 in tuple3)



"""# **Dictionany**

83.เขียนโปรแกรมสร้าง dictionary ที่มี key เป็น 'first_name' และ 'last_name' โดยมี value เป็น 'John' และ 'Doe' ตามลำดับ จากนั้นให้ทำการพิมพ์ค่าและชนิดข้อมูลของ Dictionary ที่สร้างออกมา
"""

dict1 ={'first_name':'John','last_name' :'Doe'}
print(dict1)
print(type(dict1))



"""84.กำหนดให้ dict1 = {'first_name':'John', 'last_name': 'doe'} เขียนโปรแกรมพิมพ์ value ของ key 'first_name' ออกมา"""

dict1 = {'first_name':'John', 'last_name': 'doe'}
print(dict1['first_name'])



"""85.กำหนดให้ dict1 = {'first_name': 'John', 'last_name':'Doe'} เขียนโปรแกรมพิมพ์ value ของ key 'last_name' ออกมา"""

dict1 = {'first_name':'John', 'last_name': 'doe'}
print(dict1['last_name'])



"""86.กำหนดให้ dict1 = {'first_name':'John','last_name':'Doe'} เขียนโปรแกรมพิมพ์ list ของ key ทั้งหมดใน Dict1 ออกมา"""

dict1 = {'first_name':'John', 'last_name': 'doe'}
print(dict1.keys())



"""87.กำหนดให้ dict1 = {'first_name':'John','last_name':'Doe'} เขียนโปรแกรมพิมพ์ list ของ value ทั้งหมดใน Dict1 ออกมา"""

dict1 = {'first_name':'John', 'last_name': 'doe'}
print(dict1.values())



"""88.กำหนดให้ dict1 = {'first_name':'John','last_name':'Doe'} เขียนโปรแกรมเปลี่ยน value ของ key 'first_name' เป็น 'Jane' หลังจากนั้นให้พิมพ์ dict1 ออกมา"""

dict1 = {'first_name':'John', 'last_name': 'doe'}
dict1['first_name']='Jane' 
print(dict1)



"""89.กำหนดให้ dict1 = {'first_name':'John','last_name':'Doe'} เขียนโปรแกรมสร้าง key ใหม่ชื่อ 'age' และกำหนด value เป็น 32 หลังจากนั้นให้พิมพ์ dict1 ออกมา"""

dict1 = {'first_name':'John', 'last_name': 'doe'}
dict1['age']=31
print(dict1)



"""90.กำหนดให้ dict1 = {'first_name': 'John','last_name': 'Doe'} เขียนโปรแกรมสร้าง key ใหม่ชื่อ 'age' และ 'hobby' โดยมี value เป็น 32 และ ['coding','stucding'] ตามลำดับ หลังจากนั้นให้พิมพ์ dict1 ออกมา"""

dict1 = {'first_name': 'John','last_name': 'Doe'} 
dict1.update({'age':32,'hobby':['coding','stucding']})
print(dict1)



"""91.เขียนโปรแกรมสร้าง empty dictionary และรับอินพุต 2 ตัวที่เป็นสายอักขระ (str1,str2) โดยให้ str1 เป็น key และ str2 เป็น value หลังจากนั้นให้พิมพ์ dictionary ออกมา"""

dict1 = {}
str1 = input('Please insert str1:')
str2 = input('Please insert str2:')
dict1[str1]=str2
print(dict1)



"""92.กำหนดให้ dict1 ={'firstname':'John','last_name':'Doe','age':32} เขียนโปรแกรมลบ key 'age' ออกจาก dict1 หลังจากนั้นให้พมพ์ dict1 ออกมา"""

dict1 ={'firstname':'John','last_name':'Doe','age':32}
del dict1['age']
print(dict1)



"""93.กำหนดให้ dict1 = {'first_name':'John','last_name':'Doe','age':32} เขียนโปรแกรมลบข้อมูลทั้งหมดออกจาก dict1 หลังจากนั้นให้พิมพ์ dict1 ออกมา"""

dict1 ={'firstname':'John','last_name':'Doe','age':32}
dict1.clear()
print(dict1)

"""94.กำหนดให้ dict1 = {'first_name':'John','last_name':'Doe','age':32} เขียนโปรแกรมพิมพ์จำนวน key ของ dict1 ออกมา"""

dict1 = {'first_name':'John','last_name':'Doe','age':32}
print(len(dict1))

dict1 = {'first_name':'John','last_name':'Doe','age':32}
print(len(dict1.keys()))

"""95.กำหนดให้ dict1 = {'first_name':'John','last_name':'Doe','age':32} เขียนโปรแกรมรับอินพุต 1 ตัวที่เป็นสายอักขระ (str1) ให้ทำการตรวจว่า str1 เป็นหนึ่งใน key ของ dict1 หรือไม่ จากนั้นให้พิมพ์ค่าความจริงออกมา"""

dict1 = {'first_name':'John','last_name':'Doe','age':32} 
str1 = input('Please insert st1:')
print(str1 in dict1.keys())

dict1 = {'first_name':'John','last_name':'Doe','age':32} 
str1 = input('Please insert st1:')
print(str1 in dict1)

"""96.กำหนดให้ dict1 = {'first_name':'John','last_name':'Doe','age':32} เขียนโปรแกรมรับอินพุต 1 ตัวที่เป็นสายอักขระ (str1) ให้ทำการตรวจว่า str1 เป็นหนึ่งใน value ของ dict1 หรือไม่ จากนั้นให้พิมพ์ค่าความจริงออกมา"""

dict1 = {'first_name':'John','last_name':'Doe','age':32} 
str1 = input('Please insert st1:')
print(str1 in dict1.values())



"""### **Set**

97.เขียนโปรแกรมสร้าง set ที่มีสมาชิก 1,2,3,'i','ii','iii' จากนั้านให้ทำการพิมพ์ค่าและชนิดข้อมูลของ Set ที่สร้างออกมา
"""

set1 = {1,2,3,'i','ii','iii'}
print(set1)
print(type(set1))



"""98.กำหนดให้ set1 ={1,2,3,'i','ii','iii'} เขียนโปรแกรมพิมพ์สมาชิกทุกตัวใน set1 ออกมา"""

set1 = {1,2,3,'i','ii','iii'}
for s in set1 :
  print(s)

"""99.กำหนดให้ set1 ={1,2,3,'i','ii','iii'} เขียนโปรแกรมเพิ่ม 'iv' ไปเป็นสมาชิกใน set1 จากนั้นให้พิมพ์ set1 ออกมา"""

set1 = {1,2,3,'i','ii','iii'}
set1.add('iv')
print(set1)

"""100.กำหนดให้ set1 ={1,2,3,'i','ii','iii'} เขียนโปรแกรมเพิ่ม 1 ไปเป็นสมาชิกใน set1 จากนั้นให้พิมพ์ set1 ออกมา"""

set1 = {1,2,3,'i','ii','iii'}
set1.add(1)
print(set1)

"""101.เขียนโปรแกรมสร้าง empty set และรับอินพุต 3 ตัวที่เป็นสายอักขระ(str1,str2,str3) จากนั้นให้ทำการเพิ่มสายอักขระทั้ง 3 ไปเป็นสมาชิกใน set สุดท้ายให้พิมพ์ set ออกมา"""

set1 = set()
str1 = input('Please insert str1:')
str2 = input('Please insert str2:')
str3 = input('Please insert str3:')
set1.add(str1)
set1.add(str2)
set1.add(str3)
print(set1)



"""102.เขียนโปรแกรมสร้าง empty set และรับอินพุต 3 ตัวที่เป็นสายอักขระ(str1,str2,str3) จากนั้นให้ทำการเพิ่มสายอักขระทั้ง 3 ไปเป็นสมาชิกใน set โดยการใช้เมธอด update สุดท้ายให้พิมพ์ set ออกมา"""

set1 = set()
str1 = input('Please insert str1:')
str2 = input('Please insert str2:')
str3 = input('Please insert str3:')
set1.update({str1,str2,str3})
print(set1)



"""103.กำหนดให้ set1 ={1,2,3,'i','ii','iii'} เขียนโปรแกรมลบ 'i' จาก set1 จากนั้นให้พิมพ์ set1 ออกมา"""

set1 ={1,2,3,'i','ii','iii'}
set1.remove('i')
print(set1)



"""104.กำหนดให้ set1 ={1,2,3,'i','ii','iii'} เขียนโปรแกรมพิมพ์จำนวนสมาชิกใน set1 ออกมา"""

set1 ={1,2,3,'i','ii','iii'}
print(len(set1))



"""105.กำหนดให้ set1 ={1,2,3,'i','ii','iii'} เขียนโปรแกรมรับอินพุต 1 ตัวที่เป็นจำนวนเต็ม(int1) ให้ทำการตรวจว่า int1 เป็นสมาชิกของ set1 หรือไม่ จากน้ั้นให้พิมพ์ค่าความจริงออกมา"""

set1 ={1,2,3,'i','ii','iii'} 
int1 = int(input('Please insert int1:'))
print(int1 in set1)



"""106.กำหนดให้ set1 ={1,2,3,4,5} และ set2 ={3,4,5,6} เขียนโปรแกรมพิมพ์ผลลัพธ์ที่เกิดจากการ union ระหว่าง set1 และ set2 ออกมา """

set1 ={1,2,3,4,5}
 set2 ={3,4,5,6}
 print(set1 | set2)



"""107.กำหนดให้ set1 ={1,2,3,4,5} และ set2 ={3,4,5,6} เขียนโปรแกรมพิมพ์ผลลัพธ์ที่เกิดจากการ intersection ระหว่าง set1 และ set2 ออกมา"""

set1 ={1,2,3,4,5}
 set2 ={3,4,5,6}
 print(set1 & set2)



"""108.กำหนดให้ set1 ={1,2,3,4,5} และ set2 ={3,4,5,6} เขียนโปรแกรมพิมพ์ผลลัพธ์ที่เกิดจาก set1 - set2 ออกมา"""

set1 ={1,2,3,4,5}
set2 ={3,4,5,6}
print(set1-set2)



"""109.กำหนดให้ set1 ={1,2,3,4,5} และ set2 ={3,4,5,6} เขียนโปรแกรมพิมพ์ผลลัพธ์ที่เกิดจาก set2 - set1 ออกมา"""

set1 ={1,2,3,4,5}
set2 ={3,4,5,6}
print(set2-set1)

"""110.กำหนดให้ set1 ={1,2,3,4,5} และ set2 ={3,4,5,6} เขียนโปรแกรมพิมพ์ผลลัพธ์ที่เกิดจากการ symmetric difference ระหว่าง set1 และ set2 ออกมา


"""

set1 ={1,2,3,4,5}
set2 ={3,4,5,6} 
print(set1 ^ set2)





"""111."""





"""112."""





"""113."""







"""114."""





"""115."""





"""116."""





"""117."""





"""118."""





"""# 08-07-2022 50 ข้อ

22-07-2022
"""

count_prime = 0
number = 1
while count_prime != 100:
    count = 0
    for i in range(1,number+1):
        if number%i == 0:
            count = count+1
        if count ==2:
            print(number)
            count_prime = count_prime +1
        number = number+1
    print(i)

for i in range(1,100):
    if i%3 == 0:
      print(i)

for i in range(1,100):
  if (i%3 == 0) and (i%5 == 0):
    print(i)



i = 1
while i <= 99:
  if (i%3 == 0) and (i%5 == 0):
    print(i)
  i = i+1

for i in range(1,100):
  if (i%3 == 0) or (i%5 == 0):
    print(i)

for i in range(1,1000):
  if (i%3 == 0) and (i%5 == 0) and (i%7 == 0):
    print(i)

i = 1
while i <= 1000:
  if (i%3 == 0) and (i%5 == 0) and (i%7 == 0):
    print(i)
  i= i+1

for i in range(1,99):
  if (i%3 ==0) or (i%5 == 0) or (i%7 == 0):
    print(i)

for i in range(1,100):
  if i%3 ==0:
    if i%5 == 0:
      print(i)
  else:
    if i%5 == 0:
      print(i)

for i in range(1,100):
  if (i%3 == 0) and (i%5 ==0):
    if i%2 != 0:
      print(i)

for i in range(1,100):
  if (i%3 ==0) or (i%5 ==0):
    if i%2 !=0:
      print(i)

count = 0
for i in range(1,1000):
  if i%3 ==0:
    count = count+1
    print(i)



sumx = 0
for i in range(5):
  num =int(input('get input:'+str(i+1)))
  sumx = sumx+num
print(sumx)



sumx = 0
for i in range(1,1000):
  if i%3 ==0:
    sumx = sumx+1
  print(i)

sumx =0
for i in range(5):
  if i <=5:
    num =float(input('get input No:'+str(i+1)+' คือ '))
    sumx = num+1
    print(sumx)

number = int(input('get input:'))
for i in  range(1,number+1):
  if number%i ==0:
    print(i)

for number in range(1,100):
  count = 0
  for i in range(1,number+1):
    if number%1 == 0:
      count = count+1
      if count ==2:
        print(number)

count_prime = 0
number = 1
while count_prime != 100:
  count = 0
  for i in range(1,number+1):
    if number%i ==0:
      count = count+1
  if count == 2:
      count_prime = count_prime+1
      print(number,'= จำนวนเฉพาะตัวที่',count_prime)
  number = number+1



"""**02082022**"""

def addition(a,b):
  return a+b

addition(18,32)

def addition3(a,b,c):
  return a + b + c

addition3(10,20,25)

def square(a) :
  return a**2

square(25)

def square_list(listA):
  square = []
  for a in listA:
    square.append(a**2)
    return square

square_list[1,2,3,4,5]





