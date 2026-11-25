---
title: "[Q5723] 证书吊销 OCSP/CRL：软失败、stapling 与时效裁决"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5723 · 证书吊销 OCSP/CRL：软失败、stapling 与时效裁决

难度：P7 ｜ 标签：OCSP、CRL、证书吊销、软失败、硬失败、OCSP stapling、must-staple、TLS

**问**：证书被吊销后，客户端靠什么知道——CRL 和 OCSP 各自怎么工作？OCSP 响应者宕机时软失败/硬失败两难是什么？OCSP stapling 为什么是工程正解？Python 的 ssl 默认吊销行为是什么？

**答**：
结论：吊销感知有两套机制。**CRL**（Certificate Revocation List）是 CA 定期发布的全量黑名单文件，带 `this_update`/`next_update` 时效字段——判断"未吊销"的前提是 CRL **新鲜**：`now > next_update` 的 CRL 是过期证据，不能当"good"使用，只能判 stale（走降级策略）。**OCSP**（Online Certificate Status Protocol）是单证书实时查询：客户端把证书序列号发给 CA 的 responder，换回 good/revoked/unknown 三态签名响应。工程两难在**可用性与安全性的裁决**：responder 不可达时，软失败（soft-fail）继续信任（保可用性，但吊销检查名存实亡——大量生产 TLS 客户端默认软失败，吊销体系实际覆盖率很低）；硬失败（hard-fail）直接拒连（保安全，但 responder 抖动=全量拒连事故源）。**OCSP stapling** 是正解：服务端代替客户端查询 OCSP 并把带时间戳的签名响应**随 TLS 握手 stapling 进来**，客户端零额外 RTT、无隐私泄漏（客户端不用向 CA 泄露浏览目标）、responder 故障被服务端缓存兜住；配合 `must-staple`（证书扩展声明"必须带 staple"）进一步收紧。Python `ssl` 默认加载系统信任库做**证书链与主机名校验**，吊销检查默认不启用（`verify_flags` 不含 `VERIFY_CRL_CHECK_LEAF`/`VERIFY_X509_STRICT` 这类开关），依赖 stapling 时客户端校验 `stapled OCSP response` 的逻辑要显式写。

取舍：a) 服务端：无条件上 stapling（OpenSSL 自动续取），缓存窗口取 responder 的 nextUpdate 内；b) 客户端：敏感场景（支付/内网工具）开硬失败 + must-staple，普通场景接受软失败但监控"staple 缺失率"；c) 内网出站被代理/防火墙拦 OCSP 查询时，软失败等于从未检查——审计要按"实际生效策略"而不是"配置开关"；d) CRL 的定位：离线环境/批量校验工具用 CRL 更合适（一次下载验全部），在线服务别按 CRL 做实时裁决（next_update 窗口内的吊销盲区 = 最长泄漏窗口）；e) 版本演进：证书链上游（中间 CA）吊销与叶子证书吊销分开治理，`VERIFY_CRL_CHECK_LEAF` 只查叶子。

实战：事故形态是"内网服务出站 TLS 被 nginx 反代拦截 OCSP 请求，软失败策略静默放行了一张已吊销的中间人证书（内网攻击者用泄露证书伪造服务）；复盘后对内部高敏链路切换 mTLS（Q695/Q6021）+ 显式 stapling 校验，并增加 'staple 缺失率' 监控"。下面实现吊销裁决的核心逻辑（CRL 时效 + 三态决策）。

```python
# 证书吊销 OCSP/CRL: 决策逻辑、软失败与时效
import time

print("[1] 两套吊销机制: CRL(全量黑名单, 定期发布) vs OCSP(单证书实时查询)")
crl = {
    "issuer": "cn=Example CA",
    "revoked": {"1001": "key-compromise", "1002": "affiliation-changed"},
    "this_update": time.time() - 86400,
    "next_update": time.time() + 86400,
}

def check_crl(serial: str, now: float | None = None) -> str:
    now = time.time() if now is None else now
    if now > crl["next_update"]:
        return "stale"                  # CRL 过期: 不能当'未吊销'的证据
    return crl["revoked"].get(serial, "good")

print("    serial=1001 ->", check_crl("1001"))
print("    serial=2001 ->", check_crl("2001"))
print("    过期 CRL 判定 ->", check_crl("2001", now=time.time() + 172800))

print("[2] 软失败 vs 硬失败: OCSP 服务不可达时的两难")
def ocsp_check(serial: str, responder_up: bool = False) -> str:
    if responder_up:
        return "good" if serial not in crl["revoked"] else "revoked"
    return "soft-fail"                  # 查不到: 继续信任(可用性优先) 还是拒绝(安全优先)

print("    responder 宕机 + 软失败策略 -> 放行连接 (企业网代理常见误配放大面)")
print("    responder 宕机 + 硬失败策略 -> 全量拒连 (可用性事故源)")

print("[3] 工程现实: 大量站点证书验证根本不查吊销, OCSP stapling 才是正解")
print("    stapling = 服务端代替客户端查 OCSP 并随握手带响应, 客户端零额外 RTT 且无隐私泄漏")
print("[4] Python ssl 默认走系统信任库, 吊销检查默认不启用或软失败; 高敏场景要显式加策略")
import ssl
ctx = ssl.create_default_context()
print("    verify_flags =", ctx.verify_flags, "| CHECK_REVOCATION 未默认开启")
```

**追问一**：为什么"吊销检查名存实亡"还能被业界接受？—— 风险模型下的权衡：吊销保护的是"私钥泄露/误发证书"场景，这类攻击要求攻击者**持有效私钥且证书在有效期内**，发生率远低于"中间链路劫持"；而强制吊销检查（硬失败）让一个 responder 故障变成全网不可用——历史上有 CA 的 OCSP 服务抖动导致大量站点拒连的先例。所以浏览器阵营事实上软失败为主，用证书有效期缩短（90 天 Let's Encrypt 模式）来压缩"吊销盲区"的暴露窗口：证书活得短，吊销就不再是主防线。工程上把"有效期 + stapling + 短窗口轮换"组合起来，比死磕 OCSP 硬失败更有效（Q693 的过期监控、Q6671 的证书过期全量失败复盘同族）。

**追问二**：must-staple 和 stapling 的失效模式各是什么？—— stapling 失效模式：服务端忘了续取 staple（responder 挂了/续取任务挂了）→ 客户端收到无 staple 的握手 → 软失败客户端照常连接（保护失效但无感），硬失败/must-staple 客户端拒连（服务端事故）。must-staple 的价值是把"有没有 staple"从软策略变成证书级硬契约：客户端看到带 must-staple 标志的证书却没有 staple 响应时**必须**拒绝——这把服务端的 stapling 运维变成上线前的强制项。反过来，must-staple 证书 + 客户端不支持 stapling 校验 = 保护仍然落空，所以"两端都要检查"才是完整闭环，单端配置不算部署完成。

## 背诵要点
- CRL 全量黑名单需验时效（next_update 过期=stale 不能当 good）；OCSP 单证书三态实时查询。
- 软失败保可用（吊销名存实亡）、硬失败保安全（responder 抖动=拒连）；Python ssl 默认不启用吊销检查。
- 正解：OCSP stapling（服务端带响应、零额外 RTT、无隐私泄漏）+ must-staple 硬契约 + 短有效期压缩盲区。

## 复盘追问
- 内网 TLS 出站被代理拦掉 OCSP，软失败意味着什么？（吊销检查从未生效；高敏链路换 mTLS+staple 校验）
- 为什么浏览器选择软失败而不是硬失败？（responder 故障=全网拒连；用短有效期压缩吊销盲区）
