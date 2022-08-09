import torch
#查看版本
print(torch.__version__)
#查看gpu是否可用
torch.cuda.is_available()
#返回设备gpu个数
torch.cuda.device_count()
