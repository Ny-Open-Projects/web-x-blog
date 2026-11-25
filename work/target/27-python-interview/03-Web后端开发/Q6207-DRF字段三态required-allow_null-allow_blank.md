---
title: "[Q6207] DRF 字段三态：required / allow_null / allow_blank 各管一关"
date: 2026-11-24
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6207 · DRF 字段三态：required / allow_null / allow_blank 各管一关

难度：P6 ｜ 标签：DRF、Serializer、required、allow_null、allow_blank、校验语义

**问**：PATCH 接口想"不传就跳过"，设置了 `required=False`，但前端传 `null` 还是报 "This field may not be null"；改了 `allow_null=True`，空字符串又报 "may not be blank"。这三个开关到底各管哪一关？字段"缺失"和"值为 null"在语义上有什么本质区别？PATCH 部分更新时这三个开关该怎么组合？

**答**：
结论：DRF 的字符串/对象字段校验是三道独立关卡，顺序为：**①required（缺失关）**——字段 key 不在请求体里时，required=True 直接拒绝，required=False 则跳过后续校验返回 None；**②allow_null（null 关）**——值显式为 JSON null 时，allow_null=False 拒绝，True 放行并跳过其余校验；**③allow_blank（空串关）**——仅对字符串值生效，空串在 null 之后检查。三者的核心区别是"缺失"（key 不存在，用户根本没提供）与"null"（用户明确表达'没有值'）是不同的客户端语义：前者多见于 PATCH 局部更新，后者是显式置空。三个开关正交组合，不能互相替代——`required=False` 管不到 `null`，`allow_null=True` 管不到 `""`。

取舍：a) PUT 全量更新：required=True + 默认禁 null/blank，逼客户端提交完整对象；b) PATCH 局部更新：`required=False` 是主开关，null 是否合法按业务定——"可显式清空的字段"（备注、头像 URL）配 `allow_null=True`，"不可空的核心字段" PATCH 时允许不传但不允许显式置 null；c) 空串：对"用户文本输入"通常 `allow_blank=True`（用户就爱清空文本框），对"标识/外键类"禁 blank 只允许 null；d) 数据库层要和校验层对齐：`models.CharField(blank=True, null=True)` 与 serializer 三个开关是两套体系（blank 是 Django 表单/管理界面语义，null 是数据库 NULL 语义），别混着改；e) 避免三关全开（required=False + allow_null + allow_blank）——那意味着字段永远接受一切输入，等于没有校验，多见于"不知道哪关报错就全打开"的补丁式修复。

实战：事故形态是"用户资料 PATCH 接口 nickname 设了 required=False 但没开 allow_null，前端重置资料时传 null 全量 422；前端又改成传空串，数据库 NOT NULL 约束炸出 500；最终契约定为：nickname PATCH 可不传（required=False）、可传 null（allow_null=True，落库为 NULL）、禁传空串（allow_blank=False），前后端文档同步"。下面跑一遍三关 × 四输入的行为矩阵。

```python
class CharField:
    def __init__(self, required=True, allow_null=False, allow_blank=False):
        self.required = required
        self.allow_null = allow_null
        self.allow_blank = allow_blank

    def run(self, value=..., present=True):
        if not present:
            if self.required:
                raise ValueError("This field is required.")
            return None                              # 缺省且非必填 → None
        if value is None:
            if not self.allow_null:
                raise ValueError("This field may not be null.")
            return None                              # 显式 null 且放行
        if isinstance(value, str) and value == "":
            if not self.allow_blank:
                raise ValueError("This field may not be blank.")
        return value


CASES = [
    ("缺失", dict(present=False)),
    ("显式 null", dict(value=None)),
    ("空串", dict(value="")),
    ("正常值", dict(value="alice")),
]

for label, kwargs in CASES:
    row = []
    for name, f in [("required+禁null+禁blank", CharField()),
                    ("required+可null+可blank", CharField(allow_null=True, allow_blank=True))]:
        try:
            row.append(f"{name}={f.run(**kwargs)!r}")
        except ValueError as e:
            row.append(f"{name}=拒绝({e})")
    print(f"[{label}] " + " ｜ ".join(row))
```

**追问一**：为什么 DRF 把 allow_blank 单独设开关而不复用 allow_null？—— 因为它们在数据模型里对应不同的存储语义：null 是"值不存在"（数据库 NULL），空串是"值存在且为零长度"（数据库 ''）。对唯一索引：NULL 之间不冲突（Postgres 默认），'' 之间冲突——同一个 nickname 字段，允许多个用户昵称为空与允许多个用户昵称为 '' 是两种完全不同的业务约束。序列化层把两者分开，才能让校验语义精确映射到数据库约束；合并成一个开关会丢失"显式置空"的表达能力。

**追问二**：PATCH 里"没传"和"传 null"后端分别该怎么落库？—— 没传：required=False 时该字段不出现在 `validated_data`，serializer 的 `update` 用 `validated_data.items()` 遍历自然跳过，DB 值不动——这是 DRF partial update 的天然行为。传 null（allow_null=True）：validated_data 里出现 None，update 会把它写进数据库成 NULL——**显式清空**。踩坑点在自定义 update：用 `validated_data.get('x')` 会把"没传"和"传 null"混成一个 None，导致 PATCH 没传的字段被清空。正确写法是 `'x' in validated_data` 判断存在性，或区分 `None` 与 `missing` 哨兵。

## 背诵要点
- 三关顺序：required（缺失 key）→ allow_null（显式 null）→ allow_blank（字符串空串）；缺失与 null 是不同客户端语义。
- PATCH 组合：required=False 管局部更新；可清空字段加 allow_null；文本输入放 allow_blank、标识类禁 blank。
- 自定义 update 用 `'x' in validated_data` 区分存在性；`get('x')` 会把没传与 null 混淆导致误清空。

## 复盘追问
- 前端传 null 报 may not be null，加什么开关？语义代价是什么？（allow_null=True；数据库该列需允许 NULL，且"显式置空"从此合法）
- 唯一索引下多个空串冲突而多个 NULL 不冲突，为什么？这解释了哪个开关的存在？（NULL 互不等值、'' 互相等值；allow_blank 独立于 allow_null 的存储语义）
