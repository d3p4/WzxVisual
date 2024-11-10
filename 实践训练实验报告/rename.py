import os

# 定义前缀
prefix = "2021111015位志轩"

# 获取当前目录
current_directory = os.getcwd()

# 遍历当前目录的所有文件
for filename in os.listdir(current_directory):
    # 检查是否为文件（排除目录）
    if os.path.isfile(filename):
        # 创建新文件名
        new_filename = prefix + filename
        # 重命名文件
        os.rename(filename, new_filename)
        print(f'Renamed: {filename} to {new_filename}')