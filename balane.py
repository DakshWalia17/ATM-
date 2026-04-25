from data import dept

def bal():
    mon = 0
    for _ in dept:
        mon += _
    print(f"Your Current Balance =  {mon} $")
