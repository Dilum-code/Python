print("1-Add")
print("2-Substract")
print("3-Muliply")
print("4-Divide")
 
option = int(input("Select and option from above"))

if(option in [1,2,3,4]):
    num1 = int(input("Enter 1st Number"))
    num2 = int(input("Enter 2nd Number"))
    if(option ==1):
        result=num1+num2
    elif(option == 2):
        result=num1-num2
    elif(option ==3):
        result=num1*num2
    else:
        result=num1 // num2

else:
    print("Invalid operation")

print("Result is {}".format(result))
