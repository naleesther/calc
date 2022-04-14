#22from distutils.log import error


num1=int(input("Enter a number"))
num2=int(input("Enter another number"))
op= input("Enter operator type")
if op=="multiply":
    print(num1*num2)
elif op=="addition":
    print(num1+num2)
elif op=="subtraction":
    print(num1-num2)
elif op=="division":
     print(num1%num2)
else:
       print("error" )   