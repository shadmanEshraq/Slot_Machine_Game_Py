
import time
import game_runner as gr

#  ---------------------- Global Constants ---------------------- #
DELAY = 0.5                                      # Time delay (seconds)
#  ---------------------------------------------------------------- #




# ===============================================[Main Body]====================================================== #
def main():
    
    gr.welcome_msg()                                        # Displays a welcome message to the player
    balance = gr.deposit()                                  # get deposit money
    starting_balance = balance                              # Save the initial balance 

    # ------------------- Playing the Game ------------------- #
    
    while (balance > 0):                                                # if the palyer has non-zero balance
        print(f"Current balance is : ${balance}")
        command = (input("Press any button to play (q to quit) : ")).lower()
        time.sleep(DELAY)
        if command == 'q':
            time.sleep(DELAY)
            break                                                       # ends the game 
        else:
            balance += gr.spin(balance)                                 # runs a spin of slot machine (1 round) and updates the balance
            time.sleep(DELAY)
    # ----------------------------------------------------- #

    gr.goodbye_msg(balance,starting_balance)                            # goodbye message





    
# ================================================================================================================= #


# ---------- [Run the Game]  ---------- #
if __name__=='__main__':
    main()