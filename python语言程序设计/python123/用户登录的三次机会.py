for i in range(3):
    test1 = input()
    test2 = input()
    if test1 == 'Kate' and test2 == '666666':
        print("登录成功！")
        break
else:
    print("3次用户名或者密码均有误！退出程序。")