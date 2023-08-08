# 生成曼德勃罗集图像

**GPU版本暂时无法使用！！！**
**GPU版本暂时无法使用！！！**
**GPU版本暂时无法使用！！！**

随便写的，玩玩而已，功能还不完善。
借鉴了其他大佬的思路。

## 依赖库

- numpy
- matplotlab
- numba (cuda GPU support)(但是GPU版目前用不了)

```shell
pip install numpy,matplotlib,numba
```

## 实例

```python
from try2 import mandelbrot
import matplotlab as mp
mp.hot()
mandelbrot([-0.56,-0.53],[-0.55,-0.52],100)
#前两个参数为需要生成的图形的区域（建议传入方形区域，不然可能会变形。），最后一个参数是方阵的阶数。
#更新：已支持非方形区域，最后一个参数为y轴的分辨率，x轴分辨率将根据区域的形状自动计算。
mp.show()
```

目前还有很多要改的地方。本来还想加入捕获matplotlab的鼠标事件的交互功能，但是实在没精力了。
随缘更新吧。

<!-- 现实太残酷了。 -->
