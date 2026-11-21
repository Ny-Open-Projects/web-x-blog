---
title: [Q397] str 与 bytes:编码处理的正确姿势
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q397 · str 与 bytes:编码处理的正确姿势

> 难度:★★☆ | 标签:bytes, 编码, Unicode

**问**:`str` 和 `bytes` 的边界在哪?线上中文乱码一般怎么排查?

**答**:str 是 Unicode 码点序列,bytes 是原始字节;所有 IO(文件、socket、HTTP)里都是 bytes,进出都要显式编解码(`encode`/`decode`)。排查乱码三板斧:①确认数据的真实编码(看响应头 charset/文件 BOM/抓包);②`bytes.decode("utf-8", errors="strict")` 让错误早暴露,不要 `errors="ignore"` 吞掉;③Windows 文件默认 GBK 是重灾区,读写一律显式 `encoding="utf-8"`。协议处理时记住:`b"abc"[0]` 是 int,切片才是 bytes。

```python
# file: code/02_并发与网络工程/q397_str_bytes.py
"""str 与 bytes 的转换与陷阱。"""
if __name__ == "__main__":
    s = "中文ABC"
    b = s.encode("utf-8")
    print("bytes:", b, "长度:", len(b), "(utf-8 中文 3 字节)")
    print("解码还原:", b.decode("utf-8"))

    # 陷阱 1: 索引类型不同
    print("b[0] =", b[0], type(b[0]).__name__, "| b[0:1] =", b[0:1])

    # 陷阱 2: GBK 与 UTF-8 互不兼容
    gbk = s.encode("gbk")
    print("gbk 字节:", gbk)
    try:
        gbk.decode("utf-8")
    except UnicodeDecodeError as e:
        print("乱码根因:", e)

    # 陷阱 3: errors 选项——strict 暴露问题, replace 保流程
    print("replace:", gbk.decode("utf-8", errors="replace"))
    print("十六进制:", b.hex())

    # 标准库 chardet 替代: 只能启发式判断, 生产用第三方 charset detection
    import codecs
    print("BOM 检测:", codecs.BOM_UTF8 == b"\xef\xbb\xbf")
```

**追问**:
- `UnicodeEncodeError` 和 `UnicodeDecodeError` 分别发生在哪?encode 是 str→bytes(如字符串里含 surrogate 码点),decode 是 bytes→str(字节流不符合目标编码);前者少见后者是乱码主因。
- ASCII 字符串拼接 bytes 为什么报错?Python 3 严禁 str 和 bytes 混算,必须显式 `.encode()` 或 `.decode()`,这是刻意的语言设计。
