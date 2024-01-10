'''
用于存放类
学校类 学员类 课程类 讲师类 管理员类
'''
from db import db_handler

class Base():

    @classmethod
    def select(cls, username):
        obj = db_handler.select_data(cls, username)
        return obj

    def save(self):
        '''
        保存数据
        :return:
        '''
        db_handler.save_data(self)

class Admin(Base):
    '''
    管理员类
    '''
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd

    def creat_school(self,school_name,school_addr):
        school_obj = School(school_name,school_addr)
        school_obj.save()


    def creat_course(self,course_name,school_name):
        #创建课程
        course_obj = Course(course_name)
        course_obj.save()
        #获取当前学校对象，更新course_list
        school_obj = School.select(school_name)
        school_obj.course_list.append(course_name)
        school_obj.save()

    def creat_Teacher(self,teacher_name):
        teacher_obj = Teacher(teacher_name)
        teacher_obj.save()




class School(Base):
    def __init__(self,user,addr):
        self.user = user
        self.addr = addr
        self.course_list = []




class Course(Base):
    def __init__(self,user):
        self.user = user



class Teacher(Base):
    def __init__(self,user):
        self.user = user

