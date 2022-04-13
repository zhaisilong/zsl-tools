# Black

## Usage

```shell
pip install black
pip install black[jupyter]
pip install git+https://github.com/psf/black
```

Basic Usage

```shell
black {source_file_or_directory}...
python -m black {source_file_or_directory}...
```

Interact with shell

```shell
echo "print ( 'hello, world' )" | black -
black --code "print ( 'hello, world' )"
```

Check a python script

```shell
black test.py --check
echo $?  # 0 -> OK, 1 -> modified, 2|3 -> something wrong with black

# verbose
black src/ -v
```

## Links

- [Blcak 官方文档](https://black.readthedocs.io/en/stable/)