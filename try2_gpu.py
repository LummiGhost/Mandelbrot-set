import numpy as np
import matplotlib.pyplot as plt
import os
import math
from numba import cuda
 
#定义迭代函数
iterFunc = lambda z,c:(z**2 + c)
maxIterNum = 128
class index2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y

@cuda.jit
def calcMandelbrot(img,C,accuracy):
    idx = index2D(cuda.blockIdx.x * cuda.blockDim.x + cuda.threadIdx.x , cuda.blockIdx.y * cuda.blockDim.y + cuda.threadIdx.y)
    z = complex(0,0)
    num = 0
    if idx.x<accuracy and idx.y<accuracy:
        while abs(z)<2 and num <maxIterNum:
            z = iterFunc(z , C[idx.x,idx.y])
            num = num+1
        if num == maxIterNum:
            img[idx.x,idx.y] = z.real
        else:
            img[idx.x,idx.y] = num 



def mandelbrot(xArea = [-2,2],yArea = [-2,2],accuracy = 1000):
    X,Y = np.meshgrid(np.linspace(xArea[0],xArea[1],accuracy+1),np.linspace(yArea[1],yArea[0],accuracy+1))
    C = X + Y*1j
    img = np.zeros((accuracy+1,accuracy+1))
    # resurt = np.zeros((accuracy+1,accuracy+1))

    #GPU计算
    threadsPerBlock = 1024
    blocksPerGrid = math.ceil(accuracy / threadsPerBlock)
    calcMandelbrot[blocksPerGrid,threadsPerBlock](img,C,accuracy)
    cuda.synchronize()
    return img
    

 
if __name__ =="__main__":
    # display_mandelbrot(x_num=200,y_num=200)
    # display_mandelbrot([-1,0],[0,1],x_num=200,y_num=200)
    # display_mandelbrot([-0.5226,-0.5225],[0.6243,0.6244])
    img = mandelbrot()
    # os.system('pause')
    # display_mandelbrot()
    # input()