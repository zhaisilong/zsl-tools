# colorama

Display different colors and backgrounds of fonts cross platforms

## Setup

```python
conda install colorama
```

## Usage

Fore: font color
Back: background color of the font
Style: font style

```text
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
```

```python
from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
```

## Auto reset

```python
from colorama import init
init(autoreset=True)
```

