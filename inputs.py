# ลองเขียนโปรแกรมรับค่า username and password จากผู้ใช้
# มาทำงานเปรียบเทียบค่า

print("Please enter username and password:")

# การรับค่าจากผู้ใช้
username = input("Username: ")
password = input("Password: ")

print(username)
print(password)

# เขียนเงื่อนไขตรวจสอบด้วย if...else
if(username == "admin" and password == "123456"):
    print("Login Success")
else:
    print("Login Fail!")

print('Welcome to marcuscode\'s game')
level = input('Enter level (1 - 4): ')

if level == '1':
    print('Easy')
elif level == '2':
    print('Medium')
elif level == '3':
    print('Hard')
elif level == '4':
    print('Expert')
else:
    print('Invalid level selected')