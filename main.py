import cv2
import numpy as np

file = "test.png"
image = cv2.imread(file)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 利用二值法将图像的边框画出来
_, threshold_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(threshold_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour_image = image.copy()
# 使用矩形显示
bboxs = [cv2.boundingRect(cnt) for cnt in contours]
for x, y, w, h in bboxs:
    print("x的值为：", x, "\ty的值为：", y, "\tw的值为：", w, "\th的值为：", h)
    contour_image = cv2.rectangle(contour_image, (x, y), (x + w, y + h), (255, 0, 0), thickness=2)

# Display the original image with contours
cv2.imshow('Image with Contours', contour_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
