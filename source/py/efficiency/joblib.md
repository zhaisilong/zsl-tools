# Joblib

对于大多数问题，并行计算确实可以提高计算速度。 随着 PC 计算能力的提高，我们可以通过在 PC 中运行并行代码来简单地提升计算速度。Joblib 就是这样一个可以简单地将 Python 代码转换为并行计算模式的软件包，它可非常简单并行我们的程序，从而提高计算速度。

Joblib 是一组用于在 Python 中提供轻量级流水线的工具。 它具有以下功能：

- 透明的磁盘缓存功能和“懒惰”执行模式，简单的并行计算
- Joblib对numpy大型数组进行了特定的优化，简单，快速。

## 使用

### 输出值的透明快速磁盘缓存

```python
from joblib import Memory
cachedir = 'your_cache_dir_goes_here'
mem = Memory(cachedir)
import numpy as np
a = np.vander(np.arange(3)).astype(np.float)
square = mem.cache(np.square)
b = square(a)
c = square(a)
```

### 并发

```python
from joblib import Parallel, delayed
# n_jobs is the number of parallel jobs
Parallel(n_jobs=2)(delayed(my_fun)(i, j ) for i in range(num))
```

### 快速压缩持久化

替代 pickle，有效地处理包含大数据的 Python 对象(joblib)。

```python
from joblib import dump, load

pickle_file = './pickle_data.joblib'
with open(pickle_file, 'wb') as f:
    dump(data, f)
    dump(data, f, compress='zlib')

with open(pickle_file, 'rb') as f:
    data_stored = load(f)

```

## 参考

