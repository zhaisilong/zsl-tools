# SSH

SSH-Key 与一般的 gpg 密钥有所区别

1. 私钥只有命名为 id_rsa 才有效否则需要指定。
2. 公钥必须写入 `~/.ssh/authorized_keys` 才有效。
3. 一个密钥对可重复使用。
4. 密钥的权限不能太高，否则会报错。`700`

ssh 提供两种级别的安全认证：

1. 基于口令的安全认证
2. 基于密钥的安全认证

## RSA 密钥

passphrase 是证书口令，以加强安全性，避免证书被恶意复制。

会在 `~/.ssh` 下生成 `id_rsa`, `id_rsa.pub` 两个文件，分别是 私钥/公钥。

```bash
# 生成 ssh-key，选加密算法（rsa、dsa），给秘钥命名（可选）：
ssh-keygen -t rsa -b 2048 -C "957574373@qq.com" -f ./zhaisilong_rsa

# 将公钥传输到远程服务器
ssh-copy-id -i ~/.ssh/id_rsa.pub root@172.xx.yy.zzz
```

判断公钥与私钥是否配对

```shell
ssh-keygen -y -e -f <private key>
```

下面手动演示具体流程

```bash
scp ~/.ssh/id_rsa.pub root@47.111.225.3:/root/.ssh/
# 要保证 .ssh 和 authorized_keys 都只有用户自己有写权限。否则验证无效
chmod -R 700 ~/.ssh/
chmod 600 ~/.ssh/authorized_keys

# 使用 ssh-copy-id 则不需要此步
cat id_rsa.pub >> authorized_keys
```

### 登录远程服务器

简单情况下，通过手动指定私钥文件登录

```sh
ssh -p 22 username@hostname -i "~/.ssh/my_id_rsa"
```

配置客户端，可自动指定私钥文件

```sh
vim ~/.ssh/config

Host alias
    HostName hostname
    User root
    Port 22
    IdentityFile ~/.ssh/id_rsa
```

## 配置远程主机 sshd 的配置

一般不需要配置。下面以 Ubuntu 为例

```bash
sudo vim /etc/ssh/sshd_config

PasswordAuthentication yes
PubkeyAuthentication yes
# 有了证书登录了，可以禁用密码登录
PasswordAuthentication no
# 禁用root账户登录，非必要，但为了安全性，请配置
PermitRootLogin no

# 重启 sshd 使改动生效
systemctl reload sshd
```

## See also

- [Linux下使用SSH远程执行命令方法收集](https://cloud.tencent.com/developer/article/1721823)