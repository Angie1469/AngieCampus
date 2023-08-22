p=int(input("Diga los nums: "))  
for i in range(1,p+1):              
    term1=1                         
    term=i
    if i%2==0:
        print("-",term1,"/",i, end="   ")
    else:
        print("1")
        print("+",term1,"/",i, end="   ")