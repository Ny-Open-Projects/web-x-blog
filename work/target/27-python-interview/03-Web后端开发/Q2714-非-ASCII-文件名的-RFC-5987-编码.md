---
title: [Q2714] 非 ASCII 文件名的 RFC 5987 编码
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2714 · 非 ASCII 文件名的 RFC 5987 编码

> 难度:★★★☆ | 标签:Content-Disposition, 编码, 下载

**问**:下载中文文件名的文件,浏览器显示乱码或下划线,Content-Disposition 该怎么写?

**答**:filename 头参数最早只支持 ASCII,非 ASCII 必须用 RFC 5987 的 filename* 扩展:`filename*=UTF-8''%E5%AD%A3%E5%BA%A6.pdf`,格式是 charset 后接两个单引号再接百分号编码,空格斜杠引号都不进 safe。兼容写法是两个都给:filename 填 ASCII 兜底名给老客户端,filename* 给现代浏览器,后者优先解析。三条安全纪律:CR/LF 出现在文件名里直接拒绝,防头注入;引号与反斜杠也走 filename* 路径,不塞进引号串;解析端优先 filename*、回退 filename,并按声明的 charset 解码。生成与解析要成对实现并做往返测试,只测生成不测解析的文件名功能一定在某个浏览器上翻车。

```python
# file: code/03_Web后端开发/q2714_rfc5987_filename.py
"""非 ASCII 文件名的 Content-Disposition 编码: RFC 5987 filename*(纯标准库)。"""
import re
from urllib.parse import quote, unquote


def content_disposition(filename, disposition="attachment"):
    """ASCII 安全名直接进 filename 引号串; 含非 ASCII 或特殊字符时补 filename*。

    filename* 按 RFC 5987 编码: charset''percent-encoded, 空格斜杠引号都不进 safe;
    filename 仍带一个 ASCII 兜底名, 给不认识 filename* 的老客户端。
    """
    if any(c in filename for c in "\r\n"):
        raise ValueError("非法文件名")
    if all(32 <= ord(c) < 127 for c in filename) and '"' not in filename and "\\" not in filename:
        return '%s; filename="%s"' % (disposition, filename)
    return '%s; filename="download"; filename*=UTF-8\'\'%s' % (disposition, quote(filename, safe=""))


def parse_filename(header):
    """优先解析 filename*, 拿不到再退 filename; 返回 (名字, 来源)。"""
    m = re.search(r"filename\*=([^']*)''([^;\s]+)", header)
    if m:
        return unquote(m.group(2)), m.group(1) or "UTF-8"
    m = re.search(r'filename="([^"]*)"', header)
    return (m.group(1), "ASCII") if m else (None, None)


h1 = content_disposition("report.pdf")
h2 = content_disposition("季度报告.pdf")
h3 = content_disposition('we"ird name.txt')
assert h1 == 'attachment; filename="report.pdf"', h1
assert parse_filename(h1) == ("report.pdf", "ASCII")
name, enc = parse_filename(h2)
assert name == "季度报告.pdf" and enc == "UTF-8", (name, enc)
name3, enc3 = parse_filename(h3)
assert name3 == 'we"ird name.txt' and enc3 == "UTF-8"
print("ASCII   :", h1)
print("中文    :", h2)
print("含引号  :", h3)
try:
    content_disposition("a\r\nb")
except ValueError as e:
    print("头注入拒绝:", e)
```

**追问**:
- 为什么不用 RFC 2047 的 =?UTF-8?= 形式?——那是邮件标题语法,浏览器对它在 Content-Disposition 里的支持混乱,5987 是唯一跨浏览器一致的方案。
- filename* 与 filename 同时存在时以谁为准?——现代浏览器以 filename* 为准,fallback 只给不认识 5987 的老客户端,两者内容可以不同。
