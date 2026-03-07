import time, os

RESET = "\033[0m"
GREEN = "\033[92m"
RED = "\033[91m"
GREY = "\033[90m"
BLUE = "\033[96m"
YELLOW = "\033[93m"

SLOW = 0.03
FAST = 1e-9

def slow_print(text, delay = SLOW):
    for c in text:
        print(c, end = "", flush = True)
        time.sleep(delay)
    print()

def fast_print(text, delay = FAST):
    for c in text:
        print(c, end = "", flush = True)
        time.sleep(delay)
    print()

def print_color(color, text, slow = False):
    if slow:
        slow_print(color + text + RESET)
    else:
        fast_print(color + text + RESET)

def show_mistake(text, user_input, label_example, label_user): 
    user_input += " "*(len(text)-len(user_input))
    print(label_example, end = '')
    for i in range(len(text)) :
        if user_input[i] != text[i] : print(RED + text[i] + RESET, end = '')
        else : print(GREEN + text[i] + RESET, end = '')
    
    print("\n" + label_user, end = '')
    for i in range(len(text)) :
        if user_input[i] != text[i] : print(RED + user_input[i] + RESET, end = '')
        else : print(GREEN + user_input[i] + RESET, end = '')
    print("\n", end = '')    

        
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

