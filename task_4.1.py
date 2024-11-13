import math


start=int(input("Enter the start num: "))
end=int(input("Enter the end num: "))
if start<=2 :
    print(2,end=" ")
    start=3
for i in range(start,end):
    
    prime=True
    for j in range(2,int(math.sqrt(i)+1)):
        if i%j==0:
            prime=False
            break

    if prime==True :
        print(i,end=" ")
        
