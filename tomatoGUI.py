#-*-coding:utf-8-*-
from tkinter import *
import tkinter.messagebox
import time


class ClickIt:

	def __init__(self, master):
	#sets blank page 
		#4
		frame = Frame(master,bg="red")
		frame.pack(fill=BOTH)
		master.geometry('475x610')
		master.title("CaTomato"+" - made for procrastinators")

	#adds an image to the background
		background = PhotoImage(file=r"YourLocalHere\canjica.gif")
		#animation = PhotoImage(file=r"YourLocalHere\animada.gif")
		self.label_0 = Label(image=background, bg="black")
		self.label_0.image = background
		self.label_0.pack(side=BOTTOM, fill=BOTH)

	#creates a menu bar
		menu = Menu(root)
		root.config(menu=menu)
		sub_menu = Menu(menu, tearoff=0)
		menu.add_cascade(label="Info", menu=sub_menu)
		sub_menu.add_command(label="About", command=self.open_about)
		sub_menu.add_command(label="Portability", command=self.open_portability)
		sub_menu.add_separator()
		sub_menu.add_command(label="Exit", command=root.destroy)

		#time_left = 30
		self.label_2 = Label(master, bg="white", font =('arial', 14	,'normal')) # text='%s tomatoes remaining'%str(time_left)
		self.label_2.pack(fill=BOTH, padx=2, pady=4)

	#interaction boxes and toolbar
		KITTY = "CLICKITTY CLICK IT"
		toolbar = Frame(master,bg ="red")
		self.master = master
		self.start_button = Button(frame, text=KITTY, bg="yellow", command=self.initialize)
		self.start_button.pack(padx=7, pady=4)
		self.repeat_button = Button(toolbar,text="repeat", fg="grey") #,reset
		self.repeat_button.pack(side=LEFT, padx =3, pady=3)
		self.quit_button = Button(toolbar, text = "quit", command=master.destroy) #interrupts the process
		self.quit_button.pack(side=LEFT, padx= 1)
		toolbar.pack(side=TOP, fill=X)

		'''all functions below show pop-ups'''

	#sets a countdown which begins from 30 seconds.
	def initialize(self):
	
	#1); #3).
		tkinter.messagebox.showinfo("GEEZ!","CaTomato gonna eat all tomatoes!! Hurry back to work!!!!!")
		seconds = []
		
		#lists 30 to 0
		for second in range (0,31):

			seconds.append(second)

		seconds.reverse()

		#countdown
		for countdown in range(len(seconds)):

			self.label_2['text'] = '%s tomatoes remaining'% seconds[countdown]
			#self.master.update()
			self.master.after(1000)

			if (seconds[countdown] == 0):
				self.label_2['text'] = "time's up! go get some rest"
				#self.master.update()
				break

	''' 
	self.remaining = 0
        self.countdown(10)

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.label.configure(text="time's up!")
        else:
            self.label.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown) '''

	#2) #def reset(self):

	def open_about(self):
		tkinter.messagebox.showinfo("About","A cat that eats tomatoes. It will never let you procrastinate with this much of vitamins.\nThe poor little fella needs to be fed, so keep your eyes on the job!!.")

	def open_portability(self):
		tkinter.messagebox.showinfo("Portability","Until then it works fine on Win7. A new version shall be built for Unix-like systems pretty soon in case of need.")

if __name__ == "__main__":
	root = Tk()
	click = ClickIt(root)
	root.mainloop()





# 


#5);#6);#7).

#def more_info(self):
		#opens a pop-up message

	#def tomatoes_left(self):
		#time.sleep(60)
'''
	def first_instance():
		root = Tk() #root is the main window
		top_frame = Frame(root, width=500, height=340)
		top_frame.pack()
		bottom_frame = Frame(root)
		bottom_frame.pack(side=BOTTOM)

		button_1 = Button(bottom_frame, text = "GO!", fg = "red") #defines a button an its text color
		label_1 = Label(root, text="CLICKITTY CLICK IT", bg="grey", fg="white")
		label_2 = Label(bottom_frame, text="GET 'EM TIGER", bg="grey", fg="red")
		label_1.pack(fill=BOTH)
		label_2.pack(fill=Y,side=TOP)
		#button_1.bind("<Button-1>",time_left)
		button_1.pack()

		root.mainloop() #Tk() and .mainloop() will build the main structure

	def second_instance():
		tomato_remaining = 30
		
		label_2.pack(fill=BOTH)
	first_instance()
'''


