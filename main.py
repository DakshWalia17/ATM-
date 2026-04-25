from deposit import dep
from balane import bal
from withdraw import widr
from trans import show_trans
def atm():
    while True:
        print("\nWelcome To GEN-Z Bank\n")
        print("\n Choose Operation  \n")
        print("1.  Deposit Cash               2.  Withdraw\n")
        print("3.  Check Balance              4.  View Transaction History\n")
        choice = (input("\nEnter Operation  --> "))
        if choice.isdigit():
            choice = int(choice)
            if choice == 1 :    dep()
            if choice == 2 :    widr()
            if choice == 3 :    bal()
            if choice == 4 :    show_trans()
            if choice == 5 :    
                print("\nThansk For Your Visit\n")
                break
        
        else:   print("\n------Invalid Operation------\n")    

atm()
