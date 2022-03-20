# Python Apache Arrow

[Python 官方文档](https://arrow.apache.org/docs/python/index.html)

Arrow manages data in arrays (pyarrow.Array), which can be grouped in tables (pyarrow.Table) to represent columns of data in tabular data.

Arrow also provides support for various formats to get those tabular data in and out of disk and networks. Most commonly used formats are Parquet (Reading and Writing the Apache Parquet Format) and the IPC format (Streaming, Serialization, and IPC).

## 安装

```shell
conda install -c conda-forge pyarrow
pip install pyarrow
```

## 简单使用

创建数据表

```python
import pyarrow as pa
from pyarrow.lib import Table, Int8Array, Int16Array
days: Int8Array = pa.array([1, 12, 17, 23, 28], type=pa.int8())
months: Int8Array = pa.array([1, 3, 5, 7, 1], type=pa.int8())
years: Int16Array = pa.array([1990, 2000, 1995, 2000, 1995], type=pa.int16())
birthdays_table: Table = pa.table([days, months, years],
                           names=["days", "months", "years"])
```

保存和加载数据表

```python
import pyarrow.parquet as pq
pq.write_table(birthdays_table, 'birthdays.parquet')
reloaded_birthdays = pq.read_table('birthdays.parquet')
```

计算

```python
import pyarrow.compute as pc
pc.value_counts(birthdays_table["years"])
```

处理大数据

```python
import pyarrow.dataset as ds
ds.write_dataset(birthdays_table, "savedir", format="parquet",
                 partitioning=ds.partitioning(
                    pa.schema([birthdays_table.schema.field("years")])
                ))
birthdays_dataset = ds.dataset("savedir", format="parquet", partitioning=["years"])
```
