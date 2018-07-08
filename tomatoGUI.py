#-*-coding:utf-8-*-
from tkinter import *
import time


class ClickIt:

	def __init__(self, master):
	#sets blank page 
		frame = Frame(master)
		frame.pack()
		master.geometry('450x400')
		master.title("Cat-omato")
	#adds an image to the background
		background = PhotoImage(file=r"")
		self.label_0 = Label(image=background)
		self.label_0.image = background
		self.label_0.pack(fill=BOTH)
	#interaction boxes
		self.click_button = Button(frame, text="CLICKITTY CLICK IT", command=self.print_message)
		self.click_button.pack(side=TOP)
		self.quit_button = Button(frame, text = "quit", command=master.destroy) #interrupts the process
		self.quit_button.pack(side=BOTTOM)
	#creates a menu bar
		menu = Menu(root)
		root.config(menu=menu)
		sub_menu = Menu(menu, tearoff=0)
		menu.add_cascade(label="Info", menu=sub_menu)
		sub_menu.add_command(label="About the product", command=self.open_about)
		sub_menu.add_command(label="Portability", command=self.open_portability)
		sub_menu.add_separator()
		sub_menu.add_command(label="Exit", command=root.destroy)

		time_left = 30
		
		label_2 = Label(master, text='%s tomatoes remaining'%str(time_left), bg="black", fg="green")
		label_2.pack()

	def print_message(self):
		print("Cat-omato gonna eat all tomatoes!! Hurry back to work!!!!!")

	def open_about(self):
		print("A cat that eats tomatoes. It will never let you procrastinate with this much of vitamins.\nThe poor little fella needs to be fed, so keep your hands on the job!!.")

	def open_portability(self):
		print("Until then it works fine on Win7. A new version shall be built for Linux pretty soon")

root = Tk()
click = ClickIt(root)
root.mainloop()

#def more_info(self):
		#opens a pop-up message

#def tomatoes_left(self):
		#time.sleep(60)


