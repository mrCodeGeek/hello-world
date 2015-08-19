from random import shuffle


def generate(arr, hei, wei):

	#generate list. all value from 1 to hei*wei. than random these (function shuffle)
	num_list = []
	for n in range(int(hei*wei)):
		num_list.append(n+1)
	shuffle(num_list)

	#assign value from random list to label text
	conter_1 = 0
	for n1 in range(len(arr)):
		for n2 in range(len(arr[n1])):
			arr[n1][n2].config(text=str(num_list[conter_1]))
			conter_1+=1