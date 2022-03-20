Python Debug
============

Python
的调试方法有三种，一种是执行时调试，一种是交互调试，一种是程序里埋点调试。

其中，最常用的是执行时调试，也就是 pdb 调试。

pdb 有 2 种用法：

.. code:: shell

   # 1. 非侵入式方法（不用额外修改源代码，在命令行下直接运行就能调试）
   python3 -m pdb filename.py

   # 2. 侵入式方法（需要在被调试的代码中添加一行代码然后再正常运行代码）
   import pdb;pdb.set_trace()

pdb 常用命令
------------

.. code:: text

   l 查看当前位置前后11行源代码（多次会翻页）
   ll 查看当前函数或框架的所有源代码

   添加断点
   b
   b lineno
   b filename:lineno 
   b functionname

   添加临时断点
   tbreak
   tbreak lineno
   tbreak filename:lineno
   tbreak functionname

   清除断点
   cl
   cl filename:lineno
   cl bpnumber [bpnumber ...]

   打印变量值
   p expression, expression 为 Python 表达式

   逐行调试命令
   s 执行下一行（能够进入函数体）
   n 执行下一行（不会进入函数体）
   r 执行下一行（在函数中时会直接执行到函数返回处）

   非逐行调试命令
   c 持续执行下去，直到遇到一个断点
   unt lineno 持续执行直到运行到指定行（或遇到断点）
   j lineno 直接跳转到指定行（注意，被跳过的代码不执行）

   查看函数参数
   a 在函数中时打印函数的参数和参数的值

   打印变量类型
   whatis expression

   启动交互式解释器
   interact
   启动一个 python 的交互式解释器，使用当前代码的全局命名空间（使用ctrl+d返回pdb）

   打印堆栈信息
   w

   退出 pdb
   q

See also
--------

-  `10 分钟教程掌握 Python 调试器
   pdb <https://zhuanlan.zhihu.com/p/37294138https://zhuanlan.zhihu.com/p/37294138>`__
