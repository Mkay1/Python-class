from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Setting up Main Window
root = Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')

# Adding Image and Labels in the Main Window
upload = Image.open("app_img.jpeg")
# Resize the image using resize() method
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)

label1 = Label(root,
               text="Hey User! Welcome to Denomination Counter Application.",
               bg='light blue')
label1.place(relx=0.5, y=340, anchor=CENTER)

# Function to display a messagebox and proceed if OK is clicked
def msg():
    MsgBox = messagebox.showinfo(
        "Alert", "Do you want to calculate the denomination count?")
    if MsgBox == 'ok':
        topwin()

# Adding Buttons to the main window
button1 = Button(root,
                 text="Let's get started!",
                 command=msg,
                 bg='brown',
                 fg='white')
button1.place(x=260, y=360)

# Function for opening new/top window
def topwin():
    top = Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg='light grey')
    top.geometry("500x400+50+50")
    

    label = Label(top, text="Enter total amount", bg='light grey')
    entry = Entry(top)
    lbl = Label(top, text="Here are number of notes for each denomination", bg='light grey')

    l1 = Label(top, text="1000", bg='light grey')
    l2 = Label(top, text="500", bg='light grey')
    l3 = Label(top, text="200", bg='light grey')
    l4 = Label(top, text="100", bg='light grey')
    l5 = Label(top, text="50", bg='light grey')
    l6 = Label(top, text="20", bg='light grey')
    l7 = Label(top, text="10", bg='light grey')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    t4 = Entry(top)
    t5 = Entry(top)
    t6 = Entry(top)
    t7 = Entry(top)

    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note1000 = amount // 1000
            amount %= 1000
            note500 = amount // 500
            amount %= 500
            note200 = amount // 200
            amount %= 200
            note100 = amount // 100
            amount %= 100
            note50 = amount // 50
            amount %= 50
            note20 = amount // 20
            amount %= 20
            note10 = amount // 10
            amount %= 10

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            t4.delete(0, END)
            t5.delete(0, END)
            t6.delete(0, END)
            t7.delete(0, END)

            t1.insert(END, str(note1000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note200))
            t4.insert(END, str(note100))
            t5.insert(END, str(note50))
            t6.insert(END, str(note20))
            t7.insert(END, str(note10))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    btn = Button(top, text='Calculate', command=calculator, bg='brown', fg='white')

    # Centering Widgets in the Top Window
    label.place(x=200, y=20   )
    entry.place(x=190, y=50   )
    btn.place(x=225, y=90   )
    lbl.place(x=115, y=140   )

    l1.place(x=150, y=180   )
    l2.place(x=150, y=210   )
    l3.place(x=150, y=240   )
    l4.place(x=150, y=270   )
    l5.place(x=150, y=300   )
    l6.place(x=150, y=330   )
    l7.place(x=150, y=360   )

    t1.place(x=210, y=180   )
    t2.place(x=210, y=210   )
    t3.place(x=210, y=240   )
    t4.place(x=210, y=270   )
    t5.place(x=210, y=300   )
    t6.place(x=210, y=330   )
    t7.place(x=210, y=360   )
    top.mainloop()

root.mainloop()