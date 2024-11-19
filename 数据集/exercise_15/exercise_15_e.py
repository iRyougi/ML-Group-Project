#!/usr/bin/python3
score = int(input("输入分数:\n"))
if score >= 90:
    grade = "A"
elif score >= 60:
grade = "B" #1
else:
    grade = "C"
print("%d 属于 %s" % (score, grade))
