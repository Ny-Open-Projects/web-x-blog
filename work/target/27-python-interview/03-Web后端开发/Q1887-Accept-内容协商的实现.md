---
title: [Q1887] Accept 内容协商的实现
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1887 · Accept 内容协商的实现

> 难度:★★☆☆ | 标签:HTTP, 内容协商

**问**:让我手写一个 Accept 头的内容协商,要考虑哪些规则?

**答**:解析 Accept:逗号分隔 media-range,分号参数里 q 取 0 到 1 的权重,缺省 1.0;q=0 是显式拒绝,直接从候选剔除。匹配按两级排序:先按 q 降序,同权重下按特异度降序,type/subtype 高于 type/* 高于 */*。服务端遍历候选表示,第一个命中范围者胜出;全部不命中返回 406 Not Acceptable,并在响应里说明可选表示,而不是静默回默认格式。工程细节:q 值解析要容忍格式错误(非法 q 回退 1.0),匹配大小写不敏感;协商结果必须同步写 Vary: Accept,否则缓存会串档。DRF 的 Renderer、FastAPI 的 response_class 都是这个逻辑的封装,手写一遍才能真正理解 406 的产生时机。

```python
# file: code/03_Web后端开发/q1887_accept_negotiation.py
"""Accept 内容协商: q 权重解析、特异度排序与 406 协商失败(纯标准库)。"""


def parse_accept(header):
    """解析 Accept 头, 返回按 q 降序、特异度降序的 [(type, subtype, q)]。

    特异度: type/subtype 高于 type/* 高于 */*; 同 q 下更特异者胜出。
    q=0 表示显式拒绝, 直接丢弃。
    """
    entries = []
    for part in header.split(","):
        part = part.strip()
        if not part:
            continue
        bits = [b.strip() for b in part.split(";")]
        media = bits[0]
        if "/" not in media:
            continue
        atype, asub = media.split("/", 1)
        q = 1.0
        for param in bits[1:]:
            if param.startswith("q="):
                try:
                    q = float(param[2:])
                except ValueError:
                    q = 1.0
        if q > 0:
            specificity = 2 if asub != "*" else (1 if atype != "*" else 0)
            entries.append((atype.lower(), asub.lower(), q, specificity))
    # q 降序, 再按特异度降序; 稳定排序保持原始顺序
    entries.sort(key=lambda e: (-e[2], -e[3]))
    return [(t, s, q) for t, s, q, _ in entries]


def negotiate(accept_header, available):
    """从可用表示中选出 Accept 最想要的; 全不匹配返回 None 由调用方转 406。"""
    prefs = parse_accept(accept_header)
    for atype, asub, q in prefs:
        for mime in available:
            mtype, msub = mime.lower().split("/", 1)
            type_ok = atype == "*" or atype == mtype
            sub_ok = asub == "*" or asub == msub
            if type_ok and sub_ok:
                return mime, q
    return None


AVAILABLE = ["application/json", "text/csv", "text/html"]

cases = [
    ("application/json", "application/json"),
    ("text/html;q=0.9, application/json;q=1.0", "application/json"),
    ("*/*", "application/json"),
    ("text/*", "text/csv"),
    ("application/xml;q=1.0", None),           # 无交集 -> 406
    ("text/html;q=0, application/json", "application/json"),  # q=0 显式拒绝
]
for header, expect in cases:
    result = negotiate(header, AVAILABLE)
    print("Accept: {:45s} -> {}".format(repr(header), result))
    assert (result is None) == (expect is None), header

print("协商失败时返回 406 Not Acceptable, 并在响应中给出可选表示清单")
```

**追问**:
- Accept 与 Accept-Encoding 的协商有什么不同?——前者选表示本身,后者选传输编码,都要分别写进 Vary。
- 406 和 415 的区别?——406 是服务端没有客户端想要的表示,415 是客户端发来的 payload 格式服务端不支持。
