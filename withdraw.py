from data import dept

def widr():
    print("Enter Amount To Withdraw : ")
    amt = int(input())
    dept.append(-amt)
    print(f"Amount ({amt}) Withdrawl Successful")