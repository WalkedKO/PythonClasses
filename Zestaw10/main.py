import tkinter as tk
from botanswer import BotAnswer
import os
def onclick(player_input, player_img, player_label, bot_label):
    bot_label.randomize(player_input)
    player_label.config(image = player_img)
    player_label.image = player_img
root = tk.Tk()
root.geometry("800x500")
root.title("Kamien papier nozyce")

root.columnconfigure(0,weight=2)
root.columnconfigure(1, weight=1)
root.rowconfigure(0,weight=1)

left_panel = tk.Frame(root)
left_panel.grid(column = 0, row = 0)
script_dir = os.path.dirname(os.path.abspath(__file__))
rock_path = os.path.join(script_dir, "img", "rock.png")
scissors_path = os.path.join(script_dir, "img", "scissor.png")
paper_path = os.path.join(script_dir, "img", "paper.png")

rock_img = tk.PhotoImage(file=rock_path).subsample(2, 2)
paper_img = tk.PhotoImage(file=paper_path).subsample(2, 2)
scissor_img = tk.PhotoImage(file=scissors_path).subsample(2, 2)
pc_text = tk.Label(left_panel, text="Przeciwnik:")
pc_text.grid(column=0, row=0, sticky=tk.W)

result = tk.Label(left_panel)
result.grid(column=0, row=2)

pc_answer = BotAnswer(left_panel, width=100, height=100, rock_img=rock_img, paper_img=paper_img, scissors_img=scissor_img, result=result)
pc_answer.grid(column=0, row=1, sticky=tk.W)

ur_text = tk.Label(left_panel, text="Ty:")
ur_text.grid(column=1, row=0, sticky=tk.E)
ur_answer = tk.Label(left_panel)
ur_answer.grid(column=1,row=1)

buttons = tk.Frame(root)
buttons.grid(column=1, row=0, sticky = tk.E)
buttons.rowconfigure(0, weight=1)
buttons.rowconfigure(1, weight=1)
buttons.rowconfigure(2, weight=1)
buttons.columnconfigure(0, weight=1)


k_button = tk.Button(buttons, text="Kamien",width=20, height=2, background='gray', command=lambda: onclick(0,rock_img, ur_answer, pc_answer))
k_button.grid(column=0, row = 0)
p_button = tk.Button(buttons, text="Papier",width=20, height=2, command=lambda: onclick(1,paper_img,ur_answer,pc_answer))
p_button.grid(column=0, row = 1)
n_button = tk.Button(buttons, text="Nozyce",width=20, height=2, background='cyan', command=lambda: onclick(2,scissor_img,ur_answer,pc_answer))
n_button.grid(column=0, row = 2)
root.mainloop()
