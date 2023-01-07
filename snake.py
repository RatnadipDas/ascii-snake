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

        while True:
            if self.ascii_snake.cur_key == curses.KEY_UP:
                if self.ascii_snake.prev_key != curses.KEY_DOWN:
                    self.head_y -= 1
                    break
                else:
                    self.ascii_snake.cur_key = self.ascii_snake.prev_key
                    continue

            if self.ascii_snake.cur_key == curses.KEY_DOWN:
                if self.ascii_snake.prev_key != curses.KEY_UP:
                    self.head_y += 1
                    break
                else:
                    self.ascii_snake.cur_key = self.ascii_snake.prev_key
                    continue
            if self.ascii_snake.cur_key == curses.KEY_LEFT:
                if self.ascii_snake.prev_key != curses.KEY_RIGHT:
                    self.head_x -= 1
                    break
                else:
                    self.ascii_snake.cur_key = self.ascii_snake.prev_key
                    continue
            if self.ascii_snake.cur_key == curses.KEY_RIGHT:
                if self.ascii_snake.prev_key != curses.KEY_LEFT:
                    self.head_x += 1
                    break
                else:
                    self.ascii_snake.cur_key = self.ascii_snake.prev_key
                    continue

        self.snake_pos.insert(0, (self.head_y, self.head_x))

# ----------------------------------------------------------------------------------------------------------------------------------------------------

    def killed(self):
        """Kill the snake if it's head touches boundary or it's own body."""
        if self.head_y == self.setting.start_y or self.head_y == self.setting.height-1:
            return True
        if self.head_x == self.setting.start_x or self.head_x == self.setting.width-1:
            return True

        if self.snake_pos[0] in self.snake_pos[1:]:
            return True

        return False

# ----------------------------------------------------------------------------------------------------------------------------------------------------

    def draw_snake(self, win):
        """Draw snake body on the window."""
        for body_seg in self.snake_pos:
            win.addch(body_seg[0], body_seg[1], '#')

