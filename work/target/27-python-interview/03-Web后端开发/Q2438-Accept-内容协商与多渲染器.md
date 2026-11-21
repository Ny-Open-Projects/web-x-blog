---
title: [Q2438] Accept 内容协商与多渲染器
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2438 · Accept 内容协商与多渲染器

> 难度:★★★☆ | 标签:内容协商, HTTP, 406

**问**:同一个资源怎么同时支持 HTML 与 JSON 两种出口?Accept 头的 q 值怎么参与决策?

**答**:内容协商的三件套是:解析 Accept 头为"类型加 q 值"列表并按 q 降序稳定排序、维护渲染器注册表(类型到渲染函数)、逐项匹配取第一个可用的类型,通配符 */* 映射到默认渲染器。q 值是客户端偏好权重,1.0 默认,q=0 是明确拒绝——客户端说 text/csv;q=0, application/json 时即使 csv 排在前面也必须跳过。没有任何可接受类型时返回 406 Not Acceptable,并附上服务端支持的类型列表,让客户端能自我修正。设计要点:默认渲染器要选对机器最友好的 JSON;渲染器是纯函数,吃数据吐字节,新增 XML 就是注册一项;HTML 出口要转义,防止数据里的尖括号变成 XSS。

```python
# file: code/03_Web后端开发/q2438_content_negotiation.py
"""Accept 内容协商与多渲染器: HTML 与 JSON 双出口(纯标准库)。"""
import json


def parse_accept(header):
    """解析 Accept 头为 (mime, q) 列表, q 降序稳定排序, 通配在同级靠后。"""
    entries = []
    for part in header.split(","):
        tokens = part.strip().split(";")
        mime = tokens[0].strip().lower()
        if not mime:
            continue
        q = 1.0
        for param in tokens[1:]:
            key, _, value = param.strip().partition("=")
            if key == "q":
                q = float(value)
        entries.append((mime, q))
    entries.sort(key=lambda e: (-e[1], e[0] == "*/*"))
    return entries


def negotiate(accept_header, renderers, default):
    """返回选中的渲染器名; 无可接受类型返回 None, 对应 406。"""
    for mime, q in parse_accept(accept_header):
        if q <= 0:
            continue                                  # q=0 表示明确拒绝
        if mime in renderers:
            return mime
        if mime == "*/*":
            return default
    return None


RENDERERS = {
    "application/json": lambda data: json.dumps(data, ensure_ascii=False).encode(),
    "text/html": lambda data: "<h1>{}</h1><p>{}</p>".format(
        data["title"], data["summary"]).encode(),
}

item = {"title": "周报", "summary": "本周完成了限流中间件"}

for accept in ["text/html", "application/json", "text/html;q=0.8, application/json;q=0.9",
               "*/*", "text/csv", "text/csv;q=0, application/json"]:
    chosen = negotiate(accept, RENDERERS, default="application/json")
    if chosen is None:
        print("{:48s} -> 406 Not Acceptable".format(accept))
        continue
    body = RENDERERS[chosen](item)
    print("{:48s} -> {} | {}".format(accept, chosen, body[:28]))

assert negotiate("text/html", RENDERERS, "application/json") == "text/html"
assert negotiate("application/json", RENDERERS, "text/html") == "application/json"
assert negotiate("*/*", RENDERERS, "application/json") == "application/json"
assert negotiate("text/csv", RENDERERS, "application/json") is None
assert negotiate("text/csv;q=0, application/json", RENDERERS, "application/json") == "application/json"
print("要点: 协商按 q 值降序匹配, q=0 是明确拒绝, 通配符是兜底; "
      "匹配失败回 406 并附 Accept-Post 之类的可用类型提示")
```

**追问**:
- 406 还是返回默认格式?——规范派回 406,实用派回默认并带 Warning;关键是全服务一致并写进 API 文档。
- URL 后缀 .json 与内容协商什么关系?——后缀是协商的简化,两者并存时要定优先级,通常显式 Accept 优先于后缀。
