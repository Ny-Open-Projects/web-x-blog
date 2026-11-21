---
title: [Q2426] Transfer-Encoding 与 Content-Length 的冲突裁决
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2426 · Transfer-Encoding 与 Content-Length 的冲突裁决

> 难度:★★★★ | 标签:HTTP, 报文分帧, 请求走私

**问**:同一个请求里同时出现 Transfer-Encoding: chunked 和 Content-Length,服务端、代理、客户端各自应该怎么处理?为什么这件事值得单独记?

**答**:这是 RFC 7230 明确规定的冲突场景,也是请求走私攻击的经典入口,值得背下三句话。第一,发送端不得同时携带两个头,客户端库发现双头并存应当报错或剥离 Content-Length 再发。第二,接收端 TE 优先:只要存在有效的 Transfer-Encoding,就按 chunked 规则读到 0 长度块为止,Content-Length 被整体忽略,它只是潜在的混淆向量。第三,中间人代理必须删除 Content-Length 再转发——如果前置代理信 CL、后端信 TE,两边对报文边界的理解就会分叉,多出来的字节被后端解析成第二个请求,这就是 CL.TE 走私。附带两个要点:TE 的值里最后一个必须是 chunked 才算有效分帧;HTTP/2 报文里根本没有这两个头,做协议转换的网关必须剥掉入站头再按 H1 规则重新分帧,透传等于制造歧义报文。

```python
# file: code/03_Web后端开发/q2426_te_cl_conflict.py
"""Transfer-Encoding 与 Content-Length 冲突时的裁决规则(纯标准库)。"""


def parse_framing(header_lines):
    """从原始头行中提取帧信息, 返回 (te_present, chunked, cl_value)。"""
    te, chunked, cl = False, False, None
    for line in header_lines:
        name, _, value = line.partition(":")
        name = name.strip().lower()
        value = value.strip()
        if name == "transfer-encoding":
            te = True
            if "chunked" in value.lower():
                chunked = True
        elif name == "content-length":
            cl = value
    return te, chunked, cl


def decide(role, te_present, cl_present):
    """发送端禁止并存; 接收端 TE 优先; 中间人必须删除 CL 再转发。"""
    if te_present and cl_present:
        if role == "sender":
            return "拒绝发送", "客户端库应报错或剥离 Content-Length 再发"
        if role == "proxy":
            return "删CL转发", "按 TE 分帧并移除 CL, 防止下游解析分歧"
        return "TE优先", "RFC 7230: 存在 TE 时忽略 CL, CL 只是混淆向量"
    if te_present:
        return "TE分帧", "按 chunked 规则读到 0 长度块结束"
    if cl_present:
        return "CL定长", "按 Content-Length 读取指定字节数"
    return "读到关闭", "无帧信息, 只能读到连接关闭为止"


for role, te, cl in [("sender", True, True), ("proxy", True, True),
                     ("server", True, True), ("server", True, False),
                     ("server", False, True), ("server", False, False)]:
    action, why = decide(role, te, cl)
    print("{:6s} TE={:<5} CL={:<4} -> {:6s} | {}".format(role, te, str(cl), action, why))

lines = ["Transfer-Encoding: chunked", "Content-Length: 6", "X-Other: v"]
te, chunked, cl = parse_framing(lines)
assert te and chunked and cl == "6"
assert decide("server", te, cl)[0] == "TE优先"
assert decide("proxy", te, cl)[0] == "删CL转发"
print("要点: 双头并存是请求走私的经典入口, 规则三句话: 发送端不发, 接收端 TE 优先, 中间人删 CL")
```

**追问**:
- 为什么走私攻击专挑双头并存的报文?——两个解析器各信一个头,对"报文在哪里结束"得出不同答案,差值被当作下一个请求的开头。
- 服务端拿到双头请求最稳妥的动作是什么?——按 TE 解析后直接以 400 拒绝并记录来源,歧义报文不值得继续处理。
