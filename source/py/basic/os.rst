Python OS
=============

.. code:: python

   import os
   os.chdir(path)
   os.getcwd()
   os.listdir(path)
   os.makedirs('/home/seeyou/a/b/c', exist_ok=True)
   os.mkdir('./book', exist_ok=True)
   os.remove(path)
   os.removedirs(path)
   os.rename(src, dst)
   os.chmod(path, mode)
   os.chown(path, uid, gid)
   os.close(fd)

   os.getppid() # 父进程的 id
   os.getpid() # 当前进程的 id
   import os.path
   # 返回绝对路径
   os.path.abspath(path)
   # 返回文件名
   os.path.basename(path)
   # 返回文件路径
   os.path.dirname(path)
   # 是否存在
   os.path.exists(path)
   # 文件大小
   os.path.getsize(path)
   # 判断
   os.path.isabs(path)
   os.path.isfile(path)
   os.path.isdir(path)
   os.path.islink(path)
   os.path.ismount(path)
   # 目录和文件合成
   os.path.join(path1[, path2[, ...]])
   # 将目录和文件名分割，返回一个元组
   os.path.split(path)

实战 设置临时环境变量
-------------------

.. code:: python

   os.environ['WORKON_HOME'] = "value"

   # 获取环境变量，推荐第二种
   os.environ.get('WORKON_HOME')
   os.getenv('path')
   # 删除变量
   del os.environ['WORKON_HOME']

比如 hugging face 的数据获取不了，可以如此

.. code:: python

   import os
   proxy='http://127.0.0.1:10809'
   os.environ['https_proxy'] = proxy
   os.environ['http_proxy'] = proxy
   from datasets import Dataset
   import datasets
   train_test_ds: Dataset = datasets.load_dataset('bookcorpus', split='train+test')

