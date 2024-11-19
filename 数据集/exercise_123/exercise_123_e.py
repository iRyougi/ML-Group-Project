# 1
num_strs = input("Give a comma-separated numbers: ")

# 2
num_str_list = num_strs.split(",")

# 3
num_ints = [int(num_str) for num_str in num_str_list]

# 4
reversed_nums = list(reversed(num_ints))

    print(reversed_nums) #0