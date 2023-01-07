import curses
from setting import Setting
from snake import Snake

class AsciiSnake:
    """Overall class defining behavior and logic of the game."""
    def __init__(self):
        """Setup and initialize the game."""

        # setup window
        curses.initscr() # initialize the screen

        self.setting= Setting()
        self.snake = Snake(self.setting, self)

        self.win = curses.newwin(self.setting.height, self.setting.width, self.setting.start_y, self.setting.start_x) # create a window
        self.win.keypad(True) # return keys
        curses.noecho() # turn off echoing of the keys to the screen
        curses.curs_set(0) # make cursor invisible
        self.win.border() # give border to the window
        self.win.nodelay(True) # don't wait for user event

        # key setup
        self.ESC = 27 # escape key code for  curses

        # game logic setup
        self.score = 0 # initial score of the game
        self.cur_key = curses.KEY_RIGHT # initial movement direction

# ----------------------------------------------------------------------------------------------------------------------------------------------------

    def run(self):
        """Run the game."""
        killed = False
        while True:
            self.setting.draw_score_and_title(self.win, self.score)
            self.win.timeout(self.setting.get_speed(len(self.snake.snake_pos)))
            self.get_event()
            if(self.quit()):
                break

            self.update()

            killed, wall = self.snake.killed() # get killed and wall values

            # if the snake is killed exit the game
            if killed:
                break

        curses.endwin() # decommission the window
        self.setting.write_highest_score() # write the highest score in the file

        if killed and wall:
            print("\nHEAD TOUCHED THE WALL!!!\n")
        elif killed and not wall:
            print("\nHEAD TOUCHED THE BODY!!!\n")
        elif not killed:
            print("\nGAME QUITTED!!!\n")

        # print the score and highest score on the terminal
        print(f"Your Score: {self.score}")
        print(f"Highest Score: {self.setting.highest_score}")
        
# ----------------------------------------------------------------------------------------------------------------------------------------------------

    def get_event(self):
        """Look for user events."""
        self.prev_key = self.cur_key
        self.event = self.win.getch() # get the next character and refresh the screen
        # if user pressed no key then the current key is the previous key else it is new key
        self.cur_key = self.event if self.event != -1 else self.prev_key

        if self.cur_key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, self.ESC]:
            self.cur_key = self.prev_key

# ----------------------------------------------------------------------------------------------------------------------------------------------------

    def update(self):
        """Update the game."""

        self.snake.next_head() # calculate snakes next head position

        if self.snake.snake_pos[0] == self.setting.food:
            # check if snake eats the food
            self.score += 1
            self.setting.food = ()

            while self.setting.food == ():
                self.setting.food = self.setting.get_food()

                if self.setting.food in self.snake.snake_pos:
                    self.setting.food = ()
        else:
            # move the snake
            last = self.snake.snake_pos.pop()
            self.win.addch(last[0], last[1], ' ')

            # draw snake's body segments on the window
            self.snake.draw_snake(self.win)

        self.win.addch(self.setting.food[0], self.setting.food[1], self.setting.food_char) # draw food on the window
        
# ----------------------------------------------------------------------------------------------------------------------------------------------------

    def quit(self):
        """Quit the game if ESC key is pressed."""
        if self.cur_key == self.ESC:
            return True
        
# ----------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    snake = AsciiSnake()
    snake.run()

