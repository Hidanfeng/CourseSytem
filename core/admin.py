'''
管理员视图
'''
from interface import admin_interface,common_interface
from lib import common
uerinfo = {'user': None}

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
            flag,mesg = admin_interface.admin_register_interface(username,password)
            if flag:
                print(mesg)
                break
            else:
                print(mesg)
        else:
            print('密码不一致，请重新输入')

def login():
    while True:
        username = input('请输入用户名').strip()
        password = input('请输入密码').strip()
        '''调用接口层做数据判断'''
        flag, mesg = admin_interface.admin_login_interface(username, password)
        if flag:
            print(mesg)
            # 可变类型不需要global
            uerinfo['user'] = username
            break
        else:
            print(mesg)



@common.auth('admin')
def creat_school():
    school_name = input('请输入学校名字').strip()
    school_addr = input('请输入学校地址').strip()

    flag,mesg = admin_interface.create_school_interface(school_name,school_addr,uerinfo['user'])
    if flag:
        print(mesg)
    else:
        print(mesg)

@common.auth('admin')
def create_course():
    while True:
        flag, list_or_mesg = common_interface.get_all_school_interface()
        if flag:
            for index, i in enumerate(list_or_mesg):
                print(f'编号{index}  学校{i} ')
            choice = input('请输入学校编号').strip()
            if not choice.isdigit():
                print('请输入数字')
                continue
            choice = int(choice)
            if choice not in range(len(list_or_mesg)):
                print('请输入正确编号')
                continue
            school_name = list_or_mesg[choice]
            course_name = input('请输入要创建的课程名称：').strip()
            flag ,msg = admin_interface.create_course_interface(
                school_name,course_name,uerinfo['user']
            )
            if flag:
                print(msg)
            else:
                print(msg)

        else:
            print(list_or_mesg)

@common.auth('admin')
def create_teacher():
    while True:
        teacher_name = input('请输入学生的名字>>')
        # student_name = input('请输入学生的名字>>')
        flag,msg = admin_interface.create_teacher_interface(teacher_name,uerinfo['user'])
        if flag:
            print(msg)
        else:
            print(msg)








dunc_dic={
    '1':register,
    '2':login,
    '3':creat_school,
    '4':create_course,
    '5':create_teacher,
}
def admin_view():
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
