# pydantic

pydantic 库是一种常用的用于数据接口 schema 定义与检查的库。

通过 pydantic 库，我们可以更为规范地定义和使用数据接口，这对于大型项目的开发将会更为友好。

当然，除了 pydantic 库之外，像是 valideer 库、marshmallow库、trafaret 库以及 cerberus 库等都可以完成相似的功能，但是相较之下，pydantic库的执行效率会更加优秀一些。

## 基本用法

```python
# 数据通过 BaseModel 类来定义
from pydantic import BaseModel

class Person(BaseModel):
	name: str

# 直接传值
p: Person = Person(name="Tom")
print(p.json())  # {"name": "Tom"}

# 通过字典传入
p = {"name": "Tom"}
p: Person = Person(**p)
print(p.json())  # {"name": "Tom"}

# 通过其他的实例化对象传入
p2: Person = Person.copy(p)
print(p2.json())  # {"name": "Tom"}
```

特色：
- 传入错误值：报错
- 传入未定义值：忽略

## pydantic 基本数据类型

```python
from pydantic import BaseModel
from typing import Dict, List, Sequence, Set, Tuple

class Demo(BaseModel):
    a: int # 整型
    b: float # 浮点型
    c: str # 字符串
    d: bool # 布尔型
    e: List[int] # 整型列表
    f: Dict[str, int] # 字典型，key 为 str，value 为 int
    g: Set[int] # 集合
    h: Tuple[str, int] # 元组
```

## 高级数据结构考察

```python
from enum import Enum

class Gender(str, Enum):
	man: str = "man"
	women: str = "women"
```

## See also

- https://blog.csdn.net/codename_cys/article/details/107675748