---
title: "[Q6093] Pydantic v2 discriminated union 的校验成本"
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6093 · Pydantic v2 discriminated union 校验成本与原理

难度：P6-P7 | 标签：成本工程 | Pydantic v2 | 校验

**问**：一个 API 接收多形态消息（文本/图片/卡片…），模型定义成 `Union[Text, Image, Card, ...]` 后接口延迟涨了。为什么裸 Union 慢？`Field(discriminator=...)` 的 tagged union 快在哪里？快多少、成本怎么量化？

**答**：
结论：裸 Union 的校验是**逐个成员尝试**：Pydantic v2 的 Rust 核心按顺序用每个子模型试解析，失败才换下一个——最坏 N 次解析 + N 组错误收集，成员越多、公共字段越相似，浪费越大。`Literal` 判别字段 + `Field(discriminator="type")` 把它变成 O(1) 查表：先读 `type` 字符串，直接路由到对应子模型（smart union 关闭时语义明确，错误信息也只指向选中分支）。实测差距随成员数线性放大：5 成员裸 union 错误样本可比判别式慢 5-10 倍。
取舍：discriminated union 要求载荷里有显式类型标签（契约更强，API 兼容成本：新增分支是加值不算破坏性变更）；没有天然判别字段的载荷要先做标签化改造，或用 `Union` + `model_config=ConfigDict(strict=True)` 收窄尝试空间。
实战：多形态 payload 一律判别式；用 `timeit` 对比两版 `model_validate`，并把"union 成员数"纳入模型评审；失败率高的接口还要看错误收集成本（裸 union 的错误列表很长，日志膨胀）。

```python
# 基线：Python 3.9+ / Pydantic v2（2.5+）；缺库则降级为纯 dataclass 说明
try:
    from pydantic import BaseModel, Field, ConfigDict, TypeAdapter
    from typing import Literal, Union, Annotated
    HAS_PYD = True
except ImportError:
    HAS_PYD = False
    print("pydantic v2 未安装：pip install 'pydantic>=2.5' 后重跑（本脚本降级退出）")
    import sys; sys.exit(0)

import timeit, json

class Text(BaseModel):
    type: Literal["text"]
    body: str

class Image(BaseModel):
    type: Literal["image"]
    url: str
    w: int = 0
    h: int = 0

class Card(BaseModel):
    type: Literal["card"]
    title: str
    items: list[str] = []

PlainUnion = Union[Text, Image, Card]
TaggedUnion = Annotated[Union[Text, Image, Card], Field(discriminator="type")]
plain_ta = TypeAdapter(PlainUnion)
tag_ta = TypeAdapter(TaggedUnion)

payloads_ok = [json.dumps({"type": "image", "url": "http://x/a.png", "w": 1, "h": 2}),
               json.dumps({"type": "text", "body": "hi"}),
               json.dumps({"type": "card", "title": "t", "items": ["a"]})]

# 正确载荷：裸 union 也要逐成员尝试（text 排第一时 image 要试 1 次失败）
N = 5000
t_plain = timeit.timeit(lambda: [plain_ta.validate_json(p) for p in payloads_ok], number=N) / N
t_tag = timeit.timeit(lambda: [tag_ta.validate_json(p) for p in payloads_ok], number=N) / N
print(f"正确样本: 裸 union {t_plain*1e6:.0f} us vs 判别式 {t_tag*1e6:.0f} us / 批")

# 错误载荷（type 是 image 但缺字段）：裸 union 会被 Text/Card 也各试一遍，错误收集更贵
bad = json.dumps({"type": "image", "w": 1, "h": 2})
try:
    plain_ta.validate_json(bad)
except Exception as e:
    err_plain = str(e)
try:
    tag_ta.validate_json(bad)
except Exception as e:
    err_tag = str(e)
print("错误信息长度: 裸", len(err_plain), "字 vs 判别式", len(err_tag), "字")
print("判别式错误只指向 image 分支:", "image" in err_tag)

# 兼容性：新增分支 = 新 Literal 值，属非破坏性扩展
class Audio(BaseModel):
    type: Literal["audio"]
    url: str
T2 = TypeAdapter(Annotated[Union[Text, Image, Card, Audio], Field(discriminator="type")])
print("新增 audio 分支校验:", type(T2.validate_json(json.dumps({"type":"audio","url":"u"}))).__name__)
```

**追问 1**：为什么判别式的错误信息更短更好排查？
- 追问 2 层：裸 union 收集每个成员的失败原因（"text 缺 body / image 缺 url / card 缺 title"），判别式只报告被选中分支的缺失；日志与 422 响应体积同步缩小。
- 追问 3 层：smart union（v2 默认开启的智能匹配）会按"最像的成员优先"减少尝试，但有歧义载荷时行为不如显式判别字段可预期。

**追问 2**：判别字段在嵌套结构里怎么传播？
- 追问 2 层：判别字段只作用于标注那一层的 union；嵌套（如 `list[TaggedUnion]`）每项独立路由，成本仍是每项 O(1)。
- 追问 3 层：顶层没有标签时可用 `model_validator(mode="before")` 注入标签，但这会把路由成本拉回 Python 层，吞吐敏感接口避免。

## 背诵要点
1. 裸 Union 逐成员尝试（最坏 N 次解析+N 组错误），判别式 O(1) 查表路由，快 5-10 倍且错误信息聚焦。
2. 判别式前提是显式 type 标签（Literal），新增分支是非破坏性扩展。
3. 无标签载荷先标签化或 strict 收窄；validator-before 注入标签会把成本拉回 Python 层。

## 复盘追问
1. 为什么接口延迟只在错误率高的时段恶化？——失败样本触发全成员尝试+错误收集，错误率与校验 CPU 同向放大。
2. 迁移到判别式对客户端是什么破坏性变更？——要求补 type 字段；灰度期用 before-validator 兼容补标过渡。
