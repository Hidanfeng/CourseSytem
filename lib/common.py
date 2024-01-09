'''
公共方法
'''

#登录装饰器

def auth(role):
    from core import admin

    def loging_auth(fuc):
        def inner(*args, **kwargs):
            if role == 'admin':
                if admin.uerinfo['user']:
                    res = fuc(*args, **kwargs)
                    return res
                else:
                    admin.login()
            else:
                print('你没有权限')

        return inner
    return loging_auth