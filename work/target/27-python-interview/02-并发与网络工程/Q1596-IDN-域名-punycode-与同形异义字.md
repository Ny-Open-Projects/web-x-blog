---
title: [Q1596] IDN 域名:punycode 与同形异义字
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1596 · IDN 域名:punycode 与同形异义字

> 难度:★★☆☆ | 标签:IDN, punycode, 安全

**问**:中文域名在 DNS 里是怎么存的?"аpple.com"(首字母是西里尔 а)和 "apple.com" 有什么区别?

**答**:DNS 只存 ASCII:非 ASCII 标签被 IDNA 编码成 xn-- 前缀的 punycode(ASCII 兼容编码),中文点 jp 在线上其实是 xn-- 开头的串,解析方再解码还原显示。风险在同形异义字(homograph):西里尔 а 与拉丁 a 视觉完全相同,punycode 却不同——钓鱼站注册看起来一样的域名,地址栏根本分辨不出。工程防线:多脚本混排检测(一个标签里同时出现两种文字系统即可疑)、用户输入的域名先转 ASCII 再校验、展示层还原 xn-- 时高亮非拉丁字符。

```python
# file: code/02_并发与网络工程/q1596_idn.py
"""IDN 域名: punycode 与同形异义字。

- 国际化域名在 DNS 里只能存 ASCII: 非 ASCII 标签被编码成 xn-- 前缀的
  punycode(ASCII 兼容编码 ACE), "中文.jp" 在线上其实是 xn--fiq228c.jp;
- 风险: 西里尔字母 а 与拉丁字母 a 长得一模一样, punycode 却完全不同 ——
  同形异义字(homograph)钓鱼; 多脚本混排检测是最实用的防线。
"""
import unicodedata


def to_ascii(domain):
    return domain.encode("idna").decode("ascii")


def to_unicode(domain):
    return domain.encode("ascii").decode("idna")


def label_scripts(label):
    """一个标签里出现的文字系统集合, 用于同形异义字检测。"""
    scripts = set()
    for ch in label:
        name = unicodedata.name(ch, "")
        if name:
            scripts.add(name.split()[0])
    return scripts


def looks_suspicious(domain):
    for label in domain.split("."):
        if len(label_scripts(label)) > 1:
            return True
    return False


def main():
    # 1) 编解码往返
    ace = to_ascii("中文.jp")
    back = to_unicode(ace)
    print("中文.jp -> ACE:", ace, "-> 还原:", back)
    assert back == "中文.jp", "IDN 编解码应无损往返"

    # 2) 纯 punycode 编码(不带 xn-- 外壳)
    print("münchen 的 punycode:", "münchen".encode("punycode").decode())
    assert "münchen".encode("punycode").decode().startswith("mnchen")

    # 3) 同形异义字: 视觉相同, 字节不同
    real = "apple.com"
    fake = "\u0430pple.com"          # 首字母是西里尔 а U+0430
    print("真实域名:", real, "ACE:", to_ascii(real))
    print("仿冒域名:", fake, "ACE:", to_ascii(fake))
    assert to_ascii(real) != to_ascii(fake), "视觉相同但编码必然不同"

    # 4) 混排检测
    verdicts = [(d, looks_suspicious(d)) for d in (real, fake)]
    for d, bad in verdicts:
        print("检测 %-12s -> %s" % (d, "可疑(多脚本混排)" if bad else "正常"))
    assert not looks_suspicious(real) and looks_suspicious(fake)

    print("结论: IDN 是编码层的事, 显示层的事是同形字——证书校验挡不住视觉欺骗")


if __name__ == "__main__":
    main()
```

**追问**:1) Python 的 idna 编码是哪个版本的规范?——IDNA 2003,与更严格的 IDNA 2008 和 UTS46 有差异;严格场景用第三方 idna 库。2) 多脚本混排检测为什么有效?——正常域名标签内只用一种文字系统(拉丁/希腊/西里尔各一),混排(西里尔 а+拉丁 pple)几乎必是钓鱼;这是浏览器地址栏防同形字的标准启发式,自研系统照搬即可。3) IDNA 版本差异的实际影响?——Python 内置 IDNA 2003 对某些新字符(如德语 ß、分裂字符)编码与 IDNA 2008/UTS46 不同,注册局按 2008 发的域名可能解不出来;严格场景用第三方 idna 库并固定版本。4) 生产陷阱?——把 punycode 域名直接当显示名(用户看到 xn-- 一串或被解码钓鱼);用户输入域名未先 toASCII 就查 DNS(非 ASCII 直接报错或走错);安全校验(白名单)用显示形式而攻击者用 punycode 绕过;日志里 punycode 与 Unicode 形式混存,对账困难。

---
