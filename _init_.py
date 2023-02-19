import os
import openai
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from tkinter import *
from tkinter import ttk
from time import sleep
from threading import Thread
import emoji
from key.update_key import *

# Floodgauge
global on_click
on_click = 0

root = tb.Window(themename="superhero")

#root = tk
root.title("Open AI - Movie to Emoji")
root.iconbitmap('images/smiling.ico')
root.geometry("700x550")



def responseOpenAi(sleep_time,text):
    global on_click
    if on_click == 0:
        click1 = tb.Floodgauge(my_frame1, mask="Convert Movie Titles Into Emoji "
                     + emoji.emojize(':beaming_face_with_smiling_eyes:'),
                             mode = 'indeterminate',                          
                             font=("Helvetica",28),length = '560',
                             bootstyle="info")
        click1.grid(row=0, column=0)
        on_click = 1
        click1.start()
    sleep(sleep_time)
    # Key File
    with open("key/myKey.txt", "r") as file:
        openai.api_key = file.readlines()[0].strip()
    my_prompt = """Convert movie titles into emoji.
Back to the Future: 👨👴🚗🕒 Batman: 🤵🦇 Transformers: 🚗🤖
"""+text+":"
    try:
     response = openai.Completion.create(model="text-davinci-003",
        prompt=my_prompt,
        temperature=0.8,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"])
    except:
     my_entry2.configure(state='normal',foreground="red")
     my_entry2.delete(0,END)
     my_entry2.insert(END,"Somthing went wrong :-(\nTry Again)")
     my_entry2.configure(state='readonly')
     click1.destroy()
     on_click = 0
     
    if(on_click == 1):
     answer = response["choices"][0]["text"].strip()
     my_entry2.configure(state='normal', foreground="yellow")
     my_entry2.delete(0,END)
     my_entry2.insert(END,answer)
     my_entry2.configure(state='readonly')
     click1.destroy()
     on_click = 0

def autocapitalize(*arg):
    var.set(var.get().capitalize())

 
# Create a Function for the Button
def changeToEmoji(text):
    if(text==""):
      my_entry2.configure(state='normal',foreground="orange")
      my_entry2.delete(0,END)
      my_entry2.insert(END,"Can't be empty!")
      my_entry2.configure(state='readonly')
        
    else:
     global thread01
     thread01 =  Thread(target =
                                 responseOpenAi,args=(0.8,text))
     thread01.start()
     my_entry2.configure(state='normal', foreground="yellow")
     my_entry2.delete(0,END)
     my_entry2.insert(END,"Wait, I am converter....")
     my_entry2.configure(state='readonly')




    
# Create a Frame
my_frame1 = tb.Frame(root,bootstyle="dark")
my_frame1.grid(row=0, column=0)
my_frame1.pack(pady=40)

my_frame2 = tb.Frame(root,bootstyle="dark")
my_frame2.pack(pady=20)



# Create a Label
my_label1 = tb.Label(my_frame1,text="Convert Movie Titles Into Emoji "
                     + emoji.emojize(':beaming_face_with_smiling_eyes:'),
font=("Helvetica",28), bootstyle="inverse-light")
my_label1.grid(row=0, column = 0,pady=10,padx=10)



# Create a Entry
var = StringVar()
my_entry1 = tb.Entry(my_frame2,font=("Helvetica",22),bootstyle="light",
                     foreground="white",textvariable=var)
my_entry1.pack(pady=20,padx=20)
var.trace("w", autocapitalize)

# Create a Entry for Answer
my_entry2 = tb.Entry(my_frame2,font=("Helvetica",22), foreground="yellow",
                     state="readonly",
                     bootstyle="dark")
my_entry2.pack(pady=20,padx=20)



# Create a Button
my_style = tb.Style()
my_style.configure('light.Outline.TButton',font=("Helvetica",18))
my_button = tb.Button(my_frame2,text="Convert!",style="light.Outline.TButton",
                      command=lambda:changeToEmoji(f'{my_entry1.get()}'))
my_button.pack(pady=20)



my_menu = Menu(root)
root.config(menu=my_menu)


save_key_menu = Menu(my_menu, tearoff=0)
save_key_menu.add_command(label="Update",
                          command = update_key_window)
my_menu.add_cascade(label="Update Key", menu=save_key_menu)



root.mainloop()


