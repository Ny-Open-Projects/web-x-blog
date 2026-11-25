---
title: "[Q5186] csv 的 newline 契约：引号内换行被折叠与 BOM 污染表头"
date: 2026-11-23
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5186 · csv 的 newline 契约：引号内换行被折叠与 BOM 污染表头

难度：P6 ｜ 标签：csv、newline、通用换行、BOM、utf-8-sig

**问**：用 `csv.reader(open(path))` 读一个字段里带换行的 CSV，读出来的内容和原文对不上（`\r\n` 变成了 `\n`），导出再导入就更离谱。文档为什么强制 `newline=""`？这个参数到底关掉了什么？另一个高频问题是 Excel 导出的文件第一列表头变成 `\ufeffid`，为什么 `strip()` 也去不掉？

**答**：
结论：csv 模块需要**原样看到**行结束符才能判断"这一行结束了吗"和"这个换行在引号里吗"。`open()` 默认 `newline=None` 会开启通用换行转换，把 `\r\n`、`\r` 统一翻译成 `\n`——这一步发生在 csv 解析器之前，引号内的 `\r\n` 也被改写，字段内容永久丢失原始字节。`newline=""` 关掉转换（读时不翻译、写时不替换），把换行交给 csv 自己处理，这就是文档要求它的原因。BOM 则是另一码事：Excel 写出的 UTF-8 文件开头有三个字节 `EF BB BF`，用 `utf-8` 解码会得到一个 U+FEFF 字符留在第一个字段里，`strip()` 默认不去掉它（它不是空白），必须 `lstrip("\ufeff")` 或直接用 `encoding="utf-8-sig"` 读。

取舍：`utf-8-sig` 读是幂等的（有 BOM 去掉、没有也不报错），适合"可能来自 Excel"的输入；写的时候要不要 BOM 取决于消费方——给 Excel 双击打开就写 BOM，给程序/程序间接口就别写（很多解析器会把 BOM 当数据）。检测 BOM 不要靠 `open`，直接读前 3 个字节最可靠。

实战：事故形态是"运营用 Excel 维护的配置表导进系统，表头字段名永远匹配不上，日志里看着是 `id` 但 `dict` 里 key 是 `id`"——肉眼不可见的 U+FEFF。另一类是"CSV 里有多行地址，导出再导入后行数变多/变少"，就是通用换行把引号内换行折平后 csv 重新切分。下面用原始字节构造文件，两种读法对比，再加 BOM 场景。

```python
import csv
import io
import os
import tempfile

raw = 'id,note\r\n1,"line1\r\nline2"\r\n'.encode("utf-8")

d = tempfile.mkdtemp()
p = os.path.join(d, "a.csv")
with open(p, "wb") as f:
    f.write(raw)

# 1) 默认 newline=None：通用换行把引号内的 \r\n 也折成 \n，字段内容被改写
with open(p, encoding="utf-8") as f:
    rows_default = list(csv.reader(f))
print("newline=None :", repr(rows_default[1][1]))

# 2) 契约写法 newline=""：换行原样交给 csv 解析器
with open(p, encoding="utf-8", newline="") as f:
    rows_ok = list(csv.reader(f))
print('newline=""   :', repr(rows_ok[1][1]))
print("内容一致:", rows_default == rows_ok)

# 3) 带 BOM 的文件：用 utf-8 读，第一列表头被污染
bom = os.path.join(d, "bom.csv")
with open(bom, "wb") as f:
    f.write(b"\xef\xbb\xbf" + raw)
with open(bom, encoding="utf-8", newline="") as f:
    header_plain = next(csv.reader(f))[0]
with open(bom, encoding="utf-8-sig", newline="") as f:
    header_sig = next(csv.reader(f))[0]
print("utf-8 读表头:", repr(header_plain), "==", repr("id"), "?", header_plain == "id")
print("utf-8-sig   :", repr(header_sig), "==", repr("id"), "?", header_sig == "id")

buf = io.StringIO(newline="")
csv.writer(buf).writerow(["a", "b\r\nc"])
print("写出字节:", buf.getvalue().encode("utf-8"))
```

**追问一**：`io.StringIO` 也要 `newline=""` 吗？—— 要。否则写出时同样会被换行转换，测试里用 StringIO 复现线上格式问题时这一步最容易漏（本例若不传 `newline=""`，引号内的 `\r\n` 会变成 `\n`，与线上文件不一致，测试就失真了）。

**追问二**：为什么 Windows 上不加 `newline=""` 写出的文件会变成 `\r\r\n`？—— csv 自己写 `\r\n`，文本层 `newline=None` 又把其中的 `\n` 翻译成 `os.linesep`（`\r\n`），叠加成 `\r\r\n`，Excel 打开会多出空行。`newline=""` 让文本层不做翻译，csv 写什么就是什么，跨平台字节一致。

## 背诵要点
- csv 必须拿到原样换行：读写都用 `newline=""`；`newline=None` 的通用换行会改写引号内 `\r\n`。
- Excel 的 BOM 会变成第一个字段里的 U+FEFF；`strip()` 去不掉，用 `utf-8-sig` 或 `lstrip("\ufeff")`。
- 写 BOM 看消费方（Excel 要、程序间不要）；Windows 上漏 `newline=""` 会写出 `\r\r\n`。

## 复盘追问
- 带引号换行的 CSV 导出再导入后行数变了，如何用通用换行与 csv 契约解释？（转换发生在解析器之前、`\r\n`→`\n`）
- 表头肉眼是 `id` 却匹配不上，如何定位并根治？（U+FEFF、utf-8-sig、BOM 字节检测）
