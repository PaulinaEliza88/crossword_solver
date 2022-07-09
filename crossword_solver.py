import tkinter as tk
import tkinter.scrolledtext as st


input_field: tk.Entry
text_area :st.ScrolledText

def get_dictionary():
    dictionary_open = open('slowa.txt','r',encoding="UTF-8")
    dictionary = dictionary_open.read().split()
    dictionary_open.close()
    return dictionary

def check_word(dictionary):
    test_word = input_field.get()
    non_blanks = len(test_word) - test_word.count('?')
    to_replace = ""
    for word in dictionary:
        inc_letter = 0
        inc_match = 0
        if len(word) == len(test_word):
            for letter in test_word:
                if letter == word[inc_letter]:
                    inc_match += 1
                inc_letter += 1
                if inc_match == non_blanks:
                    print(word)
                    to_replace += word + ", "
                    break
    # insert text
    text_area.configure(state='normal')
    text_area.replace('0.0', tk.END, ' ')
    text_area.insert(tk.END, to_replace[:-2])
    text_area.configure(state='disabled')

def group_function():
    my_dict = get_dictionary()
    check_word(my_dict)

root = tk.Tk()
root.title("Pomocnik krzyżówkowicza")    # title
width = 390  # window size
height = 250
half_screen_width = root.winfo_screenwidth()//2 - width//2
half_screen_height = root.winfo_screenheight()//2 - height//2
root.geometry(f"{width}x{height}+{half_screen_width}+{half_screen_height}")  # top left corner location
root.resizable(width=False, height=False)  # turn off elasticity of the window

# title label
tk.Label(root,
         text="Wpisz fragment słowa, które chcesz znaleźć.\nWstaw znaki zapytania \nw miejsce niewiadomych liter: ",
         font=("Source Serif Pro Semibold", 13),
         background='dodger blue',
         foreground="white").grid(column=0,
                                  row=0)

# input field
input_field = tk.Entry(root)
input_field.place(x=20, y=95, width=150, height=25)

# find the word button
find_word_button = tk.Button(root)
find_word_button["text"] = "Znajdź słowo"
find_word_button.place(x=180, y=95)
find_word_button["command"] = group_function

# scrolled text area
text_area = st.ScrolledText(root,
                            width=33,
                            height=4,
                            font=("Times New Roman",
                                  15))

text_area.grid(column=0, pady=60, padx=20)
text_area.insert(tk.INSERT, "Wybierz stąd słowo, którego szukasz")

# making the text read only
text_area.configure(state='disabled')

root.mainloop()