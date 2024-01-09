'''
处理数据的保存对象 查看对象
'''
import os
from conf import setting
import pickle
def save_data(obj):
    '''
    保存对象
    '''
    #1、获取对象的保存文件夹路径
    class_name = obj.__class__.__name__
    #以类名 当做 文件夹的名字
    user_dir_path  = os.path.join(
        setting.DB_PATH,class_name
    )
    #2.如果文件夹路径不存在，就创建一个
    if not os.path.exists(user_dir_path):
        os.mkdir(user_dir_path)

    #3.拼接当前用户名的pickle文件路径
    user_path = os.path.join(
        user_dir_path,obj.user
    )
    with open(user_path,'wb') as f:
        pickle.dump(obj,f)


def select_data(cls,username):
    # 1、获取对象的保存文件夹路径
    class_name = cls.__name__
    # 以类名 当做 文件夹的名字
    user_dir_path = os.path.join(
        setting.DB_PATH, class_name
    )
    # 2.如果文件夹路径不存在，就创建一个
    if not os.path.exists(user_dir_path):
        os.mkdir(user_dir_path)

    # 3.拼接当前用户名的pickle文件路径
    user_path = os.path.join(
        user_dir_path, username
    )
    if os.path.exists(user_path):
        with open(user_path, 'rb') as f:
            obj = pickle.load(f)
            return obj
    else:
        return None

