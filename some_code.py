# 以下代码是选择外接矩形或者外接圆形等等。
# def __call__(self, img):
#     mode = CONTOUR_MODE[self._mode]
#     method = CONTOUR_METHOD[self._method]
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     cnts, _ = cv2.findContours(img, mode, method)
#     img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
#     if self._bbox == RECT_CONTOUR:
#         bboxs = [cv2.boundingRect(cnt) for cnt in cnts]
#         print(bboxs)
#         for x, y, w, h in bboxs:
#             img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), thickness=2)
#     elif self._bbox == MINRECT_CONTOUR:
#         bboxs = [np.int0(cv2.boxPoints(cv2.minAreaRect(cnt))) for cnt in cnts]
#         img = cv2.drawContours(img, bboxs, -1, (255, 0, 0), thickness=2)
#     elif self._bbox == MINCIRCLE_CONTOUR:
#         circles = [cv2.minEnclosingCircle(cnt) for cnt in cnts]
#         print(circles)
#         for (x, y), r in circles:
#             img = cv2.circle(img, (int(x), int(y)), int(r), (255, 0, 0), thickness=2)
#     elif self._bbox == NORMAL_CONTOUR:
#         img = cv2.drawContours(img, cnts, -1, (255, 0, 0), thickness=2)
