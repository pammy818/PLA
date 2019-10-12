import numpy as np
import matplotlib.pyplot as plt
import random
import codecs

list1=[int(l.split()[0]) for l in open("train.txt")]
list2=[int(l.split()[1]) for l in open("train.txt")]
f = codecs.open('train.txt', mode='r', encoding='utf-8')  # open txt，read as ‘utf-8’
line = f.readline() 
list3 = []
while line:
    a = line.split()
    b = a[2:3]   #choose row
    list3.append(b)  # add 

    line = f.readline()
f.close()





def sign(n):

 if(n>0):
  n = 1
 else:
  n = -1
 return n


list4 = []
for i in range(len(list3)):
    if list3[i]==['-']:
      list4.append(-1)
    else:
      list4.append(1)



def sign(n):
 if(n>0):
  n = 1
 else:
  n= -1
 return n


w=np.zeros(3)
flag = False
for i in range(len(list1)):
 h=w[0]+w[1]*list1[i]+w[2]*list2[i]
 h_y=sign(h)
 if h_y ==list4[i]:
  flag=True
 else:
  w[0]+=list4[i]
  w[1]+=list1[i]*list4[i]
  w[2]+=list2[i]*list4[i]
  flag=False
print(w)

plt.xlabel('X1')
plt.ylabel('X2')
for i in range(len(list3)):
    if list3[i]==['-']:
     a=list1[i]
     b=list2[i]
     plt.scatter(a, b,color = 'red',marker='x')
    else:
      a=list1[i]
      b=list2[i]
      plt.scatter(a, b,color = 'blue',marker='.')
x1 = []
y1 = []
for i in range(len(list1)):
	x = list1[i]
	y = -(w[1]*x + w[0])/w[2]
	x1.append(x)
	y1.append(y)
plt.plot(x1, y1,color = 'black')
plt.show()