---
title: "[Q6222] HSTS：max-age 语义、子域覆盖与 preload 的不可回滚"
date: 2026-11-24
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6222 · HSTS：max-age 语义、子域覆盖与 preload 的不可回滚

难度：P6 ｜ 标签：HSTS、Strict-Transport-Security、max-age、includeSubDomains、preload、SSL 剥离、回滚

**问**：Strict-Transport-Security 头到底改变了浏览器的什么行为？max-age、includeSubDomains、preload 三个指令各自防什么？为什么说 HSTS 上线容易、下线极难——想回滚 HTTP 要等多久？主域开 includeSubDomains 有什么连带风险？

**答**：
结论：HSTS 是**浏览器侧的强制 HTTPS 缓存策略**：收到该头后，在 max-age 秒内，浏览器对这个域名的所有 `http://` 请求在**发往网络之前**被本地改写为 `https://`——SSL 剥离攻击（中间人把用户的 https 请求降级成 http）从"请求已发出后拦截"变成"请求根本不会以明文发出"。三条防线：①**max-age**：策略有效期，长 max-age（1 年起步）保证用户长期受保护；②**includeSubDomains**：策略覆盖全部子域——堵住攻击者从"某个没上 HTTPS 的子域"（如 `blog.example.com`）发起的降级攻击与 Cookie 注入（同源策略按注册域共享）；③**preload**：申请进入浏览器**内置名单**（Chrome/Firefox 源码里的 hstspreload 清单），让**第一次访问**就受保护——普通 HSTS 的盲区是"首次 HTTP 交互仍可能被降级"，preload 补的正是这个洞。不可回滚性：用户浏览器已缓存 max-age，服务端想恢复 HTTP，必须等**所有用户**的缓存自然过期（最长 max-age）——标准应急是先发 `max-age=0`（只解除"拿到此响应的浏览器"的策略），再等一个完整 max-age 窗口才能保证全网解除。

取舍：a) 上线节奏：先短 max-age（如 300 秒）观察、确认全站资源 HTTPS 可用后，再逐步提到 1 年——因为 HSTS 缓存的是"这个域必须 HTTPS"，如果站点还有 http 资源引用，浏览器会直接拒绝加载而不是降级；b) includeSubDomains 是双刃剑：主域开启后，任何没上 HTTPS 的子域（内部 OA、老服务）会被主流浏览器拒绝访问——**上线前必须盘点全部子域**；c) preload 准入门槛：max-age ≥ 1 年 + includeSubDomains + preload 指令 + 每个现存子域都 HTTPS，名单移除周期长达数月（浏览器发版节奏），所以 preload 是"永久承诺"；d) 纯 IP 访问、非标准端口不认 HSTS；e) API 域名同样值得上 HSTS——App 内嵌 WebView 与第三方集成方的浏览器流量都受益。

实战：事故形态是"站点上了 preload 名单后发现一个内部子域 `grafana.example.com` 只在内网 HTTP 提供，全员浏览器访问被拒；应急路径：该子域临时上 HTTPS（哪怕自签/内网 CA）恢复可用，同时主域 max-age 降到 0 发布，等一年窗口期后申请移出 preload——整个恢复周期以月计"。下面演示头解析与门槛判定。

```python
# HSTS: max-age 语义、includeSubDomains 与 preload 的不可回滚


def parse_hsts(header: str | None) -> dict:
    if not header:
        return {"enabled": False}
    policy = {"enabled": True, "max_age": 0, "include_subdomains": False, "preload": False}
    for part in header.split(";"):
        part = part.strip().lower().replace("_", "-")
        if part.startswith("max-age="):
            policy["max_age"] = int(part.split("=", 1)[1])
        elif part in ("include-subdomains", "includesubdomains"):
            policy["include_subdomains"] = True
        elif part == "preload":
            policy["preload"] = True
    return policy


print("[1] 浏览器视角: 一旦收到 HSTS 头, 之后 max-age 内所有 http:// 请求在发往网络前被本地改写为 https://")
p = parse_hsts("max-age=31536000; includeSubDomains; preload")
print("   ", p)
print("[2] 三条防线: max-age 时长 | includeSubDomains 堵子域 | preload 进浏览器内置名单(首次访问也受保护)")
print("[3] preload 准入门槛: max-age >= 1 年 + includeSubDomains + preload 指令 + 每个子域都必须 HTTPS")
print("    门槛判定:", p["max_age"] >= 31536000 and p["include_subdomains"] and p["preload"])

print("[4] 不可回滚: 用户浏览器已缓存 max-age, 服务端想回滚 HTTP 要等所有用户缓存自然过期")
print("    标准应急: 先把 max-age 降为 0 发布 (只有已访问新版的人会解除), 再等最长 max-age 的窗口")
p_off = parse_hsts("max-age=0")
print("    max-age=0 ->", p_off["max_age"], "(删除策略, 只对拿到此响应的浏览器生效)")

print("[5] 子域风险: 主域上 includeSubDomains 会波及没上 HTTPS 的内部子域 -> 上线前盘点全部子域")
print("[6] 反例: 纯 IP 访问不认 HSTS; 中间人攻击首连仍可能 -- 这才需要 preload 名单兜底")
```

**追问一**：HSTS 头只在 HTTPS 响应里生效，这是为什么？这条规则堵了什么又留了什么？—— RFC 6797 明确规定：**HTTP 明文响应里的 HSTS 头必须被浏览器忽略**。原因：明文里的 HSTS 头本身可被中间人篡改/剥离，如果 HTTP 响应也能设 HSTS，攻击者可以反过来给受害者的浏览器注入一个指向攻击者服务器的假策略。留出的盲区就是**首次访问**：用户第一次手输 `http://example.com` 时浏览器还没有任何策略，这一跳的降级攻击 HSTS 管不了——preload 名单是唯一补法（浏览器出厂即知）。工程推论：`http→https 301 跳转` 的意义只在于"引导首次访问拿到 HSTS 头"，真正的防护是策略缓存本身，跳转那一跳仍是可被攻击的窗口期。

**追问二**：max-age=0 之外的常见误配有哪些？SameSite Cookie 与 HSTS 的关系是什么？—— 误配三连：①只在首页响应加 HSTS 而子页面/接口漏加（策略靠"每次访问刷新"，漏加的入口首访盲区更大）；②max-age 设太短（如 1 小时），用户隔天回来策略已过期，退回首次访问盲区；③把 HSTS 加在 302 临时跳转的响应上——跳转目标若不稳定，策略与实际服务不一致。与 Cookie 的关系：HSTS 是 Cookie 的**前置防线**——没有 HSTS 时，降级攻击可让浏览器以 http 发出请求，`Secure` 标志能保住带标记的 Cookie，但没带 Secure 的会话 Cookie 就随明文请求泄漏；HSTS 从请求源头堵死明文，配合 `Secure` + `__Host-` 前缀 Cookie（强制 HTTPS-only 域绑定）构成完整的会话传输防线。注意 HSTS 只保护浏览器流量，App 原生 HTTP 客户端不认这个头，App 侧要用证书锁定（SSL pinning）解决同类问题。

## 背诵要点
- HSTS = 浏览器本地把 http:// 改写为 https://（发往网络前），明文响应里的 HSTS 头被忽略（防注入假策略）。
- 三指令：max-age 时长 / includeSubDomains 覆盖子域 / preload 进内置名单补"首次访问"盲区。
- 回滚极难：max-age=0 只解除已访问用户的缓存，全网解除要等一个完整 max-age；主域开子域覆盖前必须盘点全部子域。

## 复盘追问
- 首次访问的降级盲区 HSTS 怎么补？（preload 内置名单；普通 HSTS 只保护"拿到过头之后"的流量）
- HSTS 与 Secure Cookie 是什么关系？（HSTS 堵请求源头明文，Secure/`__Host-` 保 Cookie 不随明文请求泄漏，两层叠加）
