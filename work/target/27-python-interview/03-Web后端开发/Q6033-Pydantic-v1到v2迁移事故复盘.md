---
title: [Q6033] Pydantic v1→v2 迁移事故复盘
date: 2026-11-20
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6033 · Pydantic v1→v2 迁移事故复盘

> 难度:★★★★ | 标签:版本演进, Pydantic, 事故复盘

**问**：Pydantic v2 性能翻倍，为什么迁移仍然事故频发？v1/v2 的语义差异里最容易漏的四个是什么？`bump-pydantic` 这类自动迁移工具覆盖不到哪里？

**答**：v2 的核心是把校验核心移到 Rust（pydantic-core），性能大增，但**语义不只是"改 import"**。最易漏的四个差异：1) **strict/lax 语义收紧**——v2 默认 smart 模式，`"123" → int` 在 lax 下仍可通过，但 `"1.0" → int` 会被拒（v1 接受），从宽松来源（表单/CSV）接数的接口悄然 422；2) **`dict()` → `model_dump()` 且默认序列化行为变化**——v2 默认不序列化非字符串键的 dict 键为字符串，datetime/UUID 默认输出 ISO 格式但 mode 参数（python/json）不同结果不同；3) **验证器体系重构**——`@validator` → `@field_validator`/`@model_validator`，`always=True`、`pre`/`post` 语义重排，**每个值回调里 `values` 参数没了**，跨字段校验要改 model_validator(mode='after')；4) **`schema()` / `parse_obj` / `json()` 全套 API 改名**（`model_json_schema`/`model_validate`/`model_dump_json`），三方库（旧 fastapi 版本）还在调旧 API 就炸。自动工具边界：bump-pydantic 能机械改名（import/方法名），**改不了语义**——strict 收紧、验证器重排后的执行顺序必须人工逐个审。事故预防：迁移前用 v1 的测试集 + 真实流量样本做**双跑对比**（同一输入 v1/v2 输出 diff），生产灰度按端点切流。

```python
# file: code/03_Web后端开发/q6033_pydantic_v2_migration.py
"""Pydantic v2 语义差异自检. v2 为基线(>=2.0), 缺库降级为清单演示."""
import sys

try:
    from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator
    HAS_V2 = True
except ImportError:
    HAS_V2 = False
    print("pydantic 未安装(v2 基线, pip install 'pydantic>=2'), 降级为清单演示")

DIFFS = [
    "strict/smart: '1.0'->int 被 v2 拒(v1 收)",
    "dict() -> model_dump(); 序列化 mode=python/json 差异",
    "@validator -> @field_validator/@model_validator, values 参数取消",
    "parse_obj/json/schema 全套改名 model_*",
]

class Order(BaseModel):
    qty: int
    price: float
    total: float = 0

    @model_validator(mode="after")            # v2 跨字段校验的新家
    def check_total(self):
        if abs(self.total - self.qty * self.price) > 0.01:
            raise ValueError("total mismatch")
        return self

if HAS_V2:
    ok = Order(qty=2, price=9.9, total=19.8)
    print("v2 正常:", ok.model_dump(), "| json:", ok.model_dump_json())

    # 差异1: '1.0' -> int 在 v2 被拒 (v1 会收)
    try:
        Order(qty="1.0", price=1.0, total=1.0)
        print("qty='1.0' 通过(v1 语义)")
    except Exception as e:
        print("v2 拒绝 '1.0'->int:", str(e).replace(chr(10), " ")[:70])

    # 差异2: mode 差异
    import datetime
    class Ts(BaseModel):
        at: datetime.datetime
    t = Ts(at=datetime.datetime(2026, 11, 20, 12, 0))
    print("dump python:", t.model_dump(mode="python")["at"],
          "| dump json:", t.model_dump(mode="json")["at"])
else:
    for d in DIFFS:
        print("  -", d)

print("迁移纪律: bump-pydantic 只管改名; strict 收紧与验证器重排须双跑对比逐个审")
```

**追问**：1) 为什么 `"1.0" → int` 的差异杀伤力大？——它藏在"上游改了数据格式"的故障里：v1 时代上游把 int 序列化成 `1.0` 没事，v2 升级后同样的上游数据开始 422，表象是"升级后接口变脆"；防线是入口层双跑对比 + 明确 strict 化的端点清单。2) `model_validator(mode='after')` 和 v1 `@model_validator` 的差异？——after 模式拿到的是已构造的 self（字段已是验证后类型），跨字段断言更自然；但它**只在全部字段通过后执行**，v1 里能做的"改写其他字段"要改 before 模式并返回 data dict。3) FastAPI 与 Pydantic 的版本耦合怎么管？——FastAPI 版本声明支持的 Pydantic 大版本要先行锁定（依赖矩阵第一步），升级顺序"先 FastAPI 到支持 v2 的版本、再切 v2"，反向顺序必炸。

## 背诵要点
- v2 = Rust 核心 + 语义收紧；自动工具只管改名，strict/验证器/API 三类语义变化必须人工审。
- 四大差异：smart strict 拒 '1.0'→int、model_dump 与 mode、验证器重构（values 取消）、API 全改名。
- 迁移防护：真实流量样本 v1/v2 双跑 diff + 按端点灰度 + FastAPI 版本先锁定。

## 复盘追问
- 双跑对比需要多少样本才敢放量？样本分布偏斜（都是"干净数据"）会漏掉什么？
- 灰度期间 v1/v2 行为不一致的端点清单怎么生成和维护？
