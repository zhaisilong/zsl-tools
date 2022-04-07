# Subprocess

Python 运行 Shell，推荐使用 `subprocess`。

```python
#只返回结果
import subprocess
subprocess.call("echo hello world", shell=True)
```

`os.system` 方法会创建子进程运行外部程序，方法只返回外部程序的运行结果

```python
import os
# #只返回结果
print(os.system("echo hello world")) # 还会多输出一行返回状态
```

`os.popen` 方不仅仅返回结果，还返回一个类文件对象，通过调用该对象的`read()`或`readlines()`方法可以读取输出内容

```python
output = os.popen('echo hello world', 'r')
print(output.read())
```

## 实战

```python
self._len_source: int = int(subprocess.check_output("wc -l " + self._source_path, shell=True).split()[0])
```

