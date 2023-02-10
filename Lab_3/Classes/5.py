class account:
    Owner = "Name"
    Balance = 0.0
    def WithDraw():
        mon = float(input("How much you want to withdraw\n"))
        if mon > account.Balance:
            print("Not enough")
        else:
            account.Balance -= mon
        print("You have ", account.Balance, "$")
    def Deposit():
        mon = float(input("How much you want to deposit\n"))
        account.Balance += mon
        print("You have ", account.Balance, "$")


Acc1 = account
Acc1.Owner = "David"
Acc1.Balance = 45000.0
Acc1.WithDraw()
Acc1.Deposit()
    
        