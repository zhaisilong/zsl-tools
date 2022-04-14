# shutil

shutil 可以简单地理解为 `sh + util`，shell 工具的意思。shutil 模块是对 os 模块的补充，主要针对文件的拷贝、删除、移动、压缩和解压操作。

copyfileobj 是 shutil 最基础的函数
copy 文件内容到另一个文件，可以 copy 指定大小的内容

```python
import shutil
s = open('fsrc.txt','r')
d = open('fdst.txt','w')
shutil.copyfileobj(s,d,length=16*1024)
shutil.copyfile(src, dst) # 拷贝文件
shutil.copymode(src, dst) # 仅拷贝权限
shutil.copystat(src, dst) # 仅复制所有的状态信息，包括权限，组，用户，时间等。
shutil.copy(src,dst) # 同时复制文件的内容以及权限，也就是先 copyfile() 然后 copymode()
shutil.copy2(src,dst) # 复制所有信息和内容，先 copyfile() 后 copystat()
```

文件夹操作

```python
# 递归地复制目录及其子目录的文件和状态信息
shutil.copytree(src, dst)
# 忽略文件地复制
copytree(source, destination, ignore=ignore_patterns('*.pyc', 'tmp*'))
# 递归删除文件
shutil.rmtree(path[, ignore_errors[, onerror]])
# 递归地移动文件，类似mv命令
shutil.move(src, dst)
```

其他

```python
shutil.wich('echo')
```

创建归档或压缩文件，或其逆操作

```python
shutil.make_archive("d:\\3", "zip",  base_dir="d:\\1.txt")
shutil.unpack_archive("d:\\3.zip", "f:\\3", 'zip')
```

```python
import shutil
source = "/home/User/Documents/file.txt"
destination = "/home/User/Documents/file.txt"

try:
    shutil.copy(source, destination)
    print("File copied successfully.")

# If source and destination are same
except shutil.SameFileError:
    print("Source and destination represents the same file.")
 
# If there is any permission issue
except PermissionError:
    print("Permission denied.")
 
# For other errors
except:
    print("Error occurred while copying file.")
```

## 参考

[shutil | 刘江的博客教程](https://liujiangblog.com/course/python/61)