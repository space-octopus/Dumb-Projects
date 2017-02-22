from Tkinter import *
root = Tk()

def Exit():
	root.destroy()
	print('I love you senpai!')

from PIL import Image

count = 0
while (count < 9):
	RMS = Image.open("RMS.jpg")
	RMS.show()
	command = Exit
	print ("I love you senpai!")

#RMS = Image.open("RMS.jpg")
#RMS.show()

button = Button(text='Exit', command=Exit, fg='red', width=10, height=2)
button.pack()

root.mainloop()
