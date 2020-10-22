import numpy as np
import matplotlib.pyplot as plt
import os
 
#定义迭代函数
iter_func = lambda z,c:(z**2 + c)
def calc_steps(c,max_iter_num = 128):
    z = complex(0,0)
    num = 0
    while abs(z)<2 and num <max_iter_num:
        z = iter_func(z , c)
        num = num+1
    if num == max_iter_num:
        return z.real
    else:
        return num
def display_mandelbrot(xArea=[-2,2],yArea=[-2,2],num = 1000):
    X,Y = np.meshgrid(np.linspace(xArea[0],xArea[1],num+1),np.linspace(yArea[1],yArea[0],num+1))
    C = X + Y*1j
    result  = np.zeros((num+1,num+1))
    plt.ion()
    plt.hot()
    #计算出结果
    for i in range(num+1):
        for j in range(num+1):
            result[i,j] = calc_steps(C[i,j])
        if i*100%num == 0 :
            # print( i / num * 100 ) 
            plt.imshow(result,vmax=abs(result).max(),vmin=abs(result).min(),extent = xArea + yArea)
    plt.show(block=False)
    plt.pause(0.1)
        # threading._start_new_thread(plt.pause,(0.5,))
        # plt.pause(0.5)
    # plt.savefig("fig1.png")
    
    
 
if __name__ =="__main__":
    # display_mandelbrot([-0.5226,-0.5225],[0.6243,0.6244])
    # display_mandelbrot([0.2537269133080432,0.2537269133080432+0.0000000000000009],[0.000365995381749671,0.000365995381749671+0.0000000000000009],100)
    # display_mandelbrot(num = 200)
    display_mandelbrot([-0.56,-0.53],[-0.55,-0.52],4096)
    input()