import tkinter as tk
from tkinter import messagebox


def get_divisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors


def calculate():
    try:
        number = int(entry_number.get()) 
        if number <= 0:
            messagebox.showerror("error")
            return
        
        divisors = get_divisors(number)
        label_result.config(text=f"{number}의 약수: {', '.join(map(str, divisors))}")

    except ValueError:
        messagebox.showerror("error")

root = tk.Tk()
root.title("약수 계산기")


label_number = tk.Label(root, text="숫자를 입력하세요:")
label_number.pack(pady=5)
entry_number = tk.Entry(root, width=20)
entry_number.pack(pady=5)


button_calculate = tk.Button(root, text="계산", command=calculate)
button_calculate.pack(pady=20)


label_result = tk.Label(root, text="약수 결과: ")
label_result.pack(pady=5)


root.mainloop()
