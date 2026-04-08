import torch
import torch.nn as nn
import torch.nn.functional as F

class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        # 卷积层 1：输入 1 通道（黑白），输出 10 通道，卷积核 5x5 
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        # 卷积层 2：输入 10 通道，输出 20 通道，卷积核 5x5 
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        # 随机丢弃层，防止过拟合 
        self.conv2_drop = nn.Dropout2d()
        # 全连接层 1：320 个神经元到 50 个神经元 
        self.fc1 = nn.Linear(320, 50)
        # 全连接层 2：50 到 10（对应 0-9 十个数字） 
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        # 卷积 -> 池化 -> ReLU 激活 
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        # 卷积 -> 丢弃 -> 池化 -> ReLU 激活 
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        # 展平数据，为全连接层做准备 
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        # 使用 Log Softmax 输出概率 
        return F.log_softmax(x, dim=1)