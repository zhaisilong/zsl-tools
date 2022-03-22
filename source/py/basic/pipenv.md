# Python 环境

关于 Python 虚拟环境管理，很多人一开始不以为意，把编程时所有依赖的库全安装在一起，要用的时候直接导入，看似非常方便，但是会造成很多隐患：

- 当电脑/服务器里面的项目越来越大，更新迭代次数多了，会造成很多以前用到现在不需要用到的库，把这些库都写在requirements里面会造成冗余，而且 docker 化的时候安装 requirements 特别慢;
- 当电脑/服务器里面的项目越来越多，会造成很多项目的依赖库的版本相互冲突，而且也不敢随便删掉/更新某些库，因为有可能会造成某个项目的依赖无法找到或者版本不兼容的故障； 所以，Python 在实际项目应用当中，虚拟环境管理是非常重要的

## Python 虚拟环境管理工具的发展

最常用的虚拟环境管理工具是 virtualenv，virtualenvwrapper，pipenv，
事实上，这几种虚拟环境的管理都是基于 virtualenv，只是做了不同的封装，达到了更好的效果。

virtualenv -> virtualenvwrapper  -> pipenv 推介

pipenv 的优势

1. 跟踪包的关系变化，pipenv 会在项目目录下创建 Pipfile 和 Pipfile.lock 文件
2. 安装卸载包无需激活虚拟环境，直接在项目文件夹下即可操作
3. 卸载的时候，可以自动检查依赖库是否被其他包依赖，来选择是否彻底删除。也可以通过 pipenv graph 来查看各个包的依赖关系图；
4. 当代码需要在虚拟环境执行时，通过pipenv run python xx.py，即可在虚拟环境下执行python文件。
5. 便于 docker 容器化管理，Pipfile 文件支持生成 requirements 文件，便于项目代码 docker 化管理，另外，
6. pipfile 还支持 --dev 环境，可以在调试阶段安装许多调试工具等，而不影响生产环境的环境。

## 使用

```shell
pip install pipenv  # 安装 pipenv
pip uninstall pipenv  # 卸载 pipenv
pipenv --python 3.6  # 初始化特定版本的环境

# 第一次的话 初始化虚拟环境
# 根据 Pipfile 的记录，安装所有依赖包
pipenv install  


pipenv --rm  # 删除当前虚拟环境，注意 Pipfile 不会被删掉

# 进入虚拟环境
cd path/to/env
pipenv shell  


exit  # 退出虚拟环境
pipenv install xxx  # 安装相关依赖包
pipenv install --dev xxx  # 安装包到开发组
pipenv uninstall xx： # 卸载包
pipenv graph  # 查看目前按照的依赖包
pipenv --venv  # 显示虚拟环境安装路径

pipenv install requests==2.13.0
pipenv install "requests~=2.2"  # 锁定包的主版本(这相当于使用==2.*)
pipenv update --outdated  # 检查更新
pipenv update  # 更新
pipenv update <包名>  # 指定更新

pipenv lock -r > requirements.txt  # 将 Pipfile 里的全部包导出 requirements.txt
pipenv lock -r --dev-only > requirements.txt  # 只导出开发环境的包
pipenv lock -r --dev > requirements.txt  # 导出开发环境 + 默认的环境的包
pipenv install -r path/to/requirements.txt  # 安装 requirements.txt
pipenv run python --version  # 如果想进入 shell 运行 python

# 从 setup.py 安装依赖包
pipenv install -e .
```

```python
pipenv --python 3.7 创建3.7版本Python环境
```

### Pipfile

第一次在项目中运行 pipenv 命令的话，会在项目中创建一个名为 Pipfile 的文件

```ini
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
requests-html = "*"

[dev-packages]

[requires]
python_version = "3.7"
```

### Pipfile.lock 文件

Pipfile.lock 利用了 pip 中一些新的安全改进。
默认情况下，Pipfile.lock 包含每个下载的包的 sha256 哈希值。
这可以使 pip 能够保证从不信任的 PyPI 源安装包时或者在不稳定的网络环境下安装包时都能保证包的正确性与完整性。

Pipfile 和 Pipfile.lock 不一致
原因：当 pipenv install 安装一些比较大的包，比如 TensorFlow 等科学包，在安装完包，正在解析包依赖的时候，可能会花费很长时间，可能就会 ctrl+C 停止掉了，此时包已经安装完成，Pipfile 已经写入完成，但是没有解析完依赖，所以 Pipfile.lock 没有写入完成。
方法：删除 Pipfile.lock；使用 `pipenv lock` 重新生成

## 利器之环境变量：（.env）

`.env` 文件可以设置一些环境变量，在程序开发的时候模拟环境变量。

```shell
echo -e 'HELLO==WORLD \n CONFIG_PATH=${HOME}/.config/foo' >> .env 
```

如果你的 .env 文件位于不同的路径下或者有其他名称，你可以设置一个 `PIPENV_DOTENV_LOCATION` 环境变量：

```shell
PIPENV_DOTENV_LOCATION=/path/to/.env pipenv shell
```

要禁止 pipenv 加载 .env 文件，可以设置 PIPENV_DONT_LOAD_ENV 环境变量：

```shell
PIPENV_DONT_LOAD_ENV=1 pipenv shell
```

## 其他

```shell
alias prp="pipenv run python"  # 少打几个字
```

## 修改镜像源

```ini
[[source]]
url = "https://mirrors.aliyun.com/pypi/simple"
verify_ssl = true
name = "pypi"
```

### 环境的迁移

复制 Pipfile 和 Pipfile.lock 文件到新电脑 `pipenv install`

### 修改虚拟环境目录位置

有三种方法：

```shell
# 设置这个环境变量，pipenv 会在当前目录下创建 .venv 的目录，以后都会把模块装到这个 .venv 下。
export PIPENV_VENV_IN_PROJECT=1

# 自己在项目目录下手动创建 .venv 的目录，然后运行 pipenv run 或者 pipenv shell pipenv 都会在 .venv 下创建虚拟环境。
mkdir .venv
pipenv shell


# 设置 WORKON_HOME 到其他的地方 （如果当前目录下已经有.venv,此项设置失效）。
export WORKON_HOME=$HOME/.virtualenvs
```

## See also

- [Python—pipenv 精心整理教程](https://juejin.cn/post/6844904202737713160)
- [Python多环境管理神器（pipenv）](https://www.cnblogs.com/doublexi/p/15791048.html)