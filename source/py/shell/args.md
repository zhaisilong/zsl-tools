# Python Argparse

通过`argparse`模块，可以轻松编写用户友好的命令行界面。 它解析`sys.argv`中定义的参数。

`argparse`模块还会自动生成帮助和使用消息，并在用户为程序提供无效参数时发出错误。

`argparse`是标准模块； 我们不需要安装它。

使用`ArgumentParser`创建一个解析器，并使用`add_argument()`添加一个新参数。 参数可以是可选的，必需的或定位的。

建议阅读一下参考指定的教程，能帮助你理解

## add_argument

```python
defaut=2
default='hello world'
metavar='value' # 为错误的期望值命名，并提供帮助输出
required=True # 设置为必须参数
type=int # 指定类型
help="shows output" # 显示帮助信息
nargs=2 # 该选项需要两个参数
nargs=* # 该选项需要好多个参数
choices=['std', 'iso', 'unix', 'tz']

action='append' # 这个选项可以重复出现多次
action='store_true' # 保存为真假
```

## 简单的例子

```python
#!python3

import argparse
parser = argparse.ArgumentParser()

# 可选参数
## dest 指定参数的在 python 中的名称，不指定 argparse 会自动推导
## action 的 store_true 会将参数存储为 True
parser.add_argument('-o', '--output', dest='output_dest', action='store_true',
                    help="shows output")



# 必须参数
parser.add_argument('--name', required=True)
## type 指定参数的类型
parser.add_argument('-n', type=int, required=True,
                    help="define the number of random integers")

# 位置参数
parser.add_argument('age')

# append 操作
parser.add_argument('-n', '--name', dest='names', action='append',
                    help="provides names to greet")
names = args.names
for name in names:
    print(f'Hello {name}!')

args = parser.parse_args()

if args.output:
    print("This is some output")


print(f'Hello {args.name}')
```

## 子命令

子命令的例子：`pip install`和 `pip uninstall`

一个用子命令的实例：

```python
# sub-command functions
def foo(args):
	print(args.x * args.y)
def bar(args):
	print('((%s))' % args.z)

# create the top-level parser
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

# create the parser for the "foo" command
parser_foo = subparsers.add_parser('foo')
parser_foo.add_argument('-x', type=int, default=1)
parser_foo.add_argument('y', type=float)
parser_foo.set_defaults(func=foo)

# create the parser for the "bar" command
parser_bar = subparsers.add_parser('bar')
parser_bar.add_argument('z')
parser_bar.set_defaults(func=bar)

# parse the args and call whatever function was selected
args = parser.parse_args()
args.func(args)
```

## 参考

[Python argparse 教程](https://geek-docs.com/python/python-tutorial/python-argparse.html)

