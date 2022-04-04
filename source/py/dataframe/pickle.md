# Pickle


Pickling 允许您将 python 对象保存为硬盘驱动器上的二进制文件。

一句警告：不要加载你不信任的 pkl 文件。 恶意的人可以制作恶意的 pkl 文件，可能会在您的计算机上执行意外的代码（SQL注入，密码暴力强制等）。

Pickle 用于序列化和反序列化 Python 对象结构，也称为marshalling 或 flattening。
Pickle 不要与压缩相混淆！ 前者是将对象从一种表示（随机存取存储器（RAM）中的数据）转换为另一种表示（磁盘上的文本），而后者是使用较少位编码数据的过程，以节省磁盘空间。

## 代码示例

```python
import pickle
# make an example object to pickle
some_obj = {'x':[4,2,1.5,1], 'y':[32,[101],17], 'foo':True, 'spam':False}

# 写入 pkl
with open('mypickle.pickle', 'wb') as f:
    pickle.dump(some_obj, f)
# note that this will overwrite any existing file
# in the current working directory called 'mypickle.pickle'

# 读取 pkl
with open('mypickle.pickle') as f:
    loaded_obj = pickle.load(f)
print('loaded_obj is', loaded_obj)
```

使用 `pandas` 直接序列化

```python
import pandas as pd
df = pd.DataFrame([range(11), range(100,110)], columns=list('abcdefghijk'))
df.to_pickle('my_df.pickle')
df2 = pd.read_pickle('my_df.pickle')
```
