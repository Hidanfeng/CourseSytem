'''
用户的主视图
'''
from core import admin
from core import teacher
from core import student


dunc_dic={
    '1':admin.admin_view,
    '2':teacher.teacher_view,
    '3':student.student_view

}



def run():
    while True:
        print('''
        =========欢迎来到选课系统=====
            1、管理员功能
            2、学生功能
            3、老师功能
        ==============end===========
        ''')
        choice =  input('请输入功能编号').strip()
        if choice in dunc_dic:
            dunc_dic.get(choice)