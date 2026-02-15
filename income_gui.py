import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        hours = float(hours_entry.get())
        rate = float(rate_entry.get())
        gross = hours * 4 * rate
        irpf = gross * 0.21
        ss = 300
        net = gross - irpf - ss
        result_label.config(text=f"Gross: €{gross:.2f}  |  Net: €{net:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Enter numbers!")

root = tk.Tk()
root.title("Python Freelance Calculator")
root.geometry("350x250")
root.configure(bg='lightblue')

tk.Label(root, text="Freelance Income Calc", font=('Arial', 14, 'bold')).pack(pady=10)
tk.Label(root, text="Hours/week:").pack()
hours_entry = tk.Entry(root)
hours_entry.pack(pady=5)
hours_entry.insert(0, "20")

tk.Label(root, text="Rate €/h:").pack()
rate_entry = tk.Entry(root)
rate_entry.pack(pady=5)
rate_entry.insert(0, "20")

tk.Button(root, text="CALCULATE NET", command=calculate, bg='green', fg='white', font=('Arial', 12)).pack(pady=20)

result_label = tk.Label(root, text="Enter → Calculate", font=('Arial', 12))
result_label.pack(pady=10)

root.mainloop()
