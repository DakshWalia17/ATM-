# GEN-Z Bank ATM Simulator

A simple command-line ATM (Automated Teller Machine) simulation program written in Python. This project demonstrates basic Python concepts such as loops, conditionals, functions, user input, and modular programming by separating logic into different files.

## Features

- **Deposit Cash:** Add money to your account.
- **Withdraw Cash:** Take money out of your account.
- **Check Balance:** View your current account balance.
- **Transaction History:** View a log of all deposits and withdrawals.
- **Simple Console UI:** An interactive text-based interface.

## Prerequisites

- Python 3.x installed on your system.

## How to Run

1. Clone this repository or download the source code.
2. Open your terminal or command prompt.
3. Navigate to the directory containing the project files.
4. Run the main script using Python:

   ```bash
   python main.py
   ```

## File Structure

The project is broken down into several modular files for better organization:

- `main.py` - The entry point of the application. It handles the main loop and user menu.
- `data.py` - Acts as a simple in-memory database (using a Python list) to store transaction records.
- `deposit.py` - Contains the logic for depositing money.
- `withdraw.py` - Contains the logic for withdrawing money.
- `balane.py` - Calculates and displays the current account balance.
- `trans.py` - Displays a formatted history of all transactions.

## Usage Example

When you run the script, you'll see a menu like this:

```text
Welcome To GEN-Z Bank

 Choose Operation  

1.  Deposit Cash               2.  Withdraw

3.  Check Balance              4.  View Transaction History

Enter Operation  --> 
```

Type the number corresponding to the operation you want to perform and press Enter. To exit the program, you can enter `5`.

## Future Enhancements

Ideas for future improvements:
- Add persistent storage (save transactions to a `.txt` or `.csv` file).
- Add user authentication (PIN verification).
- Implement overdraft limits and balance validation to prevent withdrawing more than the current balance.
- Enhance error handling for invalid input (e.g., entering letters instead of numbers for amounts).
