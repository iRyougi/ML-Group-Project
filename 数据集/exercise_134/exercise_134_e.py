from datetime import date

d1 = date(2021, 3, 22)
d2 = date(2021, 10, 20)

diff = (d2 - d1).days

print(f"The difference between {d1} and {d2} is {diff} days")