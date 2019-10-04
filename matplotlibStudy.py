import matplotlib.pyplot as plt

import numpy as np

plt.style.use("ggplot") #%matplotlib inline是jupyter自带的方式，允许图表在cell中输出。

# 第一步：建立空白图，也可以指定所建立图的大小，添加figsize=()
fig1 = plt.figure()    
# 第二步：创建subplot，一个窗口可以添加多个子绘图区。其中subplot()函数中的三个数字，第一个表示Y轴方向的子图个数，
# 第二个表示X轴方向的子图个数，第三个则表示当前要画图的焦点。 
ax1=plt.subplot(2,2,1)      
ax2=plt.subplot(2,2,2)
ax3=plt.subplot(2,2,3)
ax4=plt.subplot(2,2,4)
# 第三步：subplot中绘图
# 调用子绘图区的方法，可以绘制点线图、频数图、散点图等常用图形。
ax1.plot(np.random.randn(50).cumsum(),'k--')  
ax4.hist(np.random.randn(30))
# 第四步：设置各种参数# 
ax1.set_xlim(-10,60)   #set_xlims设置坐标轴的上下限
ax1.set_xticks([0,20,40,60])  #set_ticks设置坐标刻度
ax1.set_xticklabels(['a','b','c','d']) #set_ticklabel设置坐标标注
# 第五步：清除和保存图形
ax1.clear()  
fig1.savefig('test.jpg')  # #windows下的路径  


import pandas as pd  
from pandas import Series,DataFrame

se1 = Series(np.random.randn(30).cumsum())  
df = DataFrame({'a':np.random.randn(30),'b':np.random.randn(30)})
se1.plot(kind = 'bar', color = 'g', alpha = 0.5, grid=True)  
df.plot(kind = 'bar', alpha=0.5)  