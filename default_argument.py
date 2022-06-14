# การสร้างฟังก์ชันใน Python
def hello():
    print("Hello Python")


# เรียกใช้งานฟังก์ชัน hello()
hello()


# การสร้างฟังก์ชันแบบมี Argument
def info(msg):
    print("Welcome to", msg)


info("ITGenius")

# การสร้างฟังก์ชันใน Python


def area(width, height):
    result = width * height
    return result


print(area(10, 20))


def show_info(name="", salary=84360, lang="Python"):
    print('Name: %s' % name)
    print('Salary: %d' % salary)
    print('Language: %s' % lang)


show_info()
