import numpy as np
import matplotlib.pyplot as plt
import random

def DataEmit():
#inter weight
	w0,w1,w2=int(input("please inter w0:")),int(input("please inter w1:")),int(input("please inter w2 :"))
#generate train.txt
	f=open("train.txt",'a')
#inter m and n 
	m,n=int(input("please inter m :")),int(input("please inter n :"))


#generate x1，x2,anf use x3 store label
	while(m>0): 
		x1 = random.randint(-80, 80)
		x2 = random.randint(-80, 80)
		if w0+x1 * w1 + x2 * w2>= 0 :
			x3 = '+'
			m=m-1
			f.write(str(x1))
			f.write('  ')
			f.write(str(x2))
			f.write('  ')
			f.write(str(x3))
			f.write('\n')
		else:
			m=m

	while(n>0): 
		x1 = random.randint(-80, 80)
		x2 = random.randint(-80, 80)
		if w0+x1 * w1 + x2 * w2< 0 :
			x3 = '-'
			n=n-1
			f.write(str(x1))
			f.write('  ')
			f.write(str(x2))
			f.write('  ')
			f.write(str(x3))
			f.write('\n')
		else:
			n=n


DataEmit()