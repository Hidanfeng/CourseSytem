import os,sys
from core import src

sys.path.append(
    os.path.dirname(__file__)
)

if __name__ == '__main__':
    print(sys.path)
    src.run()


