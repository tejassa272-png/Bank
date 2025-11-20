from Database import *

class Client():
    def __init__(self,Username,Account_number,Mobile_no,Age,City,Pin):
        self.__Username = Username
        self.__Account_number = Account_number
        self.__Mobile_no = Mobile_no
        self.__Age = Age
        self.__City = City
        self.__Pin = Pin


    def createuser(self):
        cursor.execute("""
                INSERT INTO clients 
                (Username, Account_number, Mobile_no, Age, City, Pin, Balance, Status)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                self.__Username,
                self.__Account_number,
                self.__Mobile_no,
                self.__Age,
                self.__City,
                self.__Pin,
                0,
                1
            ))
        db.commit()
