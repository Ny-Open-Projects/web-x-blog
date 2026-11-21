---
title: [Q2918] 完整 CRUD 端点骨架: 内存存储加校验加分页
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2918 · 完整 CRUD 端点骨架: 内存存储加校验加分页

> 难度:★★★☆ | 标签:FastAPI, CRUD, 分页

**问**:现在动手写一个资源 CRUD 接口的骨架, 内存存储即可: 创建、查列表、查详情、部分更新、删除都要有, 校验和分页你打算放在哪几层?

**答**:校验放最外层, 在进入业务逻辑前就把非法请求打成 422, 未知字段显式拒绝而不是静默丢弃; 分页是列表接口的出口契约, 三件套 page、page_size、total 一起返回, 且 page_size 必须有上限防御, 否则一次 page_size=100000 的请求就打穿内存。存储层即使只是内存字典也要固定排序键, 保证分页结果稳定可测。更新区分 PUT 与 PATCH 两种语义: PUT 全字段替换、PATCH 局部更新只校验出现的字段。删除与详情对不存在的资源统一 404, 让客户端能区分"没有"与"坏了"。

```python
# file: code/03_Web后端开发/q2918_crud_endpoints.py
"""完整 CRUD 端点骨架: 内存存储 + 字段校验 + 分页。

装有 fastapi 时走框架路径; 缺库时降级为等价的标准库内核演示(校验、CRUD、分页语义一致)。
"""
import sys

try:
    from typing import Optional
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel, Field
    from fastapi.testclient import TestClient
except ImportError:
    print("未安装 fastapi/pydantic, 降级为标准库内核演示(同样的校验与分页语义):")

    class ValidationError(Exception):
        pass

    REQUIRED = {"title": str, "author": str}
    MAX_PAGE_SIZE = 50

    def validate_book(payload, partial=False):
        """创建要求全字段, 更新允许部分字段; 未知键拒绝, 类型不符拒绝。"""
        if not isinstance(payload, dict):
            raise ValidationError("请求体必须是对象")
        unknown = set(payload) - set(REQUIRED)
        if unknown:
            raise ValidationError("未知字段: %s" % ",".join(sorted(unknown)))
        for key, typ in REQUIRED.items():
            if key in payload:
                if not isinstance(payload[key], typ):
                    raise ValidationError("%s 必须是字符串" % key)
            elif not partial:
                raise ValidationError("缺少必填字段: %s" % key)
        return True

    class BookStore:
        def __init__(self):
            self._items = {}
            self._next_id = 1

        def create(self, payload):
            validate_book(payload)
            item = dict(payload, id=self._next_id)
            self._items[self._next_id] = item
            self._next_id += 1
            return item

        def get(self, item_id):
            if item_id not in self._items:
                raise KeyError(item_id)
            return self._items[item_id]

        def list(self, page=1, page_size=10):
            page_size = min(max(page_size, 1), MAX_PAGE_SIZE)  # page_size 上限防御
            page = max(page, 1)
            ordered = sorted(self._items.values(), key=lambda i: i["id"])
            start = (page - 1) * page_size
            return {"items": ordered[start:start + page_size], "page": page,
                    "page_size": page_size, "total": len(ordered)}

        def update(self, item_id, payload):
            validate_book(payload, partial=True)
            item = self.get(item_id)
            item.update(payload)
            return item

        def delete(self, item_id):
            item = self.get(item_id)
            del self._items[item_id]
            return item

    store = BookStore()
    b1 = store.create({"title": "流畅的Python", "author": "Ramalho"})
    b2 = store.create({"title": "Fluent Python 2e", "author": "Ramalho"})
    try:
        store.create({"title": "缺作者的书"})
    except ValidationError as e:
        print("创建缺字段被拒:", e)
    try:
        store.create({"title": "多余字段", "author": "x", "price": 1})
    except ValidationError as e:
        print("未知字段被拒:", e)
    store.update(b1["id"], {"title": "流畅的Python第2版"})
    page = store.list(page=1, page_size=1)
    print("分页: 第%s页 共%s条 返回%s条" % (page["page"], page["total"], len(page["items"])))
    store.delete(b2["id"])
    try:
        store.get(b2["id"])
    except KeyError:
        print("删除后读取 -> 404 语义")
    sys.exit(0)

# ---------- 框架路径 ----------
app = FastAPI()
BOOKS = {}
_next_id = 1
MAX_PAGE_SIZE = 50


class BookIn(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    author: str = Field(min_length=1, max_length=50)


class BookPatch(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=100)
    author: Optional[str] = Field(default=None, min_length=1, max_length=50)


@app.post("/books", status_code=201)
def create_book(book: BookIn):
    global _next_id
    item = book.dict()
    item["id"] = _next_id
    _next_id += 1
    BOOKS[item["id"]] = item
    return item


@app.get("/books")
def list_books(page: int = 1, page_size: int = 10):
    page = max(page, 1)
    page_size = min(max(page_size, 1), MAX_PAGE_SIZE)
    ordered = sorted(BOOKS.values(), key=lambda i: i["id"])
    start = (page - 1) * page_size
    return {"items": ordered[start:start + page_size], "page": page,
            "page_size": page_size, "total": len(ordered)}


@app.get("/books/{book_id}")
def get_book(book_id: int):
    if book_id not in BOOKS:
        raise HTTPException(status_code=404, detail="book not found")
    return BOOKS[book_id]


@app.patch("/books/{book_id}")
def patch_book(book_id: int, patch: BookPatch):
    if book_id not in BOOKS:
        raise HTTPException(status_code=404, detail="book not found")
    data = {k: v for k, v in patch.dict().items() if v is not None}
    BOOKS[book_id].update(data)
    return BOOKS[book_id]


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    if book_id not in BOOKS:
        raise HTTPException(status_code=404, detail="book not found")
    del BOOKS[book_id]


client = TestClient(app)
r = client.post("/books", json={"title": "流畅的Python", "author": "Ramalho"})
assert r.status_code == 201, r.text
book_id = r.json()["id"]
client.post("/books", json={"title": "第二本", "author": "某人"})
assert client.get("/books", params={"page": 1, "page_size": 1}).json()["total"] == 2
assert client.get("/books/999").status_code == 404
assert client.post("/books", json={"title": ""}).status_code == 422
patched = client.patch("/books/%d" % book_id, json={"title": "流畅的Python第2版"})
assert patched.json()["title"].endswith("第2版")
assert client.delete("/books/%d" % book_id).status_code == 204
assert client.get("/books").json()["total"] == 1
print("框架路径: 创建/校验422/分页/404/更新/删除 全部通过")
```

**追问**:
- PATCH 的 partial 校验与 PUT 有什么差别?——PUT 是整体替换要求全字段, PATCH 是局部更新只校验出现的字段, 校验器必须能区分这两种模式。
- 列表接口为什么返回 total 而不是让客户端翻到空页?——total 让前端一次算出页数, 翻空页的隐式约定会在并发增删时产生跳页歧义。
