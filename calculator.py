import tkinter as tk
from tkinter import ttk, messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Hesap Makinesi")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        self.expression = ""
        self.result_var = tk.StringVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        # Ekran
        screen_frame = tk.Frame(self.root, height=80)
        screen_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        
        screen = tk.Entry(screen_frame, textvariable=self.result_var, font=('Arial', 24), 
                         justify='right', bd=10, relief=tk.RIDGE, state='readonly')
        screen.pack(fill=tk.BOTH, expand=True)
        
        # Tuşlar
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('C', 4, 0), ('⌫', 4, 1)
        ]
        
        for (text, row, col) in buttons:
            if text == '=':
                btn = tk.Button(buttons_frame, text=text, font=('Arial', 18), 
                               command=self.calculate, bg='orange', fg='white')
            elif text in ['C', '⌫']:
                btn = tk.Button(buttons_frame, text=text, font=('Arial', 18), 
                               command=self.clear if text == 'C' else self.backspace, 
                               bg='lightcoral')
            else:
                btn = tk.Button(buttons_frame, text=text, font=('Arial', 18), 
                               command=lambda t=text: self.add_to_expression(t))
            
            btn.grid(row=row, column=col, sticky='nsew', padx=5, pady=5, ipadx=10, ipady=10)
            buttons_frame.grid_columnconfigure(col, weight=1)
            buttons_frame.grid_rowconfigure(row, weight=1)
    
    def add_to_expression(self, value):
        self.expression += str(value)
        self.result_var.set(self.expression)
    
    def calculate(self):
        try:
            result = eval(self.expression)
            self.result_var.set(result)
            self.expression = str(result)
        except Exception as e:
            messagebox.showerror("Hata", "Geçersiz ifade!")
            self.clear()
    
    def clear(self):
        self.expression = ""
        self.result_var.set("")
    
    def backspace(self):
        self.expression = self.expression[:-1]
        self.result_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()