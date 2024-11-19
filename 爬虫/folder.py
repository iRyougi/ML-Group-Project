import os
import shutil
import json

# 设置源文件夹路径
source_folder = r"example"
# 设置目标文件夹路径
target_folder = r"example"  # 可以自己设定目标位置

# 创建目标文件夹，如果不存在
os.makedirs(target_folder, exist_ok=True)

# 遍历文件编号101到190
for i in range(101, 191):
    # 定义文件名和对应文件夹路径
    file_name = f"exercise_{i}.py"
    folder_name = f"exercise_{i}"
    folder_path = os.path.join(target_folder, folder_name)

    # 创建对应文件夹
    os.makedirs(folder_path, exist_ok=True)

    # 源文件路径
    source_file = os.path.join(source_folder, file_name)

    # 目标文件路径
    target_file = os.path.join(folder_path, file_name)

    # 复制代码文件到目标文件夹
    if os.path.exists(source_file):
        shutil.copy2(source_file, target_file)

        # 创建代码文件的副本 (exercise_X_e.py)
        e_copy_file = os.path.join(folder_path, f"exercise_{i}_e.py")
        shutil.copy2(source_file, e_copy_file)

        # 创建空的 JSON 文件 (result_X.json)
        result_file = os.path.join(folder_path, f"result_{i}.json")
        with open(result_file, "w") as json_file:
            json.dump({}, json_file)

print("文件已成功分配到各个文件夹中。")
