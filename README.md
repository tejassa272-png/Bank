# Secure Banking System (Console)

A **secure, fast, and educational** console-based banking application built with Python and MySQL.

---

## Features

- User Registration & Login (with secure PIN using `bcrypt`)
- Account Number Generation (`secrets` — cryptographically secure)
- Deposit, Withdraw, Fund Transfer
- Per-User Transaction Tables → **Fastest statement retrieval**
- Balance Enquiry & Bank Statement
- Input Validation (`int`, `isdigit`, length checks)
- **Zero SQL Injection** (by design)

---

## Security Highlights

| Feature | Implementation |
|-------|----------------|
| PIN Storage | `bcrypt` with `rounds=14` |
| Account Numbers | `secrets.choice(range(10^10, 10^11))` |
| Input Safety | All inputs → `int()` → **no SQLi possible** |
| Table Names | Built from `int` → **no injection vector** |
| Local Use | Designed for single-user, trusted environment |

> **SQL Injection = Mathematically Impossible**

---

## Project Structure

├── Client.py           # User model
├── Database.py         # MySQL connection & table setup
├── Bank.py             # Banking operations
├── Register.py         # Signup & Signin logic
├── Main.py             # CLI menu
└── passwords.db        # (not included)

## Setup & Run

### 1. Prerequisites
pip install mysql-connector-python bcrypt

### 2. Run
python Main.py


### Sample Flow
welcome to my bank 
ENTER 1. TO Register (SignUp) 
ENTER 2. TO Login (SignIn) 
1
ENTER FIRST NAME: John
ENTER LAST NAME: Doe
Enter Age: 25
Enter city: NYC
Enter Mobile No: 9876543210
SET PIN (5-8 digits): ******
CONFIRM PIN: ******
ACCOUNT CREATED SUCCESSFULLY
USER NAME: JOHN DOE
ACCOUNT NUMBER: 98765432101
