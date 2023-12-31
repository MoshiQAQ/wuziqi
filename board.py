from tkinter import *
import tkinter.messagebox
import numpy as np

root = Tk()
root.title("Wuziqi")
window = Canvas(root, width=600, height=600, background='chocolate')
window.pack()



for i in range(0, 15):
    window.create_text(20 + 40 * i, 10, text=str(i), font=('Arial', 10))
    window.create_text(10, 20 + 40 * i, text=str(i), font=('Arial', 10))
    window.create_line(i * 40 + 20, 20, i * 40 + 20, 580)
    window.create_line(20, i * 40 + 20, 580, i * 40 + 20)

window.create_oval(135, 135, 145, 145, fill='black')
window.create_oval(135, 455, 145, 465, fill='black')
window.create_oval(465, 135, 455, 145, fill='black')
window.create_oval(455, 455, 465, 465, fill='black')
window.create_oval(295, 295, 305, 305, fill='black')

num = 0
A = np.full((15, 15), 0)
B = np.full((15, 15), '')

def display(matrix):
    m, n = matrix.shape
    for i in range(m):
        for j in range(n):
            if matrix[j][i] == 'w':
                print(1, end=' ')
            elif matrix[j][i] == 'b':
                print(0, end=' ')
            else:
                print(-1, end=' ')
        print()
    print()

def callback(event):
    global num, A
    for j in range(0, 15):
        for i in range(0, 15):
            if (event.x - 20 - 40 * i) ** 2 + (event.y - 20 - 40 * j) ** 2 <= 2 * 20 ** 2:
                break
        if (event.x - 20 - 40 * i) ** 2 + (event.y - 20 - 40 * j) ** 2 <= 2 * 20 ** 2:
            break

    if num % 2 == 0 and A[i][j] != 1:
        window.create_oval(40 * i + 5, 40 * j + 5, 40 * i + 35, 40 * j + 35, fill='black')
        A[i][j] = 1
        B[i][j] = 'b'
        num += 1
        
    if num % 2 != 0 and A[i][j] != 1:
        window.create_oval(40 * i + 5, 40 * j + 5, 40 * i + 35, 40 * j + 35, fill='white')
        A[i][j] = 1.
        B[i][j] = 'w'
        num += 1

    display(B)

    f = [[-1, 0], [-1, 1], [0, 1], [1, 1]]
    for z in range(0, 4):
        a, b = f[z][0], f[z][1]
        count1, count2 = 0, 0
        x, y = i, j
        while B[x][y] == B[i][j]:
            count1 += 1
            if x + a >= 0 and y + b >= 0 and x + a < 15 and y + b < 15 and B[x + a][y + b] == B[i][j]:
                [x, y] = np.array([x, y]) + np.array([a, b])
            else:
                x, y = i, j
                break
        while B[x][y] == B[i][j]:
            count2 += 1
            if x - a < 15 and y - b < 15 and x - a >= 0 and y - b >= 0 and B[x - a][y - b] == B[i][j]:
                [x, y] = np.array([x, y]) - np.array([a, b])
            else:
                break
        if count1 + count2 == 6:
            if B[i][j] == 'b':
                tkinter.messagebox.showinfo('提示', '黑棋获胜')
            else:
                tkinter.messagebox.showinfo('提示', '白棋获胜')

window.bind("<Button-1>", callback)
window.pack()

def quit():
    root.quit()

u = Button(root, text='退出', command=quit)
u.pack()

mainloop()