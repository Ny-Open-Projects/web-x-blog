---
title: "[Q7716] stop 序列出现在代码里：输出被腰斩"
date: 2026-11-23
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7716 · stop 序列出现在代码里：输出被腰斩

难度：P6 ｜ 标签：stop sequence、截断、结构化输出、事故复盘

基线：Python 3.12；纯 Python 模拟停止序列的截断行为。

**问**：代码助手用 `stop=["三个反引号"]` 防止模型输出多余的 markdown 围栏。某天用户让模型"写一个包含 markdown 代码块示例的 Python 函数"，模型输出到函数中间就停了，JSON 参数也没闭合，前端报解析错误。stop 序列为什么会在正常内容里触发？该怎么设？

**答**：
- **结论**：`stop` 是**字面字符串匹配**，只要生成内容里出现该串就立即停止，不管它出现在代码块、字符串字面量还是 JSON 值里。用三个反引号作为 stop，在"模型本来就要输出代码围栏"的任务里必然误伤。更隐蔽的是 `stop=["\n\n"]` 会切断正常段落，`stop=["}"]` 会切掉 JSON 的闭合括号。
- **取舍**：stop 适合**对话边界**（如 `"\nUser:"`、`"<|im_end|>"`）这类不会出现在正文里的标记；对代码/JSON 任务，应该用**结构化输出约束**（JSON Schema/语法约束解码）或让模型自然结束，而不是靠 stop 截断。停止序列越短、越常见，误伤概率越高。
- **实战**：① 代码任务不要用反引号/`}` 这类结构字符做 stop；② 用供应商的特殊结束 token 或对话角色标记；③ 即使设了 stop，也要校验 `finish_reason` 与输出完整性，截断要能识别并重试；④ 把 stop 配置纳入按任务分组的配置，不要全局一套。

```python
def generate(tokens: list[str], stop: list[str]) -> tuple[str, str]:
    out = []
    for tok in tokens:
        out.append(tok)
        text = "".join(out)
        if any(text.endswith(s) for s in stop):
            return text[:-len(next(s for s in stop if text.endswith(s)))], "stop"
    return "".join(out), "eos"


if __name__ == "__main__":
    fence = chr(96) * 3
    tokens = list("示例：" + fence + 'python\nprint("hi")\n' + fence + "\n以上是代码。")
    truncated, reason = generate(tokens, [fence])
    print("stop=[fence] ->", repr(truncated), reason)
    truncated2, reason2 = generate(tokens, ["\nUser:"])
    print("stop=[\\nUser:] -> 长度", len(truncated2), reason2)
    print("结论：结构字符做 stop 会腰斩正文，代码任务应依赖结构化约束")
```

**追问一**：`finish_reason=stop` 和 `finish_reason=length` 在处理上有什么不同？
→ 解析：`stop` 表示命中了停止序列或自然结束，内容可能是完整的，也可能是被 stop 误截的；`length` 表示达到 `max_tokens`，内容一定不完整，必须重试或续写。两者都不能直接信任，要结合内容校验（JSON 能否解析、括号是否闭合）。

**追问二**：为什么"让模型输出 JSON 后用 stop 截取第一个 `}`"不可靠？
→ 解析：JSON 可以嵌套，第一个 `}` 可能只是内层对象的结束；字符串值里也可能出现 `}`。按字符截取会破坏结构。正确做法是解析完整 JSON，或用语法约束解码保证输出合法。
