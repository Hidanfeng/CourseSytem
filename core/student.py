'''
学生视图
'''
from interface import student_interface

def register():
    '''
    登录
    :return:
    '''
    while True:
        username = input('请输入用户名').strip()
        password = input('请输入密码').strip()
        re_password = input('请确认密码').strip()
        if password == re_password:
            '''调用接口层做数据判断'''
            flag,mesg = student_interface.student_register_interface(username,password)
            if flag:
                print(mesg)
                break
            else:
                print(mesg)
        else:
            print('密码不一致，请重新输入')

dunc_dic={
    '1':''
}
def student_view():
    while True:
        print('''
                =========欢迎来到管理员页面=====
                    1、注册
                    2、登录
                    3、创建学校
                    4、创建课程
                    5、创建老师
                ==============end===========
                ''')
        choice = input('请输入功能编号').strip()
        if choice in dunc_dic:
            dunc_dic.get(choice)()
