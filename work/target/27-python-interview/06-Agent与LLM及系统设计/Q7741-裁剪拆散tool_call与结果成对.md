---
title: "[Q7741] 裁剪历史时把 assistant.tool_calls 和 tool 结果拆开，接口直接 400"
date: 2026-11-24
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7741 · 裁剪历史时把 assistant.tool_calls 和 tool 结果拆开，接口直接 400

难度：P7 ｜ 标签：LLM、工具调用、上下文裁剪、消息协议

基线：Python 3.12；用消息列表 + 协议校验器模拟 OpenAI/Anthropic 的 tool 消息约束。

**问**：长会话按 token 预算裁历史，规则是"从最旧的开始删，直到装得下"。上线后偶发 400：`messages with role 'tool' must be a response to a preceding message with 'tool_calls'`，以及 `An assistant message with 'tool_calls' must be followed by tool messages responding to each 'tool_call_id'`。重试一次有时又好（因为这次裁剪的边界不同）。裁剪逻辑哪里错了？

**答**：
- **结论**：工具调用是**成对的结构**：`assistant(tool_calls=[id...])` 必须紧跟每个 id 对应的 `tool` 消息，缺一不可、顺序不能乱、也不能只删一半。按"消息条数/token 从旧到新删"的贪心裁剪会从中间切断一对：删掉 `assistant` 留下 `tool`（孤儿结果），或删掉后面的 `tool` 留下 `tool_calls`（悬空调用），两种都直接违反协议。
- **取舍**：正确做法是**以"调用块"为最小单位**裁剪：把 `assistant(tool_calls)` + 它对应的全部 `tool` 结果打包成一个不可分割的 block，删除时整块删；同时保留 `system` 与最后一条 `user`，并保证裁剪后第一条非 system 消息不是 `tool`。更稳的是"摘要代替删除"：把旧块压成一条 `assistant` 文本摘要，既省 token 又不破坏结构。
- **实战**：① 裁剪后跑一遍协议校验（本地就能写：每个 `tool` 必须有前置声明、每个 `tool_call_id` 必须有结果），失败就回退到"不裁这一块"而不是硬删；② 用"轮次"而不是"条数"做预算单位，一轮 = user + 若干 assistant/tool 往返；③ 记录裁剪前后的消息 id 列表，出问题能复现；④ 别在裁剪时改角色（把 tool 结果改写成 user 文本）——那会改变模型对"这是工具返回值"的认知，影响后续调用。

```python
"""按条裁剪会拆散 tool_call/tool 结果；按块裁剪才满足协议。"""
import json

SYSTEM = {"role": "system", "content": "你是客服助手，必须先查订单再退款。" * 8}
HISTORY = [
    {"role": "user", "content": "帮我查订单 123，然后退款"},
    {"role": "assistant", "content": None,
     "tool_calls": [{"id": "call_1", "name": "get_order", "arguments": {"order_id": "123"}}]},
    {"role": "tool", "tool_call_id": "call_1",
     "content": json.dumps({"status": "paid", "amount": 100})},
    {"role": "assistant", "content": None,
     "tool_calls": [{"id": "call_2", "name": "refund", "arguments": {"order_id": "123"}}]},
    {"role": "tool", "tool_call_id": "call_2", "content": json.dumps({"ok": True})},
    {"role": "assistant", "content": "已退款 100 元。"},
    {"role": "user", "content": "那发票呢？"},
]


def tokens(msg: dict) -> int:
    size = len(msg.get("content") or "")
    size += len(json.dumps(msg.get("tool_calls") or [], ensure_ascii=False))
    return max(1, size // 2)          # 粗估：2 字符 ≈ 1 token


def validate(msgs: list[dict]) -> list[str]:
    errors = []
    pending: set[str] = set()
    for i, m in enumerate(msgs):
        if m["role"] == "assistant" and m.get("tool_calls"):
            if pending:
                errors.append(f"#{i} 上一个 tool_calls 还有未回应的 id: {sorted(pending)}")
            pending = {c["id"] for c in m["tool_calls"]}
        elif m["role"] == "tool":
            cid = m["tool_call_id"]
            if cid not in pending:
                errors.append(f"#{i} 孤儿 tool 消息: {cid} 没有前置 tool_calls")
            else:
                pending.discard(cid)
        else:
            if pending:
                errors.append(f"#{i} tool_calls 未全部回应: {sorted(pending)}")
                pending = set()
    if pending:
        errors.append(f"结尾仍有未回应的 tool_calls: {sorted(pending)}")
    return errors


def trim_naive(msgs: list[dict], budget: int) -> list[dict]:
    out = list(msgs)
    while sum(tokens(m) for m in out) > budget and len(out) > 2:
        out.pop(1)                    # 从最旧的 user 开始删，不管结构
    return out


def blocks(history: list[dict]) -> list[list[dict]]:
    out, i = [], 0
    while i < len(history):
        m = history[i]
        if m["role"] == "assistant" and m.get("tool_calls"):
            ids = {c["id"] for c in m["tool_calls"]}
            block = [m]
            i += 1
            while i < len(history) and history[i]["role"] == "tool" and history[i]["tool_call_id"] in ids:
                block.append(history[i])
                i += 1
            out.append(block)         # 整块，不可拆
        else:
            out.append([m])
            i += 1
    return out


def trim_by_block(system: dict, history: list[dict], budget: int) -> list[dict]:
    out = blocks(history)
    while sum(tokens(m) for b in out for m in b) + tokens(system) > budget and len(out) > 1:
        out.pop(0)
    return [system] + [m for b in out for m in b]


if __name__ == "__main__":
    naive = trim_naive([SYSTEM] + HISTORY, budget=160)
    print("按条裁剪 roles:", [m["role"] for m in naive])
    print("  错误:", validate(naive))

    fixed = trim_by_block(SYSTEM, HISTORY, budget=160)
    print("\n按块裁剪 roles:", [m["role"] for m in fixed])
    print("  错误:", validate(fixed) or "无，协议合法")
    print("  保留了最后一条 user:", fixed[-1]["content"])
    print("\n结论：tool_calls 与结果是不可分割的块；裁剪单位必须是块，不是消息条数")
```

**追问一**：把旧的 `tool` 结果改写成一条 `user` 文本（"之前查到订单已支付"）为什么也不行？

→ 解析：协议上合法（不再有孤儿 tool），但语义上破坏了模型的"工具—结果"因果链：它会以为这是**用户说的话**，从而降低对工具可信度的判断，甚至在下一轮重复调用同一工具；更糟的是改写时容易把结构化字段（金额、状态）压成自然语言，精度丢失。要省 token，正确做法是把整块（调用 + 结果）压成一条 `assistant` 摘要，并标注"以下为历史摘要"，保持"这是助手自己说过的话"的语义。

**追问二**：如果模型一次返回多个并行 tool_calls，裁剪要注意什么？

→ 解析：一个 `assistant` 携带 N 个 `tool_call_id` 时，**N 个结果必须全部到齐**才能进入下一轮；只保留其中一部分同样 400。裁剪的块定义为"该 assistant + 它声明的全部 id 对应的 tool 消息"，缺任何一条都算块不完整。另外并行调用的结果消息顺序通常要与 `tool_calls` 顺序一致（部分供应商强制），裁剪/重排时不要打乱。若某个工具调用超时，正确的做法是补一条 `tool` 消息说明失败（`is_error: true`），而不是删掉它——删了就是悬空调用。
