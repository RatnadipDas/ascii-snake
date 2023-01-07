import curses
from setting import Setting

class OpenClose:
    """Class to show starting and ending window."""
    def __init__(self):
        self.START_MSG = """
            Keys:

                W - UP
                S - DOWN
                A - LEFT
                D - RIGHT
                SPACE - PLAY/PAUSE

            Press SPACE to continue
        """

        self.setting = Setting()

# ----------------------------------------------------------------------------------------------------------------------------------------------------

    def start(self):
        """Display the control keys."""
        curses.initscr()
        win = curses.newwin(self.setting.height, self.setting.width, self.setting.start_y, self.setting.start_x) # create a window
        win.keypad(True) # return keys
        curses.curs_set(0) # make cursor invisible
        curses.noecho() # turn off echoing of the keys to the screen
        win.nodelay(True) # don't wait for user event

        while True:
            event = win.getch()
            win.addstr(self.setting.start_y, self.setting.start_x, self.START_MSG)
            if event == self.setting.SPACE:
                break
        curses.endwin()

# ----------------------------------------------------------------------------------------------------------------------------------------------------

    def end(self, score, highest_score, msg):
        """Display the score, highest score and reason for game termination."""
        END_MSG = f"""
            {msg}

            Your Score: {score}
            Highest Score: {highest_score}

            Press SPACE to exit
        """
        curses.initscr()
        win = curses.newwin(self.setting.height, self.setting.width, self.setting.start_y, self.setting.start_x) # create a window
        win.keypad(True) # return keys
        curses.curs_set(0) # make cursor invisible
        curses.noecho() # turn off echoing of the keys to the screen
        win.nodelay(True) # don't wait for user event

        while True:
            event = win.getch()
            win.addstr(self.setting.start_y, self.setting.start_x, END_MSG)
            if event == self.setting.SPACE:
                break
        curses.endwin()
