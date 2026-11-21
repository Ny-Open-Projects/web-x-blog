---
title: [Q096] FastAPI 路径参数与类型校验
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q096 · FastAPI 路径参数与类型校验

> 难度:★☆☆ | 标签:FastAPI, 参数校验

**问**:路径参数如何声明类型?类型不匹配会发生什么?

**答**:路径参数通过函数签名 + 类型标注声明,FastAPI 依据标注自动解析和校验:声明 `item_id: int` 时请求 `/items/abc` 会返回 422 错误并给出详细原因;配合 `Path` 可以加约束(如 `ge=1`)和文档描述。枚举类型可以用 `Enum` 限定路径取值,`/items/{item_id}` 这样的固定路径与 `/items/latest` 这类字面路径共存时,固定路径要注册在前。

```python
# file: code/03_Web后端开发/q096_path_params.py
from enum import Enum
try:
    from fastapi import FastAPI, Path
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()

class Category(str, Enum):
    book = 'book'
    food = 'food'

@app.get('/items/latest')            # 固定路径必须声明在动态路径之前
def latest():
    return {'id': 0, 'name': 'latest'}

@app.get('/items/{item_id}')
def read_item(item_id: int = Path(..., ge=1, description='商品 ID 大于 0')):
    return {'item_id': item_id}

@app.get('/categories/{category}')
def read_category(category: Category):
    return {'category': category.value}
```

**追问**:
- 422 响应体长什么样?——`{"detail": [{"loc": [...], "msg": "...", "type": "..."}]}` 的结构化错误列表,可用自定义异常处理器改格式(Q112)。
- 固定路径和路径参数冲突谁赢?——先注册的赢,FastAPI 按注册顺序匹配;`/items/latest` 必须在 `/items/{item_id}` 之前。
- Path 约束 ge=1 失败返回什么?——422,detail.loc 指向 path 参数;客户端可据此修正,不要用 400 混淆语义。
- 路径参数能传负数或特殊字符吗?——`/items/-1` 按 int 解析成功再被 ge=1 拦;特殊字符要 URL 编码,FastAPI 自动解码。
