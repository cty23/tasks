import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
import time

# --- 1. 定义 LeNet-5 结构 ---
class LeNet5(nn.Module):
    def __init__(self):
        super(LeNet5, self).__init__()
        self.c1 = nn.Conv2d(1, 6, kernel_size=5, padding=2)
        self.c3 = nn.Conv2d(6, 16, kernel_size=5)
        self.c5 = nn.Linear(16 * 5 * 5, 120)
        self.f6 = nn.Linear(120, 84)
        self.output = nn.Linear(84, 10)

    def forward(self, x):
        x = F.max_pool2d(F.relu(self.c1(x)), 2)
        x = F.max_pool2d(F.relu(self.c3(x)), 2)
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.c5(x))
        x = F.relu(self.f6(x))
        return self.output(x)

# --- 2. 训练与测试逻辑 ---
def train(model, device, train_loader, optimizer, epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = F.cross_entropy(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % 200 == 0:
            print(f'Train Epoch: {epoch} [{batch_idx * len(data)}/{len(train_loader.dataset)}] Loss: {loss.item():.6f}')

def test(model, device, test_loader):
    model.eval()
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(target.view_as(pred)).sum().item()
    print(f'\nTest set Accuracy: {correct}/{len(test_loader.dataset)} ({100. * correct / len(test_loader.dataset):.2f}%)\n')

# --- 3. 执行主程序 ---
if __name__ == "__main__":
    print("正在启动 LeNet-5 训练任务...")
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    # 数据加载
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))])
    train_loader = torch.utils.data.DataLoader(datasets.MNIST('data', train=True, download=True, transform=transform), batch_size=64, shuffle=True)
    test_loader = torch.utils.data.DataLoader(datasets.MNIST('data', train=False, transform=transform), batch_size=1000)

    model = LeNet5().to(device)
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    start_time = time.time()
    for epoch in range(1, 4): # 训练3轮
        train(model, device, train_loader, optimizer, epoch)
        test(model, device, test_loader)
    
    end_time = time.time()
    print(f"总计训练用时: {end_time - start_time:.2f} 秒")