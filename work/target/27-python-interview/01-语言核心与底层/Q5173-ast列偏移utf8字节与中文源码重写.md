---
title: "[Q5173] AST 列偏移是 UTF-8 字节：中文源码重写错位事故"
date: 2026-11-23
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5173 · AST 列偏移是 UTF-8 字节：中文源码重写错位事故

难度：P6-P7 ｜ 标签：ast、col_offset、UTF-8、codemod、源码重写

**问**：写了一个 codemod，用 `src[node.col_offset:node.end_col_offset]` 截出表达式再替换。英文仓库一切正常，上了含中文文案的仓库后批量改坏代码——切出来的片段多/少了几个字符，替换后语法错误。AST 的位置信息到底以什么为单位？`ast.get_source_segment()` 为什么不会错？多行表达式的 `lineno/end_lineno` 又该怎么用？与 Q5125（ast 版本演进）、Q473（最小 linter）的边界在哪？

**答**：
结论：`lineno` 从 1 开始，`col_offset/end_col_offset` 是**该行内的 UTF-8 字节偏移**，不是 Unicode 字符偏移。CPython 的解析器工作在 UTF-8 缓冲区上，位置信息直接来自 tokenizer 的字节计数；源码里出现中文、emoji 时，一个字符占 3~4 字节，用 `str` 切片就会错位。`ast.get_source_segment(src, node)` 内部按行取源码、再按字节偏移解码，所以它是对的；自己切片的正确做法是先 `src.encode("utf-8")`，切完再 `decode`，且偏移是**行内**的，多行节点要先用 `splitlines(keepends=True)` 拼回绝对位置。Q5125 讲 AST 节点结构跨版本演进（`ast.Num` 移除、`end_col_offset` 的来历），Q473 讲 NodeVisitor 怎么写 lint；本题专攻"位置信息的编码单位"这一类重写事故。

取舍：能不动源码字符串就不动——优先用 `ast.unparse()` 重新生成整棵树，代价是注释、空行、引号风格全丢（Q5125 已说明它是反编译不是还原）。必须做最小 diff 时，用 `get_source_segment` 取原文、用字节偏移做拼接，并在替换后立刻 `ast.parse` 验证；跨行替换还要处理 `end_lineno` 与行尾换行符，别把下一行吞掉。

实战：事故形态是"批量给函数加类型注解"的脚本在中文注释/中文字符串文件里把代码切坏，CI 报 `SyntaxError`，但 diff 里看不出规律。下面用一行含中文的源码复现：按字符切片会多带一个换行（把 6 个 UTF-8 字节当成 6 个字符），按字节切片与 `get_source_segment` 一致；随后用字节级拼接完成一次等长替换并重新解析。

```python
import ast

src = 'total = "中文" + suffix\n'
tree = ast.parse(src)
node = tree.body[0].value                    # BinOp

print("col_offset/end =", node.col_offset, node.end_col_offset)
print("按字符切片 :", repr(src[node.col_offset:node.end_col_offset]))
print("按字节切片 :", repr(src.encode()[node.col_offset:node.end_col_offset].decode()))
print("官方片段   :", repr(ast.get_source_segment(src, node)))

new_text = '"英文"'
raw = src.encode()
patched = raw[:node.left.col_offset] + new_text.encode() + raw[node.left.end_col_offset:]
print("字节级重写 :", patched.decode().strip())

try:
    ast.parse(patched.decode())
    print("重写后可解析: True")
except SyntaxError as e:
    print("重写后语法错误:", e)
```

**追问一**：为什么 `get_source_segment` 能处理多行节点，而简单切片不能？——多行节点的 `col_offset` 是起始行的列、`end_col_offset` 是结束行的列，两个偏移不在同一坐标系里；`get_source_segment` 会按 `lineno..end_lineno` 取出整段行、把中间行完整保留、首尾行按列裁切，再统一解码。自己实现时等价于用 `splitlines(keepends=True)` 建行偏移表，把 `(行, 列)` 映射成绝对字节位置。

**追问二**：为什么 `ast.unparse` 重写后语义可能变？——它按 AST 重新生成最小合法源码，注释、`# type: ignore`、字符串引号/转义风格、隐式字符串拼接、括号换行都会丢或改写；对依赖 `__doc__` 的 docstring 一般能保留（作为常量），但 `# noqa` 这类工具指令会消失。安全做法是"能局部替换就局部替换"，整树 unparse 只用于生成新文件或格式化，不要用于原地 codemod。

## 背诵要点
- `lineno` 1-based；`col_offset/end_col_offset` 是行内 **UTF-8 字节**偏移，不是字符偏移。
- 切片重写要 `encode("utf-8")` 后用字节偏移，或多行场景用 `ast.get_source_segment`；偏移是行内坐标。
- `ast.unparse` 会丢注释/格式，是反编译不是还原；重写后必须 `ast.parse` 复验。

## 复盘追问
- 英文仓库正常的 codemod 在中文仓库切坏代码，如何从偏移单位解释并给出两种修复？（`encode/decode` 字节切、`get_source_segment`，多行需行表）
- 为什么"用 `ast.unparse` 重写整个文件"不适合原地 codemod？（注释/指令/风格丢失，diff 巨大，语义可能变化）
