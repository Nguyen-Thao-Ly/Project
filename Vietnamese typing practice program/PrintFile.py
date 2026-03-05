import time

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