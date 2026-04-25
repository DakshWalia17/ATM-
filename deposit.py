
from data import dept

def dep():
    print("Enter Amount To Deposit")
    amt = int(input())
    dept.append(amt)
    print(f" Amount {amt} was Successfully Deposited To Your Account.")

