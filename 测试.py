use = 123456
password = 123456


while True:
    cuse = int(input("请输入你的账号："))
    cpassword = int(input("请输入你的密码："))
    if cuse == use and cpassword == password:
        print("登陆成功！")
        break
    else:
        print("登陆失败!")


