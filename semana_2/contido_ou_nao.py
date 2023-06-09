str1 = input()
str2 = input()
str3 = input()
if (str1 in str2) and (str1 in str3):
    print(str1 + " CONTIDO EM " + str2 + " E " + str1 + " CONTIDO EM " + str3)
elif (str1 not in str2) and (str1 in str3):
    print(str1 + " NÃO CONTIDO EM " + str2 + " MAS " + str1 + " CONTIDO EM " + str3)
elif (str1 in str2) and (str1 not in str3):
    print(str1 + " CONTIDO EM " + str2 + " MAS " + str1 + " NÃO CONTIDO EM " + str3)
else:
    print(str1 + " NÃO CONTIDO EM " + str2 + " E " + str1 + " NÃO CONTIDO EM " + str3)
