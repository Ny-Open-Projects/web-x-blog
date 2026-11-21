---
title: [Q961] 数据校验分层: Pydantic 在哪一层把关
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q961 · 数据校验分层: Pydantic 在哪一层把关

> 难度:★★★☆ | 标签:Pydantic, 架构

**问**:请求校验、领域规则、数据库约束三层校验各管什么?会重复吗?

**答**:三层各司其职、深度递增:入口层(Pydantic)管"形状"——类型、必填、长度、格式,拒绝畸形请求并返回友好 422;领域层管"语义"——库存够不够、状态能不能流转,这是业务规则不是校验库的事;数据库层管"不变量"——唯一、外键、NOT NULL、CHECK,是并发下最后的真相防线。三者不重复而是递进:Pydantic 防意外,领域层防业务错误,数据库约束防程序 bug 与并发。常见错误是把"手机号唯一"只写在 Pydantic(先查后插有竞态,Q925)或把"邮箱格式"写进数据库 CHECK(迁移地狱)。原则:能并发发生的一切不变量必须有数据库约束兜底。

```python
# file: code/04_数据库与缓存/q961_pydantic_layers.py
"""三层校验: Pydantic 形状 -> 领域语义 -> 数据库约束"""
try:
    from pydantic import BaseModel, Field, field_validator
except ImportError:
    print("该题演示需要第三方库 pydantic:pip install pydantic,原理见正文")
    raise SystemExit(0)

class CreateOrderReq(BaseModel):
    sku: str = Field(min_length=1, max_length=32)
    qty: int = Field(gt=0, le=1000)

    @field_validator("sku")
    @classmethod
    def sku_charset(cls, v):
        if not v.isalnum():
            raise ValueError("sku 只允许字母数字")
        return v

STOCK = {"x": 5}

def domain_check(req) -> None:                 # 领域层: 业务语义
    if STOCK.get(req.sku, 0) < req.qty:
        raise ValueError("库存不足")

def db_write(req) -> bool:                     # 数据库层: 不变量
    import sqlite3
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE o (id INTEGER PRIMARY KEY, sku TEXT UNIQUE, qty INT)")
    try:
        conn.execute("INSERT INTO o (sku, qty) VALUES (?, ?)", (req.sku, req.qty))
        return True
    except sqlite3.IntegrityError:
        return False                            # 并发下最后防线

if __name__ == "__main__":
    try:
        CreateOrderReq(sku="x#bad", qty=1)
    except Exception as e:
        print("形状校验拒绝:", type(e).__name__)
    req = CreateOrderReq(sku="x", qty=99)
    try:
        domain_check(req)
    except ValueError as e:
        print("领域校验拒绝:", e)
    req2 = CreateOrderReq(sku="x", qty=2)
    domain_check(req2)
    print("落库:", db_write(req2))
```

**追问**:
- Pydantic 校验和 ORM 模型校验重复了怎么办?——ORM 的 nullable/length 是数据库映射不是业务校验,入口 DTO 与 ORM 模型职责不同,少量重复是必要冗余。
- 错误信息怎么统一?——Pydantic 的报错映射成标准 422 结构,领域错误转 409/400,数据库 IntegrityError 不直接透出,统一包装避免泄漏 schema。

---
