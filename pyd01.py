str1 = input()
str2 = input()
str3 = input()
str4 = input()
num1 = float(str1)
num2 = float(str2)
num3 = float(str3)
num4 = float(str4)
print("|{0:>7.2f} {1:>7.2f}|".format(num1,num2))
print("|{0:>7.2f} {1:>7.2f}|".format(num3,num4))
print("|{0:<7.2f} {1:<7.2f}|".format(num1,num2))
print("|{0:<7.2f} {1:<7.2f}|".format(num3,num4))