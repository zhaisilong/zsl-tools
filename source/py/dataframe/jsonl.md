# Jsonlines

[Jsonlines 手册](https://jsonlines.readthedocs.io/en/latest/)

```shell
pip install jsonlines
```

```python
import jsonlines

with jsonlines.open('input.jsonl') as reader:
    for obj in reader:

with jsonlines.open('output.jsonl', mode='w') as writer:
    writer.write(...)
```