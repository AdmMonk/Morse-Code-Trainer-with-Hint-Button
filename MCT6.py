import random
import time
import tkinter as tk

# Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
}

def get_random_word():
    letters = list(morse_code_dict.keys())
    word_length = random.randint(2, 4)
    return ''.join(random.choice(letters) for _ in range(word_length))

def get_morse_code(word):
    return ' '.join(morse_code_dict[letter] for letter in word)

# Function to display English letters in Morse code
def show_morse_to_text():
    morse_to_text_window = tk.Toplevel(root)
    morse_to_text_window.title("Morse Code to Text")

    morse_to_text = "Morse Code to English Letters:\n"
    for letter, code in morse_code_dict.items():
        morse_to_text += f"{code}: {letter}\n"

    morse_to_text_label = tk.Label(morse_to_text_window, text=morse_to_text)
    morse_to_text_label.pack()

# The rest of the functions and GUI creation remain the same...

def show_new_word():
    global correct_answer, start_time
    random_word = get_random_word()
    morse_code = get_morse_code(random_word)
    word_label.config(text="Word: " + random_word)
    correct_answer = morse_code
    start_time = time.time()
    result_label.config(text="")
    entry.delete(0, tk.END)

def show_hint():
    hint_text = "\n".join([f"{key}: {value}" for key, value in morse_code_dict.items()])
    hint_window = tk.Toplevel(root)
    hint_window.title("Morse Code Hint")
    hint_label = tk.Label(hint_window, text=hint_text)
    hint_label.pack()

def check_answer():
    user_input = entry.get().upper()
    if user_input == "EXIT":
        root.destroy()
        return

    if user_input == correct_answer:
        result_label.config(text="Correct! Time taken: {:.2f} seconds".format(time.time() - start_time))
    else:
        result_label.config(text="Incorrect. The correct Morse code is: {}".format(correct_answer))



root = tk.Tk()
root.title("Morse Code Training")

word_label = tk.Label(root, text="Word: ")
word_label.pack()

entry = tk.Entry(root)
entry.pack()

new_word_button = tk.Button(root, text="New Word", command=show_new_word)
new_word_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

hint_button = tk.Button(root, text="Hint", command=show_hint)
hint_button.pack()

submit_button = tk.Button(root, text="Submit", command=check_answer)
submit_button.pack()


show_new_word()  # Show the first word when the GUI starts

root.mainloop()
