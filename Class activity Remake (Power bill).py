
k=0
n=3
i=0
while i <=n:
    i +=1

    name = input("Enter your name:")
    units = int(input("Enter the amount of unit used:"))

    if units>=10 and units<50:
        cost=units*50
        print(name, end="")
        print(" your total cost is #",cost)
    elif units>=50 and units<100:
        cost=(units*50)+85
        print(name, end="")
        print(" your total cost is #",cost)
    elif units>=100 and units<300:
        cost=(units*50)+108
        print(name, end="")
        print(" your total cost is #",cost)
    elif units==300:
        cost=((units*50)+200)
        print(name, end="")
        print(" your total cost is #",cost)
    elif units>300 and units<500:
        cost=((units*50)+200)-((units*50)+200)*0.05
        print(name, end="")
        print(" your total cost is #",cost)
    elif units>=500:
        cost=((units*50)+230)-((units*50)+230)*0.05
        print(name, end="")
        print(" your total cost is #",cost)
    elif units==300:
        k=+1
    else :
        n+= 1
        print("this bill will not be processed it is too little.")

print(k,"Consumer used over 300units")




