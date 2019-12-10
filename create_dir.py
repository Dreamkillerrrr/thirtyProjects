# Script name  : create a dir
# Author       : yub
# Created      : 2019/12/10

# import os module
import os


def create_dir(file_name):
    try:
        home = os.path.expanduser('~')
        print(home)
        if not os.path.exists(os.path.join(home, file_name)):
            os.makedirs(os.path.join(home, file_name))
        else:
            print('the directory already exists')
    except Exception as e:
        print(e)


create_dir('testdirectory')
