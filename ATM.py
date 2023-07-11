print=int(input("enter your four digit pin:"))
password=4518
balance=50000
choice=0
if pin==password:
    if choice!=4:
        print("lists")
        print("1_balance")
        print("2_deposite")
        print("3_withdraw")
        print("4_cancel")
        choice=int(input("enter you option:"))
        if choice==1:
            print("balance=R",balance)
        elif choice==2:
            dep=int(input("enter your deposite R:"))
            balance+=dep
            print("deposited amount:R",dep)
            print("balance=R",balance)
        elif choice==3:
            wit=int(input("enter the to withdraw:R"))
            balance-=wit
            print("withdraw amount:R",wit)
            print("balance=R",balance)
        elif choice==4:
            print("session ended!!goodbye")
        else:
            print("invalid entry!!")
    else:
        print("nothing")
else:
    print("pin incorrect!try again")
    