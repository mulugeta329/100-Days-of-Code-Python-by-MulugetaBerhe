import os
import tkinter as tk


def clear_terminal():
  os.system('cls' if os.name == 'nt' else 'clear')


clear_terminal()


# 1. Conversion Logic
def miles_to_km():
  try:
    miles = float(miles_input.get())
    km = miles * 1.60934
    kilometer_result_label.config(text=f'{km:.2f}')
  except ValueError:
    kilometer_result_label.config(text='Error')


# 2. Window Setup
window = tk.Tk()
window.title('Mile to Km Converter')
window.config(padx=20, pady=20)

# 3. GUI Layout Grid Elements
miles_input = tk.Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = tk.Label(text='Miles')
miles_label.grid(column=2, row=0)

is_equal_label = tk.Label(text='is equal to')
is_equal_label.grid(column=0, row=1)

kilometer_result_label = tk.Label(text='0')
kilometer_result_label.grid(column=1, row=1)

kilometer_label = tk.Label(text='Km')
kilometer_label.grid(column=2, row=1)

calculate_button = tk.Button(text='Calculate', command=miles_to_km)
calculate_button.grid(column=1, row=2)

# 4. Main Event Loop
window.mainloop()