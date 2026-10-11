import os
import random
import tkinter as tk
import pandas

BACKGROUND_COLOR = '#B1DDC6'


# ---------------------------- ASSET & DATA GENERATOR ------------------------------- #
def generate_assets():
  if not os.path.exists('french_words.csv'):
    with open('french_words.csv', 'w', encoding='utf-8') as f:
      f.write(
          'French,English\npartir,to leave\ntemps,time\npeu,little\nvoir,to'
          ' see\nvouloir,to want\ndire,to say\njour,day\nsavoir,to know'
      )
  if not os.path.exists('card_front.png'):
    from PIL import Image

    Image.new('RGB', (800, 526), '#ffffff').save('card_front.png')
  if not os.path.exists('card_back.png'):
    from PIL import Image

    Image.new('RGB', (800, 526), '#91c499').save('card_back.png')
  if not os.path.exists('right.png'):
    from PIL import Image

    Image.new('RGB', (100, 100), '#9bdeac').save('right.png')
  if not os.path.exists('wrong.png'):
    from PIL import Image

    Image.new('RGB', (100, 100), '#e7305b').save('wrong.png')


generate_assets()

current_card = {}
to_learn = {}

try:
  data = pandas.read_csv('words_to_learn.csv')
except FileNotFoundError:
  original_data = pandas.read_csv('french_words.csv')
  to_learn = original_data.to_dict(orient='records')
else:
  to_learn = data.to_dict(orient='records')


# ---------------------------- CARD MECHANISM ------------------------------- #
def next_card():
  global current_card, flip_timer
  window.after_cancel(flip_timer)
  current_card = random.choice(to_learn)
  canvas.itemconfig(card_title, text='French', fill='black')
  canvas.itemconfig(card_word, text=current_card['French'], fill='black')
  canvas.itemconfig(card_background, image=card_front_img)
  flip_timer = window.after(3000, func=flip_card)


def flip_card():
  canvas.itemconfig(card_title, text='English', fill='white')
  canvas.itemconfig(card_word, text=current_card['English'], fill='white')
  canvas.itemconfig(card_background, image=card_back_img)


def is_known():
  to_learn.remove(current_card)
  data = pandas.DataFrame(to_learn)
  data.to_csv('words_to_learn.csv', index=False)
  next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title('Flashy - Flash Card App')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = tk.Canvas(width=800, height=526)
card_front_img = tk.PhotoImage(file='card_front.png')
card_back_img = tk.PhotoImage(file='card_back.png')
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(
    400, 150, text='', font=('Ariel', 40, 'italic')
)
card_word = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = tk.PhotoImage(file='wrong.png')
unknown_button = tk.Button(
    image=cross_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card
)
unknown_button.grid(row=1, column=0)

check_image = tk.PhotoImage(file='right.png')
known_button = tk.Button(
    image=check_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known
)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()