# batch_file_rename
# Created by yub at 2019/12/09
import os

# define a update flag
update_flag = 2


def batch_rename(work_dir):
    # os.listdir获取目录文件清单，是列表形式
    for filename in os.listdir(work_dir):
        print(filename)
        if update_flag == 1:
            new_name = 'test' + filename
        elif update_flag == 2:
            name = filename.replace('test','')
            new_name = name
        print(new_name)
        # 定义本文件调用才能更改
        if __name__ == '__main__':
            os.rename(work_dir + filename, work_dir+'/'+new_name)


file = r'C:\\Users\\10640\\Desktop\\金盘项目\\02蓝图设计\\TO-BE流程\\'
batch_rename(file)