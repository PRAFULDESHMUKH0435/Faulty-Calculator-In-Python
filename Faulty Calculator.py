
             # FAULTY CALCULATOR


print("Faulty calculator for \n45*3=555\n"
      "56+9=77\n"
      "56/6=4\n"
      "")



print("PLEASE ENTER YOUR FIRST NUMBER: ")
a=int(input())
print("PLEASE ENTER YOUR SECOND NUMBER: ")
b=int(input())
print("PLEASE ENTER AN OPERATOR : ")
c=input()





if(a==45 and b==3 and c=="*"):
    print("555")

elif(a==56 and b==9 and c=="+"):
    print("77")

elif(a==56 and b==6 and c=="/"):
    print("4")

elif(c=="*"):
    print(a*b)

elif(c=="+"):
    print(a+b)

elif(c=="/"):
    print(a/b)

elif(c=="+"):
    print(a+b)

elif(c=="-"):
    print(a-b)

else:
    print("Invalid Input")
