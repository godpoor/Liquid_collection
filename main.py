import cv2
import numpy as np
global filtered_bboxs
file = "other/BTSTO_176.png"
image = cv2.imread(file)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 利用二值法将图像的边框画出来
_, threshold_image = cv2.threshold(gray_image, 40, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(threshold_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour_image = image.copy()
# 使用矩形显示
bboxs = [cv2.boundingRect(cnt) for cnt in contours]

# 使用列表排序按照第三项加上第四项的值进行排序
sorted_bboxs = sorted(bboxs, key=lambda x: x[2] + x[3], reverse=True)

# 如果bboxs中有多个元素，保留第三项加上第四项最大的元素
if len(sorted_bboxs) > 1:
    filtered_bboxs = [sorted_bboxs[0]]  # 先将第一个元素加入筛选后的列表中
    max_sum = sorted_bboxs[0][2] + sorted_bboxs[0][3]  # 记录第一个元素的第三项加上第四项的和
    for bbox in sorted_bboxs[1:]:
        if bbox[2] + bbox[3] > max_sum:
            filtered_bboxs = [bbox]  # 如果当前元素的第三项加上第四项的和大于之前记录的最大和，则更新筛选后的列表
            max_sum = bbox[2] + bbox[3]
        elif bbox[2] + bbox[3] == max_sum:
            filtered_bboxs.append(bbox)  # 如果当前元素的第三项加上第四项的和等于最大和，则将其加入筛选后的列表中

    print("Filtered Bboxes:", filtered_bboxs)



# print(type(bboxs),bboxs[0],bboxs[2])
for x, y, w, h in filtered_bboxs:
    # if w>3 and  h>3:
        print("x的值为：", x, "\ty的值为：", y, "\tw的值为：", w, "\th的值为：", h)
        contour_image = cv2.rectangle(contour_image, (x, y), (x + w, y + h), (255, 0, 0), thickness=2)

# Display the original image with contours
cv2.imshow('Image with Contours', contour_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
