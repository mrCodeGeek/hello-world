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

	labels.append([])
	for names in range(w):

		lb = Label(root, text=str(names+1), pady=pady_v, width=width_v, bd=2, relief=RIDGE)
		lb.grid(row=name, column=names)
		labels[name].append(lb)

root.mainloop()
