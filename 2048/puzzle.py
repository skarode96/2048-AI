import random
import logic
from tkinter import Frame, Label, CENTER


import constants as c


class Event:
    def __init__(self, char):
        self.char = char


class GameGrid(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title('2048')
        self.master.bind("<Key>", self.key_down)
        self.master.bind("<Escape>", lambda q: self.master.destroy())
        self.master.bind("<<UP>>", lambda q: self.key_down(Event("w")))
        self.master.bind("<<DOWN>>", lambda q: self.key_down(Event("s")))
        self.master.bind("<<LEFT>>", lambda q: self.key_down(Event("a")))
        self.master.bind("<<RIGHT>>", lambda q: self.key_down(Event("d")))

        # self.gamelogic = gamelogic
        self.commands = {c.KEY_UP: logic.up, c.KEY_DOWN: logic.down,
                         c.KEY_LEFT: logic.left, c.KEY_RIGHT: logic.right,
                         c.KEY_UP_ALT: logic.up, c.KEY_DOWN_ALT: logic.down,
                         c.KEY_LEFT_ALT: logic.left, c.KEY_RIGHT_ALT: logic.right,
                         c.KEY_H: logic.left, c.KEY_L: logic.right,
                         c.KEY_K: logic.up, c.KEY_J: logic.down}

        self.grid_cells = []
        self.init_score()
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()
        # self.mainloop()

    def init_score(self):
        self.score = 0

    def init_grid(self):
        background = Frame(self, bg=c.BACKGROUND_COLOR_GAME,
                           width=c.SIZE, height=c.SIZE)
        background.grid()
        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                cell = self.create_cell(i, j, background, "")
                grid_row.append(cell)
            self.grid_cells.append(grid_row)
        score_text_cell = self.create_cell(4, 0, background, "Score")
        score_cell = self.create_cell(4, 1, background, self.score)
        self.grid_cells.append([score_text_cell, score_cell])

    def create_cell(self, x, y, background, text):
        cell = Frame(background, bg=c.BACKGROUND_COLOR_SCORE,
                     width=c.SIZE / c.GRID_LEN,
                     height=c.SIZE / c.GRID_LEN)
        cell.grid(row=x, column=y, padx=c.GRID_PADDING,
                  pady=c.GRID_PADDING)
        t1 = Label(master=cell, text=text,
                   bg=c.BACKGROUND_COLOR_SCORE,
                   justify=CENTER, font=c.FONT, width=5, height=2)
        t1.grid()
        return t1

    def gen(self):
        return random.randint(0, c.GRID_LEN - 1)

    def init_matrix(self):
        self.matrix = logic.new_game(4)
        self.history_matrixs = list()
        self.matrix = logic.add_two(self.matrix)
        self.matrix = logic.add_two(self.matrix)

    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(
                        text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=str(
                        new_number), bg=c.BACKGROUND_COLOR_DICT[new_number],
                        fg=c.CELL_COLOR_DICT[new_number])
        self.grid_cells[4][0].configure(text="Score", bg=c.BACKGROUND_COLOR_SCORE,
                                        fg=c.FOREGROUND_COLOR_SCORE)
        self.grid_cells[4][1].configure(text=str(self.score), bg=c.BACKGROUND_COLOR_SCORE,
                                        fg=c.FOREGROUND_COLOR_SCORE)
        self.update_idletasks()

    def key_down(self, event):
        key = repr(event.char)
        if key == c.KEY_BACK and len(self.history_matrixs) > 1:
            self.matrix = self.history_matrixs.pop()
            self.update_grid_cells()
            print('back on step total step:', len(self.history_matrixs))
        elif key in self.commands:
            self.matrix, done, local_score = self.commands[repr(event.char)](self.matrix)
            self.score += local_score
            if done:
                self.matrix = logic.add_two(self.matrix)
                # record last move
                self.history_matrixs.append(self.matrix)
                self.update_grid_cells()
                done = False
                if logic.game_state(self.matrix) == 'win':
                    self.grid_cells[1][1].configure(
                        text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(
                        text="Win!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                if logic.game_state(self.matrix) == 'lose':
                    self.grid_cells[1][1].configure(
                        text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(
                        text="Lose!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)

    def generate_next(self):
        index = (self.gen(), self.gen())
        while self.matrix[index[0]][index[1]] != 0:
            index = (self.gen(), self.gen())
        self.matrix[index[0]][index[1]] = 2


