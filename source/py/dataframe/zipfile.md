# ZipFile

## 使用

```python
import zipfile

zipFile = zipfile.ZipFile(file_dir, mode="r")

zipFile.infolist()
zipFile.namelist()
zipFile.printdir()

# 解压文件
zipFile = zipfile.ZipFile(file_dir)
for file in zipFile.namelist():
    zipFile.extract(file, 'to_dir')
zipFile.close()

## 解压文件 简单版
zipFile.extractall('to_dir')
```

```python
import zipfile
import os

def make_zip(source_dir, output_filename):
    """压缩目录中的文件
    source_dir 中不能包含目录
    example:
        make_zip('data', 'data.zip')
    """
    zipf = zipfile.ZipFile(output_filename, 'w')    
    pre_len = len(os.path.dirname(source_dir))
    for parent, _, filenames in os.walk(source_dir):
        for filename in filenames:
            pathfile = os.path.join(parent, filename)
            arcname = pathfile[pre_len:].strip(os.path.sep)
            zipf.write(pathfile, arcname)
    zipf.close()
```