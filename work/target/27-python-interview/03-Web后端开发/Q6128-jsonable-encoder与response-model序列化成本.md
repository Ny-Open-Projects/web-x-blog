---
title: [Q6128] FastAPI jsonable_encoder 与响应序列化成本账
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6128 · FastAPI jsonable_encoder 与响应序列化的成本账

> 难度:★★★★☆ | 标签:成本工程, FastAPI, 序列化

**问**:一个返回大列表的 FastAPI 接口，响应路径上到底发生了几次"转换"？`jsonable_encoder` 慢在哪？response_model 的二次校验什么时候是白付的？从 orjson 响应类到 `model_dump(mode="json")` 的优化阶梯怎么排？

**答**:结论：FastAPI 默认响应路径是三层：Pydantic **校验**（response_model：把 dict/ORM 对象再 validate 一次）→ `jsonable_encoder` **递归归一化**（datetime/UUID/枚举等转 JSON 可表示，纯 Python 逐字段递归）→ `json.dumps`（标准库慢于 orjson 2-5 倍）。对 1 万条记录的列表，每条记录三层遍历，纯 CPU 可到几十上百毫秒——这就是"业务很快、接口很慢"的隐形大头。优化阶梯（按收益/风险排）：a) **跳过二次校验**：返回 `Response(content=...)` 或 `response_model=None`，前提是数据已被上游（如 Pydantic 查询参数模型）保证——省一层；b) **Pydantic v2 原生路径**：`model_dump(mode="json")` 在 Rust 核里完成归一化，替代逐字段 jsonable_encoder——省二层的大头；c) **换序列化器**：`ORJSONResponse`（orjson，Rust 实现）替代 json.dumps——省三层；d) 终极：分页+流式（大列表别一次序列化，呼应 Q6103/Q6078）。降级：无 orjson 时用 `JSONResponse`+自定义 default，收益降级但结构不变。注意坑：跳过 response_model 后 **OpenAPI schema 丢失**（文档与契约测试失效），要二选一或在代码注释里登记。

```python
# 基线: FastAPI>=0.100 + Pydantic v2；orjson 可选（缺库自动降级标准 json）
import json, time, dataclasses
from datetime import datetime, timezone

try:
    from pydantic import BaseModel
    HAS_PD2 = True
except ImportError:
    HAS_PD2 = False

try:
    import orjson
    def fast_dumps(obj): return orjson.dumps(obj)
    ORJSON = True
except ImportError:
    ORJSON = False
    def fast_dumps(obj): return json.dumps(obj, default=str).encode()
    print("orjson 缺库 -> 降级标准 json（生产建议 orjson>=3.9）")

Row = dataclasses.make_dataclass("Row", ["id", "name", "created_at"])
rows = [Row(i, f"user-{i}", datetime(2026, 11, 21, tzinfo=timezone.utc))
        for i in range(10_000)]

# ---- 1) 层 1+2: jsonable_encoder 风格的手写递归归一化（慢路径原型） ----
def manual_encode(obj):
    if dataclasses.is_dataclass(obj):
        return {k: manual_encode(v) for k, v in obj.__dict__.items()}
    if isinstance(obj, datetime):
        return obj.isoformat()
    if isinstance(obj, list):
        return [manual_encode(x) for x in obj]
    return obj

t0 = time.perf_counter()
a = json.dumps(manual_encode(rows)).encode()
t1 = time.perf_counter()
print(f"手写递归归一化 + json.dumps: {(t1-t0)*1000:.0f} ms / 1 万条")

# ---- 2) Pydantic v2 路径: model_dump(mode="json")（Rust 归一化） ----
if HAS_PD2:
    class M(BaseModel):
        id: int
        name: str
        created_at: datetime
    models = [M(**r.__dict__) for r in rows]          # 构建成本不计入, 只比归一化
    t0 = time.perf_counter()
    b = json.dumps([m.model_dump(mode="json") for m in models]).encode()
    t1 = time.perf_counter()
    print(f"Pydantic v2 model_dump(mode='json') + json: {(t1-t0)*1000:.0f} ms")

# ---- 3) 序列化器层: orjson ----
t0 = time.perf_counter()
c = fast_dumps(manual_encode(rows))
t1 = time.perf_counter()
print(f"{'orjson' if ORJSON else 'json 降级'} dumps: {(t1-t0)*1000:.0f} ms"
      + ("（orjson 快 2-5x）" if ORJSON else ""))

# ---- 4) 结构决策: 大列表分页 ----
print("终极优化: 1 万条 -> limit/offset 分页 100 条, 单次序列化成本降 100 倍（呼应 Q6053 深分页账）")
```

**追问一层**:为什么 `jsonable_encoder` 不走 Pydantic 的 Rust 归一化？（它面向"任意 Python 对象"（dict/ORM/任意类）设计，必须纯 Python 通用递归；而 `model_dump` 只服务已知的模型结构，才能下放 Rust）。
**追问二层**:`response_class=ORJSONResponse` 与 `default_response_class` 的作用域差异？（router/app 级默认 vs 单路由覆盖；中间件链上的 JSONResponse 引用也要同步改，否则混用两种编码器）。
**追问三层**:跳过 response_model 后如何保住契约？（对"内部已知结构"的路径用 response_model=None 并用 OpenAPI 手工片段/schemathesis 对拍；对外契约敏感的路径保留校验——按消费者分层决定）。

## 背诵要点
- FastAPI 默认响应三层税：response_model 二次校验 → jsonable_encoder 递归归一化 → json.dumps。
- 优化阶梯：跳过二次校验 → model_dump(mode="json")（Rust）→ ORJSONResponse → 分页/流式。
- 跳过 response_model 会丢 OpenAPI 契约；按消费者分层决定校验保留与否。

## 复盘追问
- 某接口业务查询 20ms、总响应 300ms，如何用 py-spy/cProfile 证明大头在 jsonable_encoder？
- orjson 上线后出现 `TypeError: Type is not JSON serializable`，哪些类型是 orjson 的已知盲区（datetime 之外的 Decimal/set/自定义类）？
