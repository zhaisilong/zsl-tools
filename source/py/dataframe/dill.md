# dill

```shell
pip install dill
```

```python
import dill as pickle 

with open('kilgariff_ngram_model.pkl', 'wb') as fout:
    pickle.dump(model, fout)

with open('kilgariff_ngram_model.pkl', 'rb') as fin:
    model_loaded = pickle.load(fin)
```
