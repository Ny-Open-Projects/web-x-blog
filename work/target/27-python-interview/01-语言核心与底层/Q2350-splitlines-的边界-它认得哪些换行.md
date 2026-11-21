---
title: [Q2350] splitlines 的边界:它认得哪些换行
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2350 · splitlines 的边界:它认得哪些换行

> 难度:★★★☆☆ | 标签:splitlines, 换行, 文本处理

**问**:split("\n") 和 splitlines() 差在哪?处理跨平台文本该用哪个?

**答**:splitlines 认得一整套 Unicode 换行界符:\n、\r、\r\n 之外还有 \v、\f、\x85(Next Line)、\u2028(Line Separator)、\u2029(Paragraph Separator),把文本按「行」的语义切分;split("\n") 只认一个字面量,遇到 \r\n 会留下尾部 \r,遇到旧 Mac 的 \r 更是完全不切。第二个关键差异在结尾: "a\nb\n".split("\n") 产生空尾行 ["a", "b", ""],splitlines 不产生——解析表格文本时 splitlines 更干净。需要保留行尾符时用 `splitlines(keepends=True)`,便于写「重组后与原文完全一致」的处理器。反过来,在确定只有 \n 的场合(程序内部生成的数据),split 更快也更可预测。读外部文件时还有第三条路:文件对象按 universal newlines 直接迭代行,连 \r\n 都已归一成 \n。

```python
# file: code/01_语言核心与底层/q2350_splitlines.py
"""splitlines 的边界:识别哪些换行、行尾空行与 split 的差异。"""

if __name__ == "__main__":
    text = "a\nb\r\nc\rd\x85e\u2028f"
    print("转义视图:", text.encode("unicode_escape"))
    print("splitlines:", text.splitlines())
    print("split('\\n'):", text.split("\n"))
    print("keepends:", text.splitlines(keepends=True))

    nl = "a\nb\n"
    print("splitlines 无空尾行:", nl.splitlines())
    print("split 有空尾行:", nl.split("\n"))

    body = "姓名,年龄\n张三,20\n李四,30\n"
    rows = [line.split(",") for line in body.splitlines() if line]
    print("解析结果:", rows)
```

**追问**:1) \x85 和 \u2028 为什么危险?——它们是合法换行界符但肉眼不可见,来自 EBCDIC 与某些编辑器;按 split("\n") 解析外部文本时会把多行粘成一行,splitlines 则按语义切开。2) splitlines 与 split 的语义差?——splitlines 认全部换行界符(\n \r \r\n \v \f \x1c-\x1e \x85 \u2028 \u2029)且可 keepends;split("\n") 只认一个;跨平台文本要用 splitlines。3) 与 universal newlines 的配合?——文件读时 text 模式已把 \r\n 归一为 \n;网络协议字节流要先 decode 再 splitlines。4) 生产陷阱?——解析外部(Windows/编辑器)文件用 split("\n") 粘行;行计数与真实行数不一致;按行数断言的测试遇到隐形换行失败。
