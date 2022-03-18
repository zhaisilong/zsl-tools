# Proc

```shell
/proc/cpuinfo cpu的信息
/proc/mounts 系统中使用的所有挂载
/proc/uptime 系统已经运行了多久
/proc/version Linux内核版本和gcc版本
/proc/swaps 交换空间的使用情况
/proc/stat 所有的CPU活动信息
/proc/net 网卡设备信息
/proc/tty tty设备信息
/proc/vmstat 虚拟内存统计信息
/proc/diskstats 取得磁盘信息
/proc/zoneinfo 显示内存空间的统计信息，对分析虚拟内存行为很有用
```

以下是 `/proc` 目录中进程 N 的信息

```shell
/proc/N pid为N的进程信息
/proc/N/cmdline 进程启动命令
/proc/N/cwd 链接到进程当前工作目录
/proc/N/environ 进程环境变量列表
/proc/N/exe 链接到进程的执行命令文件
/proc/N/fd 包含进程相关的所有的文件描述符
/proc/N/maps 与进程相关的内存映射信息
/proc/N/mem 指代进程持有的内存，不可读
/proc/N/root 链接到进程的根目录
/proc/N/stat 进程的状态
/proc/N/statm 进程使用的内存的状态
/proc/N/status 进程状态信息，比stat/statm更具可读性
/proc/self 链接到当前正在运行的进程
```

