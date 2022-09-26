import cv2
import numpy as np
import matplotlib.pyplot as plt
def scan(img):
    # Resize image to workable size
    dim_limit = 1080
    max_dim = max(img.shape)
    if max_dim > dim_limit:
        resize_scale = dim_limit / max_dim
        img = cv2.resize(img, None, fx=resize_scale, fy=resize_scale)
    # Create a copy of resized original image for later use
    orig_img = img.copy()
    # Repeated Closing operation to remove text from the document.
    kernel = np.ones((5, 5), np.uint8)
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=5)
    return img   
img = cv2.imread('FinalYearProject\Project\inputs\img5.jpg')
scanned_img = scan(img)
plt.imshow(scanned_img)
print("scanned")
plt.show()
cv2.destroyAllWindows()

