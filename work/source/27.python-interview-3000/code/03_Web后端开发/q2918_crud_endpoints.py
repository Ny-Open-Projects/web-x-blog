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
