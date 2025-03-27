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
    entry.insert(0, f"Please enter a base-{selected_base} number")

# Create the main window
root = tk.Tk()
root.title("Base Converter")

# Input section
frame_input = ttk.Frame(root, padding="10")
frame_input.grid(row=0, column=0, sticky="W")

ttk.Label(frame_input, text="Input Number:").grid(row=0, column=0, sticky="W")
entry = ttk.Entry(frame_input, width=20)
entry.grid(row=0, column=1, sticky="W")

ttk.Label(frame_input, text="Input Base:").grid(row=1, column=0, sticky="W")
base_input = ttk.Combobox(frame_input, values=[2, 8, 10, 16, 18, 24], width=17)
base_input.grid(row=1, column=1, sticky="W")
base_input.set(10)

base_input.bind("<<ComboboxSelected>>", update_placeholder)

ttk.Button(frame_input, text="Convert", command=convert).grid(row=2, column=0, columnspan=2)

# Output section
frame_output = ttk.Frame(root, padding="10")
frame_output.grid(row=1, column=0, sticky="W")

result_labels = {}
row = 0
for base in [2, 8, 10, 16, 18, 24]:
    ttk.Label(frame_output, text=f"Base-{base}:").grid(row=row, column=0, sticky="W")
    result_labels[base] = ttk.Label(frame_output, text="")
    result_labels[base].grid(row=row, column=1, sticky="W")
    row += 1

root.mainloop()
"""
MIT License

Copyright (c) 2025 anyncfunction

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
