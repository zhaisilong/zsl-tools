# Poetry

poetry 是一个 Python 虚拟环境和依赖管理的工具。
poetry 和 pipenv 类似，另外还提供了打包和发布的功能。

如果您不熟悉 [pipenv](./pipenv) 请阅读

“应该有一种明显的方法，最好只有一种。” 

请阅读 [Poetry 的历史](https://learnku.com/python/t/38708)

相比 Pipenv，Poetry 是一个更好的选择

- [Github](https://github.com/python-poetry/poetry)
- [官网](https://python-poetry.org/)
- [官方文档](https://python-poetry.org/docs)

## poetry 安装

方式一：（推荐） 

```shell
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

方式二：（pip）为了防止依赖冲突不推荐使用 pip 的方式直接安装

```shell
pip install --user poetry
```

## 使用

### 工程初始化

```shell
poetry new poetry-demo
```

创建结构如下

```text
poetry-demo
├── pyproject.toml
├── README.rst
├── poetry_demo
│ └── __init__.py
└── tests
├── __init__.py
└── test_poetry_demo.py
```

除了新建工程，还可以在已有工程的基础上进行创建，

```shell
poetry init  # 生成 pyproject.toml
```

### 常用命令

```shell
poetry install  # 解析并安装 pyproject.toml 的依赖包
poetry add numpy requests  # 安装包
poetry add pytest --dev  # 指定为开发依赖
poetry add flask=2.22.0  # 指定具体的版本
poetry install --no-dev  # 一般部署时使用
poetry update  # 更新所有锁定版本的依赖包
poetry self update
poetry update numpy  # 更新指定依赖包
poetry remove numpy  # 
poetry show --outdated  # 查看可以更新的依赖
poetry show  # 查看项目安装的依赖
poetry show  numpy # 查看项目安装的依赖
poetry show -t  # 树形结构查看项目安装的依赖
```

虚拟环境管理

```shell
poetry lock  # 锁定 （不安装） 中指定的依赖项

# 指定解释器
poetry env use python3.7
poetry env use /full/path/to/python
poetry env use system

poetry shell
poetry run python -V
poetry env info
poetry env list
poetry env list --full-path
poetry env remove python3.7  # 删除现有的虚拟环境
poetry run python -V

# 导出
poetry export -f requirements.txt --output requirements.txt
# --dev
# --extras (-E): 额外的依赖
# --without-hashes: 忽略哈希
```

包的分发

```shell
poetry build

# pypi
poetry config http-basic.pypi username password
poetry publish

# 公司有自己的私有仓库
poetry config repositories.foo https://foo.bar/simple/
poetry config http-basic.foo username password
poetry publish -r my-repository
```

### 自定义镜像源

```toml
[[tool.poetry.source]]
name = "aliyun"
url = "https://mirrors.aliyun.com/pypi/simple/"

[[tool.poetry.source]]
name = "tsinghua"
url = "https://pypi.tuna.tsinghua.edu.cn/simple/"
```

也可以用命令行

```shell
poetry config repositories.tuna https://pypi.tuna.tsinghua.edu.cn/simple
poetry config repositories.tuna --unset
```

## 进阶

构建软件包并且指定可执行的脚本

指定可执行程序的函数入口：

```toml
[tool.poetry.scripts]
abc = "bca.abc:main"
```

### 依赖配置

版本限制：

- 尖括号：^1.2 代表 >=1.2.0 <2.0.0 
- 波浪号：~1.2.3 代表 >=1.2.3 <1.3.0
- 星号：1.* 代表 >=1.0.0 <2.0.0

### poetry 的全局配置

Tips: poetry config 之后接 `--unset`、`--local`

- unset :重置某项的配置
- local：配置只对本地的项目生效，不影响全局配置

```shell
poetry config --list

# 可以设置虚拟环境默认安装到项目的 .venv 目录里
poetry config virtualenvs.in-project true

# 在部署时先使用这个命令可以使所有的包安装到系统中，而不是虚拟环境里
poetry config virtualenvs.create false --local

poetry config virtualenvs.path .virtualenvs  --local
```

> 注意: python3.8(包括) 以下，不能 poetry config virtualenvs.in-project true

### Python Poetry 管理包安装速度慢的解决办法

因为 Poetry 是依靠 pip 来进行安装的，所以我们可以通过更改 pip 镜像源来加快速度。

```shell
mkdir -p ~/.pip && vim ~/.pip/pip.conf

[global]
index-url = http://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host = mirrors.aliyun.com
```

## See also

- [Python 包管理之 poetry 的使用](https://www.cnblogs.com/-wenli/p/13337188.html)
- [Poetry 科学管理 Python 虚拟环境 ](http://www.limich.cn/2020/04/13/Poetry%E7%A7%91%E5%AD%A6%E7%AE%A1%E7%90%86Python%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83/)
