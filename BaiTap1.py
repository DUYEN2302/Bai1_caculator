import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("CACULATOR")
        self.root.geometry("400x600")
        self.root.configure(bg="#3b3b3b")
        self.root.resizable(False, False)

        # Kết quả hiển thị
        self.result_var = tk.StringVar()
        self.result_entry = tk.Entry(root, textvariable=self.result_var, font=('Arial', 24), fg="#ffffff", bg="#333333", bd=10, insertwidth=4, width=14, borderwidth=4, justify='right')
        self.result_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

        # Các nút của máy tính
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0), ('%', 5, 1), ('√', 5, 2), ('x²', 5, 3),
            ('ax²+bx+c=0', 6, 0, 4)  # Nút giải phương trình bậc hai
        ]
        
        for button_info in buttons:
            if len(button_info) == 4:
                text, row, col, colspan = button_info
            else:
                text, row, col = button_info
                colspan = 1  # Giá trị mặc định của colspan là 1 nếu không có

            button = tk.Button(root, text=text, font=('Arial', 18), padx=10, pady=10, fg="#ffffff", bg="#4a4a4a", activebackground="#707070", command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)

        # Điều chỉnh kích thước các cột và hàng cho hợp lý
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
        for i in range(1, 7):
            root.grid_rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.result_var.set('')
        elif char == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Lỗi", "Phép tính không hợp lệ")
        elif char == '√':
            try:
                result = math.sqrt(float(self.result_var.get()))
                self.result_var.set(result)
            except ValueError:
                messagebox.showerror("Lỗi", "Giá trị không hợp lệ")
        elif char == 'x²':
            try:
                result = float(self.result_var.get()) ** 2
                self.result_var.set(result)
            except ValueError:
                messagebox.showerror("Lỗi", "Giá trị không hợp lệ")
        elif char == '%':
            try:
                result = float(self.result_var.get()) / 100
                self.result_var.set(result)
            except ValueError:
                messagebox.showerror("Lỗi", "Giá trị không hợp lệ")
        elif char == 'ax²+bx+c=0':
            self.solve_quadratic()
        else:
            self.result_var.set(self.result_var.get() + char)

    def solve_quadratic(self):
        def solve():
            try:
                a = float(a_entry.get())
                b = float(b_entry.get())
                c = float(c_entry.get())
                d = b ** 2 - 4 * a * c
                if d > 0:
                    x1 = (-b + math.sqrt(d)) / (2 * a)
                    x2 = (-b - math.sqrt(d)) / (2 * a)
                    result = f"Nghiệm x1: {x1:.2f}, x2: {x2:.2f}"
                elif d == 0:
                    x = -b / (2 * a)
                    result = f"Nghiệm kép x: {x:.2f}"
                else:
                    result = "Phương trình vô nghiệm"
                messagebox.showinfo("Kết quả", result)
            except ValueError:
                messagebox.showerror("Lỗi", "Giá trị không hợp lệ")

        # Tạo cửa sổ nhập a, b, c
        window = tk.Toplevel(self.root)
        window.title("Giải phương trình bậc hai")
        window.configure(bg="#3b3b3b")

        tk.Label(window, text="a:", font=('Arial', 14), fg="#ffffff", bg="#3b3b3b").grid(row=0, column=0)
        a_entry = tk.Entry(window, font=('Arial', 14), fg="#ffffff", bg="#4a4a4a")
        a_entry.grid(row=0, column=1)

        tk.Label(window, text="b:", font=('Arial', 14), fg="#ffffff", bg="#3b3b3b").grid(row=1, column=0)
        b_entry = tk.Entry(window, font=('Arial', 14), fg="#ffffff", bg="#4a4a4a")
        b_entry.grid(row=1, column=1)

        tk.Label(window, text="c:", font=('Arial', 14), fg="#ffffff", bg="#3b3b3b").grid(row=2, column=0)
        c_entry = tk.Entry(window, font=('Arial', 14), fg="#ffffff", bg="#4a4a4a")
        c_entry.grid(row=2, column=1)

        tk.Button(window, text="Giải", font=('Arial', 14), fg="#ffffff", bg="#707070", activebackground="#707070", command=solve).grid(row=3, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
