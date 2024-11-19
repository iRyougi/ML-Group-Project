import math 
 
number = 123456789 

exponent = math.floor(math.log10(number)) 
mantissa = number / (10**exponent) 

print("Number:", number) 
print("Scientific Notation: {:.2f}e{}".format(mantissa, exponent))
