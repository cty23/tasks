import face_recognition
import numpy as np
from PIL import Image, ImageDraw

def process_and_draw_faces(file_buffer):
    """
    处理上传的图片，返回绘制了边框的图片对象、人脸数量及特征编码。
    """
    # 将上传的文件流读取为 face_recognition 可用的 numpy 数组
    image = face_recognition.load_image_file(file_buffer)
    
    # 获取人脸位置 (top, right, bottom, left)
    face_locations = face_recognition.face_locations(image)
    
    # 获取 128 维人脸特征编码
    face_encodings = face_recognition.face_encodings(image, face_locations)
    
    # 转换为 Pillow Image 对象以便画图
    pil_image = Image.fromarray(image)
    draw = ImageDraw.Draw(pil_image)
    
    # 遍历并在人脸周围画框
    for (top, right, bottom, left) in face_locations:
        draw.rectangle(((left, top), (right, bottom)), outline=(0, 255, 0), width=4)
        
    del draw # 释放画笔
    
    return pil_image, len(face_locations), face_encodings