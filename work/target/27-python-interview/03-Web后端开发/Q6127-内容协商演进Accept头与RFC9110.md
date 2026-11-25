---
title: [Q6127] 内容协商演进：Accept 头、q 值与 RFC 9110 语义
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6127 · 内容协商演进：Accept 头解析、q 值与 406 语义

> 难度:★★★★☆ | 标签:版本演进, 内容协商, HTTP

**问**:`Accept: text/html;q=0.9, application/json;q=0.8` 服务端该怎么选？406 状态码什么时候该返回、什么时候是"过度严谨"？Vary 头和协商的关系是什么？内容协商这些年怎么演进（RFC 2616→9110）？

**答**:结论：内容协商 = 服务端按 `Accept/Accept-Language/Accept-Encoding` 等头的**加权优先级（q 值，默认 1，0-1）**从多种表示里选一个。算法三步：a) 解析 `type/subtype;params;q`，q 默认 1；b) **最具体者胜**：精确匹配 > `type/*` > `*/*`，同具体度比 q；c) 无候选可匹配时 RFC 9110 允许两种立场——严格返回 **406 Not Acceptable**，或务实地返回默认表示（实践中后者更常见，406 往往只用于 API 明确声明多格式时）。演进要点：RFC 2616 的语法歧义（q 值越界、重复参数）在 **RFC 9110** 收紧；`Vary: Accept` 头是缓存正确性的命门——协商响应必须声明"按哪个头变化"，否则缓存会拿 JSON 喂 HTML 请求（缓存键不包含 Accept 的事故）；`Accept-Encoding` 的协商在 CDN/应用间双层进行，呼应压缩取舍（Q6011/Q6094）。实战：Python 里手写协商器要处理 q=0（明确拒绝）、`*/*` 兜底、参数匹配（`application/json;charset` 的 media type 参数不参与选择）；框架用户直接用 Starlette 的 `media_type` 协商或手写白名单，禁止把客户端 Accept 原样透传给下游再信任。

```python
def parse_accept(header: str):
    """解析 Accept 头 -> [(q, type, subtype, specificity)]。"""
    out = []
    for part in header.split(","):
        bits = part.strip().split(";")
        mt = bits[0].strip()
        q = 1.0
        for p in bits[1:]:
            k, _, v = p.strip().partition("=")
            if k == "q":
                try:
                    q = min(max(float(v), 0.0), 1.0)
                except ValueError:
                    q = 1.0
        t, _, s = mt.partition("/")
        spec = 2 if (t != "*" and s != "*") else (1 if s == "*" else 0)
        out.append((q, t or "*", s or "*", spec))
    return sorted(out, key=lambda x: (-x[3], -x[0]))    # 先具体度后 q

def negotiate(accept: str, available: list[str]):
    """返回 (选中的 media type 或 None, 是否 406)。q=0 的类型被明确排除。"""
    cands = parse_accept(accept)
    banned = set()
    for q, t, s, spec in cands:
        if q == 0:
            for av in available:                         # q=0: 明确拒绝该类型
                at, _, as_ = av.partition("/")
                if (t == "*" or t == at) and (s == "*" or s == as_):
                    banned.add(av)
    for q, t, s, spec in cands:
        if q == 0:
            continue
        for av in available:
            if av in banned:
                continue
            at, _, as_ = av.partition("/")
            if (t == "*" or t == at) and (s == "*" or s == as_):
                return av, False
    return None, True                                    # 严格派: 无可匹配 -> 406 不给内容

AVAIL = ["application/json", "text/html", "text/csv"]
cases = [
    "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",   # 浏览器
    "application/json",                                                  # API 客户端
    "text/csv;q=0.7, application/json;q=0.9",                            # csv 也接受
    "image/webp",                                                        # 无匹配
    "*/*",
    "application/json;q=0",                                              # q=0 明确拒绝 json
]
for a in cases:
    picked, is406 = negotiate(a, AVAIL)
    print(f"{a[:45]:47s} -> {picked or '406 Not Acceptable':22s} 406={is406}")

# ---- Vary: 协商响应的缓存正确性 ----
print("协商响应必须: Vary: Accept（缓存键纳入 Accept, 否则 JSON 喂给 HTML 请求）")
```

**追问一层**:为什么 q 值比较要"具体度优先"而不是纯 q 排序？（`text/*;q=0.9` 语义上仍不如 `text/html;q=0.8` 匹配意图——RFC 9110 规定更具体的 media range 优先，q 只在同具体度内比）。
**追问二层**:`Vary: *` 意味着什么？（响应按"一切"变化=禁止缓存复用；中间件动态响应常见误写，等价于放弃缓存——要具体列出参与协商的头）。
**追问三层**:proactive（头驱动）与 reactive（307 重定向到扩展名）协商怎么选？（API 用头驱动；面向人的文件导出用 reactive（加 `.csv` 后缀）更抗缓存与代理干扰）。

## 背诵要点
- 协商算法：解析 q（默认 1、q=0 拒绝）→ 最具体者胜（精确 > type/* > */*）→ 无匹配严格派 406 / 务实派默认表示。
- RFC 2616→9110 收紧语法与语义；协商响应必须 Vary 参与协商的头，Vary:* 等于禁缓存。
- 手写协商器别信透传的 Accept；白名单 + 默认表示是工程常态。

## 复盘追问
- 线上偶发"JSON 接口返回了 HTML"，从 Vary 缺失与代理缓存两个角度还原事故并给修复。
- 设计一个需要同时吐 JSON/CSV 的导出接口，协商、缓存、错误路径（406）各自怎么定？
