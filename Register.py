# Register.py
from Client import *
import getpass, sys, bcrypt
from Database import *
from Bank import *
import secrets
import time


def signup():
    while True:
        Account_number = secrets.choice(range(10000000000, 100000000000))
        cursor.execute("SELECT 1 FROM clients WHERE Account_number = %s", (Account_number,))
        if not cursor.fetchone():
            break

    while True:
        firstname = input("ENTER FIRST NAME:").strip()
        if firstname.isalpha() and len(firstname) <= 25:
            break
        print("INVALID INPUT PLEASE TRY AGAIN")

    while True:
        lastname = input("ENTER LAST NAME").strip()
        if lastname.isalpha() and len(lastname) <= 20:
            break
        print("INVALID INPUT PLEASE TRY AGAIN")
    Username = (firstname + " " + lastname).upper()

    while True:
        try:
            Age = int(input("Enter Age:").strip())
            if 0 < Age <= 100:
                break
            print("INVALID AGE")
        except ValueError:
            print("INVALID INPUT FOR AGE PLEASE TRY AGAIN")

    while True:
        City = input("Enter city").strip()
        if City.isalpha() and len(City) <= 16:
            break
        print("INVALID CITY / LENGTH EXCEEDED")

    while True:
        Mobile_no = input("Enter Mobile No:")
        if len(Mobile_no) == 10 and Mobile_no.isdigit():
            cursor.execute("SELECT 1 FROM clients WHERE Mobile_no = %s", (Mobile_no,))
            if not cursor.fetchone():
                break
        print("Invalid / Already registered")

    while True:
        p1 = getpass.getpass("SET PIN (5-8 digits):")
        p2 = getpass.getpass("CONFIRM PIN:")
        if len(p1) < 5 or len(p1) > 8:
            print("INVALID PIN LENGTH")
            continue
        if p1 != p2:
            print("MISMATCH TRY AGAIN")
            continue
        Pin = bcrypt.hashpw(p1.encode('utf-8'), bcrypt.gensalt(rounds=14))
        break

    print("ACCOUNT CREATED SUCCESSFULLY")
    print(f"USER NAME: {Username}")
    print(f"ACCOUNT NUMBER: {Account_number}")
    print(f"MOBILE NO: {Mobile_no}")
    print(f"AGE: {Age}")
    print(f"CITY: {City}")

    obj = Client(Username, Account_number, Mobile_no, Age, City, Pin)
    obj.createuser()
    bobj = bank(Account_number)
    bobj.create_transaction_table()

def signin():
    try:
        Account_number = int(input("Enter Your Account Number:"))
        cursor.execute("SELECT 1 FROM clients WHERE Account_number = %s", (Account_number,))
        if not cursor.fetchone():
            print("ACCOUNT NOT FOUND")
            choice = input("1: Try again  2: Sign up  3: Exit: ")
            if choice == "1": return signin()
            if choice == "2": signup(); return None
            sys.exit()

        while True:
            Mobile_no = input("Enter Mobile No:")
            if len(Mobile_no) == 10 and Mobile_no.isdigit(): break
            print("Invalid")

        cursor.execute("SELECT Mobile_no, Pin FROM clients WHERE Account_number = %s", (Account_number,))
        row = cursor.fetchone()
        if row and row[0] == Mobile_no:
            attempts = 0
            while True:
                p = getpass.getpass("Enter Pin:")
                if bcrypt.checkpw(p.encode('utf-8'), row[1]):
                    print("Sign in Successfully")
                    return Account_number
                else:
                    attempts+=1
                    if attempts <4:
                        print("INVALID PASSWORD TRY AGAIN")
                        continue
                    else:
                        print("MAXIMUM ATTEMPTS REACHED EXITING")
                        sys.exit()
                        
                        
        else:
            print("ACCOUNT HOLDER NOT FOUND")
            choice = input("1: Try again  2: Sign up  3: Exit: ")
            if choice == "1": return signin()
            if choice == "2": signup(); return None
            sys.exit()
    except ValueError:
        print("Invalid Input")
        return signin()