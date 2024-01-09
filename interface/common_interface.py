'''
公共的调用接口
'''
from conf import setting
import  os
def get_all_school_interface():
    school_dir = os.path.join(
        setting.DB_PATH,'School'
    )
    if not os.path.exists(school_dir):
        return False,'请联系管理员新增学校'

    school_list = os.listdir(school_dir)
    return True,school_list




# if __name__ == '__main__':
#     a, b = get_all_school_interface()
#     print(b)