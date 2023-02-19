import tkinter

def update_key_window():
    def save_key(window):
        with open("key/myKey.txt", "w") as file:
            file.write(key_entry.get())
        window.destroy()
    window = tkinter.Tk()
    tkinter.Label(window, text = "Enter Your Key").grid(row=0, column=0, padx = 10, pady = 10)
    key_entry = tkinter.Entry(window, width = 20)
    key_entry.grid(row=0, column=1, pady = 10)
    tkinter.Button(window, text = "Change Key",
                   width = 10, font=("Arial", "8"),
                   command =lambda: save_key(window)).grid(row=1,
                                            columnspan = 2,
                                            pady = 10)

