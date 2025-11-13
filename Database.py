import mysql.connector as sql
import getpass
import sys

print("=== Secure Bank Database Connection ===")
passwd = getpass.getpass("Enter MySQL root password: ")
    
try:
    db = sql.connect(
                host = "localhost",
                user = "root",
                passwd = passwd,
                database = "my"    
    ) 
except sql.Error as err:
    print("Wrong Password, Access Denied") 
    sys.exit()
cursor = db.cursor()


def create_client_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
        Username       VARCHAR(30)   NOT NULL,
        Account_number BIGINT UNSIGNED NOT NULL UNIQUE,
        Mobile_no      VARCHAR(12)   NOT NULL UNIQUE,
        Age            INTEGER       NOT NULL,
        City           VARCHAR(20)   NOT NULL,
        Pin            VARBINARY(300) NOT NULL,
        Balance        BIGINT        NOT NULL DEFAULT 0,
        Status         TINYINT(1)    NOT NULL DEFAULT 1,
        PRIMARY KEY (Account_number)
        )
        ''')
    db.commit()

create_client_table()