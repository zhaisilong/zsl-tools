# Numpy

## NumPy 数据类型

```python
numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)  # -> ndarray

ndarray.ndim # 数组维度
ndarray.dtype
ndarray.itemsize # 数组元素的内存大小
ndarray.size # 数组大小，flatten 后长度 shape: (3, 2) -> size: 6
b.size * b.itemsize  # 数组占内存
ndarray.shape # 数组形状

# 重构数组对象
ndarray.reshape(2,3)
```

### 数据类型对象：dtype


创建 `dtype` 对象， 用于指定数组的数据类型

```python
dt = np.dtype(np.int32)
```

创建结构化数据类型

```python
dt = np.dtype([('age', np.int8)]) # 格式是：[('字段名', 字段类型)]
a = np.array([(10,),(20,),(30,)], dtype = dt) # -> [(10,) (20,) (30,)]
a['age'] # 字段名可用于访问列的内容
```

更好的例子

```python
student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student) 
```

修改数据类型

```python
arr.astype()
```

### 结构化数据类型 dtype

读者应该优先使用 dtype 对象来表示数据类型，而不是这些字符编码。
‘b’ − boolean
‘i’ − (signed) integer
‘u’ − unsigned integer
‘f’ − floating-point
‘c’ − complex-floating point
‘m’ − timedelta
‘M’ − datetime
‘O’ − (Python) objects
‘S’, ‘a’ − (byte-)string
‘U’ − Unicode
‘V’ − raw data (void)

dtype 对象

```python
bool
inti  # 平台决定精度的整数
int8, int16, int32, int64,
uint8, uint16, uint32, uint64
float16, float32
float64  # or float
complex64
complex128  # complex
```

## 创建 NumPy 数组

### 由已有对象创建

```python
list = [1,2,3,4]
arr = np.array(list)
arr = np.asarray(list) # 只要是序列即可
# 使用可迭代对象创建ndarray数组
it = iter(list)
x = np.fromiter(it, dtype = float, count = 2)  
```

### 使用 NumPy 函数创建

```python
np.empty((3, 2), dtype = int)
np.zeros((2, 3), order = 'C') # C 是按行排列, F 是按列排列
np.eye(2)
np.ones((2, 3))
np.arange(7) # [0 1 2 3 4 5 6]
np.repeat([1, 2], 2) # [1, 1, 2, 2]
np.tile([1, 2], 2) # [1, 2, 1, 2]
mat = np.matrix('1 2; 3 4')
mat.T
mat.H # 共轭转置
mat.I # 逆矩阵
np.matlib.identity(5)
```

### 基于数值区间创建数组

```python
np.arange(start, stop, step, dtype)
np.linspace(start, stop, num, dtype)
np.logspace(start, stop, num, base, dtype)
```

## NumPy 数组操作

### 数组间的算术运算

```python
a = np.array([[1,2,30],[10,15,4]])  
b = np.array([[1,2,3],[12, 19, 29]])
a+b
a*b
a/b
```

### 数组拼接

```python
np.vstack((a,b))  # 上下
np.hstack((a,b))  # 水平
```

### 数组切片

```python
arr_name[start: end: step]
# 均匀分布与linspace
np.linspace(5,15,10)
# 通过内置slice函数创建一个切片
a = np.arange(10) 
s = slice(2,7,2) 
a[s]
```

### 数组索引与变换

`,` 区分不同的维度
多个冒号可以用一个省略号 `...` 来代替
`b[0, :, :]` = `b[0, ...]`

```python
a[:,1] # 取列
a[:,[1,2]] # 取多列
a[1,:] # 取行
a[[1,2],:] # 取多行
a[1:1] # 取元素
a[a[:,1]>2,] # 单条件过滤
a[(a[:,1]>2) & (a[:,1]<4),] # 多条件过滤
a.T # 转置
```

```python
np.transpose(a) # 转置
a.flatten() # 展平，返回拷贝
a.ravel() # 展平，返回视图，变则原变
a.shape = (6,4)  # 直接设置形状
a.reshape((6,4))  # 返回拷贝
a.resize((6,4))  # 返回视图
```

数组的组合

```python
# 水平组合
hstack((a, b))
concatenate((a, b), axis=1)
# 垂直组合
vstack((a, b))
concatenatel((a, b), axis=0)
dstack((a, b))  # 深度堆积
```

数组的分隔

```python
hsplit(a, 3)  # 三个子数组
split(a, 3, axis=1)
vsplit(a, 3)
split(a, 3, axis=0)
dplit(a, 3)
```

数组的转换

```python
b.tolist()
a.astype(int)  # 修改数组类型
```

### 数组的排序

```python
np.sort(a)
a.sort()
a.sort(axis=0) # 按列排序
np.argsort(a) # 返回排序后的下标
a[np.argsort(-a)] # 数组的降序
```

### NumPy 数组迭代

```python
a = np.array([[1,2,3,4],[2,4,5,6],[10,20,39,3]])
# 可通过修改 order 来指定迭代方向
for x in np.nditer(at):  
    print(x, end= ' ')
# 二重枚举迭代与广播
for x,y in np.nditer([a,b]): 
    print ("%d:%d" % (x,y))
```

## NumPy 数组函数

```python
ndarray.max(axis = 0) # 对列进行操作，输出单行
ndarray.min()
ndarray.sum()
```

### NumPy 字符串操作

```py
np.char.add(['hello'],[' qikegu.com'])
np.char.add(['hello', 'hi'],[' qikegu.com', ' kevin'])
np.char.multiply('qikegu ', 3)
np.char.center('qikegu', 20, fillchar = '*') # -> ******qikegu********
np.char.capitalize()
np.char.title()
np.char.lower()
np.char.upper()
np.char.split()
np.char.splitlines() # 返回字符串中的行列表，在行边界处断开。
np.char.strip()
np.char.join(':','dmy')
np.char.join([':','-'],['dmy','ymd'])
np.char.replace()

# 字符解码与编码
a = np.char.encode('qikegu', 'gb2312') 
print (a)
print (np.char.decode(a,'gb2312'))
```

### NumPy 排序、查找、计数

| 种类      | 速度 | 最差情况    | 工作区 | 稳定性 |
| :-------- | :--- | :---------- | :----- | :----- |
| quicksort | 1    | O(n^2)      | 0      | no     |
| mergesort | 2    | O(n*log(n)) | ~n/2   | yes    |
| heapsort  | 3    | O(n*log(n)) | 0      | no     |

```py
np.sort(a, axis, kind, order) # kind='quicksort', e.g. order = 'name'
np.argsort() # 返回数组排序后的索引，用于重构数组
np.lexsort() # 多序列排序，返回数组排序后的索引，用于重构数组
np.argmax() # -> Index
np.argmin() # -> Index
np.nonzero() # -> Index
np.where() # 查找数组中符合条件的元素，返回其索引
numpy.extract() # # -> 符合条件的元素
```

## NumPy 函数

### NumPy 数学函数

```py
np.sqrt()
np.std()

# 三角函数
sin()
cos()
tan()
arcsin()
arccos()
arctan()
degrees() # 查看度数结果
around(num, decimals)
floor()
ceil()
```

## NumPy 统计函数

```py
a = np.array([[2,10,20],[80,43,31],[22,43,10]])  
# 查找指定轴上，数组元素的最小值和最大值
np.amin(a,0) # 对列进行操作
np.amax()

# 返回数组某个轴方向的峰间值，即最大值最小值之差
np.ptp(a,1)

# 百分位数是统计中使用的度量，表示小于这个值的观察值占总数的百分比。
np.percentile(input, q, axis) # q: 要计算的百分位数，在 0 ~ 100 之间

# 计算数组项的中值、平均值、加权平均值
np.median() # 中值
np.mean() # 平均值

## 加权平均值
wt = np.array([0, 0, 10])
np.average(a, axis=1, weights = wt))

# 标准差与方差
np.std([1,2,3,4])
np.var([1,2,3,4])
```

## 其他

### 随机

```python
np.random.rand(10, 1)  # 二维数据
np.random.rand(10)  # 一维数据
# 指定集合和概率的随机
np.random.choice([3, 5, 7, 9],
			  p=[0.1, 0.3, 0.6, 0.0],
			  size=(100))
```

```python
np.random.seed(99)  
arr = np.array([1, 2, 3, 4, 5])
# 随机排列
new_arr = np.random.permutation(arr)
# shuffle
np.random.shuffle(arr)  # 原位操作
```

随机分布

```python
# 正态分布
x = np.random.normal(loc=1, scale=2, size=(2, 3))
# 二项式分布
np.random.binomial(n=10, p=0.5, size=10)
# 多项式分布
np.random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
```


### NumPy 副本和视图

NumPy 数组赋值，传的是指针。

```py
ndarray.view() # shallow copy，类似指针传值
ndarray.copy() # deep copy，内存独立
```

### NumPy 矩阵库函数

numpy.matlib 模块

```py
numpy.matlib.empty(shape, dtype, order)
numpy.matlib.zeros()
numpy.matlib.ones()
numpy.matlib.eye() # mn不等单位矩阵
numpy.matlib.identity()
```

### NumPy 线性代数

numpy.linalg 模块

| SN   | 函数                 | 描述               |
| :--- | :------------------- | :----------------- |
| 1    | dot()	两个数组的点积 |
| 2    | vdot()               | 两个向量的点积     |
| 3    | inner()              | 两个数组的内积     |
| 4    | matmul()             | 两个数组的矩阵乘积 |
| 5    | det()                | 计算矩阵的行列式   |
| 6    | solve()              | 解线性矩阵方程     |
| 7    | inv()                | 求矩阵的乘法逆矩阵 |