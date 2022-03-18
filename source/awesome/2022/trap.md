# 踩坑记

## 20220318

```shell
export https_proxy=https://127.0.0.1:10809 http_proxy=http://localhost:10809
```

错误原因：`https_proxy=http://127.0.0.1:10809`

两个代理都应该是 `http scheme`