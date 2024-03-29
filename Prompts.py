import tkinter


def button_save(entry_text):
    with open('C:\\Users\\fabi_\\PycharmProjects\\Productivity Suit\\Data\\tasks.txt', 'a') as f:
        f.write(entry_text + '\n')
        prompt1.destroy()
        #Startpage.Label_to_do_list = tkinter.Label(startpage,text=TO_DO_LEISTE.todo())
        #Label_to_do_list.place(relx=0.01, rely=0.19)



def add_new_task():
    global prompt1
    prompt1 = tkinter.Tk()
    prompt1.title("Neue Aufgabe")
    q1 = tkinter.Label(prompt1,text="Welche Aufgabe?")
    q1.pack()
    e1 = tkinter.Entry(prompt1)
    e1.pack()
    b1 = tkinter.Button(prompt1,text="Save", command=lambda: button_save(e1.get()))
    b1.pack()
    prompt1.mainloop()


