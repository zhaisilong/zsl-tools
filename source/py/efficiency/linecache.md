# Linecache

linecache 模块的作用是将文件内容读取到内存中，进行缓存，而不是每次都要从硬盘中读取，这样效率提高很多，又省去了对硬盘 IO 控制器的频繁操作。

linecache 里面最常用到的就是 getline 方法，简单实用可以直接从内容中读到指定的行，日常编程中如果涉及读取大文件，一定要使用首选linecache 模块，相比 open() 那种方法要快 N 倍，它是你读取文件的效率之源。

```python
linecache.getlines('poetry.lock')
linecache.getline('poetry.lock', 2)  # 注意 2 是行号，返回的字符串包含换行符
```

## 实战

```python
import linecache

line: str = linecache.getline(self._file_path, idx + 1).strip()
```