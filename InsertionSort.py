list = [ 4, 8, 3, 9, 1, 6, 14, 13, 7, 19, 2, 12, 5, 11, 10, 15, 17, 16, 18, 20]
#insertion sort
for i in range(1,20):
	save = list[i]
	j = i-1
	while j >=0 :
		if save < list[j]:
			list[j+1] = list[j]
			list[j] = save
		else :
			break
		j = j-1
#print
for i in range(0,20):
	print list[i]