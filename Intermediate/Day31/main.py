from tkinter import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 526
BACKGROUND_COLOR = "#B1DDC6"

# ---   --- UI Setup ---    ---
window = Tk()
window.title("Spanish-English Flash card game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

card_back_img = PhotoImage(file="Intermediate/Day31/images/card_back.png")
card_front_img = PhotoImage(file="Intermediate/Day31/images/card_front.png")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, image=card_front_img)
canvas.create_text(WINDOW_WIDTH/2, 150, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, text="Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_answer_img = PhotoImage(file="Intermediate/Day31/images/wrong.png")
wrong_btn = Button(image=wrong_answer_img, highlightthickness=0)
wrong_btn.grid(row=1, column=0)

correct_answer_img = PhotoImage(file="Intermediate/Day31/images/right.png")
correct_btn = Button(image=correct_answer_img, highlightthickness=0)
correct_btn.grid(row=1, column=1)

window.mainloop()
