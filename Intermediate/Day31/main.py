from tkinter import *
import word_generator as wg

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 526
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
TEXT_FILL = {wg.ENGLISH: "white", wg.SPANISH: "black"}

word_gen = wg.WordGenerator()
current_word = word_gen.nextWord()
current_language = wg.SPANISH

def flip_card():
    global current_language
    if current_language == wg.ENGLISH:
        # Flip to front - Spanish.
        current_language = wg.SPANISH
        canvas.itemconfig(canvas_image, image=card_front_img)
    elif current_language == wg.SPANISH:
        # Flip to back - English.
        current_language = wg.ENGLISH
        canvas.itemconfig(canvas_image, image=card_back_img)
    
    canvas.itemconfig(card_title, text=current_language, fill=TEXT_FILL[current_language])
    canvas.itemconfig(card_word, text=current_word[current_language], fill=TEXT_FILL[current_language])

def update_word():
    global current_word, flip_timer
    current_word = word_gen.nextWord()

    canvas.itemconfig(card_title, text=current_language, fill=TEXT_FILL[current_language])
    canvas.itemconfig(card_word, text=current_word[current_language], fill=TEXT_FILL[current_language])

    window.after_cancel(flip_timer)
    flip_timer = window.after(3000, flip_card)

# ---   --- UI Setup ---    ---
window = Tk()
window.title("Spanish-English Flash card game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_img = PhotoImage(file="Intermediate/Day31/images/card_back.png")
card_front_img = PhotoImage(file="Intermediate/Day31/images/card_front.png")
canvas_image = canvas.create_image(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, image=card_front_img)
card_title = canvas.create_text(WINDOW_WIDTH/2, 150, text=current_language, font=TITLE_FONT, fill=TEXT_FILL[current_language])
card_word = canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, text=current_word[current_language], font=WORD_FONT, fill=TEXT_FILL[current_language])
canvas.grid(row=0, column=0, columnspan=2)

wrong_answer_img = PhotoImage(file="Intermediate/Day31/images/wrong.png")
wrong_btn = Button(image=wrong_answer_img, highlightthickness=0, command=flip_card)
wrong_btn.grid(row=1, column=0)

correct_answer_img = PhotoImage(file="Intermediate/Day31/images/right.png")
correct_btn = Button(image=correct_answer_img, highlightthickness=0, command=update_word)
correct_btn.grid(row=1, column=1)

window.mainloop()
