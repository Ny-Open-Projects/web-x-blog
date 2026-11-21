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
