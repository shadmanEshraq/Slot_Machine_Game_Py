import random
import time

#  ---------------------- Global Constants ---------------------- #
MAX_LINES = 3                                    # slot machine lines
MAX_BET = 100                                    # max betting per line
MIN_BET = 1                                      # min betting per line 

ROWS = 3                                         # slot machine rows
COLS = 3                                         # slot machine cols
DELAY = 0.5                                      # Time delay (seconds)
#  ---------------------------------------------------------------- #

# slot machine column symbols dict {symbol: num of symbol}
symbols_count = {
    'A':3,
    'B':5,
    'C':5,
    'D':7
}

# slot machine column symbols value dict {symbol: value of symbol}
symbols_value = {
    'A':5,
    'B':4,
    'C':3,
    'D':2
}
#  -------------------------------------------------------------- #



# ------------------------------------ Function -1 --------------------------------
def deposit():
 """
 Prompts user for depositing money into the slot machine.

  Args:
  -----
    NONE.
    DELAY :   Global Constant, delay amount for text display (seconds)

  Returns:
  --------
    An integer containing the deposit amount .
  """
 while True:
        amount = input("What would you like to deposit ? $:")   # Deposit Prompt
        time.sleep(DELAY)   
        amount = amount.strip()                                 # stripping extra spaces 
        if amount.isdigit():                            # checks if a valid num, stripping spaces
            amount = int(amount)                        # converts to float 
            if amount <= 0:
                print("Deposit amount must be greater than $0 .")
                time.sleep(DELAY)                       # Time delay 
            else:
                break                                    # Deposit successful 
        else:
            print("Please enter a number.")              # Wrong deposit, prompt again 
            time.sleep(DELAY)   

 return amount

# ------------------------------------ Function -2 --------------------------------
def get_num_of_lines():
    """
    Prompts user for choosing number of lines to bet.

    Args:
    -----
    NONE.
    DELAY :   Global Constant, delay amount for text display (seconds)

    Returns:
    --------
        An integer containing the number of lines to bet .
    """
    while True:
        lines = input("Enter the number of lines to bet on (1 -"+str(MAX_LINES)+") ? :")   # Num of lines  Prompt
        lines = lines.strip()                                 # stripping extra spaces 
        if lines.isdigit():                                   # checks if a valid num, stripping spaces
            lines = int(lines)                                # converts to float 
            if 1<= lines <= MAX_LINES:
                break                                             # valid lines 
            else:

                print("Please enter a valid number of lines.")    # prompt
                time.sleep(DELAY) 
        else:
            print("Please enter a number.")                       # Wrong , prompt again 
            time.sleep(DELAY) 

    return lines

# ------------------------------------ Function -3 --------------------------------
def get_bet():
    """
    Prompts user for betting money on the slot machine line.

    Args:
    -----
    None.

    Returns:
    ------
    An integer containing the betting amount per line.
    """
    while True:
        amount = input("What would you like to bet ? $:")   # Deposit Prompt
        amount = amount.strip()                                 # stripping extra spaces 
        if amount.isdigit():                            # checks if a valid num, stripping spaces
            amount = int(amount)                        # converts to int
            if MIN_BET <= amount <= MAX_BET:            # checks the condition
                break                                   # Betting successful 
            else:
                print(f"Betting amount must be between ${MIN_BET} - ${MAX_BET}.")         # Wrong deposit, prompt again       
        else:
            print("Please enter a number.")              # Wrong deposit, prompt again 

    return amount
# ============================================================================================================ #

# ------------------------------------ Function -4 --------------------------------
def get_slot_machine_spin(rows, cols, symbols):
    """
    Runs the slot machine, generates the symbols on each individual column.

    Args:
    -----
    rows:       number of rows of the slot machine.
    cols:       number of columns of the slot machine.
    symbols:    a dictionary containing slot machine symbol and the frequency.

    Returns:
    ------
    columns:    A list of lists- each internal list represents the contents of a single column of the slot machine.
    """
    all_symbols =[]                                    # container list

    # filling up the container list (dict-> List)
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):                  # annonymous variable
            all_symbols.append(symbol)

    columns = []                                       # list of cols- each item represents a column of the machine 

    for _ in range (cols):
        column = []
        current_symbols = all_symbols[:]               # copy of all_symbols
        for _ in range(rows):
            value = random.choice(current_symbols)         # ramdomly choose a symbol
            current_symbols.remove(value)                  # deletes (the 1st occurance) of it from the copied list
            column.append(value)
        
        columns.append(column)                         # add a single column to the container list

    return columns

# ------------------------------------ Function -5 --------------------------------
def print_slot_machine(columns):
    """
    Prints the slot machine symbols, mimics the slot machine 'display'.

    Args:
    -----
    columns:    A list of lists- each internal list represents the contents of a single column of the slot machine.
    DELAY :     Global Constant, delay amount for text display (seconds)

    Returns:
    ------
    None
    """
    print("# ----------------------------------------------------- #")
    print("                  Machine spinning...                    ")
    print("# ----------------------------------------------------- #")
    time.sleep(DELAY)                                                             # time delay                                                  

    # performing 'the column Transpose'
    for row in range(len(columns[0])):               # num rows = num of elements in a column
        for i,column in enumerate(columns):          # looping over the individual columns 
            if i != len(columns)-1:                  # pipe operator wont be printed for the last element of a row
                print(column[row],end=" | ") 
            else:
                 print(column[row],end="") 
                 
        print()                                                 # starts a new line to print the next row   
        print("---------")                                      # pretty display  
        time.sleep(DELAY)                                       # time delay           
    return None

# ------------------------------------ Function -6 --------------------------------
def check_winnings(columns, lines, bet, symbols_value):
    """
    Prints the slot machine symbols, mimics the slot machine 'display'.

    Args:
    -----
    columns:            A list of lists- each internal list represents the contents of a single column of the slot machine.
    lines:              Number of lines the player has placed bets.
    bet:                Betting amount on a single line. 
    symbols_value:      A dictionary containing the symbols as keys and corresponding value of the symbol as values. 

    Returns:
    ------
    winnings              :    An integer representing the amount the player won for a single round.
    winning_line          :    An list representing the index of the lines a player won for a single round.
    """
    winnings = 0                                     # won amount on a single round 
    winning_line = []                                # list of lines(index) that the player has won on

    # Symbol checking logic
    for line in range(lines):
        first_symbol = columns[0][line]               # get the first symbol of a line (row)
        for column in columns:
            symbol_to_check = column[line]            # keep checking with other symbols 
            if (first_symbol != symbol_to_check):
                break                                 # no match, break the loop
        else:
            winnings += symbols_value[first_symbol] * bet    # update and increment the winning amount 
            winning_line.append(line+1)                      # update the list of winning line 
    
    return winnings, winning_line



# ------------------------------------ Function -7 --------------------------------
def spin(balance):
    """
    Generates one complete spin (1 round) of the solt machine game.

    Args:
    -----
    balance :             Updated balance after the previous spin
    DELAY :               Global Constant, delay amount for text display (seconds)

    Returns:
    ------
    (winnings-total_bet)  :  the won (positive) or lost(negative) amount by the player in a single round(spin) of the game .
    """

    lines = get_num_of_lines()                                   # get number of lines to bet 

    # checks if the player has enough balance to bet
    while True:
            bet = get_bet()                                      # get betting amount per line 
            total_bet = bet*lines                                # calculates total bet on a single round

            if total_bet > balance:
                print(f"You do not have enough amount to bet. Your current balance is ${balance}")
            else:
                break

    print(f'You are betting ${bet} on {lines} lines. Total bet is $ {total_bet}')            # Showing status to the player 

    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)                          #  Generating the Slot Machine
    time.sleep(DELAY)
    print_slot_machine(slots)                                                         #  display of the machine slots
    time.sleep(DELAY)
    winnings, winning_lines = check_winnings(slots,lines,bet,symbols_value)           #  checks the winning amount, winning lines 

    time.sleep(DELAY)
    print("----------------------------------------------------------------------------------------------")  
    print(f"You won ${winnings} on this round !")                                # winning status 
    print(f"You won on lines : ", *winning_lines)                                # splat/ unpack operator
    print(f"You net winning amount on this round is  : $ {winnings-total_bet}")    # splat/ unpack operator
    print("----------------------------------------------------------------------------------------------")  

    return winnings-total_bet                                     # the won/lost amount in a single round  



# ------------------------------------ Function -8 --------------------------------
def welcome_msg():
    """
    Displays a welcome message to the user.

    Args:
    -----
    NONE.
    DELAY       -   Global Constant, delay amount for text display (seconds).

    Returns:
    ------
    None.
    """
    time.sleep(DELAY*2)
    print(" ================== Welcome to the Slot Machine Game ================== ")                    # closing message  
    time.sleep(DELAY) 
    print("# ------------$$$ Today might be your lucky day! $$$ ----------------- #") 
    time.sleep(DELAY*2)


    return None
# ============================================================================================================ #


# ------------------------------------ Function - 9 --------------------------------
def goodbye_msg(balance,starting_balance):
    """
    Displays exit messages to the user at the end of the game.

    Args:
    -----
    balance             -   The updated balance at the end of the game.
    starting_balance    -   The initial balance at the beginning of the game.
    DELAY               -   Global Constant, delay amount for text display (seconds)

    Returns:
    ------
    None.
    """
    time.sleep(DELAY*1.5)
    print(" ------------------ !!! Game over !!! ------------------ ")                    # closing message  
    time.sleep(DELAY) 
    print("# ===================================================== #") 
    print(f"-----------------( You left with ${balance} )-------------------")                   # closing message 
    
    time.sleep(DELAY*1.5)
    # different messages based on the net balance
    if (balance < starting_balance):                                             # net win
        print("#------------( Better luck next time... )--------------#") 
    elif (balance > starting_balance):                                           # net loss
        print("# --------(Congratulations on the winnings !)--------- #") 
        print("# --------   ( See you on the next game ! )  --------- #")
    else:                                                                        # break even
        print("# ---------- (Wow, you are on break-even !)----------- #") 
        print("# -------- (Best wishes for the next game !) ----------#")

    # closing message 
    print("# ===================================================== #") 
    print("#--- Please run the script again to start a new game ---#")                   


    return None
# ============================================================================================================ #




