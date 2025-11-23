import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class GUIApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Исмонов Хакимджон Мукимджонович")
        self.root.geometry("600x400")
        
        self.notebook = ttk.Notebook(self.root)
        
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Калькулятор")
        self.create_calculator()
        
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Выбор")
        self.create_checkboxes()
        
        self.tab3 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab3, text="Текст")
        self.create_text_tab()
        
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)
    
    def create_calculator(self):
        tk.Label(self.tab1, text="Число 1:").grid(row=0, column=0, padx=5, pady=5)
        self.num1 = tk.Entry(self.tab1)
        self.num1.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(self.tab1, text="Число 2:").grid(row=1, column=0, padx=5, pady=5)
        self.num2 = tk.Entry(self.tab1)
        self.num2.grid(row=1, column=1, padx=5, pady=5)
        
        self.operation = tk.StringVar(value="+")
        operations = ["+", "-", "*", "/"]
        op_menu = tk.OptionMenu(self.tab1, self.operation, *operations)
        op_menu.grid(row=0, column=2, rowspan=2, padx=5, pady=5)
        
        calc_btn = tk.Button(self.tab1, text="Вычислить", command=self.calculate)
        calc_btn.grid(row=2, column=0, columnspan=3, pady=10)
        
        self.result = tk.Label(self.tab1, text="Результат: ")
        self.result.grid(row=3, column=0, columnspan=3)
    
    def calculate(self):
        try:
            n1 = float(self.num1.get())
            n2 = float(self.num2.get())
            op = self.operation.get()
            
            if op == "+":
                res = n1 + n2
            elif op == "-":
                res = n1 - n2
            elif op == "*":
                res = n1 * n2
            elif op == "/":
                res = n1 / n2 if n2 != 0 else "Ошибка: деление на 0"
            
            self.result.config(text=f"Результат: {res}")
        except ValueError:
            self.result.config(text="Ошибка: введите числа")
    
    def create_checkboxes(self):
        self.var1 = tk.BooleanVar()
        self.var2 = tk.BooleanVar()
        self.var3 = tk.BooleanVar()
        
        cb1 = tk.Checkbutton(self.tab2, text="Первый", variable=self.var1)
        cb2 = tk.Checkbutton(self.tab2, text="Второй", variable=self.var2)
        cb3 = tk.Checkbutton(self.tab2, text="Третий", variable=self.var3)
        
        cb1.pack(pady=5)
        cb2.pack(pady=5)
        cb3.pack(pady=5)
        
        show_btn = tk.Button(self.tab2, text="Показать выбор", command=self.show_selection)
        show_btn.pack(pady=10)
    
    def show_selection(self):
        selected = []
        if self.var1.get():
            selected.append("Первый")
        if self.var2.get():
            selected.append("Второй")
        if self.var3.get():
            selected.append("Третий")
        
        if selected:
            messagebox.showinfo("Выбор", f"Вы выбрали: {', '.join(selected)}")
        else:
            messagebox.showinfo("Выбор", "Вы ничего не выбрали")
    
    def create_text_tab(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="Загрузить текст", command=self.load_text)
        
        self.text_area = tk.Text(self.tab3, wrap=tk.WORD)
        scrollbar = tk.Scrollbar(self.tab3, orient="vertical", command=self.text_area.yview)
        self.text_area.configure(yscrollcommand=scrollbar.set)
        
        self.text_area.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def load_text(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(1.0, content)
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось загрузить файл: {str(e)}")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = GUIApp()
    app.run()