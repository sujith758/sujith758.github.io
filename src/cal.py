import sys
#Arguments must be given
arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]
#Giving variables to arguments
num1 = arg2
num2 = arg3
cal = arg1
result = 0
#If condition for getting results and to perform add,multiply and division
if cal == 'add':
    result = int(num1) + int(num2)
    print("operation:", cal, num1, "and", num2, "output:", result)
elif cal == 'mul':
    result = int(num1) * int(num2)
    print("operation:", cal, num1, "and", num2, "output:", result)

elif cal == 'div':
    result = int(num1) / int(num2)
    print("operation:", cal, num1, "and", num2, "output:", result)
