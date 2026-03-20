import cv2
import numpy as np
import matplotlib.pyplot as plt

# 任务1：使用 OpenCV 读取一张测试图片
image_path = 'test.jpg'  
img = cv2.imread(image_path)

if img is None:
    print("错误：无法读取图片，请检查图片路径！")
else:
    # 任务2：输出图像基本信息
    height, width, channels = img.shape
    dtype = img.dtype
    print(f"图像尺寸（宽 x 高）: {width} x {height}")
    print(f"图像通道数: {channels}")
    print(f"像素数据类型: {dtype}")
    
    # 任务3：显示原图
    # 使用OpenCV显示
    cv2.imshow('Original Image (OpenCV)', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # 任务4：转换为灰度图
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 显示灰度图
    cv2.imshow('Grayscale Image', gray_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 任务5：保存处理结果
    output_gray_path = 'gray_image.jpg'
    cv2.imwrite(output_gray_path, gray_img)
    print(f"灰度图已保存为: {output_gray_path}")
    
    # 任务6：裁剪左上角一块区域（例如50x50像素）并保存
    crop_size = 50
    cropped = img[0:crop_size, 0:crop_size]  # 从原图裁剪
    cv2.imshow('Cropped Region', cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # 保存裁剪区域
    crop_path = 'cropped_region.jpg'
    cv2.imwrite(crop_path, cropped)
    print(f"裁剪区域已保存为: {crop_path}")
    
    # 将图像左上角50x50区域置为黑色
    img_copy = img.copy()
    img_copy[0:50, 0:50] = [0, 0, 0]  # 设置为黑色
    cv2.imshow('Modified Image (Black Corner)', img_copy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    modified_path = 'modified_image.jpg'
    cv2.imwrite(modified_path, img_copy)
    print(f"修改后的图像已保存为: {modified_path}")

print("所有任务完成！")