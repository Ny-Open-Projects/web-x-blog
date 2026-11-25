---
title: "[Q7729] 工具结果里的 NaN：Python 能序列化，前端解析不了"
date: 2026-11-23
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7729 · 工具结果里的 NaN：Python 能序列化，前端解析不了

难度：P6 ｜ 标签：工具调用、JSON、NaN、序列化

基线：Python 3.12；`json.dumps(allow_nan=...)`；严格 JSON 解析器（JS `JSON.parse`、Go）。

**问**：一个计算转化率的工具，分母为 0 时返回 `float('nan')`，`json.dumps` 正常输出 `{"rate": NaN}`，Python 侧 `json.loads` 也能读回来。但同一个工具结果发给前端/别的服务就报 `Unexpected token N in JSON`，模型有时还把 `NaN` 当成字符串复述进答案。NaN 到底算不算合法 JSON？工具结果该怎么清洗？

**答**：
- **结论**：`NaN`、`Infinity`、`-Infinity` **不是合法 JSON**。Python 的 `json` 模块默认 `allow_nan=True`，会输出这些裸字面量，并且自己的 `loads` 也宽容地接受；但 JS 的 `JSON.parse`、Go 的 `encoding/json` 等严格解析器会直接报错。工具结果跨语言传输时，一个 NaN 就能让整条链路解析失败；模型看到裸 `NaN` 也可能把它当普通词复述。
- **取舍**：`allow_nan=False` 能让问题在**序列化时**暴露（抛 `ValueError`），比在消费端炸更好；但要求上游先把 NaN 处理掉。把 NaN 转成 `null` 语义最清晰（"无值"），转成 `0` 会把"未知"伪装成"零"（转化率 0 与无数据是两件事），转成字符串 `"NaN"` 则会让类型漂移。推荐 `null` + 显式的缺失说明。
- **实战**：① 工具出口统一过一层 `sanitize`：`NaN/inf` → `None`，并记录字段名；② `json.dumps(..., allow_nan=False)` 作为最后一道闸，失败即告警；③ 数值计算前判断分母，能返回 `None` 就不要产生 NaN；④ 契约测试覆盖空数据、除零、极大值，断言输出可被严格解析器解析。

```python
"""NaN/Infinity 不是合法 JSON：Python 宽松、严格解析器拒绝。"""
import json
import math


def strict_loads(text: str):
    """模拟 JS JSON.parse / Go：遇到 NaN/Infinity 直接拒绝。"""
    def reject(token: str):
        raise ValueError(f"非法 JSON 常量: {token}")
    return json.loads(text, parse_constant=reject)


def sanitize(obj):
    if isinstance(obj, float) and (math.isnan(obj) or math.isinf(obj)):
        return None
    if isinstance(obj, dict):
        return {k: sanitize(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [sanitize(v) for v in obj]
    return obj


if __name__ == "__main__":
    payload = {"rate": float("nan"), "growth": float("inf"), "ok": 1.0}

    loose = json.dumps(payload)
    print("Python 默认输出:", loose)
    print("Python 自己能读:", json.loads(loose))

    try:
        strict_loads(loose)
    except ValueError as e:
        print("严格解析器:", e)

    try:
        json.dumps(payload, allow_nan=False)
    except ValueError as e:
        print("allow_nan=False:", e)

    clean = sanitize(payload)
    text = json.dumps(clean, allow_nan=False)
    print("清洗后:", text, "-> 严格解析:", strict_loads(text))

    # NaN != NaN 影响去重/缓存
    print("NaN == NaN:", float("nan") == float("nan"),
          "-> 不能当 dict key 做缓存命中判断")
```

**追问一**：为什么把 NaN 转成 0 是危险的？
→ 解析：0 是**有效值**，NaN 是**未知/未定义**。转化率分母为 0 时，0% 和"没有样本"业务含义完全不同；转 0 会让报表、均值、同比全部失真，且下游无法区分。应该用 `null` 表示缺失，并在展示层显示"暂无数据"。

**追问二**：NaN 作为字典 key 或缓存 key 会有什么问题？
→ 解析：`NaN != NaN`，所以 `d[float('nan')]` 写入后无法用另一个 NaN 取回；即使同一个对象，哈希行为也依赖实现。用它做缓存 key 会导致**永远 miss** 或**无限增长**。缓存 key 应先规范化（缺失用固定哨兵字符串），不要直接把浮点特殊值塞进去。

**追问三（可选）**：模型在工具结果里看到 `null` 和看到 `NaN`，行为差异大吗？
→ 解析：`null` 是 JSON 标准里的"无值"，模型训练中见过大量 `null` 语义，通常会描述为"无数据/未计算"；裸 `NaN` 不在标准 JSON 里，模型可能把它当普通标识符复述、或误以为是一个数值参与计算。工具结果应始终输出合法 JSON，避免把解析层的问题变成模型行为问题。
