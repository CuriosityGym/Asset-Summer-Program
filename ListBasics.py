primesList=[]
p=input("Please enter a number")
p=int(p)

for index in range(0,p+1):
    primesList.append(index)


for prime in range(2,p+1):
    for primeIndex in range (prime*2, p+1, prime):
        primesList[primeIndex]=0
        #print(primeIndex)


while 0 in primesList:
    primesList.remove(0) 
print(primesList)
