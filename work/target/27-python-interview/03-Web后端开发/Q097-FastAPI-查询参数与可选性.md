---
title: [Q097] FastAPI 查询参数与可选性
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q097 · FastAPI 查询参数与可选性

> 难度:★☆☆ | 标签:FastAPI, 查询参数

**问**:查询参数怎么声明?必填、可选、默认值、约束分别怎么表达?

**答**:签名中不属于路径参数的简单类型参数自动识别为查询参数:有默认值即可选,默认 `...` 即必填,`None` 类型即可为空;用 `Query` 附加校验(最大长度、正则、别名)与文档元数据。列表型查询参数(如 `?tag=a&tag=b`)用 `list[str]` 声明。布尔参数 FastAPI 也会自动转换 `1/true/yes` 等形式。

```python
# file: code/03_Web后端开发/q097_query_params.py
try:
    from fastapi import FastAPI, Query
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()

@app.get('/search')
def search(
    keyword: str = Query(..., min_length=1, max_length=50),  # 必填
    page: int = Query(1, ge=1),                              # 可选带约束
    size: int = Query(10, le=100),
    tag: list[str] | None = Query(None),                     # ?tag=a&tag=b
    exact: bool = False,                                     # ?exact=true
):
    return {'keyword': keyword, 'page': page, 'size': size,
            'tags': tag or [], 'exact': exact}
```

**追问**:
- list[str] 查询参数怎么传?——`?tag=a&tag=b` 重复键;默认值用 `Query(default=[])`,注意可变默认值由 FastAPI 内部处理为每次新列表。
- 别名什么时候用?——上游字段名是 Python 关键字或不合规范(如 `from`)时 `Query(alias='from')`,内部仍用合法名。
- 必填与「可为 None」的区别?——`x: str` 必填且不可空;`x: str | None = None` 可不传;`x: str = ...` 必填但可为 None 传 null,语义三种不同。
