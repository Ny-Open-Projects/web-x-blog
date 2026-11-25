---
title: "[Q6168] OpenAPI 破坏性变更判定矩阵与 CI 门禁"
date: 2026-11-23
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6168 · OpenAPI 破坏性变更判定矩阵与 CI 门禁

难度：P7 ｜ 标签：OpenAPI、破坏性变更、契约测试、schema diff、CI 门禁

**问**："加字段"一定是兼容的吗？"删字段"一定破坏吗？请把 ① 删字段 ② 加必填字段 ③ 加可选字段 ④ 改类型 ⑤ 收窄枚举 ⑥ 放宽枚举 这六种变更分成"破坏/兼容"，并解释对**生产者（服务端）与消费者（客户端）**分别意味着什么。为什么"服务端加必填字段"是破坏而"客户端加必填字段"是服务端兼容的？如何把这套判定做成 CI 里的自动门禁？本题与 Q851（契约测试）、Q1626（schema 漂移检测）、Q6048（OpenAPI 3.1 演进）的边界在哪？

**答**：
结论：破坏性判定要看"**谁先部署、谁承受失败**"。对服务端生产者：① 删字段——破坏（消费者读不到）；② 加必填字段——**破坏**（旧客户端请求里没有该字段，服务端校验直接 422）；③ 加可选字段——**兼容**（旧客户端忽略即可）；④ 改类型——破坏（反序列化失败）；⑤ 收窄枚举——破坏（旧客户端发的值被拒）；⑥ 放宽枚举——兼容。对消费者（请求侧）则相反：客户端新增必填字段是"我要求更强"，服务端旧版本不返回该字段就失败——所以**"客户端加必填"破坏的是客户端对旧服务端的兼容**，而服务端视角下"响应新增可选字段"是兼容的。核心原则：**生产者先部署时，新 schema 必须能被旧消费者接受**（向后兼容）；消费者先部署时（consume-first），新客户端必须能容忍旧响应——这就是消费者驱动契约（CDC）的价值。Q851 讲契约测试的工作流、Q1626 讲"文档与实现是否漂移"、Q6048 讲 OpenAPI 3.1 的规范演进，本题专攻"**破坏性变更的可判定清单与门禁规则**"——三者不重复。

取舍：CI 门禁不能只做"文本 diff"（注释/顺序变化会误报），要做**语义 schema diff**：按上面六类规则判定，输出"破坏性/兼容性"清单；破坏性变更默认拒绝合并，确需破坏时走"版本号升级 + 双写过渡 + 消费者迁移完成"的显式流程。误报治理：把"仅新增可选字段/放宽枚举/改描述"标为兼容不拦；对 `additionalProperties` 与 `oneOf`/`anyOf` 这类复杂结构要有专门规则，否则门禁要么漏判要么误拦。

实战：事故形态是"服务端加了个 `region` 必填字段上线，所有旧客户端 422"——门禁应在 merge 前就拦住。下面实现一个最小 schema-diff 判定器（stdlib dict），跑六种变更，输出破坏性清单。

```python
def breaking_changes(old, new):
    """最小语义 diff：返回破坏性变更清单（示意，生产用 openapi-schema-diff 类工具）。"""
    issues = []
    op, np = old.get("properties", {}), new.get("properties", {})
    oreq, nreq = set(old.get("required", [])), set(new.get("required", []))

    for name in op.keys() - np.keys():                 # ① 删字段
        issues.append(f"BREAK removed field: {name}")
    for name in nreq - oreq:                           # ② 加必填字段
        issues.append(f"BREAK new required: {name}")
    for name in np.keys() - op.keys():                 # ③ 加可选字段
        if name not in nreq:
            pass                                        # 兼容：旧消费者忽略
    for name in op.keys() & np.keys():                  # ④ 改类型
        ot, nt = op[name].get("type"), np[name].get("type")
        if ot != nt:
            issues.append(f"BREAK type changed: {name} {ot}->{nt}")
        oe, ne = set(op[name].get("enum", [])), set(np[name].get("enum", []))
        if oe and ne and ne < oe:                       # ⑤ 收窄枚举
            issues.append(f"BREAK enum narrowed: {name} {sorted(oe)}->{sorted(ne)}")
        if oe and ne and oe < ne:                       # ⑥ 放宽枚举
            pass                                        # 兼容
    return issues

base = {"properties": {
            "id": {"type": "integer"},
            "status": {"type": "string", "enum": ["new", "done"]},
        }, "required": ["id"]}

cases = {
    "加可选字段": {"properties": {**base["properties"], "note": {"type": "string"}}, "required": ["id"]},
    "加必填字段": {"properties": {**base["properties"], "region": {"type": "string"}}, "required": ["id", "region"]},
    "删字段":     {"properties": {"id": {"type": "integer"}}, "required": ["id"]},
    "改类型":     {"properties": {"id": {"type": "string"}, "status": base["properties"]["status"]}, "required": ["id"]},
    "收窄枚举":   {"properties": {"id": {"type": "integer"}, "status": {"type": "string", "enum": ["done"]}}, "required": ["id"]},
    "放宽枚举":   {"properties": {"id": {"type": "integer"}, "status": {"type": "string", "enum": ["new", "done", "archived"]}}, "required": ["id"]},
}
for name, new in cases.items():
    issues = breaking_changes(base, new)
    print(f"{name:8}: {'COMPAT' if not issues else ' / '.join(issues)}")
```

**追问一**：为什么"服务端加必填字段"是破坏，而"响应里新增可选字段"是兼容？——因为请求字段由客户端提供，加必填等于要求旧客户端"凭空多给一个它不知道的值"，旧请求一律 422；响应字段由服务端提供，新增可选字段时旧客户端按 JSON 松散解析忽略未知字段即可（前提是客户端没开 `additionalProperties=false` 严格模式）。方向性决定了同一操作在请求/响应上的compat 判定相反——门禁必须区分 request/response schema。

**追问二**：为什么"文本 diff"做不好 schema 门禁？——因为 schema 的等价性不是文本等价：字段顺序、key 顺序、`description`/`title` 变化、多余的 `examples` 都不改变契约语义，文本 diff 会大量误报；反过来 `enum` 收窄、类型从 `integer` 改 `number` 这类破坏在文本上可能只是几个字符，容易被忽略。门禁必须做**语义级 diff**：解析成结构、按规则逐项判定、区分 request/response 与生产者/消费者角色——这正是 Q1626"漂移检测"要升级到的层次。

## 背诵要点
- 服务端破坏清单：删字段、加请求必填字段、改类型、收窄枚举；兼容：加可选字段、放宽枚举、改描述。
- 方向性：请求加必填破坏旧客户端，响应加可选字段兼容旧客户端；门禁要区分 request/response 与谁先部署（CDC）。
- 语义 diff 而非文本 diff：字段顺序/描述变化不拦，类型/enum 收窄要拦；与 Q851/Q1626/Q6048 是工作流/漂移/规范/门禁四层次。

## 复盘追问
- 服务端上线加了 `region` 必填字段导致所有旧客户端 422，如何用破坏性矩阵解释并给出 CI 门禁？（请求必填方向性、语义 diff 规则、双写过渡与 CDC，讨论与文本 diff 的误报）
- 为什么"客户端先部署"时契约规则会反过来？（新客户端要求旧服务端还没有的响应字段，讨论 consume-first 与 CDC 的协作）
