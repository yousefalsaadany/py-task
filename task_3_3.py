balance=1000
option=int(input("Select an option(balance=1,deposit money=2,withdraw money=3)"))
if option==1:
    print("Your balance is: ",balance)
elif option==2:
    print("Your balance is: ",balance)
    deposit=int(input("How much money do you want to deposit: "))
    balance+=deposit
    print("You added: ",deposit," | Your New balance: ",balance)
else :
    print("Your balance is: ",balance)
    withdraw=int(input("How much money do you want to withdraw: "))
    if withdraw<=balance:
        balance-=withdraw
        print("You withdrew money : ",withdraw," | Your New balance: ",balance)
    else:
        print("************ Transaction ERROR ************")
