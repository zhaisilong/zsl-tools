# PyTorch

## Basic

```python
torch.__version__

# 随机
torch.manual_seed(42)  # Setting the seed

# 张量
x = torch.Tensor(2, 3, 4)
torch.zeros
torch.ones
torch.rand(*size, ): uniformly sampled between 0 and 1 
torch.randn: normal distribution with mean 0 and variance 1
torch.randint(low=0, high=2, size=(self.size, 2), dtype=torch.float32)
torch.arange: from n to m torch.Tensor (input list)

# 数据类型转换

torch.from_numpy(np_arr1)
x.numpy()
x.cpu().numpy()  # 对显卡上的数据   

# 张量操作
x2.add_(x1)  # 原位
torch.matmul(x, W)
torch.mm
torch.bmm  # b,n,m @ b,m,p -> b,n,p
torch.einsum  # matrix multiplications
x.view(2, 3)  # reshape
x.requires_grad_(True)  # 默认的矩阵不求导

y.backward()
x.grad

# Size is same as Shape
x.shape
x.size()
```

### 显卡

```python
device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

x = torch.zeros(2, 3)
x = x.to(device)
```

GPU 的随机需要手动设置

```python
# GPU operations have a separate seed we also want to set
if torch.cuda.is_available():
    torch.cuda.manual_seed(42)
    torch.cuda.manual_seed_all(42)

# Additionally, some operations on a GPU are implemented stochastic for efficiency
# We want to ensure that all operations are deterministic on GPU (if used) for reproducibility
torch.backends.cudnn.determinstic = True
torch.backends.cudnn.benchmark = False
```

## 模型

### 模型的设计

#### 模型可视化

直接 `print(model)` 可以展示层级结构

```python
# 查看权重矩阵的 size
for name, param in model.named_parameters():
    print(f"Parameter {name}, shape {param.shape}")
```

### 保存与恢复

```python
# 从模型保存
state_dict = model.state_dict()
torch.save(state_dict, "our_model.tar")

# 从 tar 恢复
state_dict = torch.load("our_model.tar")
new_model = SimpleClassifier(num_inputs=2, num_hidden=4, num_outputs=1)
new_model.load_state_dict(state_dict)
```

## 日志

当 `print` 用

```python
from logging import getLogger
import os

logger = getLogger()

if os.path.isfile(config.file_path) is False:
            raise ValueError(f"Input file path {config.file_path} not found")
        logger.info(f"Creating features from dataset file at {config.file_path}")
```
