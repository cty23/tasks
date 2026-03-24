import streamlit as st
import numpy as np
from src.face_utils import process_and_draw_faces

st.set_page_config(page_title="人脸检测与识别", page_icon="👤")

st.title("👤 人脸检测与特征提取")
st.markdown("上传一张包含人脸的图片，系统将自动检测人脸位置，并提取 **128 维特征向量**。")

# 1. 图片上传组件
uploaded_file = st.file_uploader("请选择一张图片 (支持 jpg, jpeg, png)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 划分左右两列对比展示
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("原始图片")
        st.image(uploaded_file, use_container_width=True)
        
    # 添加一个按钮触发检测，避免每次改变组件都重新跑模型
    if st.button("开始检测并提取特征", type="primary"):
        with st.spinner("正在调用 dlib 处理中..."):
            
            # 调用封装好的核心逻辑
            processed_image, face_count, encodings = process_and_draw_faces(uploaded_file)
            
            with col2:
                st.subheader("检测结果")
                st.image(processed_image, use_container_width=True)
                
            st.success(f"处理完成！在这张图片中共检测到 **{face_count}** 张人脸。")
            
            # 2. 展示 128 维特征编码
            if face_count > 0:
                st.divider()
                st.subheader("🧬 128 维特征编码提取")
                for i, encoding in enumerate(encodings):
                    with st.expander(f"查看 人脸 {i+1} 的特征向量", expanded=False):
                        # 将浮点数数组截断显示以防过长，或者展示全部
                        st.text(f"Vector shape: {encoding.shape}")
                        st.code(np.array2string(encoding, precision=4, separator=', ', suppress_small=True))