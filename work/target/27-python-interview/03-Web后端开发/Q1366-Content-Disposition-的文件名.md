---
title: [Q1366] Content-Disposition 的文件名注入
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1366 · Content-Disposition 的文件名注入

> 难度:★★ | 标签:HTTP 头, 文件安全

**问**:下载文件名来自用户输入,会有什么风险?怎么安全地放进响应头?

**答**:两类风险:**头注入**(文件名里带 CRLF 可以拆出额外响应头)和**编码与路径混淆**(引号、反斜杠破坏头结构,非 ASCII 乱码)。防御是先剥离 CR/LF/引号/路径分隔符,再用双字段写法:`filename="ascii 兜底"` 给老客户端,`filename*=UTF-8''percent-encoded` 给现代客户端按 RFC 5987 处理中文。同时响应加 `X-Content-Type-Options: nosniff`,Content-Type 按真实类型给,防止下载内容被浏览器嗅探执行。

```python
# file: code/03_Web后端开发/q1366_disposition.py
"""安全构造 Content-Disposition 文件名(纯标准库)。"""
from urllib.parse import quote


def content_disposition(name):
    # 剥离会造成头注入与结构破坏的字符
    cleaned = "".join(ch for ch in name if ch not in '\r\n"\\/')
    ascii_fallback = cleaned.encode("ascii", "ignore").decode() or "download"
    return (f'attachment; filename="{ascii_fallback}"; '
            f"filename*=UTF-8''{quote(cleaned)}")


print(content_disposition("月度报表 2026.xlsx"))
evil = 'a.txt"\r\nX-Injected: 1'
safe = content_disposition(evil)
print("恶意输入已消毒 ->", safe.replace("\r\n", "|"))
assert "\r" not in safe and "\n" not in safe
```

**追问**:
- 为什么还要 ascii 兜底?——老浏览器与部分代理不认 filename*,双字段保证兼容且非 ASCII 不乱码。
- 下载 HTML 要不要强制 attachment?——要,凡用户可控内容的下载都带 attachment,防同源渲染成页面偷 Cookie。
