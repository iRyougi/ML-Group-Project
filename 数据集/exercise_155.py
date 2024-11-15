# A program that converts a string to camel-case
def camel(string):
    words = string.split(" ")
    parts_upper = [word.title() for word in words]
    return "".join(parts_upper)

# Example run
string = "this is a test"
camel = camel(string)

print(camel)