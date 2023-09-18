import tkinter


window = tkinter.Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=300, height=300)
window.config(padx=50, pady =100)


input = tkinter.Entry(width=5)
input.grid(row=0, column=1)


miles = tkinter.Label(text="Miles", font=("Arial", 10, "italic"))
miles.grid(row=0, column=2)


is_equal = tkinter.Label(text="is equal to", font=("Arial", 10, "italic"))
is_equal.grid(row=1, column=0)

km = tkinter.Label(text="Km", font=("Arial", 10, "italic"))
km.grid(row=1, column=2)

number = tkinter.Label(text=0, font=("Arial", 10, "italic"))
number.grid(row=1, column=1)


def calc():
    m = int(input.get())
    to_km = round(m * 1.6, 2)
    number.config(text=to_km)


btn = tkinter.Button(text="Convert", command=calc)
btn.grid(row=2, column=1)


window.mainloop()
