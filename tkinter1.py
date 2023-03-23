import tkinter as tk
'''
TO DO

Nappula mikä tallettaa textBoxista infon muuttujaan

'''
window = tk.Tk()
window.title("Testi ikkuna")

greeting = tk.Label(text= "Hello 123")
greeting.pack()

label = tk.Label(
    text="Valkosta mustalla",
    fg="white",
    bg="black",
    width=30,
    height=5
)
label.pack()

textBox = tk.Entry()
textBox.pack(anchor="s")
textBox.insert(0,"Kirjoita tähän")

closeBtn = tk.Button(text="Sulje ikkuna", command=window.destroy)
closeBtn.pack()



root = tk.Tk()
frm = tk.Frame(root)
frm.grid()
tk.Label(frm, text="Terveppä jooo!").grid(column=0, row=0)
tk.Button(frm, text="Sulje ikkuna", command=root.destroy).grid(column=1, row=0)


root.mainloop()