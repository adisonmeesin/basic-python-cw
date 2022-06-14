numbers = [-1, 2, 5, 8, 10, 13]
names = ['Mateo', 'Danny', 'James', 'Thomas', 'Luke']
mixed_type = [-2, 5, 84.2, "Mountain", "Python"]

print(numbers)
print(numbers[3])
print(names[3])
print(mixed_type[0])

print(numbers[-1])
print(names[-2])

# การสร้าง List แบบว่าง
numbers2 = []

# เพิ่มสมาชิกเข้าไปใน list ว่าง
numbers2.append(5)
numbers2.append(10)
numbers2.append(15)
numbers2.append(20)

print(numbers2)

# อ่านสมาชิกทั้งหมดใน list
sum = 0
for index, value in enumerate(numbers):
    print(index, value)
    sum += value

print(sum)