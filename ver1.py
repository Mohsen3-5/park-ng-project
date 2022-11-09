import matplotlib.pyplot as plt
import cv2
import numpy as np
import math

def slope(x1, y1, x2, y2):
    m = (y2-y1)/(x2-x1)
    return m
def clear_points(mylist):
    print(len(mylist))
    for i in range(0, len(mylist)):
        for j in range(i + 1, len(mylist)):
            if len(mylist) <= j:
                break
            if math.dist([mylist[i][0], mylist[i][1]], [mylist[j][0], mylist[j][1]]) < 10:
                mylist.remove([mylist[j][0], mylist[j][1]])
    return  mylist


def plot_gray(input_image, output_image1, output_image2):
    """
       Converts an image from BGR to RGB and plots

    """

    # change color channels order for matplotlib
    fig, ax = plt.subplots(nrows=1, ncols=3)

    ax[0].imshow(input_image, cmap='gray')
    ax[0].set_title('Input Image')
    ax[0].axis('off')

    ax[1].imshow(output_image1, cmap='gray')
    ax[1].set_title('Histogram Equalized ')
    ax[1].axis('off')

    ax[2].imshow(output_image2, cmap='gray')
    ax[2].set_title('Histogram Equalized ')
    ax[2].axis('off')

    plt.show()


img = cv2.imread('pic2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
equ = cv2.equalizeHist(gray)
# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(gray)
plot_gray(gray, equ, cl1)
gray = cl1

# res = np.hstack((gray, equ, cl1))
color=[(255, 0, 0),(255, 0, 255),(255, 255, 255)]
kernel_size = 17
blur_gray = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)
plt.imshow(blur_gray)
plt.show()

low_threshold = 50
high_threshold = 110
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)
plt.imshow(edges)
plt.show()
rho = 1  # Hough (pürüzlü) ızgarasının piksel cinsinden uzaklık çözünürlüğü
theta = np.pi / 180  # Hough (sert) ızgarasının radyanlarında açısal çözünürlük
threshold = 25  # Minimum oy sayısı (Hough grid cell'deki kesitler)
min_line_length = 70  # bir satır oluşturan minimum piksel sayısı
max_line_gap = 20  # bağlanılabilir çizgi parçaları arasındaki maksimum piksel aralığı
line_image = np.copy(img) * 0  # çizgi çizmek için boşluk oluşturma


lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]),
                        min_line_length, max_line_gap)
a=[]
b=[]

for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 5)




"""
def mousepoint(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter]=x,y
        counter=counter+1
        print(circles)


"""





lines_edges = cv2.addWeighted(img, 0.8, line_image, 1, 0)
plt.imshow(lines_edges)
plt.show()

#round(slope(lines[i][0][0],lines[i][0][1],lines[i][0][2],lines[i][0][3]))==round(slope(lines[j][0][0],lines[j][0][1],lines[j][0][2],lines[j][0][3]))