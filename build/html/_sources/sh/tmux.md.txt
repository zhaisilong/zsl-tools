# tmux

## Common Commands

```sh
sudo apt-get install tmux  # Setup
tmux new -s <session-name>
tmux detach # Ctrl+b d
tmux ls # 
tmux attach -t 0 # attach to session 0
tmux attach -t <session-name> # attach to session by name
tmux switch -t 0
tmux switch -t <session-name>
```

切换绘话：推荐使用 `Ctrl+b s` 然后上下键选择

## Tmux Windows

```shell
Ctrl+b %  # 左右分

Ctrl+b "  # 上下分

Ctrl+b x # 关闭当前窗格

Ctrl+b Ctrl+<arrow key>  # 按箭头方向调整窗格大小。

Ctrl+b q  # 显示窗格编号。

ctrl+b ,  # rename the window

ctrl+b $   # rename the session

Ctrl+b ;  # 光标切换到上一个窗格。

ctrl+b [  # 然后鼠标就可以移动了

ctrl+b :new -t new_session_name  # new a session and move into
```



