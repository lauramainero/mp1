num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 > num2 > num3:
    print("maior: " + str(num1))
    print("menor: " + str(num3))
elif num2 > num1 > num3:
    print("maior: " + str(num2))
    print("menor: " + str(num3))
elif num1 > num3 > num2:
    print("maior: " + str(num1))
    print("menor: " + str(num2))
elif num2 > num3 > num1:
    print("maior: " + str(num2))
    print("menor: " + str(num1))
elif num3 > num2 > num1:
    print("maior: " + str(num3))
    print("menor: " + str(num1))
else:
    print("maior: " + str(num3))
    print("menor: " + str(num2))