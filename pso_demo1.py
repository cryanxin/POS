#粒子群算法
#求 (x-1)*(x-2)*(x-3)*(x-4) 的最小值
#-*-coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

N = 50         #迭代次数
c1 = c2 = 2    #初始学习因子为2
wight = 1      #权重
m = 50         #粒子数目

def fun(x):
    return (x-1)*(x-2)*(x-3)*(x-4)

x0 = np.linspace(-10,10,m)
v0 = np.random.randn(m)
y0 = fun(x0)
p = np.array([x0,y0],dtype=np.float32) #记录每一个点的最好位置和最好位置对应的值 5
pg = np.array([x0,y0],dtype=np.float32) #记录所有最好位置和最好位置对应的值 5


x_old = np.array(x0)
v_old = v0
y_old = np.array(y0)
x_mid = np.array(x0)
y_mid = np.array(y0)

result = []
for i in range(N):
    v_new = wight*v_old + c1*np.random.rand()*(p[0] - x_old) + c2*np.random.rand()*(pg[0]-x_old)
    x_new = x_old + v_old
    y_new = fun(x_new)

    for i in range(m):
        if(y_new[i]<y_old[i]):
            y_mid[i] = y_new[i]
            x_mid[i] = x_new[i]
        else:
            y_mid[i] = y_old[i]
            x_mid[i] = x_old[i]
    p = np.array([x_mid, y_mid], dtype=np.float32)

    a_old = x_old   #这四个在后面求pg用
    a_new = x_new
    b_old = y_old
    b_new = y_new

    x_old = x_new
    y_old = y_new
    v_old = v_new

    for i in range(m):
        b_max = np.max(b_new)
        index = np.where(b_new == b_max)
        if (b_old[i] < b_max):
            b_new[index] = b_old[i]
            a_new[index] = a_old[i]
    pg = np.array([a_new,b_new],dtype=np.float32)
    result.append(min(pg[1]))

print(min(result))
plt.plot(result)
plt.show()
