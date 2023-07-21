from tkinter import *
import word_generator as wg
import time

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 526
BACKGROUND_COLOR = "#B1DDC6"

word_gen = wg.WordGenerator()
word = word_gen.nextWord()


# ---   --- UI Setup ---    ---
window = Tk()
window.title("Spanish-English Flash card game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

card_back_img = PhotoImage(file="Intermediate/Day31/images/card_back.png")
card_front_img = PhotoImage(file="Intermediate/Day31/images/card_front.png")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, image=card_front_img)
canvas.create_text(WINDOW_WIDTH/2, 150, text=wg.SPANISH, font=("Arial", 40, "italic"), tags=("title"))
canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, text=word[wg.SPANISH], font=("Arial", 60, "bold"), tags=("word"))
canvas.grid(row=0, column=0, columnspan=2)

def updateWord():
    canvas.delete("word")
    word = word_gen.nextWord()
    canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, text=word[wg.SPANISH], font=("Arial", 60, "bold"), tags=("word"))

wrong_answer_img = PhotoImage(file="Intermediate/Day31/images/wrong.png")
wrong_btn = Button(image=wrong_answer_img, highlightthickness=0, command=updateWord)
wrong_btn.grid(row=1, column=0)

correct_answer_img = PhotoImage(file="Intermediate/Day31/images/right.png")
correct_btn = Button(image=correct_answer_img, highlightthickness=0, command=updateWord)
correct_btn.grid(row=1, column=1)

window.mainloop()
