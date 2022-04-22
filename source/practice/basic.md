# PyTorch 基础

## 张量

```python
torch.stack([x1, x2], dim=-1)  # 最后一维堆叠
torch.FloatTensor(2, 3, 4)
torch.LongTensor
torch.Tensor(2, 3, 4)
torch.zeros
torch.ones(*(3,4)).fill_(1)
torch.rand(*size, )  # uniformly sampled between 0 and 1 
torch.randn  # normal distribution with mean 0 and variance 1
torch.randint(low=0, high=2, size=(self.size, 2), dtype=torch.float32)
torch.arange  # from n to m torch.Tensor (input list)
# dim 不能超过 x 的维度
torch.cat([x1, x2], dim=1)
```

张量求导

```python
from torch.autograd import Variable
Variable(x)
```

张量属性

```python
x = torch.Tensor
x.data  # data 用索引下表访问
```

## Basic

```python
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

## 拓展学习资料

- [Pytorch 中的 masked_fill() 方法](https://mp.weixin.qq.com/s?__biz=MzAwNjU0NjA3Ng==&mid=2247489300&idx=2&sn=2f57774e6bbc24a3e3d48da5ed39a30f&chksm=9b0ae0e7ac7d69f168152b8fe872d98fb6cb92962005e0bd146b3ef12fb44ea953c1c6fd19c4&mpshare=1&scene=1&srcid=0419skTv7Thxh4EGyHVDfIyD&sharer_sharetime=1650328747544&sharer_shareid=f66ef27ade3d509229b2afd8611df712#rd)