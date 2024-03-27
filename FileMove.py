import os
import shutil

source_dir = "../../../百峰网后台备份"

# 获取源目录下的所有文件名
files = os.listdir(source_dir)

# 遍历所有文件名
for fileName in files:
    # 获取id
    id = fileName[:5]
    # 拼接目标目录路径
    target_dir = os.path.join(source_dir, id)
    # 判断目标目录是否存在，若不存在则创建目录
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    # 将文件移到目标目录下
    shutil.move(os.path.join(source_dir, fileName), os.path.join(target_dir, fileName))
