from tkinter import *
from PIL import Image, ImageTk
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
btn1 = Button(window, text="Click\n Me")
btn2 = Button(window, text="Click Me")
btn3 = Button(window, text="Click Me")
btn4 = Button(window, text="Click Me")
btn1.grid(column=1, row=0)
btn2.grid(column=2, row=0)
btn3.grid(column=4, row=1)
btn4.grid(column=4, row=3)

llave = Image.open("D:\\Curso Python MC\\Ejercicios Python\\Hoja08\\Ej_02\\testll.png")
ll1 = ImageTk.PhotoImage(llave)

label = Label(image=ll1)
label.image = ll1
label.place(x=170, y=50)
#lbl0 = Label(window, text="___", font=("Arial Bold", 30))
#lbl1 = Label(window, text="|", font=("Arial Bold", 30))
#lbl2 = Label(window, text="|", font=("Arial Bold", 30))
#lbl3 = Label(window, text="|", font=("Arial Bold", 30))
#lbl0.grid(column=2, row=1)
#lbl1.grid(column=2, row=2)
#lbl2.grid(column=1, row=3)
#lbl3.grid(column=3, row=3)

window.mainloop()