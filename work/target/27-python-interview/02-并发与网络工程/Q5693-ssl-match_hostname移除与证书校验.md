---
title: "[Q5693] 3.12 移除 ssl.match_hostname：自研证书校验的迁移"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5693 · 3.12 移除 ssl.match_hostname：自研证书校验的迁移

难度：P7 ｜ 标签：ssl、证书校验、match_hostname、CERT_NONE、IP SAN、TLS

**问**：老代码里 `ssl.match_hostname(cert, hostname)` 做自定义证书校验，升级到 3.12 后直接 `AttributeError`。这个函数为什么被删？手工校验主机名到底少了什么？`verify_mode` 和 `check_hostname` 谁管谁？连接用 IP 直连时证书该怎么签？

**答**：
结论：`ssl.match_hostname` 是"先拿字典形式的证书、再手工比对 SAN"的旧接口，问题在于它与 `SSLContext` 的校验链路是两套逻辑：容易漏掉 `subjectAltName`、通配符规则、IDNA 编码、以及"证书链是否可信"这一步，形成"校验了但没完全校验"的假安全。3.12 起移除，正解是让 `SSLContext` 自己做：`check_hostname=True` + `verify_mode=CERT_REQUIRED`，握手时用 `server_hostname`（SNI + 主机名校验）一次性完成链校验与名字校验。

取舍：a) 标准客户端用 `ssl.create_default_context()`，连接时传 `server_hostname=host`，不要自己比名字；b) 需要固定证书（pinning）时，在 `check_hostname` 通过后额外比对 `getpeercert(binary_form=True)` 的指纹，而不是关掉默认校验后手写；c) 内部服务用私有 CA 时，`load_verify_locations(cafile=...)` 提供 CA，仍然保持 `check_hostname=True`；d) 千万不要为了"让 IP 直连能通"而 `check_hostname=False` + `CERT_NONE`，那等于裸奔。IP 直连要求证书里带 **IP SAN**（`subjectAltName = IP:10.0.0.5`），只写 DNS SAN 的名字校验必然失败。

实战：事故形态是"运维把服务地址从域名改成 ClusterIP，TLS 校验突然失败，开发顺手 `CERT_NONE`，之后中间人可随意劫持内网流量"。下面演示 3.12 里 `match_hostname` 已不存在、`CERT_NONE` 与 `check_hostname` 的先后约束、以及默认上下文的正确状态。

```python
import ssl

print("[1] 3.12 还有 ssl.match_hostname 吗:", hasattr(ssl, "match_hostname"))

ctx = ssl.create_default_context()
print("[2] 默认上下文: check_hostname=%s verify_mode=%s"
      % (ctx.check_hostname, ctx.verify_mode))

# check_hostname=True 时不允许把 verify_mode 降到 CERT_NONE
try:
    ctx.verify_mode = ssl.CERT_NONE
except ValueError as e:
    print("[3] 先关校验模式:", e)

# 正确顺序：先关 check_hostname，再降 verify_mode
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
print("[4] 显式裸奔后:", ctx.check_hostname, ctx.verify_mode)

# 正确姿势：保留校验，只补 CA
ctx2 = ssl.create_default_context()
ctx2.load_default_certs()
print("[5] 私有 CA 场景仍是强校验:", ctx2.check_hostname, ctx2.verify_mode)
print("[6] 主机名由握手参数决定: server_hostname 同时用于 SNI 与名字校验")
print("[7] IP 直连需要证书含 IP SAN，而非仅 DNS SAN")
```

**追问一**：`check_hostname=True` 时 `verify_mode` 能设成 `CERT_OPTIONAL` 吗？—— 不能，会抛 `ValueError: Cannot set verify_mode to CERT_OPTIONAL when check_hostname is enabled`。原因是 `CERT_OPTIONAL` 允许"对端没证书也继续"，这与"必须校验主机名"矛盾。要放宽只能先关 `check_hostname`，再改 `verify_mode`，而这个顺序本身就是一种"我知道我在降低安全性"的显式声明。

**追问二**：为什么 IP 直连必须用 IP SAN，不能靠 CN？—— RFC 6125 早已弃用 CN 作为主机名来源，现代客户端只看 `subjectAltName`；IP 地址必须以 `iPAddress` 类型出现在 SAN 里，用 DNS 类型的 `10.0.0.5` 字符串不算。内部服务用 IP 访问又想过 TLS，就要在签发时把 IP 加进 SAN（`openssl req -addext "subjectAltName=IP:10.0.0.5"`），否则只能走"域名 + 内部 DNS"。

## 背诵要点
- 3.12 移除 `ssl.match_hostname`；正解是 `SSLContext` + `check_hostname=True` + `server_hostname`。
- `check_hostname=True` 时不能设 `CERT_NONE`/`CERT_OPTIONAL`，必须先关名字校验再降级（等于显式裸奔）。
- IP 直连要求证书含 `iPAddress` 类型的 SAN；CN 已不被现代客户端采信。

## 复盘追问
- 升级 3.12 后 `match_hostname` 报 AttributeError，如何无痛迁移？（默认上下文 + server_hostname，别手写比对）
- 把服务从域名改成 IP 后 TLS 校验失败，根因与正确修法？（IP SAN、内部 DNS、禁止 CERT_NONE）
