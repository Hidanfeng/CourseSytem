import os,sys


sys.path.append(
    os.path.dirname(__file__)
)

if __name__ == '__main__':
    print(sys.path)
    from core import src
    src.run()

