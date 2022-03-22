# torchtext introduction

## torchtext 的组件

Field: 主要包含以下数据预处理的配置信息，比如指定分词方法，是否转成小写，起始字符，结束字符，补全字符以及词典等等

Dataset: 继承自 pytorch 的 Dataset，用于加载数据，提供了 TabularDataset 可以指点路径，格式，Field 信息就可以方便的完成数据加载。同时 torchtext 还提供预先构建的常用数据集的Dataset对象，可以直接加载使用，splits 方法可以同时加载训练集，验证集和测试集。

Iterator: 主要是数据输出的模型的迭代器，可以支持 batch 定制

### Field

Field 包含一写文本处理的通用参数的设置，同时还包含一个词典对象，可以把文本数据表示成数字类型，进而可以把文本表示成需要的 tensor类型

## 应用

- [构造词表](https://www.ylkz.life/deeplearning/p10449077/)