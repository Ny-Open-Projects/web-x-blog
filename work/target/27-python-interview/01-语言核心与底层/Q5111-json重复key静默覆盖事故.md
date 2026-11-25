---
title: [Q5111] JSON 重复 key 静默覆盖事故
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5111 · JSON 重复 key 静默覆盖事故

> 难度:★★★★☆ | 标签:事故复盘, json, object_pairs_hook

**问**:上游系统推送的 JSON 里同名 key 出现两次（人工合并配置导致），`json.loads` 不报错，后取值取到了"另一份"值，对账时才发现金额对不上。为什么标准库不报错？如何在解析层把重复 key 变成显式错误？

**答**:结论：JSON 规范（RFC 8259）本身**不禁止重复 key**，只说"名称 SHOULD 唯一"，所以 CPython 的 `json` C 解析器按"后者覆盖前者"处理，静默无告警——这是设计取舍：宽容解析换来通用性，把唯一性责任推给调用方。实战上不能靠下游自觉，要在**解析入口加 `object_pairs_hook`**：hook 拿到的是"有序键值对列表"（dict 构建前），逐对检查重复即可把覆盖变成异常或告警。注意取舍：hook 一旦提供就**禁用了 C 加速路径**（走纯 Python `scanstring` 回调），大报文解析成本会明显上升（实测差 5-10 倍），所以要么只在关键入口（计费、对账）开校验，要么 hook 内只查重不建复杂结构。另一个细节：hook 是"逐层对象"调用，嵌套对象每层各触发一次，校验逻辑天然递归生效。

```python
import json

raw = '{"amount": 100, "amount": 200, "currency": "CNY"}'

# 默认行为：静默后者覆盖前者
print(json.loads(raw))  # {'amount': 200, ...} 金额 100 消失了

# 方案：object_pairs_hook 查重（逐层对象生效）
def reject_dup(pairs):
    seen = {}
    for k, v in pairs:
        if k in seen:
            raise ValueError(f"重复 key: {k!r}")
        seen[k] = v
    return seen

try:
    json.loads(raw, object_pairs_hook=reject_dup)
except ValueError as e:
    print("拦截:", e)

# 若只告警不拒绝：保留最后一个并记录冲突（对账场景常用）
def warn_dup(pairs):
    d = {}
    for k, v in pairs:
        if k in d:
            print(f"[告警] key={k} 覆盖 {d[k]!r} -> {v!r}")
        d[k] = v
    return d
print(json.loads(raw, object_pairs_hook=warn_dup))

# 成本对照：hook 会关掉 C 加速器
import timeit
plain = '{"k": %d}' % 1
big = "[" * 50 + "]" * 50  # 简单负载即可看出数量级差异
payload = json.dumps({str(i): i for i in range(200)})
t1 = timeit.timeit(lambda: json.loads(payload), number=1000)
t2 = timeit.timeit(lambda: json.loads(payload, object_pairs_hook=reject_dup), number=1000)
print(f"plain x1000={t1:.3f}s  hook x1000={t2:.3f}s  比值≈{t2/t1:.1f}")
```

**追问一层**:`object_pairs_hook` 与 `object_hook` 的区别是什么？为什么查重必须用前者？
**追二层**:如果要兼容"合法的重复 key"协议（如某些流式日志聚合字段追加语义），hook 该怎么设计才不破坏 C 加速的普通路径？

**背诵要点**
- JSON 规范不禁止重复 key，CPython json 默认后者覆盖前者、零告警。
- 查重必须用 `object_pairs_hook`（拿到 dict 构建前的有序对），`object_hook` 拿到的已是覆盖后的 dict。
- 提供 hook 会禁用 C 加速器，大报文成本上升一个量级，只在关键入口开。

**复盘追问**
- 对账系统已经上线，无法改解析层，怎么在上游把住重复 key？提示：schema 校验层（jsonschema strict 模式）或中间人抓包复核。
- "后者覆盖"与"首个生效"是两个方向的选择，Java 的 Gson 默认哪个？为什么跨语言对账时这是坑？提示：实现各异，靠契约测试兜底。
