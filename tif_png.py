import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
# 打开TIF图像
img = Image.open('other/BTSTO_176.tif')
# 将图像转换为NumPy数组
img = np.array(img)

# 获取图像的高度和宽度
height, width = img.shape
print(height, width)
for i in range(height):
    for j in range(width):
        if img[i,j]<0:
            img[i, j]=0

#整数部分的所有的值
data_max = 30
data_min = 0  # 负数已经截断为0

# # # 将正数线性映射到0-255范围
norm_data = (img - data_min) / (data_max - data_min) * 255
norm_data = norm_data.astype(np.uint8)

plt.figure()
plt.imshow(norm_data,cmap='gray',vmin=0,vmax=100)
# 关闭坐标轴
plt.axis('off')

# 保存图像为PNG格式
plt.savefig('output_image.png', bbox_inches='tight')
# img = Image.fromarray(img)
# img.save('output_image.png')
plt.show()
# # 获取正数部分的最大最小值
# data_max = data.max()
# data_min = 0  # 负数已经截断为0
#
# # # 将正数线性映射到0-255范围
# # norm_data = (data - data_min) / (data_max - data_min) * 255
# # norm_data = norm_data.astype(np.uint8)
#
# # 使用PIL保存为PNG
# img = Image.fromarray(img)
# # img.save('output_image.tif')
# img.save('output_image.png')