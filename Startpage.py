import tkinter
import time
import PIL
import API
import Prompts
import TO_DO_LEISTE

#Functions




startpage = tkinter.Tk()
startpage.title("Productivity Suit")
startpage.iconbitmap("Data/img.png")
startpage.geometry("1000x1000")

daytime = ""
def check_time():
    global daytime
    hour = time.localtime().tm_hour
    if hour <= 12:
        daytime = "Morgen"
    elif hour <= 16:
        daytime = "Nachmittag"
    elif hour <= 18:
        daytime = "Präabend"
    elif hour <= 21:
        daytime = "Abend"
    else:
        daytime = "Nacht"
    gruss.config(text="Guten "+daytime+", Fabian!")
    startpage.after(10000, check_time)

gruss = tkinter.Label(startpage, text="", font=("Calibri bold", 30))
gruss.place(relx=0.01, rely=0.06, anchor="sw")
quote_of_the_day = tkinter.Label(startpage,text=API.get_quote(), font=("Times New Roman ", 19, "italic"))
quote_of_the_day.place(relx=0.01,rely=0.1)
check_time()

Button_new_task = tkinter.Button(startpage,text="Neue Aufgabe",font=("Calibri light",15),command=lambda: Prompts.add_new_task())
Button_new_task.place(relx=0.7, rely=0.3)

header = tkinter.Label(startpage, text=" Liste of TODO's ", font=("Arial bold", 13))
header.place(relx= 0.01, rely=0.15)
global label_list
label_list = []
for tasks in TO_DO_LEISTE.todo():
    label_list.append(tkinter.Button(startpage,text=tasks))

counter_a = 0

for elements in label_list:
    elements.place(relx=0.01, rely=0.19+counter_a )
    counter_a += 0.04


def button_save(entry_text):
    global label_list
    with open('C:\\Users\\fabi_\\PycharmProjects\\Productivity Suit\\Data\\tasks.txt', 'a') as f:
        f.write(entry_text + '\n')
        prompt1.destroy()
        for elements in label_list:
            elements.destroy()
        label_list = []
        counter_a = 0
        for task in TO_DO_LEISTE.todo():
            elements.place(relx=0.01, rely=0.19 + counter_a)
            counter_a += 0.04




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


startpage.mainloop()

