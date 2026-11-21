---
title: [Q1372] 缓存新鲜度的计算:解析 Cache-Control
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1372 · 缓存新鲜度的计算:解析 Cache-Control

> 难度:★★★ | 标签:HTTP 缓存, 中间件

**问**:自己写一个 HTTP 缓存层,怎么根据响应头和 age 判断"这条缓存还能不能直接用"?

**答**:把 Cache-Control 解析成指令字典,再按优先级判定:`no-store` 直接不存;`no-cache` 或 `must-revalidate` 且过期 → 必须协商验证;有 `max-age` 且 `age < max-age` → 新鲜直接用;过期但落在 `stale-while-revalidate` 窗口内 → 可先回旧值同时后台刷新;窗口外 → 回源。age 要累计响应头 Age 与本地滞留时间。注意指令值都是字符串,解析要防御缺省与非法值;这套判定和 CDN 行为一致,写对了对齐排查很有帮助。

```python
# file: code/03_Web后端开发/q1372_freshness.py
"""Cache-Control 解析与新鲜度判定(纯标准库)。"""


def parse_cache_control(header):
    directives = {}
    for part in header.split(","):
        part = part.strip()
        if not part:
            continue
        if "=" in part:
            key, _, value = part.partition("=")
            directives[key.strip()] = value.strip().strip('"')
        else:
            directives[part] = True
    return directives


def num(directives, key):
    value = directives.get(key)
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def cache_decision(directives, age):
    if directives.get("no-store"):
        return "do-not-store", 0
    if directives.get("no-cache"):
        return "revalidate-first", 0
    max_age = num(directives, "max-age")
    if age < max_age:
        return "fresh", max_age - age
    swr = num(directives, "stale-while-revalidate")
    if age < max_age + swr:
        return "serve-stale-then-refresh", max_age + swr - age
    return "refetch", 0


cases = [
    ("public, max-age=60", 30),
    ("public, max-age=60, stale-while-revalidate=300", 100),
    ("public, max-age=60, stale-while-revalidate=300", 500),
    ("no-cache", 0),
    ("no-store", 0),
]
for header, age in cases:
    print(f"{header:52s} age={age:3d} -> {cache_decision(parse_cache_control(header), age)}")
```

**追问**:
- max-age 缺省时按什么算?——回退到 Expires 与 Date 的差,再缺省按启发式(如 Last-Modified 距今 10%),生产建议总是显式给 max-age。
- 服务器时钟漂移影响吗?——age 按响应头的 Date 与请求时间差计算,时钟不准会整体偏移,NTP 是前提。
