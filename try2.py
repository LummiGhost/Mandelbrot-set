import numpy as np
import matplotlib.pyplot as plt
import os

MAX_ITER_NUM = 128
 
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

# def mandelbrot(xArea=[-2,2],yArea=[-2,2],num = 1000):
#     X,Y = np.meshgrid(np.linspace(xArea[0],xArea[1],num+1),np.linspace(yArea[1],yArea[0],num+1))
#     C = X + Y*1j
#     result  = np.zeros((num+1,num+1))
#     for i in range(num+1):
#         for j in range(num+1):
#             result[i,j] = calcPoints(C[i,j])
#         ##打印百分比
#         if i*10%num == 0 :
#             print( i / num * 100 ) 
#     plt.imshow(result,vmax=abs(result).max(),vmin=abs(result).min(),extent = xArea + yArea)
#     return result

def mandelbrot(xArea=[-2,2],yArea=[-2,2],num = 1000):
    size = (num, int(num * (xArea[1]-xArea[0]) / (yArea[1] - yArea[0])))
    Z = np.zeros((size[0],size[1]),dtype=complex)
    result = np.zeros((size[0],size[1]))
    X,Y = np.meshgrid(np.linspace(xArea[0],xArea[1],size[1]),np.linspace(yArea[1],yArea[0],size[0]))
    C = X + Y*1j
    count = 0
    while count < MAX_ITER_NUM:
        Z = iterFunction(Z,C)
        count = count + 1
        result[(np.abs(Z) > 2) & (result == 0)] = count
    # result[result == 0] = Z.real
    return result


    
    
 
if __name__ =="__main__":
    # display_mandelbrot([-0.5226,-0.5225],[0.6243,0.6244])
    # display_mandelbrot(num = 200)
    plt.hot()
    # mandelbrot([-0.56,-0.53],[-0.55,-0.52],1024)
    xArea = [-0.56,-0.52]
    yArea = [-0.55,-0.52]
    num = 2048
    result = mandelbrot(xArea,yArea,num)
    plt.imshow(result,vmax=abs(result).max(),vmin=abs(result).min(),extent = xArea + yArea)
    # plt.imshow()
    plt.show()