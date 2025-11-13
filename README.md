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
