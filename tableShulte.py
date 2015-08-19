# -*- coding: utf-8 -*-

from tkinter import *
from functions import functions_main as fun_m

root = Tk()

labels = []
h = 7
w = 7
pady_v = 7
width_v = 4

gameZone = Frame(root)
gameZone.pack_propagate(False)
gameZone.pack()

for name in range(h):

	labels.append([])
	for names in range(w):

		lb = Label(gameZone, text=str(0), pady=pady_v, width=width_v, bd=2, relief=RIDGE)
		lb.grid(row=name, column=names)
		labels[name].append(lb)


b = Button(root, text="Generate", command= lambda: fun_m.generate(labels, h, w))
b.pack()

root.mainloop()
