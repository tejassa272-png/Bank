from Database import *



class bank():
    def __init__(self,Account_number):
        self.__Account_number = Account_number
    
    def create_transaction_table(self):
        table_name = f"{self.__Account_number}_Transaction"
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS `{table_name}`(
            id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            timedate VARCHAR(30) NOT NULL,
            Account_number BIGINT UNSIGNED NOT NULL,
            remarks VARCHAR(100) NOT NULL,
            amount BIGINT NOT NULL,
            balance BIGINT NOT NULL DEFAULT 0 )ENGINE InnoDB 
            """  )
        db.commit()
    
    def balanceenquiry(self):
        temp = cursor.execute("SELECT Balance FROM clients WHERE Account_number= %s",(self.__Account_number,))
        temp = cursor.fetchone()
        print(f"\nBALANCE IS {temp[0]}")
    
    def deposit(self,amount):
        temp = cursor.execute("SELECT Balance FROM clients WHERE Account_number = %s",(self.__Account_number,))
        temp = cursor.fetchone()
        temp1 = amount + temp[0]
        cursor.execute("UPDATE clients SET Balance = %s WHERE Account_number = %s",
                      (temp1, self.__Account_number))
        db.commit()

        table = f"{self.__Account_number}_Transaction"
        query = f"""
                INSERT INTO `{table}` 
                (timedate, Account_number, remarks, amount, balance)
                VALUES (NOW(), %s, 'CREDIT', %s, %s)
                """
        cursor.execute(query,(self.__Account_number,amount,temp1))
        db.commit()
        print(f"Amount Successfully Credited Into {self.__Account_number}")
    
    
    def withdraw(self,amount):
        temp = cursor.execute("SELECT Balance FROM clients WHERE Account_number = %s",(self.__Account_number,))
        temp = cursor.fetchone()
        if amount>temp[0]:
            print("INSUFFICENT BALANCE")
            return
        else:
            temp1 = temp[0] - amount
        cursor.execute("UPDATE clients SET Balance = %s WHERE Account_number = %s",
                       (temp1,self.__Account_number))
        db.commit()
        table = f"{self.__Account_number}_Transaction"
        query = f"""
                INSERT INTO `{table}`
                (timedate,Account_number,remarks,amount,balance)
                VALUES(NOW(),%s,'DEBIT',%s, %s)
                """
        cursor.execute(query,(self.__Account_number,amount,temp1))
        db.commit()
        print(f"Amount Successfully Debited From {self.__Account_number}")
        
        
    def fundtransfer(self,receive,amount):
        temp = cursor.execute("SELECT Balance FROM clients WHERE Account_number = %s",(self.__Account_number,))
        temp = cursor.fetchone()
        if amount > temp[0]:
            print("INSUFFICIENT MONEY")
            return
        else:
            temp1 = cursor.execute("SELECT Balance FROM clients WHERE Account_number = %s",(receive,))
            temp1 = cursor.fetchone()
            if not temp1:
                print("ACCOUNT NUMBER DOES NOT EXISTS")
                return
            else:
                test1 = temp[0] - amount
                test2 = amount + temp1[0]
                cursor.execute("UPDATE clients SET Balance = %s where Account_number = %s",(test1,self.__Account_number))
                db.commit()
                cursor.execute("UPDATE clients SET Balance = %s where Account_number = %s",(test2,receive))
                db.commit()

                
                #reciver
                cursor.execute(
                    f"INSERT INTO `{receive}_Transaction`"
                    f"(timedate,Account_number,remarks,amount,balance)"
                    f"VALUES(NOW(),%s, %s, %s , %s)",
                    (receive,f"AMOUNT RECEIVED FROM {self.__Account_number}",amount,test2))
                
                #sender
                cursor.execute(
                    f"INSERT INTO`{self.__Account_number}_Transaction`"
                    f"(timedate,Account_number,remarks,amount,balance)"
                    f"VALUES(NOW(),%s,%s,%s,%s)",
                    (self.__Account_number,f"AMOUNT TRANSFERED TO {receive}",amount,test1))
                
                db.commit()
                print(f"{amount} SUCCESSFULLY TRANSFERRED")
        
