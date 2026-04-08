MNIST 手写数字识别项目
本项目包含两个卷积神经网络实现：极简 CNN（任务一）和经典的 LeNet-5（任务二）。

环境要求
Python 版本: 3.8+

深度学习框架: PyTorch

安装步骤
克隆或下载本项目到本地。

在项目根目录下打开终端或 PowerShell。

执行以下命令安装依赖：

Bash
pip install -r requirements.txt
数据集说明

自动下载: 程序运行时会自动检测 data 文件夹。若不存在，将自动从 PyTorch 官方镜像下载 MNIST 数据集（约 50MB） 。

手动下载 (备选): 若网络连接失败，请手动下载 MNIST 的四个 gz 压缩包，并放置在项目目录下的 ./data/MNIST/raw/ 路径中。

运行命令
运行任务一：极简 CNN
Bash
python train.py
该程序将启动一个包含单卷积层的轻量级模型训练，预计准确率约为 97% 。

运行任务二：LeNet-5
Bash
python lenet5.py
该程序将启动经典的 LeNet-5 模型训练。根据实测，在 RTX 系列显卡或主流 CPU 上，总训练耗时约为 30 秒，最终测试集准确率可达 98.5% 以上。
