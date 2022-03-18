# Git

远程仓库和本地仓库名字的区别：

- origin 远程库名
- main 本地分支名
- origin/main 远程库中的远程分支

## Git

### Setup

```shell
sudo apt install git
```

### 配置

每个仓库的 Git 配置文件都放在当前目录下的 `.git/config` 文件中。

- `/etc/gitconfig 文件`：系统中对所有用户都普遍适用的配置。若使用 `git config` 时用 `--system` 选项，读写的就是这个文件。
- `~/.gitconfig 文件`：用户目录下的配置文件只适用于该用户。若使用 `git config` 时用 `--global` 选项，读写的就是这个文件。
-  `当前文件夹/.git/config 文件`: 这里的配置仅仅针对当前项目有效。使用 `git config`

```bash
# 查看当前配置信息
git config --list
git config --global --list 

# 修改用户信息
git config --global user.email "zhaisilong@outlook.com"
git config --global user.name "zhaisilong"

# 添加 GPG 密钥 要先上传公钥
#E GPG 用于签名验证 注释
git config --global user.signingkey D482B92E13D3FCBA
# 自动验证签名 自动加上 -S
git config --global commit.gpgsign true

# 文本编辑器
git config --global core.editor emacs
# 差异分析工具
git config --global merge.tool vimdiff
# 开启界面颜色
git config --global color.ui true

```

### 配置自动换基

自动换基，保持开发线的整洁。

```bash
git config --global pull.rebase true
git config --global rebase.autoStash true
```

#### 配置 ssh key

##### 配置文件的编辑
```sh
vim ~/.ssh/config 
# github
Host github.com
HostName github.com
PreferredAuthentications publickey
IdentityFile ~/.ssh/git.rsa

# gitee
Host gitee.com
HostiName gitee.com
PreferredAuthentications publickey
IdentityFile ~/.ssh/git.rsa
```

### 常用命令

```shell
# 初始化仓库
git init

# 增加文件
git add [file1] [file2]
# 增加所有文件
git add -A

# 提交到本地仓库 并附加说明
# `-m`后面输入的是本次提交的说明
git commit -m "wrote a readme file"
# 签名验证，需要配置 gpg
git commit -S -m "..."

# -M, --move --force:
git branch -M main  #重命名分支名
# 列出所有分支
git branch -a
# 查看远程库的信息
git remote -v 

# 添加远程库
## 可以从这个仓库克隆出新的仓库，也可以把一个已有的本地仓库与之关联，然后，把本地仓库的内容推送到GitHub仓库。
git remote add {{remote_name}} {{remote_url}}
git remote add origin https://github.com/xxzhai123/PbootCMS.git
git remote remove {{remote_name}}
git remote rename {{old_name}} {{new_name}}

# 将本地库推到远程
## 当只有一个分支名时，简写成git push
git push {{remote_name}} {{local_branch}}
# 指定远程分支名将本地库上传
git push {{remote_name}} -u {{remote_branch}}
# 删除远程库中的一个分支
git push {{remote_name}} --delete {{remote_branch}}

# 拉取远程仓库
git fetch # 拉取
git merge # 合并
git pull # 拉取并合并
git pull origin master # 指定远程库的分支拉取

# 查看状态
git status
git diff # 命令查看文件是如何被修改
git log # 查看合并日志，以及 Head 信息
git log --oneline --decorate --graph
```

#### 分支的创建与合并

注意 `iss53` 从未出现在远端

```bash
git checkout -b iss53 # 在当前分支，创建新分支
# 等价于下面两条
git branch iss53
git checkout iss53
# 然后修复 bug

# 修复好回到 main
git checkout main
git merge iss53
# 最后删除 iss53
git branch -d iss53
```

如果不允许不想干分支合并请用
```bash
git merge iss53 --allow-unrelated-histories
```

#### 如何更换 git 的远程库

ssh 地址：`git@github.com:zhaisilong/software.git`
https 地址：`https://github.com/zhaisilong/software`

```sh
git remote set-url origin <ssh地址> | <https地址>
```

#### 配置命令别名

```shell
# 告诉Git，以后st就表示status：
$ git config --global alias.st status
```

## 忽略特殊文件

不需要从头写`.gitignore`文件，GitHub已经为我们准备了各种配置文件，只需要组合一下就可以使用了。所有配置文件可以直接在线浏览：<https://github.com/github/gitignore>

`.gitignore` 文件的格式规范如下：
1. `＃` 注释
    - 不允许行内注释
2. 可以使用标准的 glob 模式匹配
3. `!` 开头表示不忽略
4. `/` 开头表示根目录,`/`结尾表示目录
`/*.js`可以匹配`app.js`，但无法匹配`js/app.js`。
5. `**`表示匹配零到多级目录

## 子模块

子模块允许你将一个 Git 仓库作为另一个 Git 仓库的子目录。默认情况下，子模块会将子项目放到一个与仓库同名的目录中。

创建名为 `.gitmodules` 的文件。该配置文件保存了项目 URL 与已经拉取的本地目录之间的映射

```sh
git submodule add
```

### 克隆带有子模块的仓库

正常 clone 包含子模块的函数之后，由于.submodule 文件的存在 someSubmodule 已经自动生成。但是里面是空的。还需要执行 2 个命令。

```shell
# clone 父仓库的时候加上 --recursive，会自动初始化并更新仓库中的每一个子模块
git clone --recursive https://github.com/chaconinc/MainProject


# 或者分步拉取
## 用来初始化本地配置文件
git submodule init 
## 从该项目中抓取所有数据并检出父项目中列出的合适的提交(指定的提交)。
git submodule update

# 更新子模块
## Git 将会进入子模块然后抓取并更新，默认更新 master 分支
git submodule update --remote
```

## 标签管理

如果你达到一个重要的阶段，并希望永远记住那个特别的提交快照，你可以使用 git tag 给它打上标签。

```bash
git tag # 查看标签信息
git tag -a v1.0
git tag -a v0.9 85fc7e7 # 追加标签，忘记了的话
git log --oneline --decorate --graph
# 指定标签信息
git tag -a v1.0 -m "runoob.com标签"
# 用 gpg 指定标签信息
```

## Gitee

使用 GitHub 时，国内的用户经常遇到的问题是访问速度太慢，有时候还会出现无法连接的情况（原因你懂的）。

如果我们希望体验 Git 飞一般的速度，可以使用国内的 Git 托管服务——[Gitee](https://www.gitee.com)

## git-lfs

```sh
# 安装
sudo apt-get install git-lfs
# 关联 git，这一步的目的是改变 git 的全局配置，查看 .gitconfig 文件
git lfs install
```

用 LFS 追踪的文件，这一步的目的是下面的文件变成 LFS 文件，支持通配符。操作完成后会生成或更新 *.gitattributes* 配置文件

```sh
git lfs track "*.sql"
git lfs untrack "文档.doc"
git lfs ls-files
git add .gitattributes
git commit -m "add .gitattributes"
```
