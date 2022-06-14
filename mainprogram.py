# import number

# print(number.factorial(5))
# print(number.fibonacci(100))

#การ import บางสฟังก์ชัน
# from number import factorial, fibonacci
# from number import *

# print(factorial(5))
# print(fibonacci(100))

# import พร้อมตั้งชื่อนามแฝง
# from numberpackage.number import factorial as ft, fibonacci as fb

# print(ft(5))

# print(fb(100))

# import จาก Package
# from numberpackage import calculate as cl
# print(cl.plus(2,3))

# from numberpackage import *

# print(numberpackage.calculate.plus(2,3))
# print(numberpackage.number.factorial(5))
# print(numberpackage.number.fibonacci(100))

import numberpackage

print(numberpackage.plus(2,3))
print(numberpackage.factorial(5))
print(numberpackage.fibonacci(100))
