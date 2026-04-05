import calculate as ct
import tkinter as tk

class GUICalculator(tk.Frame):
    def __init__(self, main_window):
        self.window = main_window
        self.window.title('GUI Calculator')
        self.window.geometry('400x400')
        self.janela.minsize(400, 400)
        self.janela.maxsize(400, 400)
        self.window.resizable(False, False)

        self.calculate = ct.Calculate()

        self.display_text = tk.StringVar()
        self.display_text.set('0')

        self._build_display()
        self._build_bottons()

    def _build_display(self):
        display = tk.Entry(
            self.window,
            textvariable = self.display_text,
            font = ('Arial', 20),
            justify = 'right',
            state = 'readonly'
        )

        display.grid(row = 0, column = 0, columnspan = 4, sticky = 'nsew', ipadx = 8, ipady = 20)

    def _build_bottons(self):
        bottons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for i in range(5):
            self.window.grid_rowconfigure(i, weight = 1)
            self.window.grid_columnconfigure(i, weight = 1)

        for text, row, column in bottons:
            command = lambda t = text: self._callback(t)

            botton = tk.Button(self.window, text = text, font = ('Arial', 18), command = command)
            botton.grid(row = row, column = column, sticky = 'nsew', padx = 2, pady = 2)

    def _callback(self, text):
        actual_display_text = self.display_text.get()
        error_text = 'An error ocurred. Sorry...'
        operators = ['+', '-', '*', '/']

        if text == 'C':
            self.display_text.set('0')
        elif text == '=':
            try:
                expression = self.display_text.get()
                result = self.calculate.start_calculation(expression)

                self.display_text.set(str(result))
            except Exception as exception:
                self.display_text.set(error_text)
        elif text in operators:
            self.display_text.set(actual_display_text + f' {text} ')
        else:
            if actual_display_text == '0' or actual_display_text == error_text:
                self.display_text.set(text)
            else:
                self.display_text.set(actual_display_text + text)

if __name__ == '__main__':
    root = tk.Tk()
    app = GUICalculator(root)
    root.mainloop()