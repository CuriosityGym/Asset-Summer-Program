firstNo=input("Please put the first number: ")
secondNo=input("Please put the second Number: ")
operation=input("What would you like to do? 1)Add 2)Subtract 3)Multiply 4) Divide: ")

firstNo=int(firstNo)
secondNo=int(secondNo)
operation=int(operation)
#print(firstNo+secondNo)

if(operation==1):
    print(firstNo+secondNo)
if(operation==2):
    print(firstNo-secondNo)
if(operation==3):
    print(firstNo*secondNo)
    
if(operation==4):
    if(secondNo!=0):
        print(firstNo/secondNo)
    else:
        print("Division by 0 not allowed")




