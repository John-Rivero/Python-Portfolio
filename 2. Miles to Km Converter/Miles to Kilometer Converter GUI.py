from tkinter import *

window = Tk()



def button_clicked():
    miles = input.get()
    math = float(miles) * 1.609344
    result.config(text=math)
    

window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)
window.minsize(width=350, height=80)


input = Entry(width=10)
miles = input.get()
input.grid(column=2, row=0)

miles_label = Label(text='miles')
miles_label.grid(column=3, row=0)

is_equal = Label(text='is equal to')
is_equal.grid(column=1, row=2)

result = Label(text='result')
result.grid(column=2, row=2)

km = Label(text='km')
km.grid(column=3, row=2)


button = Button(text='Calculate', command=button_clicked)
button.grid(column=2, row=3)










window.mainloop()