from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ---   --- UI Setup ---    ---
window = Tk()
window.title("Spanish-English Flash card game")
window.maxsize(width=1000, height=800)
#window.config(padx=50, pady=50)



card_back_img = PhotoImage(file="Intermediate/Day31/images/card_back.png")
card_front_img = PhotoImage(file="Intermediate/Day31/images/card_front.png")

wrong_answer_img = PhotoImage(file="Intermediate/Day31/images/wrong.png")
wrong_btn = Button(image=wrong_answer_img, highlightthickness=0)

correct_answer_img = PhotoImage(file="Intermediate/Day31/images/right.png")
correct_btn = Button(image=correct_answer_img, highlightthickness=0)

canvas = Canvas(width=1000, height=800, background=BACKGROUND_COLOR)
canvas.create_image(250, 250, image=card_back_img)
canvas.pack()

window.mainloop()
