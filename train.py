import torch
import torch.optim as optim
from torchvision import datasets, transforms
from model import SimpleCNN  # 导入上面定义的模型 

# 配置参数
batch_size = 64
learning_rate = 0.01
momentum = 0.5
device = torch.device("cuda" if torch.cuda.is_available() else "cpu") 

# 1. 数据准备：加载并标准化 MNIST 数据集 
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

train_loader = torch.utils.data.DataLoader(
    datasets.MNIST('data', train=True, download=True, transform=transform),
    batch_size=batch_size, shuffle=True)

test_loader = torch.utils.data.DataLoader(
    datasets.MNIST('data', train=False, transform=transform),
    batch_size=batch_size, shuffle=True)

# 2. 初始化模型、优化器和损失函数 
model = SimpleCNN().to(device)
optimizer = optim.SGD(model.parameters(), lr=learning_rate, momentum=momentum)

# 3. 训练函数 
def train(epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()  # 梯度清零
        output = model(data)   # 前向传播
        loss = torch.nn.functional.nll_loss(output, target) # 计算损失
        loss.backward()        # 反向传播
        optimizer.step()       # 更新参数
        if batch_idx % 100 == 0:
            print(f'Train Epoch: {epoch} [{batch_idx * len(data)}/{len(train_loader.dataset)}] Loss: {loss.item():.6f}')

# 4. 测试函数 
def test():
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            test_loss += torch.nn.functional.nll_loss(output, target, reduction='sum').item()
            pred = output.data.max(1, keepdim=True)[1]
            correct += pred.eq(target.data.view_as(pred)).sum()
    
    test_loss /= len(test_loader.dataset)
    print(f'\nTest set: Average loss: {test_loss:.44f}, Accuracy: {correct}/{len(test_loader.dataset)} ({100. * correct / len(test_loader.dataset):.0f}%)\n')

# 执行训练
for epoch in range(1, 4):
    train(epoch)
    test()