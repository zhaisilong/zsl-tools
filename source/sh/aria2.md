# Aria2

## Setup

```sh
conda install aria2 -c biconda # Recommended
sudo apt-get install aria2 # Debian
yay -S aria2 # Arch
```

WebUI can be found with google chrome plugins, search by *aria2 for chrome*.

Most useful commands

```sh
# --continue, --split, max, j 同时下载数, --out
aria2c {{URL}} -c -s2 -x8 -j 10  -o out.zip
# download to pwd
aria2c <URL>
# 
aria2c -s2 -o out.type <URL>
# 
aria2c -c <URL>
# use proxy
aria2c all-proxy=127.0.0.1:10809 <URL>

# 种子下载
aria2c xxx.torrnet
aria2c -S target.torrent # 列出种子内容
aria2c --select-file=1,4-7 target.torrent # 选择下载种子
```

## Configuration

这里需要注意，`aria2.session` 与 `aria2.conf` 一定要在 `etc` 中，否则无法以 daemon 形式启动

```sh
sudo mkdir -p /etc/aria2 && cd /etc/aria2 #新建文件夹
sudo touch aria2.session #新建 session 文件，用来缓存下载，可断点续传
sudo chmod 777 aria2.session #设置aria2.session可写
sudo vim aria2.conf #创建配置文件
```

```shell
# aria2.conf
# 注意，配置不支持行内注释
dir=/home/seeyou/下载 
disable-ipv6=true

#打开 rpc 的目的是为了给 web 管理端用
enable-rpc=true
rpc-allow-origin-all=true
rpc-listen-all=true

#rpc-listen-port=6800
#断点续传
continue=true
input-file=/etc/aria2/aria2.session
save-session=/etc/aria2/aria2.session

#最大同时下载任务数
max-concurrent-downloads=20
save-session-interval=120

# Http/FTP 相关
connect-timeout=120
#lowest-speed-limit=10K
#同服务器连接数
max-connection-per-server=10
#max-file-not-found=2
#最小文件分片大小, 下载线程数上限取决于能分出多少片, 对于小文件重要
min-split-size=10M

#单文件最大线程数, 路由建议值: 5
split=10
check-certificate=false
#http-no-cache=true

# 使用代理
all-proxy=127.0.0.1:10809
```

## 启动

```shell
sudo aria2c --conf-path=/etc/aria2/aria2.conf -D
```

开机启动，可以以脚本的形式加入 KDE 桌面，tips：`alt` + `space` -> `autostart`。

在 Debian 系电脑自己编写开机启动脚本

```sh
sudo vim /etc/init.d/aria2c # 增加开机启动脚本
sudo chmod 755 /etc/init.d/aria2c # 修改文件权限为755 (a+x)
sudo update-rc.d aria2c defaults # 添加 aria2c 服务到开机启动
sudo service aria2c start # 启动服务
sudo systemctl status aria2c # 查看服务状态
```

```sh
#!/bin/sh
### BEGIN INIT INFO
# Provides: aria2
# Required-Start: $remote_fs $network
# Required-Stop: $remote_fs $network
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# Short-Description: Aria2 Downloader
### END INIT INFO
 
case "$1" in
start)
 
 echo -n "已开启Aria2c"
 aria2c --conf-path=/etc/aria2/aria2.conf -D
;;
stop)
 
 echo -n "已关闭Aria2c"
 killall aria2c
;;
restart)
 
 killall aria2c
 aria2c --conf-path=/etc/aria2/aria2.conf -D
;;
esac
exit
```
