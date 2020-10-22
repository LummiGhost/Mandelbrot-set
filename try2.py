import numpy as np
import matplotlib.pyplot as plt
import os
 
#定义迭代函数
iterFunction = lambda z,c:(z**2 + c)
def calcPoints(c,maxIterNum = 128):
    z = complex(0,0)
    num = 0
    while abs(z)<2 and num <maxIterNum:
        z = iterFunction(z , c)
        num = num+1
    if num == maxIterNum:
        return z.real
    else:
        return num

def mandelbrot(xArea=[-2,2],yArea=[-2,2],num = 1000):
    X,Y = np.meshgrid(np.linspace(xArea[0],xArea[1],num+1),np.linspace(yArea[1],yArea[0],num+1))
    C = X + Y*1j
    result  = np.zeros((num+1,num+1))
    for i in range(num+1):
        for j in range(num+1):
            result[i,j] = calcPoints(C[i,j])
        ##打印百分比
        if i*10%num == 0 :
            print( i / num * 100 ) 
    plt.imshow(result,vmax=abs(result).max(),vmin=abs(result).min(),extent = xArea + yArea)
    return result
    
    
 
if __name__ =="__main__":
    # display_mandelbrot([-0.5226,-0.5225],[0.6243,0.6244])
    # display_mandelbrot(num = 200)
    plt.hot()
    mandelbrot([-0.56,-0.53],[-0.55,-0.52],100)
    # plt.imshow()
    plt.show()