import cv2
import numpy as np

def compute_mse(image_path1, image_path2):
    r = cv2.imread(image_path1, cv2.IMREAD_GRAYSCALE)  
    p = cv2.imread(image_path2, cv2.IMREAD_GRAYSCALE)  

    if r is None or p is None:
        raise ValueError("One or both images could not be loaded.")
    if r.shape != p.shape:
        raise ValueError("Images must have the same dimensions.")
    M, N = r.shape  

    diff = r.astype(np.float64) - p.astype(np.float64)
    squared_diff = diff ** 2
    mse = np.sum(squared_diff) / (M * N)

    return mse

def compute_mse_color(image_path1, image_path2):
    r = cv2.imread(image_path1)
    p = cv2.imread(image_path2)

    if r is None or p is None:
        raise ValueError("One or both images could not be loaded.")
    if r.shape != p.shape:
        raise ValueError("Images must have the same dimensions.")
    M, N, C = r.shape

    diff = r.astype(np.float64) - p.astype(np.float64)
    mse = np.sum(diff ** 2) / (M * N * C)

    return mse

if __name__ == "__main__":
    mse_value = compute_mse("./istockphoto-1369976302-612x612.jpg", "F:\\Programming\\Pyhthon\\Python-programming\\istockphoto-1369976302-612x6123.jpg")
    mse_value_color=compute_mse_color("./istockphoto-1369976302-612x612.jpg", "F:\\Programming\\Pyhthon\\Python-programming\\istockphoto-1369976302-612x6123.jpg")

    print("MSE:", mse_value)
    print("MSE_color",mse_value_color)
