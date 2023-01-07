from random import randint
import json

class Setting:
    """Class for settings and score of the game."""
    def __init__(self):
        # title of the game
        self.TITLE = " ASCII SNAKE"

        # MSG for users
        self.MSG = " Press ESC to QUIT "

        # score file name
        self.score_file = 'score.json'

        # game display properties
        self.width = 60 # width of the display
        self.height = 30 # height of the display
        self.start_x = 0 # starting x position
        self.start_y = 0 # starting y position

        # game properties
        
        # minimum and maximum speed of the game
        self.speed_min_max = (100, 150)

        # food initial position
        self.food = self.get_food()

        # if highest score file exist get it
        self.highest_score = self.get_highest_score()

# ----------------------------------------------------------------------------------------------------------------------------------------------------

    def get_food(self):
        """Draw food at a random location."""
        return (randint(self.start_y + 1, self.height - 2), randint(self.start_x + 1, self.width - 2))

# ----------------------------------------------------------------------------------------------------------------------------------------------------

    def draw_score_and_title(self, win, score):
        """Draw score, highest score, msg and title on the window."""
        if score > self.highest_score:
            self.highest_score = score

        # score and highest score massage
        score_msg = f" Score {score} "
        highest_score_msg = f" High {self.highest_score} "

        win.addstr(0, 2, score_msg)
        win.addstr(0, (self.width - len(self.TITLE))//2, " ASCII SNAKE ")
        win.addstr(self.height - 1, (self.width - len(self.MSG))//2, self.MSG)
        win.addstr(0, self.width - len(highest_score_msg) - 6, highest_score_msg)

# ----------------------------------------------------------------------------------------------------------------------------------------------------

    def get_highest_score(self):
        """Get the highest score and return it."""
        try:
            with open(self.score_file, 'r') as f_obj:
                return json.load(f_obj)
        except FileNotFoundError:
            return 0

# ----------------------------------------------------------------------------------------------------------------------------------------------------

    def write_highest_score(self):
        """Write the current highest score in the file."""
        with open(self.score_file, 'w') as f_obj:
            json.dump(self.highest_score, f_obj)
            
# ----------------------------------------------------------------------------------------------------------------------------------------------------

    def get_speed(self, snake_len):
        """Set the speed relative to length of the snake."""
        return max([self.speed_min_max[0], self.speed_min_max[1] - snake_len])

