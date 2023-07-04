import re
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

import nltk
from nltk.corpus import words

nltk.download('words')

class SpellingChecker:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Yazim Denetleyici')
        self.root.geometry('600x500')
        self.root.resizable(False, False)
        self.root.config(bg='lightblue')

        self.text = ScrolledText(self.root, font=('Helvetica', 14))
        self.text.bind('<KeyRelease>', self.check)
        self.text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.clear_button = tk.Button(self.root, text='Clear', command=self.clear_text)
        self.clear_button.pack(padx=10, pady=10, side=tk.BOTTOM)

        self.old_spaces = 0

        self.root.mainloop()

    def check(self, event):
        content = self.text.get('1.0', tk.END)
        space_count = content.count(' ')

        if space_count != self.old_spaces:
            self.old_spaces = space_count

            for tag in self.text.tag_names():
                self.text.tag_delete(tag)

            for word in content.split(' '):
                if re.sub(r'[^\w]', '', word.lower()) not in words.words():
                    position = content.find(word)
                    self.text.tag_add(word, f'1.{position}', f'1.{position + len(word)}')
                    self.text.tag_config(word, foreground='red', underline=True)

    def clear_text(self):
        self.text.delete('1.0', tk.END)


SpellingChecker()
