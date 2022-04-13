# Configparser

常见的基础的配置文件 `*.ini`, `*.toml`, `*.cfg`

Section 下有键值对

```ini
[DEFAULT]
serveraliveinterval = 45
compression = yes
compressionlevel = 9

[bitbucket]
user = kk

[topsecrect]
port = 22
```

## 生成配置文件

```python
import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {'serveraliveinterval' : '4',
                     'compression' : 'yes',
                     'compressionlevel' : '9'}

config['bitbucket'] = {}
config['bitbucket']['user'] = 'kk'

config['topsecrect'] = {}
topsecrect = config['topsecrect']

topsecrect['port'] = '22'

with open('example.ini', 'w') as configfile:
    config.write(configfile)
```

## 读取配置文件

```python
import configparser

config = configparser.ConfigParser()

config.read('example.ini')

for key in config['DEFAULT']:
    print(key)
```

带数据类型的读取: 一般情况下，configpaser 类是无法识别配置文件中的 value 的数据类型的，它总是以字符串的形式来存储这些类型，所以当涉及到 int float 等类型的时候就需要我们自己对它进行转换

```python
import configparser

config = configparser.ConfigParser()

config.read('example.ini')

port = config['topsecrect'].getint('port')

print(port)

compression = config.getboolean('DEFAULT', 'compression')
print(compression)
```