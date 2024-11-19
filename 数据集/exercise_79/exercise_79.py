str1 = "abcde"
str2 = "efdis"
str3 = "adk"
print (str1,str2,str3)
if str1 > str2 : str1,str2 = str2,str1
if str1 > str3 : str1,str3 = str3,str1
if str2 > str3 : str2,str3 = str3,str2
print ("after being sorted.")
print (str1,str2,str3)
