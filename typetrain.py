import curses
from curses import wrapper      
import time
import random


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    entry_message(stdscr)
    
    while(True):

        wpm_type(stdscr)
        stdscr.addstr(2 ,0 ,"You finished the race! Press anything to continue or exit with the escape button ... ")
        key = stdscr.getkey()

        if ord(key) == 27:
            break


def entry_message(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to Typing training .  press any key to start ... (press escape to exit!)")
    stdscr.refresh()
    stdscr.getkey()
   



def Showing_text(stdscr , targeted, current,wpm=0):
    stdscr.addstr(targeted)
    stdscr.addstr(1 ,0 ,f"wpm = {wpm}")

    for i , char in enumerate(current):
        correct = targeted[i]
        color = curses.color_pair(1)

        if  char != correct:
             color = curses.color_pair(2)

        stdscr.addstr(0, i, char, color)




def dict():
    with open("dict.txt" , "r") as f:
        line = f.readlines()
        return repeated_word(random.choice(line).strip())




def repeated_word(the_word):
    words = []
    the_word = the_word

    for i in range(0,10):
        words.append(the_word)
    
    finished_word = ' '.join([str(item) for item in words])
    return finished_word



def users_word(stdscr):
    user_text = []
    stdscr.clear()
    stdscr.addstr("Write your word!:")
    stdscr.nodelay(True)
    while (True):

        try:
            key = stdscr.getkey()
        except:
            continue

        if ( key == '\n'):
            stdscr.nodelay(False)
            return repeated_word("".join(user_text))

        if ord(key) == 27:
            break

        if key in ("KEY_BACKSPACE", '\b', "\x7f" ):
            if len(user_text) > 0:
                user_text.pop()
                #user_text.append(" ")
                
                stdscr.clrtoeol()
                stdscr.refresh() 
               
                                      
        else:
            user_text.append(key)

        for i , char in enumerate(user_text):
            stdscr.addstr(0, i+17, char)

            
                



def wpm_type(stdscr):
    stdscr.clear()
    stdscr.addstr("Press 'Y' to enter your word or 'U' for one of our words")

    Entry_key = stdscr.getkey()

    if Entry_key in ("u" ,"U"):
            target_text = users_word(stdscr)
    elif ord(Entry_key) == 27:
        return False
    else:
            target_text = dict()

    
    current_text = []
    starting_time = time.time()
    wpm = 0
    stdscr.nodelay(True)

    while(True):
        time_ran = max(time.time() - starting_time, 1)
        wpm = round(len(current_text) / (time_ran / 60) / 5)

        stdscr.clear()
        
        Showing_text(stdscr ,target_text ,current_text ,wpm)
        
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break
        
        try:
            key = stdscr.getkey()
        except:
            continue
        if ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()

        elif len(current_text) < len(target_text):
                current_text.append(key)





wrapper(main)