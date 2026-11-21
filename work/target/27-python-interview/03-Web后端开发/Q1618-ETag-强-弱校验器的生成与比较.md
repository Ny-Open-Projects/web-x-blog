---
title: [Q1618] ETag 强/弱校验器的生成与比较
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1618 · ETag 强/弱校验器的生成与比较

> 难度:★★☆☆ | 标签:HTTP 缓存, ETag

**问**:ETag 前面的 W/ 是什么意思?强校验器和弱校验器各自适用什么场景?

**答**:强校验器保证字节级一致(同一资源的每次表示完全相同),适合 If-Match 乐观锁与断点续传的 If-Range;弱校验器只保证语义等价(渲染结果相同但字节可能不同,比如页面里带时间戳),只适合 If-None-Match 这类内容变没变的协商缓存判定。生成策略上,内容哈希 sha256 天然是强标签,mtime 加 size 组合(类似 Nginx 的 W/ 前缀格式)是典型弱标签。比较语义两条:强比较要求双方都是强标签且完全相等;弱比较忽略 W/ 前缀只比标签本体。用错比较语义,乐观锁就会放过字节级差异。

```python
# file: code/03_Web后端开发/q1618_etag_validators.py
"""ETag 强/弱校验器: 生成策略与两种比较语义(纯标准库)。"""
import hashlib


def strong_etag(body):
    """内容哈希生成强标签: 字节级一致才相等。"""
    return '"' + hashlib.sha256(body).hexdigest()[:32] + '"'


def weak_etag(mtime, size):
    """mtime+size 生成弱标签: 语义等价即可, 类似 Nginx 的 W/"mtime-size"。"""
    return 'W/"%x-%x"' % (mtime, size)


def strip_weak(tag):
    return tag[2:] if tag.startswith("W/") else tag


def strong_eq(a, b):
    """强比较: 都必须是强标签且完全一致。"""
    return not a.startswith("W/") and not b.startswith("W/") and a == b


def weak_eq(a, b):
    """弱比较: 忽略 W/ 前缀, 只比标签本体。"""
    return strip_weak(a) == strip_weak(b)


e1 = strong_etag(b"hello")
print("强标签:", e1)
print("同内容重算一致:", e1 == strong_etag(b"hello"), "强比较:", strong_eq(e1, e1))
w1 = weak_etag(1730000000, 5)
plain = '"%x-%x"' % (1730000000, 5)
print("弱标签:", w1, "与无前缀版本弱比较:", weak_eq(w1, plain), "但强比较:", strong_eq(w1, plain))
w2 = weak_etag(1730000999, 5)
print("mtime 变了:", w2, "弱比较:", weak_eq(w1, w2))
print("规则: If-None-Match 用弱比较, If-Match 与 If-Range 必须强比较")
```

**追问**:
- 强标签能当弱标签用吗?——能,强蕴含弱;反之不行,If-Match 收到弱标签要直接拒绝。
- 大文件每次算哈希太贵怎么办?——不可变文件用内容哈希,可变文件用 mtime 加 size 的弱标签,Nginx 就是这个权衡。
