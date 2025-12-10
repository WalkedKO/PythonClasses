import tkinter as tk
from random import randint
class BotAnswer(tk.Label):
    def __init__(self, root, width: float, height: float, rock_img: tk.PhotoImage, paper_img: tk.PhotoImage, scissors_img: tk.PhotoImage):
        super().__init__(root, width=width, height = height)
        self.rock_img = rock_img
        self.paper_img = paper_img
        self.scissors_img = scissors_img
        self.state = 0
    def randomize(self, player_input, result_text):
        self.state = randint(0, 2)
        print(self.state)
        if self.state == 0:
            self.config(image = self.rock_img)
            self.image = self.rock_img
        elif self.state == 1:
            self.config(image=self.paper_img)
            self.image = self.paper_img
        else:
            self.config(image=self.scissors_img)
            self.image = self.scissors_img

        if (player_input, self.state) in ((0,2), (1, 0), (2, 1)):
            result_text.config(text="Wygrales!")
            result_text.text = "Wygrales!"
        elif player_input == self.state:
            result_text.config(text="Remis")
            result_text.text = "Remis"
        else:
            result_text.config(text="Przegrales...")
            result_text.text = "Przegrales..."
