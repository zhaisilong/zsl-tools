# Oh My Zsh

## 安装

安装 zsh

```sh
yay -S zsh # arch
sudo apt-get install zsh # Debian
```

安装 zsh 插件

zsh-autosuggestions 自动建议
zsh-syntax-highlighting 代码高亮
zsh-theme-powerlevel10k 提供漂亮的提示符的主题

Ubuntu 的 zsh-theme-powerlevel10k 稍后安装，因为 apt 没有版本 10

```sh
yay -S zsh-autosuggestions zsh-syntax-highlighting zsh-theme-powerlevel10k zsh-completions
sudo apt-get install zsh-autosuggestions zsh-syntax-highlighting
```

### 如果安装不上，手动安装

```shell
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

git clone https://github.com/zsh-users/zsh-completions ${ZSH_CUSTOM:=~/.oh-my-zsh/custom}/plugins/zsh-completions

vim ~/.zshrc

plugins=( 
  # other plugins...
  git
  zsh-autosuggestions
  zsh-syntax-highlighting
  zsh-completions
)
```

如果无法访问 github ，我们可以用代理下载脚本，要先安装和配置 [qv2ray](https://seeyou.wecook.top/index.php/archives/software.html)

```sh
export https_proxy=127.0.0.1:10809
sudo apt install git # 如果没有安装
# yay -S git
sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
```

更改默认 shell

```shell
chsh -s /usr/bin/zsh
```

## zsh 主题

### Ubuntu

```sh
git clone https://github.com/romkatv/powerlevel10k.git $ZSH_CUSTOM/themes/powerlevel10k
vim ~/.zshrc
# 然后设置 ~/.zshrc 中的变量 ZSH_THEME
ZSH_THEME="powerlevel10k/powerlevel10k"
# 并在 ~/.zshrc 最后名加入
source /usr/share/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
```

### Arch

在 `~/.zshrc` 后面加入以下内容

```sh
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh-theme-powerlevel10k/powerlevel10k.zsh-theme
```

## 升级

```bash
omz update
```

## 参考

- [配置一个简洁高效的 Zsh](https://linux.cn/article-13030-1.html)
