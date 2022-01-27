import os
#输入想要存储图像的路径
# os.chdir('路径')

import matplotlib.pyplot as plt
import numpy as np
#改变绘图风格
import seaborn as sns
sns.set(color_codes=True)


cell = ['18 Dirs','18 Dirs(D)','ESPCN','SR-q-DL', '3D CNN', 'SARDI1',
        'SARDI2','SARDI3']
pvalue = [33.01,33.65,33.05,34.76,
          35.14,35.77,35.89,36.26]


width = 0.60
index = np.arange(len(cell))
p1 = np.arange(0,len(cell),0.01)
p2 = 0.05 + p1*0

q1 = np.arange(0,len(cell),0.01)
q2 = 0.1 + p1*0

figsize = (10,8)#调整绘制图片的比例
# plt.plot(p1,p2,color = 'red',label = '5% significance level')#绘制直线
# plt.plot(q1,q2,color = 'yellow',label = '10% significance level')#绘制直线
#若是不想显示直线，可以直接将上面两行注释掉
plt.bar(index, pvalue, width,color='#00008B') #绘制柱状图'#00008B'"#87CEFA"
#plt.xlabel('cell type') #x轴
plt.ylabel('dB') #y轴
plt.ylim(30, 37)
plt.title('The PSNR of GFA') #图像的名称
plt.xticks(index, cell,fontsize=8) #将横坐标用cell替换,fontsize用来调整字体的大小
plt.legend() #显示label
plt.savefig('test.png',dpi = 600) #保存图像，dpi可以调整图像的像素大小