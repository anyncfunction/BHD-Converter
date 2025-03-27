import tkinter as tk
from tkinter import ttk

def convert():
    try:
        decimal_value = int(entry.get(), int(base_input.get()))
        results = {
            2: bin(decimal_value)[2:],
            8: oct(decimal_value)[2:],
            10: str(decimal_value),
            16: hex(decimal_value)[2:].upper(),
            18: base_convert(decimal_value, 18),
            24: base_convert(decimal_value, 24)
        }
        for base, result in results.items():
            result_labels[base].config(text=result)
    except ValueError:
        for label in result_labels.values():
            label.config(text="Invalid Input")

def base_convert(number, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result if result else "0"

def update_placeholder(event):
    selected_base = base_input.get()
    entry.delete(0, tk.END)
    entry.insert(0, f"请输入{selected_base}进制数字")

# 创建主窗口
root = tk.Tk()
root.title("进制转换器")

# 输入部分
frame_input = ttk.Frame(root, padding="10")
frame_input.grid(row=0, column=0, sticky="W")

ttk.Label(frame_input, text="输入数字:").grid(row=0, column=0, sticky="W")
entry = ttk.Entry(frame_input, width=20)
entry.grid(row=0, column=1, sticky="W")

ttk.Label(frame_input, text="输入进制:").grid(row=1, column=0, sticky="W")
base_input = ttk.Combobox(frame_input, values=[2, 8, 10, 16, 18, 24], width=17)
base_input.grid(row=1, column=1, sticky="W")
base_input.set(10)

base_input.bind("<<ComboboxSelected>>", update_placeholder)

ttk.Button(frame_input, text="转换", command=convert).grid(row=2, column=0, columnspan=2)

# 输出部分
frame_output = ttk.Frame(root, padding="10")
frame_output.grid(row=1, column=0, sticky="W")

result_labels = {}
row = 0
for base in [2, 8, 10, 16, 18, 24]:
    ttk.Label(frame_output, text=f"{base}进制:").grid(row=row, column=0, sticky="W")
    result_labels[base] = ttk.Label(frame_output, text="")
    result_labels[base].grid(row=row, column=1, sticky="W")
    row += 1

root.mainloop()
