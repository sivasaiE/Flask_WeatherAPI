import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLUMNS = 3

symbols = {
    "A":1,
    "B":2,
    "C":3,
    "D":4
}

values = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def slot_winnings(columns, bet, lines, values):
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += bet*values[symbol]
            print(f'Your total winnings is {winnings}')
    return winnings




def get_slot_machine_spin(ROWS, COLUMNS, symbols):
    all_symbols = []
    for symbol, symbol_value in symbols.items():
        for _ in range(symbol_value):
            all_symbols.append(symbol)

    columns = []
    for _ in range(COLUMNS):
        current_column = all_symbols[:]
        column = []
        for _ in  range(ROWS):
            value = random.choice(current_column)
            current_column.remove(value)
            column.append(value)

        columns.append(column)
    return columns


def print_slot_spins(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i!= len(columns)-1:
                print(column[row], "|", end = ' ')
            else:
                print(column[row])


def deposit():
    while True:
        amount = input("Enter amount in rupees:")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("Enter amount which is greater then zero:")
        else:
            print("Enter a valid amount")
    return amount

def get_lines():
    while True:
        lines = input("Enter lines in (1-"+str(MAX_LINES)+"):")
        if lines.isdigit():
            lines = int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print("Enter lines which is greater then zero:")
        else:
            print("Enter a valid lines")
    return lines

def get_bet():
    while True:
        bet = input("Enter bet in (1-"+str(MAX_BET)+"):")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET<=bet<=MAX_BET:
                break
            else:
                print(f'Enter bet between :{MIN_BET} and {MAX_BET}')
        else:
            print("Enter a valid bet")
    return bet

def spin_winnings(balance):
    balance = deposit()
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = lines*bet
        if balance < bet:
            print(f"You cannot bet amount greater than your balance as your balance is {balance}$")
        else:
            break
    print(f"you are betting {bet}$ on {lines} lines and your total balance is {bet*lines}$")

    slots = get_slot_machine_spin(ROWS, COLUMNS, symbols)
    print_slot_spins(slots)

    winnings = slot_winnings(slots, bet, lines, values)
    return winnings-total_bet

def main():
    balance = deposit()
    while True:
        print(f'your current balance is {balance}$')
        spin = input("press enter to continue | q to quit:")
        if spin=="q":
            break
        else:
            balance+=spin_winnings(balance)
        
    

main()