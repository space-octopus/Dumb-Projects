from Tkinter import *
root = Tk()

def Hello():
	print ('Hello!')

def GoodBye():
	print ('Goodbye!')
	root.destroy()

def Love():
	print ('I love you developer kun')
	print ('SOMETHING HAPPEND :(')
	root.destroy():

b01 = Button(text = 'Hello!', command = Hello, fg = 'GREEN', bg = 'GRAY', height = 3, width = 10)
b01.grid(row = 1, column = 2)
b02 = Button(text = 'Goodbye!', command = GoodBye, fg = 'RED', bg = 'GRAY', height = 3, width = 10)
b02.grid(row = 1, column = 3)
b03 = Button(text = 'Love...', command = Love, fg = 'PINK', bg = 'GRAY', height = 3, width = 10)
b03.grid(row = 1, column = 1)

root.mainloop()
