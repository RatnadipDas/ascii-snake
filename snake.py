import curses

class Snake:
    """Overall class to calculate and update snake positions."""
    def __init__(self, setting, ascii_snake):
        # snake initial position
        self.snake_pos = [(3, 10), (3, 9), (3, 8)]
        self.setting = setting
        self.ascii_snake = ascii_snake

# ----------------------------------------------------------------------------------------------------------------------------------------------------

    def next_head(self):
        """Calculate next head position of snake."""
        self.head_y = self.snake_pos[0][0]
        self.head_x = self.snake_pos[0][1]

        self.play_pause() # play or pause the snake

        while True:
            if self.ascii_snake.cur_key == curses.KEY_UP or self.ascii_snake.cur_key == self.setting.W:
                if self.ascii_snake.prev_key != curses.KEY_DOWN and self.ascii_snake.prev_key != self.setting.S:
                    self.head_y -= 1
                    break
                else:
                    self.ascii_snake.cur_key = self.ascii_snake.prev_key
                    continue

            if self.ascii_snake.cur_key == curses.KEY_DOWN or self.ascii_snake.cur_key == self.setting.S:
                if self.ascii_snake.prev_key != curses.KEY_UP and self.ascii_snake.prev_key != self.setting.W:
                    self.head_y += 1
                    break
                else:
                    self.ascii_snake.cur_key = self.ascii_snake.prev_key
                    continue
            if self.ascii_snake.cur_key == curses.KEY_LEFT or self.ascii_snake.cur_key == self.setting.A:
                if self.ascii_snake.prev_key != curses.KEY_RIGHT and self.ascii_snake.prev_key != self.setting.D:
                    self.head_x -= 1
                    break
                else:
                    self.ascii_snake.cur_key = self.ascii_snake.prev_key
                    continue
            if self.ascii_snake.cur_key == curses.KEY_RIGHT or self.ascii_snake.cur_key == self.setting.D:
                if self.ascii_snake.prev_key != curses.KEY_LEFT and self.ascii_snake.prev_key != self.setting.A:
                    self.head_x += 1
                    break
                else:
                    self.ascii_snake.cur_key = self.ascii_snake.prev_key
                    continue

        self.snake_pos.insert(0, (self.head_y, self.head_x))

# ----------------------------------------------------------------------------------------------------------------------------------------------------

    def killed(self):
        """If snake's head touches boundary return (True, True) and if head touches it's body return (True, False)."""
        if self.head_y == self.setting.start_y or self.head_y == self.setting.height-1:
            return (True, True)
        if self.head_x == self.setting.start_x or self.head_x == self.setting.width-1:
            return (True, True)

        if self.snake_pos[0] in self.snake_pos[1:]:
            return (True, False)

        return (False, False)

# ----------------------------------------------------------------------------------------------------------------------------------------------------

    def play_pause(self):
        """If SPACE key is pressed pause the snake."""
        if self.ascii_snake.cur_key == self.setting.SPACE:
            self.ascii_snake.cur_key = self.ascii_snake.prev_key
            self.ascii_snake.pause = True

        while self.ascii_snake.pause:
            event = self.ascii_snake.win.getch() # get the next character and refresh the screen
            if event == self.setting.SPACE:
                self.ascii_snake.pause = False

# ----------------------------------------------------------------------------------------------------------------------------------------------------

    def draw_snake(self, win):
        """Draw snake body on the window."""
        for body_seg in self.snake_pos:
            win.addch(body_seg[0], body_seg[1], self.setting.snake_body_char)
