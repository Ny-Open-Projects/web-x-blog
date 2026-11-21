---
title: [Q1869] inet_pton 解析校验:严格校验与 inet_aton 的宽容陷阱
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1869 · inet_pton 解析校验:严格校验与 inet_aton 的宽容陷阱

> 难度:★☆ | 标签:inet_pton, 输入校验, 安全

**问**:校验用户输入的 IP 地址,为什么必须用 inet_pton 而不是 inet_aton?

**答**:inet_pton 只接受规范形式:点分十进制四段、每段 0-255、不认前导八进制与十六进制,任何畸形都抛 OSError;inet_aton 为了兼容历史格式,三段式、八进制、十六进制都放行。

- 校验实验:256.1.1.1、1.2.3、五段、夹带空白全部被 inet_pton 拒绝;而 inet_aton 对 1.2.3、010.0.0.1、0x7f.1 全部放行,010.0.0.1 实际是 8.0.0.1——拿它做访问控制就是 SSRF 绕过;

- 平台差异要记住:BSD/Darwin 的 inet_pton 接受前导零(十进制语义),Linux glibc 拒绝,跨平台校验不能依赖这个边界;

- 工程用法:解析 X-Forwarded-For 时逐段 inet_pton,取第一个合法项,不合法的直接跳过。

IPv6 同理:inet_pton 校验规范形式,inet_ntop 输出规范形式,一来一回就归一化了。

```python
# file: code/02_并发与网络工程/q1869_inet_pton_check.py
# -*- coding: utf-8 -*-
"""inet_pton 解析校验: 严格解析拒绝畸形地址, inet_aton 的宽容是 SSRF 后门。

- inet_pton 只接受点分十进制的唯一规范形式, 多一位少一位一位超 255 都拒绝;
- inet_aton 兼容历史格式: 三段式、八进制、十六进制都能过, 用于校验是危险的;
- 校验用户输入的 IP(X-Forwarded-For 等)一律用 inet_pton, 先挑有效再进业务。
"""
import socket

V4_CASES = [
    ("127.0.0.1", True),
    ("8.8.8.8", True),
    ("256.1.1.1", False),          # 一段超 255, 各平台一致拒绝
    ("1.2.3", False),              # 只有三段
    ("1.2.3.4.5", False),          # 五段
    ("1 .2.3.4", False),           # 夹带空白
]
LEADING_ZERO = "01.2.3.4"          # 前导零: 平台差异点, 单独观察
V6_CASES = [
    ("::1", True),
    ("2001:db8::1", True),
    (":::", False),
    ("1:2:3:4:5:6:7:8:9", False),  # 九组
    ("12345::", False),            # 一组超 4 位十六进制
]


def strict_ip(s):
    """返回 (family, ip) 或 None, 只认规范形式。"""
    for fam in (socket.AF_INET, socket.AF_INET6):
        try:
            socket.inet_pton(fam, s)
            return fam, s
        except OSError:
            pass
    return None


def main():
    ok4 = []
    for s, expect in V4_CASES:
        got = strict_ip(s)
        ok4.append((got is not None) == expect)
        print("v4 %-10s -> %-5s 期望 %s" % (s, got is not None and "有效" or "拒绝", expect))
    assert all(ok4), "v4 校验规则必须全部符合预期"

    # 平台差异: BSD/Darwin 的 inet_pton 接受前导零(十进制语义), Linux glibc 拒绝
    if strict_ip(LEADING_ZERO):
        print("前导零 %s 本机被接受(BSD 实现), Linux 上会拒绝, 校验仍要防八进制歧义"
              % LEADING_ZERO)
    else:
        print("前导零 %s 本机被拒绝(严格实现)" % LEADING_ZERO)

    ok6 = []
    for s, expect in V6_CASES:
        got = strict_ip(s)
        ok6.append((got is not None) == expect)
        print("v6 %-18s -> %-5s 期望 %s" % (s, got is not None and "有效" or "拒绝", expect))
    assert all(ok6), "v6 校验规则必须全部符合预期"

    # 对照: inet_aton 的宽容是历史包袱, 校验场景禁用
    lenient = ["1.2.3", "010.0.0.1", "0x7f.1"]
    for s in lenient:
        raw = socket.inet_aton(s)              # 全部能过!
        print("inet_aton 接受 %-10s -> %s 字节" % (s, raw.hex()))

    # 工程用法: X-Forwarded-For 里挑第一个合法地址
    xff = "1.2.3, 10.0.0.1, ::1"
    picked = None
    for part in xff.split(","):
        picked = strict_ip(part.strip())
        if picked:
            break
    print("XFF 提取第一个合法地址:", picked)
    assert picked is not None and picked[1] == "10.0.0.1", \
        "1.2.3 不合法, 第一个合法项是 10.0.0.1"

    print("结论: 校验用 inet_pton 的严格, 解析历史数据才轮到 inet_aton")


if __name__ == "__main__":
    main()
```

**追问**:1) 前导零的歧义具体指什么?——早期实现把 010 当八进制(等于 8),现代实现有的当十进制;同一字符串在不同系统解析出不同地址,安全校验必须拒绝歧义输入而不是猜语义。2) inet_aton 的宽容格式各对应什么真实地址?——1.2.3=1.2.0.3(a.b.c 补齐);010.0.0.1=8.0.0.1(八进制);0x7f.1=127.0.0.1(十六进制);这些「历史兼容」让用户输入的字符串语义与直觉完全不同——校验层必须拒绝歧义而不是猜。3) 前导零的平台差异怎么写健壮代码?——BSD/Darwin 的 inet_pton 接受前导零(十进制),glibc 拒绝;跨平台校验不能依赖这个边界,自己加「拒绝前导零」的显式检查(正则或字符串判断)——「平台差异边界」永远不进安全逻辑。4) 生产陷阱?——访问控制用 inet_aton(SSRF 绕过,见原问);X-Forwarded-For 取第一段未校验(伪造);IPv6 输入没走 inet_pton(AF_INET6);前导零行为不同被当「确定性」依赖;把 IP 归一化(去前导零)与校验混为一谈。


---
