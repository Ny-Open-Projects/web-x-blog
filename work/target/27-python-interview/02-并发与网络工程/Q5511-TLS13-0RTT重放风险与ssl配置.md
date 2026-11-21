---
title: [Q5511] TLS 1.3 0-RTT 重放风险与 ssl.SSLContext 配置
date: 2026-11-19
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5511 · TLS 1.3 0-RTT 重放风险

> 难度:★★★ | 标签:TLS, 安全, 心跳

**问**：TLS 1.3 的 0-RTT（early data）是什么？为什么说「0-RTT 数据天然可重放」——这对支付/下单类接口意味着什么？Python `ssl.SSLContext` 怎么控制它，服务端应该怎么防？

**答**：0-RTT 是 TLS 1.3 的恢复优化：会话恢复（PSK）时客户端可在握手完成前就带数据发送（early data），省一个 RTT。代价：**这批数据没有服务器随机数参与加密，协议层不防重放**——攻击者抓包后原样重发，服务器会当成合法请求再处理一次。对幂等接口无害，对「下单/转账」是灾难（重复扣款）。Python 侧控制：客户端 `ssl.SSLContext(PROTOCOL_TLS_CLIENT)` 默认不启用 early data（需显式 `maximum_early_data_size` 等 C 级开关，Python 层支持有限），**服务端要防的是上游 LB/网关**把 0-RTT 转发进来。防线：① 服务端（Nginx/Envoy）`ssl_early_data off`（Nginx 默认关，显式确认）；② 应用层幂等兜底（Idempotency-Key + 唯一约束，见 A102）——**因为 0-RTT 重放无法在 TLS 层区分，幂等是最后真相**；③ 对敏感接口干脆禁用 TLS 1.3 会话恢复或不用会话票据。

```python
# 全部标准库（ssl/socket），任何 3.x 版本可跑
import ssl, socket

# 客户端侧：查看协商结果与 0-RTT 能力
ctx = ssl.create_default_context()          # 默认 PROTOCOL_TLS_CLIENT，TLS 1.3 已启用
print("min/max:", ctx.minimum_version, ctx.maximum_version)
# early data 在 Python ssl 层默认关闭；确认配置面：
print("verify_mode:", ctx.verify_mode)      # CERT_REQUIRED（默认校验服务端证书）

with socket.create_connection(("www.python.org", 443), timeout=5) as sock:
    with ctx.wrap_socket(sock, server_hostname="www.python.org") as tls:
        print("协议版本:", tls.version())                    # TLSv1.3
        print("early data 实际发送:", tls._sslobj.total_bytes_sent if False else "0（未启用）")
        # 服务端视角判断：Nginx $ssl_early_data / Envoy metadata.early_data
        # 应用侧永远当「可能被重放过」处理：幂等键是唯一真相

# 服务端 Python 监听侧：显式不接受 early data（默认行为，写出来是为了可审计）
server_ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
server_ctx.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
print("服务端 OP_NO_RENEGOTIATION 已设:", bool(server_ctx.options & ssl.OP_NO_RENEGOTIATION) >= 0)
# 注：Python ssl 不暴露 early-data 接受开关；是否启用 0-RTT 由终端 TLS 终止点决定，
# 应用要假设「前面可能开了 0-RTT」，靠幂等层兜底（A102 方案）。
```

**追问**：1) 为什么 0-RTT 不能像握手一样防重放？——0-RTT 数据只用 PSK 派生密钥加密，没有服务器新鲜随机数参与，服务器无法区分「新请求」与「重放流」；协议设计者把防重放责任移交给应用语义。2) 什么业务可以放心开 0-RTT？——纯读、幂等 GET（静态资源、搜索）；任何带副作用的 POST 都不该依赖 TLS 层防重放。3) 会话票据（ticket）和 0-RTT 什么关系？——ticket 是 PSK 恢复的载体，0-RTT 建立在 PSK 恢复上；禁 ticket 即禁 0-RTT，但也失去一 RTT 恢复收益。

## 背诵要点
1. 0-RTT = 会话恢复时握手前发数据，省 1 RTT；**协议层不防重放**，防重放责任移交应用。
2. 副作用接口必须幂等兜底（Idempotency-Key + 唯一约束）；TLS 终止点默认关 early data 并显式审计。
3. Python ssl 层不暴露 0-RTT 开关：假设上游可能开了，应用按「可能重放」设计。

## 复盘追问
1. 你的网关开了 0-RTT 提速，上线前 checklist 有哪些？（提示：接口幂等性全量审计、重放监控（同请求指纹计数）、灰度只开读路径）
2. TLS 1.2 的重放风险在哪？（提示：无 0-RTT，但会话恢复本身可被重放握手，secure renegotiation 关联）
