#-*-coding:utf-8-*-
from tkinter import *
import tkinter.messagebox
import time


class ClickIt:

	def __init__(self, master):
	#sets blank page 
		frame = Frame(master,bg="red")
		frame.pack(fill=BOTH)
		master.geometry('475x610')
		master.title("CaTomato"+" - made for procrastinators")

	#adds an image to the background
		background = PhotoImage(file=r"YourLocalHere\canjica.gif")
		animation = PhotoImage(file=r"YourLocalHere\animada.gif")
		self.label_0 = Label(image=background, bg="black")
		self.label_0.image = background
		self.label_0.pack(side=BOTTOM, fill=BOTH)

	#interaction boxes and toolbar
		KITTY = "CLICKITTY CLICK IT"
		toolbar = Frame(master,bg ="red")
		self.start_button = Button(frame, text=KITTY, bg="yellow", command=self.initialize)
		self.start_button.pack(padx=7, pady=4)
		self.repeat_button = Button(toolbar,text="repeat", fg="grey") #,reset
		self.repeat_button.pack(side=LEFT, padx =3, pady=3)
		self.quit_button = Button(toolbar, text = "quit", command=master.destroy) #interrupts the process
		self.quit_button.pack(side=LEFT, padx= 1)
		toolbar.pack(side=TOP, fill=X)

	#creates a menu bar
		menu = Menu(root)
		root.config(menu=menu)
		sub_menu = Menu(menu, tearoff=0)
		menu.add_cascade(label="Info", menu=sub_menu)
		sub_menu.add_command(label="About", command=self.open_about)
		sub_menu.add_command(label="Portability", command=self.open_portability)
		sub_menu.add_separator()
		sub_menu.add_command(label="Exit", command=root.destroy)

		time_left = 30
		self.label_2 = Label(master, text='%s tomatoes remaining'%str(time_left), bg="grey", fg="black")
		self.label_2.pack(fill=BOTH, padx=2, pady=4)

	def initialize(self):
	#sets pop-ups
		tkinter.messagebox.showinfo("GEEZ!","CaTomato gonna eat all tomatoes!! Hurry back to work!!!!!")

	#def reset(self):

	def open_about(self):
		tkinter.messagebox.showinfo("About","A cat that eats tomatoes. It will never let you procrastinate with this much of vitamins.\nThe poor little fella needs to be fed, so keep your eyes on the job!!.")

	def open_portability(self):
		tkinter.messagebox.showinfo("Portability","Until then it works fine on Win7. A new version shall be built for Unix-like systems pretty soon in case of need.")

root = Tk()
click = ClickIt(root)
root.mainloop()