from tkinter import *
from tkinter.font import Font
root=Tk()
root.title("TO DO Application")
root.geometry("400x400")

#define our font
my_font=Font(
    family="Arial",  #name of the font
    size=15

)
#create frame
my_frame=Frame(root)
my_frame.pack(pady=10)
#create listbox
my_list=Listbox(my_frame,
                font=my_font,
                width=25,
                height=5,
                bg="SystemButtonFace",
                bd=0,
                fg="#464646",
                highlightthickness=0,
                selectbackground="#a6a6a6",
                activestyle="none"
                )
#create scroll bar
scrollbar = Scrollbar(my_frame, orient="vertical")
#position the scrollbar on the right side of the listbox
scrollbar.pack(side=RIGHT, fill=Y)
#position the listbox on the left side of the frame and fill the available space
my_list.pack(side=LEFT, fill=BOTH)
#create dummy list
stuff=["learn tkinter", "update the profile","lunch with kiran","meet with team to pratice presentation"]
 #add dummy list 
for item in stuff:
    my_list.insert(END,item)
    
#connect list and scroll bar
my_list.configure(yscrollcommand=scrollbar.set)
scrollbar.config(command=my_list.yview)
my_entry=Entry(root,font=("Helvetica",24))
my_entry.pack(pady=20)
button_frame=Frame(root)
button_frame=Frame(root, bg="light blue")
button_frame.pack(pady=20)

def delete_item():
    my_list.delete(ANCHOR)
def add_item():
    my_list.insert(END,my_entry.get())
    my_entry.delete(0,"end")
delete_button=Button(button_frame,text="Delete_item",command=delete_item,bg="salmon",activebackground="green")
add_button=Button(button_frame,text="Add_item",command=add_item,bg="gold",activebackground="red")
delete_button.grid(row=0,column=0)


add_button.grid(row=0,column=1,padx=20)

root['bg']="light blue"




root.mainloop()
