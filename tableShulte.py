# -*- coding: utf-8 -*- 

from tkinter import *

root = Tk()

labels = []
h = 5
w = 5
pady_v = 7
width_v = 4

# gameZone = Frame(root, height=500, width=500)
# gameZone.pack_propagate(False) # don't shrink
# gameZone.pack()

for name in range(h):
	for names in range(w):
		lb = Label(root, text=str(names), pady=pady_v, width=width_v, relief=GROOVE)
		lb.grid(row=w, column=(h+1))
		labels[name][names]=lb
		lb.pack()

root.mainloop()
