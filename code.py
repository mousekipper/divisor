import tkinter as tk
from tkinter import messagebox

# 약수를 구하는 함수
def get_divisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

# 계산 함수
def calculate():
    try:
        number = int(entry_number.get())  # 입력한 숫자
        if number <= 0:
            messagebox.showerror("error")
            return
        
        divisors = get_divisors(number)
        label_result.config(text=f"{number}의 약수: {', '.join(map(str, divisors))}")

    except ValueError:
        messagebox.showerror("error")

# GUI 설정
root = tk.Tk()
root.title("약수 계산기")

# 숫자 입력
label_number = tk.Label(root, text="숫자를 입력하세요:")
label_number.pack(pady=5)
entry_number = tk.Entry(root, width=20)
entry_number.pack(pady=5)

# 계산 버튼
button_calculate = tk.Button(root, text="계산", command=calculate)
button_calculate.pack(pady=20)

# 결과 레이블
label_result = tk.Label(root, text="약수 결과: ")
label_result.pack(pady=5)

# 메인 루프
root.mainloop()
