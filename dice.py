import numpy as np 
num = 100000
a = np.random.randint(1, 7, size=(5,num))
print(a.shape)


b=np.ones(num)
for i in range(0,num):
    b[i] = np.sum(a[:,i])
print(b)

for x in range(5,31): 
    count = 0
    for i in b:
        if i == x:
            count += 1
    print("num = %d : %.2f%%"%(x,count/num*100))

