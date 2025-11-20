from Register import *
from Bank import*
Status = False
print ("welcome to my bank ")
while True:
    try:
        print("ENTER 1. TO Register (SignUp) ")
        print("ENTER 2. TO Login (SignIn) ")
        choice = input()
        if choice == '1':
            signup()
        elif choice == '2':
            user = signin()
            Status = True
            break
        else:
            print("INVALID INPUT")
    except ValueError:
        print("INVALID INPUT")
        continue
    
if Status:
    while user:
        print("\n==BANKING OPERATIONS==")
        print("Enter 1 to Deposit")
        print("Enter 2 to Withdraw")
        print("Enter 3 to Check Balance")
        print("Enter 4 to Transfer Funds")
        print("Enter 5 to Get Bank Statement")
        print("Enter 6 to Exit")
        try:
            choice = int(input("ENTER YOUR CHOICE: "))
            if choice<0 or choice>7:
                print("ENTER VALID INPUT")
                continue 
            else: 
                if choice == 1:
                    while True:
                        try:
                            amount = int(input("ENTER THE AMOUNT TO BE DEPOSITED:"))
                            if amount and amount>0:
                                bobj = bank(user)
                                bobj.deposit(amount)
                                bobj.balanceenquiry()
                                break
                            else:
                                print("ENTER ONLY IN DIGITS") 
                        
                        except ValueError:
                            print("ENTER VALID INPUT")
                            continue
                
                elif choice == 2:
                    while True:
                        try:
                            amount = int(input("ENTER THE AMOUNT TO BE DEBITED:"))
                            if amount:
                                bobj = bank(user)
                                bobj.withdraw(amount)
                                bobj.balanceenquiry()
                                break
                        except ValueError:
                            print("ENTER VALID INPUT")
                            continue
            
                elif choice == 3:
                    bobj = bank(user)
                    bobj.balanceenquiry()
                
                elif choice == 4:
                    while True:
                        try:
                            receive = int(input("ENTER THE RECEIVERS ACCOUNT NUMBER:"))
                            if receive:
                                try:
                                    amount = int(input("ENTER THE AMOUNT TO BE TRANSFERRED:"))
                                    if amount:
                                        bobj = bank(user)
                                        bobj.fundtransfer(receive,amount)
                                        bobj.balanceenquiry()
                                        break
                                    else:
                                        print("INVALID INPUT")
                                        continue   
                                except ValueError:
                                    print("INVALID INPUT")
                                    continue                              
                            else:
                                print("INVALID INPUT")
                                continue
                        except ValueError:
                            print("ENTER VALID INPUT")
                            continue
                
                elif choice == 5:
                    bobj = bank(user)
                    cursor.execute(f"SELECT timedate, remarks, amount, balance FROM `{user}_Transaction` ORDER BY id")
                    print("\nTRANSACTION HISTORY")
                    print("-"*70)
                    for row in cursor.fetchall():
                        print(f"{row[0]} | {row[1]:35} | {row[2]:10} | Bal: {row[3]}")
                
                elif choice == 6:
                    print("THANK YOU")    
                    break  
                        
        except ValueError:
            print("ENTER VALID INPUT")
            continue
