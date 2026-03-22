# 人脸识别系统 - 作业三
基于 face_recognition 与 Streamlit 实现的人脸检测/识别 Web 系统

## 项目结构
```
hw03/
├── app.py              # 主程序：人脸检测/识别逻辑 + Streamlit 可视化界面
├── requirements.txt    # Python 依赖库清单
├── README.md           # 项目说明文档
└── known_faces/        # 已知人脸库（存放「姓名.jpg」格式图片，用于人脸比对）
```

## 功能说明
### 核心功能
1. **人脸检测**：自动定位图片中的人脸，用红色框标注位置
2. **人脸特征编码**：提取人脸的 128 维特征向量（人脸识别的核心特征）
3. **人脸比对识别**：与 `known_faces` 文件夹中的已知人脸库匹配，输出识别身份

### 检测/识别流程
1. 上传图片 → 转换为 RGB 格式
2. 调用 face_recognition 检测人脸坐标 → 提取 128 维特征编码
3. 若选择「人脸比对识别」，则与已知人脸库的特征编码进行比对，输出匹配结果
4. 在 Web 界面可视化标注人脸框与识别结果

## 人脸库准备（可选）
若需使用**人脸比对识别**功能：
1. 在 `hw03` 文件夹下新建 `known_faces` 文件夹
2. 将需要识别的人脸图片放入该文件夹，命名格式为 `姓名.jpg`（如 `张三.jpg`）
3. 程序运行时会自动加载这些图片，提取特征并建立人脸库

## 运行与访问方式
### 环境准备
1. 创建并激活 Python 环境（推荐 Anaconda）：
   ```bash
   conda create -n hw03 python=3.10 -y
   conda activate hw03
   ```
2. 安装 dlib（Windows 推荐用 conda 避免编译）：
   ```bash
   conda install -c conda-forge dlib -y
   ```
3. 安装 Python 依赖：
   ```bash
   pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
   ```

### 运行命令
在 `hw03` 文件夹路径下执行：
```bash
streamlit run app.py
```

### 访问方式
- 本地访问：http://localhost:8501
- 若浏览器未自动弹出，手动复制上述 URL 到浏览器打开即可

