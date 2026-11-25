---
title: "[Q5195] 邮件头注入：sendmail 的字符串参数绕过 email 包的换行校验"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5195 · 邮件头注入：sendmail 的字符串参数绕过 email 包的换行校验

难度：P7 ｜ 标签：smtplib、email、头注入、CRLF、输入校验、标准库暗坑

**问**：通知服务把用户昵称拼进邮件主题，`f"Subject: {name}"` 之后交给 `smtplib.sendmail`。安全扫描报"邮件头注入"，但本地用 `EmailMessage()["Subject"] = name` 却直接抛异常，看起来明明有防护。为什么两种写法一个拦一个不拦？攻击者能注入出什么效果？正确的构造与校验顺序是什么？

**答**：
结论：`email.message` 的策略层（`policy.header_store_parse`）在**赋值时**就检查头值里不能含 `\r`/`\n`，所以 `EmailMessage()["Subject"] = "a\r\nBcc: x"` 会抛 `ValueError: Header values may not contain linefeed or carriage return characters`。但 `smtplib.SMTP.sendmail(from_addr, to_addrs, msg)` 接受的是**已经序列化好的 str/bytes**，它只负责把这段字节写进 `DATA`，不做任何头解析或校验。于是一旦你用 f-string 手工拼头，`\r\n` 就变成了"头结束 + 新头开始"，注入完全成立：加 `Bcc:` 偷发、覆盖 `From:` 伪造发件人、插入空行后伪造正文、甚至注入 `Content-Type`。

取舍：a) 一律用 `EmailMessage` + `set_content()` + `send_message()`，让策略层在赋值时拦住换行；b) 进入头部的用户输入做**白名单/拒绝**（发现 `\r`/`\n` 直接拒绝或整段丢弃），不要把换行替换成空格——那会静默改变语义，让审计看不到攻击；c) 需要非 ASCII 主题时用 `email.headerregistry`/`policy.SMTPUTF8` 或 `Header` 编码，而不是自己拼 `=?utf-8?B?...?=`；d) 发件人/收件人地址同样要校验，`to_addrs` 是列表但地址里带换行也能搞事（不同 MTA 行为不一）。

实战：事故形态是"营销邮件主题支持用户自定义，攻击者提交带 `\r\nBcc:` 的主题，服务一次给几百个外部地址发了推广邮件，被当成开放中继拉黑"。下面演示手工拼接被解析出额外的 `Bcc`、`EmailMessage` 的拦截，以及入口校验的写法。

```python
from email import policy
from email.message import EmailMessage
from email.parser import Parser


def build_raw(subject):
    return (
        "From: noreply@shop.example\r\n"
        "To: user@example.com\r\n"
        f"Subject: {subject}\r\n"
        "\r\n"
        "body\r\n"
    )


attacker = "Hello\r\nBcc: attacker@evil.example\r\nX-Injected: 1"
raw = build_raw(attacker)
parsed = Parser(policy=policy.compat32).parsestr(raw)

print("[1] 解析出的头:")
for key, value in parsed.items():
    print("   ", key, "=", value)
print("[2] 多出来的收件人:", parsed.get_all("Bcc"))
print("[3] SMTP DATA 里已经是两封邮件的头结构")

msg = EmailMessage()
try:
    msg["Subject"] = attacker
except ValueError as e:
    print("[4] EmailMessage 赋值时拦截:", e)

msg["Subject"] = "Hello"
msg["From"] = "noreply@shop.example"
msg["To"] = "user@example.com"
msg.set_content("body")
print("[5] 正常构造的头数:", len(msg.items()), "| Subject:", msg["Subject"])


def safe_header(value: str) -> str:
    if "\r" in value or "\n" in value:
        raise ValueError(f"header 含换行: {value!r}")
    return value


for candidate in ("Hello", attacker):
    try:
        print("[6] 校验通过:", repr(safe_header(candidate)))
    except ValueError as e:
        print("[6] 入口拒绝:", e)
```

**追问一**：`send_message()` 就绝对安全吗？—— 它内部会把 `EmailMessage` 序列化成字节再交给 `sendmail`，头值已被策略层校验过，所以比手工拼字符串安全；但如果你自己用 `msg.__setitem__` 之外的方式改 `_headers`、或用 `email.generator` 自定义 `policy` 关掉校验，仍然能造出非法头。安全边界在"进入头部的值是否被校验"，而不是"用了哪个 API"。

**追问二**：为什么不能把 `\r\n` 替换成空格了事？—— 替换会改变用户可见内容（主题被截断/拼接），且掩盖了攻击信号：日志里看不到注入尝试，WAF 与审计都失去线索。更稳的是"拒绝 + 记录 + 返回 400"，让攻击面暴露；如果业务必须接受多行（比如签名），那就不是"头值"而是"正文"，应该走 `set_content()` 而不是塞进 Subject。

## 背诵要点
- `EmailMessage` 赋值时校验头值不含 `\r`/`\n`；`smtplib.sendmail` 收字符串时不做任何校验，注入由此发生。
- 头注入可加 `Bcc`、覆盖 `From`、插入空行伪造正文；`to_addrs` 与地址字段同样要校验。
- 正解：`EmailMessage` + `set_content` + `send_message`，入口对 `\r\n` 拒绝并记录，而不是静默替换。

## 复盘追问
- 同一段用户输入，为什么 `EmailMessage` 抛异常、`sendmail` 却照发？（策略层校验 vs 原始字节透传）
- 邮件头注入能造成哪些具体后果？如何从"头值不可信"设计防线？（Bcc 偷发、From 伪造、正文伪造、入口拒绝 + 审计）
