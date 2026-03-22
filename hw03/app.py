import streamlit as st
import face_recognition
import numpy as np
from PIL import Image, ImageDraw

# 页面配置
st.set_page_config(page_title="人脸识别系统", page_icon="👤", layout="wide")
st.title("👤 基于face_recognition的人脸识别系统")
st.divider()

# 功能选项
func_mode = st.radio("选择功能", ["人脸检测", "人脸特征编码", "人脸比对识别"], horizontal=True)
uploaded_file = st.file_uploader("上传图片", type=["jpg", "jpeg", "png"])

# 加载已知人脸库（识别功能用）
def load_known_faces():
    known_encodings = []
    known_names = []
    try:
        import os
        for img_name in os.listdir("known_faces"):
            if img_name.endswith(("jpg", "png")):
                img = face_recognition.load_image_file(f"known_faces/{img_name}")
                encode = face_recognition.face_encodings(img)[0]
                known_encodings.append(encode)
                known_names.append(img_name.split(".")[0])
    except:
        pass
    return known_encodings, known_names

known_encodings, known_names = load_known_faces()

# 处理上传图片
if uploaded_file is not None:
    # 打开图片
    img = Image.open(uploaded_file).convert("RGB")
    img_np = np.array(img)
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("原始图片")
        st.image(img, use_column_width=True)
    
    # 人脸检测
    face_locations = face_recognition.face_locations(img_np)
    face_encodings = face_recognition.face_encodings(img_np, face_locations)
    
    # 绘制框
    img_draw = img.copy()
    draw = ImageDraw.Draw(img_draw)
    face_names = []
    
    # 人脸比对
    for encode in face_encodings:
        matches = face_recognition.compare_faces(known_encodings, encode)
        name = "未知"
        face_dis = face_recognition.face_distance(known_encodings, encode)
        if len(face_dis) > 0:
            best_idx = np.argmin(face_dis)
            if matches[best_idx]:
                name = known_names[best_idx]
        face_names.append(name)
    
    # 画框+标注
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        draw.rectangle([(left, top), (right, bottom)], outline="red", width=3)
        draw.text((left, top-10), name, fill="red")
    
    with col2:
        st.subheader("检测结果")
        st.image(img_draw, use_column_width=True)
    
    # 结果展示
    st.divider()
    st.subheader("检测信息")
    st.write(f"检测到人脸数量：{len(face_locations)}")
    if func_mode == "人脸特征编码":
        st.write("128维人脸特征编码（前10位）：")
        for i, encode in enumerate(face_encodings):
            st.write(f"人脸{i+1}：{encode[:10]}")
    if func_mode == "人脸比对识别" and len(known_names) > 0:
        st.write(f"识别结果：{face_names}")
else:
    st.info("请上传图片开始检测")