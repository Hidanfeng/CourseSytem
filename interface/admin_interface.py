'''
管理员接口
'''
from db import models


def admin_register_interface(username,password):
    '''
    判断用户是否存在
    1、存在不允许注册，返回用户自己的视图层
    2、不存在允许注册，调用类实例化得到对象并保存
    :param username:
    :param password:
    :return:
    '''

    # 判断用户是否存在
    # 1、存在不允许注册，返回用户自己的视图层
    admin_obj = models.Admin.select(username)
    if admin_obj:
        print(admin_obj.user)
        return False,'用户存在'

    # 2、不存在允许注册，调用类实例化得到对象并保存
    admin_obj = models.Admin(username,password)
    admin_obj.save()
    return True,'注册成功'

def admin_login_interface(username,password):
    admin_obj = models.Admin.select(username)
    if not admin_obj:
        return False,'用户不存在'
    if username == admin_obj.user and password == admin_obj.pwd:
        return True,'登录成功'
    else:
        return False,'登录失败'

def create_school_interface(school_name,school_addr,admin_name):
    #School自己去查
    school_obj = models.School.select(school_name)
    #判断学校是否存在，不存在创建 注意要管理员来创建 Admin下面有一个create_school方法
    if not school_obj:
        admin_obj = models.Admin.select(admin_name)
        admin_obj.creat_school(school_name,school_addr)
        return True,'创建成功'
    #存在就展示学校
    else:
        return False,f'{school_name} 已经存在'


def create_course_interface(school_name,course_name,admin_user):
    #先判断学校中的课程列表是否存在
    school_obj = models.School.select(school_name)
    course_list = school_obj.course_list
    if course_name not  in course_list:
        models.Admin.select(admin_user).creat_course(course_name,school_name)
        return True,f'{course_name} 创建成功，绑定给{school_name}校区成功'
    else:
        return False,'当前课程已经存在'


def create_teacher_interface(teacher_name,admin_name):
    teacher_obj = models.Teacher.select(teacher_name)
    if not teacher_obj:
        admin_obj = models.Admin.select(admin_name)
        admin_obj.creat_Teacher(teacher_name)
        return True, '创建成功'
    else:
        return False,f'{teacher_name} 已经存在'





















