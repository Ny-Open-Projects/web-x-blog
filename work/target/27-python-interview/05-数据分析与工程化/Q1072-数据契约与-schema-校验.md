---
title: [Q1072] 数据契约与 schema 校验
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1072 · 数据契约与 schema 校验

> 难度:★★★★ | 标签:数据工程, 数据契约

**问**:上游改了个字段类型,下游报表半夜全红。数据契约怎么落地才能拦住这种事故?

**答**:数据契约是生产者与消费者对 schema、语义、SLA 的书面承诺,落地为代码里的显式 schema 定义 + 双端校验:生产端在写表前校验(不合契约不出门),消费端在读取后校验(不合契约不消费并告警)。校验内容四件套:字段与类型、空值率阈值、取值域(枚举/正则)、统计边界(值域/分布突变)。变更管理:加列默认向后兼容,删列/改类型必须升版本并给消费方迁移窗口。工具思想同 pandera/great expectations,关键是契约文件进版本管理、校验失败可阻断。

```python
# file: code/05_数据分析与工程化/q1072_data_contract.py
import re

SCHEMA = {
    "user_id": {"type": int, "nullable": False},
    "email": {"type": str, "nullable": False, "pattern": r"^[^@\s]+@[^@\s]+\.[a-z]{2,}$"},
    "amount": {"type": float, "nullable": True, "min": 0, "max": 1_000_000},
}

def validate(row):
    errs = []
    for field, rule in SCHEMA.items():
        v = row.get(field)
        if v is None:
            if not rule["nullable"]:
                errs.append(f"{field} 不可为空")
            continue
        if not isinstance(v, rule["type"]):
            errs.append(f"{field} 类型应为 {rule['type'].__name__}")
            continue
        if "pattern" in rule and not re.match(rule["pattern"], v):
            errs.append(f"{field} 不匹配取值域")
        if ("min" in rule and v < rule["min"]) or ("max" in rule and v > rule["max"]):
            errs.append(f"{field} 超出统计边界")
    return errs

rows = [
    {"user_id": 1, "email": "a@b.com", "amount": 9.9},
    {"user_id": 2, "email": "bad-mail", "amount": -1},
    {"email": "c@d.com", "amount": None},
]
for i, r in enumerate(rows):
    print(i, validate(r) or "通过")
```

**追问**:
- 追问 1:校验放生产端还是消费端?—— 两端都要:生产端拦截写入,消费端兜底防绕过,单一端都存在绕过路径。
- 追问 2:空值率阈值怎么定?—— 按历史分布设基线加容忍带,突变即告警,比拍一个 5% 更有解释力。
