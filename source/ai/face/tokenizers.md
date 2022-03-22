# Tokenizers

## 常用

直接转成 tensor

```python
# Returns PyTorch tensors
model_inputs = tokenizer(sequences, padding=True, return_tensors="pt")
```

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSequenceClassification.from_pretrained(checkpoint)
sequences = [
  "I've been waiting for a HuggingFace course my whole life.",
  "So have I!"
]

tokens = tokenizer(sequences, padding=True, truncation=True, return_tensors="pt")
output = model(**tokens)
```

multi 的两个句子长短不一，需要 padding，有三种方法

```python
inputs_multi = tokenizer(sequence_multi, padding="longest") # 将序列填充到最大序列长度
inputs_multi = tokenizer(sequence_multi, padding="max_length") # 将序列填充到模型最大长度 bert 512
inputs_multi = tokenizer(sequence_multi, padding="max_length", max_length=8) # 将序列填充到指定最大长度
```

## See also

- [Transformers Tokenizer API 的使用](https://zhuanlan.zhihu.com/p/390821442)

### 实战

- [PyTorch 的 BERT 微调教程](https://www.xiuweihan.cn/2021/04/15/2021-04-15-nlp%E4%B9%8Btransformers%E5%BA%93/#toc-heading-4)