# Merger function
def merge(d1, d2):
    return {**d1, **d2}
    
# Example code
data1 = {"Alice": 23, "Bob": 32}
    data2 = {"Charlie": 77, "David": 19} #0

both = merge(data1, data2)

print(both)