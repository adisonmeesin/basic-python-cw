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

a = (1, 2, 3, 4)
b = 1, 2, 3, 4
c = tuple(['C++', 'C#', 'Java', 'Pyhton'])
d = tuple(range(1, 10, 2))
e = ('a', )
f = ()

print(a)
print(b)
print(c)
print(c[0])
print(d)
print(e)
print(f)

numbers = (1, 2, 3, 4, 5)
print('numbers[0] =', numbers[0])
print('numbers[3] =', numbers[3])
print('numbers[-1] =', numbers[-1])

mixed_type = (1.1, 1, 'Python', [10, 20, 30])
print('mixed_type[0] =', mixed_type[0])
print('mixed_type[3] =', mixed_type[3])
print('mixed_type[3][0] =', mixed_type[3][0])

print("\n")

numbers2 = (10, 20, 30, 40, 50, 60, 70, 80)
for n in numbers2:
    print(n, end = ' ')

print("\n")

names = ('James', 'Alex', 'Bobby', 'Johnny', 'Nathan')
for i in range(0, len(names)):
    print(names[i], end = ' ')

print("\n")