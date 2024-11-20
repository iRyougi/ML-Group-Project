import copy  # 导入 copy 模块

names = ["Alice", "Bob", "Charlie"]

# 使用 copy.deepcopy() 进行深拷贝
names_clone = copy.deepcopy(names)

print(names_clone)  # 输出: ['Alice', 'Bob', 'Charlie']
