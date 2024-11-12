import os

print(len([file for file in os.listdir('.') if os.path.isfile(file)]))