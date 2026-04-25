from data import dept

def show_trans():
    print("\n--- Transaction History ---")
    if len(dept) == 0:
        print("No transactions yet.")
    else:
        i = 1
        for amount in dept:
            if amount > 0:
                print(f"{i}. Deposit:    +{amount} $")
            else:
                print(f"{i}. Withdrawal: {amount} $")
            i += 1
    print("---------------------------\n")
