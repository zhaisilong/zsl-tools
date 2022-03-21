# Pandas

## 创建数据对象

```python
# 标准导入
import pandas as pd

pd.Series([1, 3, 5, np.nan, 8])
# 指定 series 的 index， index 可重复
pd.Series([1, 3, 5, np.nan, 6, 8], index=['c', 'a', 'i', 'yong', 'j', 'i'])
# 创建 DataFrame
pd.DataFrame(np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]), index=['i', 'ii', 'iii'], columns=['A', 'B', 'C'])
```

## 访问

```python
df.head(2)
df.tail(3)
df.describe()  # 描述统计信息
```

### 索引

```python
df['A']  # 按列名取
df[0:3]  # 按行数取
df.loc['2021-01-01':'2021-01-02', ['A', 'B']]  # 指定具体的标签
df.iloc[3:5, 0: 3]  # 指定标签的索引位置
```

## 函数

```python
# 对列排序
df.sort_values(by='C')
# 选择某列最大的 n 行数据
df.nlargest(2, 'A')
# 采样
df.sample(5)
df.sample(frac=0.01)  # 采样 1%

```

## 赋值

```python
# 坐标赋值
df.iloc[2, 2] = 1111
# 轴名赋值
df.loc['20130101', 'B'] = 2222
# 根据条件赋值
df.B[df.A > 4] = 0
# 整列赋值
df['F'] = np.nan
df['E'] = pd.Series([1, 2, 3, 4, 5, 6])  # 长度要一致
# 多列赋值
a = [['a', '1.2', '4.2'], ['a', '70', '0.03'], ['b', '5', '0']]
df = pd.DataFrame(a, columns=['col1', 'col2', 'col3'])
df.col1[df.col1 == 'a'] = 'm'
```

```python
data['type'].str.contains('red')
data['type'].isin(['red', 'yellow'])
```

布尔索引取反

python 内置 sum 对布尔索引求和，即计算其总数

```python
abnormal = (data[areas[1]] < 10) | (data[areas[1]] > 1e4)
data = data[~abnormal]
sum(abnormal)
```

统计某一列中不同种类的个数：

```python
data['Type'].value_counts()[0:20]
```

## df 转换为 array

```python
df.values
```

## 处理缺失值

```python
df2.dropna(how='any')  # 非原位操作
df2.fillna(df2.mean())
```

## 绘图

```python
np.random.seed(999)
df = pd.DataFrame(np.random.rand(10,4), columns = ['a', 'b', 'c', 'd'])
df.plot()
df.plot.bar()
df.plot.bar(stacked=True)
df.T  # 转置
```

## 拼接

```python
pd.concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False)
```

