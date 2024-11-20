def calculate_distance_and_height(height, times):
    total_distance = 0
    current_height = height

    for i in range(1, times + 1):
        # 从第二次开始，落地时的距离应该是反弹高度乘以2（弹到最高点再落下）
        if i == 1:
            total_distance += current_height
        else:
total_distance += current_height * 2  # 每次下落和反弹的距离  #3
        current_height /= 2  # 反弹后的高度

    return total_distance, current_height


# 初始高度为100米，计算第10次落地时的总距离和反弹高度
height = 100
bounce_times = 10
total_distance, final_height = calculate_distance_and_height(height, bounce_times)

print(f"第{bounce_times}次落地时，共经过 {total_distance} 米。")
print(f"第{bounce_times}次反弹的高度为 {final_height} 米。")
