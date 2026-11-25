---
title: "[Q5743] DoH 与 DoT：DNS 解析的加密通路与应用层解析器"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5743 · DoH 与 DoT：DNS 解析的加密通路与应用层解析器

难度：P6 ｜ 标签：DoH、DoT、RFC 8484、RFC 7858、DNS 隐私、wire format、应用层解析、getaddrinfo、缓存策略

**问**：系统 getaddrinfo（Q641）走的传统 UDP 53 解析有什么隐私/安全问题？DoT（RFC 7858）与 DoH（RFC 8484）分别怎么解决、差异是什么？DoH 的 wire format 与 GET/POST 两种传输形态怎么工作？应用侧引入 DoH 解析器后，缓存、超时与回退链怎么设计？

**答**：
结论：传统解析（UDP 53 明文）的两个问题：①**内容可窃听/篡改**——链路上任何设备（运营商、公共 WiFi、中间盒）能看到你查的域名并注入假答案（劫持广告/钓鱼），DNSSEC 只保证记录来源签名、不加密传输；②**元数据泄露**——查询行为本身就是浏览记录。两条加密通路：①**DoT（RFC 7858）**——DNS over TLS，**独立端口 853**，TLS 里直接跑传统 DNS wire format，改动最小（防火墙一眼识别、可整段屏蔽，运营商级封锁容易）；②**DoH（RFC 8484）**——DNS over HTTPS，**复用 443 端口与 HTTP 基建**，DNS 报文作为 HTTP 载体（GET 的 `?dns=` 参数是 **base64url 的完整 DNS 报文**，或 POST 的 `application/dns-message` body）——与普通 HTTPS 流量不可区分，抗封锁强，且能用上 HTTP 连接复用/代理生态；代价是解析器与 HTTP 栈耦合。两者 wire format 相同（header + QNAME + 问题段 + 资源记录，Q5741 的 DNS-SD 解析是同族知识），差异只在**传输层容器**。应用侧设计要点：DoH 解析器是**应用进程内的解析客户端**（绕过系统 resolver），必须自带缓存（对齐记录 TTL）、超时预算（DNS 是阻塞一切的前置依赖）、**回退链**（DoH 失败 → 系统 getaddrinfo → 告警），以及"**该不该用**"的判断——企业内网环境里私有域名系统 resolver 才认识，DoH 公共解析器反而解析不了（split-horizon DNS 矛盾）。

取舍：a) 客户端隐私 vs 企业可管理性：DoH 绕过企业 DNS 策略与日志（合规部门恨它），企业环境往往要显式禁用或把 DoH 指向内部 DoH 服务；b) GET vs POST：GET 可被 HTTP 缓存层（CDN/浏览器）按 TTL 缓存、便于调试，但 URL 长度限制与日志里的查询隐私（URL 会进访问日志）；POST 更私密、无长度限制，但不能借 HTTP 缓存——公共 DoH 服务两者都支持，应用选 POST+自管缓存更可控；c) 超时预算：解析失败拖垮请求链路，DoH 超时要**小于**上游请求超时且带对冲（同时查 DoH 与系统解析，谁快用谁——Q2143 的对冲竞速同思路）；d) 缓存层次：应用内存缓存（TTL 精确对齐，负缓存短 TTL）→ DoH 服务端缓存 → 权威 DNS；连接级缓存（HTTP/2 复用）让高频解析的边际成本趋近于零；e) 安全面：DoH 服务商成为新的信任锚点（你的域名查询全给 Cloudflare/Google），选型要看隐私政策与组织策略，自建 DoH（如 CoreDNS + DoH 前端）是中间道路。

实战：事故形态是"出浢单元把公共 DoH 硬编码为唯一解析器，客户内网（split-horizon）私有域名 `api.corp.local` 全部解析失败——链路上层重试风暴。修复为解析路由表：corp 域走系统 resolver、公网域走 DoH、DoH 失败降级系统 resolver 并采样告警；同时把 DoH 超时 1s、对冲 300ms 写进连接层预算（Q6019 超时分配的解析前置段）"。下面手写 DNS wire format 查询的 base64url 编码与最小应答解析（离线演示，不依赖网络）。

```python
# DoH wire format: 查询构建、base64url 编码与最小应答解析 (RFC 8484 离线演示)
import base64
import socket
import struct

def enc_qname(name: str) -> bytes:
    """域名 → wire format: 长度前缀标签 + 根 (与 Q5741 同族)"""
    out = b""
    for label in name.rstrip(".").split("."):
        raw = label.encode()
        out += bytes([len(raw)]) + raw
    return out + b"\x00"

def build_query(name: str, qtype: int = 1, qid: int = 0) -> bytes:
    """标准查询: header(12B) + qname + qtype/qclass; DoH 的 qid 常置 0 (HTTP 已有请求关联)"""
    header = struct.pack(">HHHHHH", qid, 0x0100, 1, 0, 0, 0)   # flags: RD=1
    return header + enc_qname(name) + struct.pack(">HH", qtype, 1)

def dec_qname(data: bytes, off: int):
    labels = []
    while True:
        ln = data[off]
        off += 1
        if ln == 0:
            break
        labels.append(data[off:off + ln].decode())
        off += ln
    return ".".join(labels), off

print("[1] 构建 wire format 查询并编码进 GET 路径")
q = build_query("api.example.com", qtype=1)                     # A 记录
b64 = base64.urlsafe_b64encode(q).rstrip(b"=").decode()         # RFC 4648 无填充 base64url
print("    wire 查询:", len(q), "字节:", q.hex())
print("    GET /dns-query?dns=", b64[:44] + "...", "(完整报文作为参数)")

print("[2] 模拟 DoH 应答: 1 个 A 记录, TTL=60")
ip_bytes = socket.inet_aton("93.184.215.14")
resp = (struct.pack(">HHHHHH", 0, 0x8180, 1, 1, 0, 0)           # flags: QR+RD+RA, rcode=0
        + enc_qname("api.example.com") + struct.pack(">HH", 1, 1)
        + enc_qname("api.example.com") + struct.pack(">HHIH", 1, 1, 60, 4) + ip_bytes)

print("[3] 解析应答: 头 → rcode → answer 的 A 记录")
_, flags, qd, an, _, _ = struct.unpack_from(">HHHHHH", resp)
rcode = flags & 0xF
print("    rcode =", rcode, "(0=NOERROR) | answer 数 =", an)
off = 12
for _ in range(qd):                                             # 跳过 question 段
    _, off = dec_qname(resp, off)
    off += 4
for _ in range(an):
    _, off = dec_qname(resp, off)                               # name (教学版无压缩指针)
    rtype, rclass, ttl, rdlen = struct.unpack_from(">HHIH", resp, off)
    off += 10
    rdata = resp[off:off + rdlen]
    off += rdlen
    if rtype == 1:
        print(f"    A 记录: {socket.inet_ntoa(rdata)} (ttl={ttl}s -> 缓存对齐这个值)")

print("[4] 应用侧设计: 缓存(TTL 对齐) / 超时预算(小于上游) / 回退链(DoH->系统 resolver)")
print("[rule ] DoT=853 独立端口可被整段封锁; DoH=443 不可区分; 企业 split-horizon 域走系统 resolver")
```

**追问一**：DoH 把 DNS 变成 HTTPS 后，原来 UDP 的"无连接快速失败"没了——解析超时与并发策略怎么重设计？—— 传统 UDP 解析失败快（无连接、内核超时即弃），DoH 挂在 HTTP 上：连接建立（TLS 握手成本，可复用缓解）、请求排队、HTTP 超时——失败路径变慢变复杂。重设计三原则：①**预算切割**——解析是请求的前置依赖，DoH 总超时必须小于上游请求超时的合理份额（如上游 3s，解析 800ms，含连接建立）；②**对冲与并行**——300ms 无响应就并发第二个查询（同 QID 不同传输：DoH+系统解析双路竞速，谁先用谁，Q2143 对冲模式），并给连接池保温（HTTP/2 复用让常驻解析的边际成本只有 RTT）；③**负缓存**——NXDOMAIN/失败结果也缓存（短 TTL 如 30s），防止对同一坏域名反复打 DoH；再加熔断（Q1882 思路：连续失败后短窗内直接走系统 resolver）。口径：DoH 解析器的工程难点不在协议（wire format 反而简单），在**把"解析从不失败"的假设改成"解析是可能慢的依赖"**——超时、对冲、缓存、熔断四件套一个不能少。

**追问二**：企业内网部署 DoH 有哪些矛盾？"私有域名 + 公共 DoH"的 split-horizon 冲突具体怎么发生？—— split-horizon（内外视图 DNS）：`api.corp.local` 只在内网权威 DNS 里有记录，公网解析器 NXDOMAIN。矛盾链：应用内嵌 DoH（指向公共服务商）→ 查 `api.corp.local` → 公共解析器无此权威 → NXDOMAIN → 应用认为服务不存在；反过来企业出口防火墙拦 443 之外的 DNS（DoT 853 被禁）或强制透明代理改写 DoH 流量。企业落地的三条路线：①**统一内部 DoH**——CoreDNS/Bind 挂 DoH 前端，应用 DoH 指向内网地址（继承私有域视图 + 日志合规）；②**域名路由表**——应用解析器按后缀分流（`.corp.local`/`.svc` 走系统 resolver，公网走 DoH），实现简单但路由表要运维维护；③**禁用内嵌 DoH**——终端统一管理（浏览器策略、SDK 开关），保留系统 resolver 的中心化。决策依据是"谁是 DNS 策略的 owner"：合规重企业用 ①③，产品出海面向公网用户用 ②+公共 DoH 提升用户隐私与解析质量。工程红线：**永远不要让 DoH 成为唯一解析路径**——回退链与告警是最后防线。

## 背诵要点
- 传统 UDP 53 明文可窃听可篡改可画像；DoT=853 独立端口（易被整段封锁），DoH=443 HTTPS 容器（GET ?dns=base64url 报文 / POST application/dns-message），wire format 与传统 DNS 相同。
- 应用内 DoH 解析器必须自带：TTL 对齐缓存+负缓存、小于上游的超时预算、双路对冲、熔断回退链（DoH→系统 resolver）——解析是可能慢的依赖。
- split-horizon 矛盾：私有域名公共 DoH 必 NXDOMAIN；企业路线=内部 DoH/域名路由表/禁用内嵌 DoH；DoH 永不作为唯一解析路径。

## 复盘追问
- DoT 与 DoH 的本质差异与各自被封禁的风险？（DoT 独立端口 853 防火墙一眼识别可整段拦；DoH 复用 443 与普通 HTTPS 不可区分，抗封锁但绕过企业 DNS 策略）
- 应用接 DoH 后解析失败拖垮链路怎么防？（预算切割+对冲竞速+负缓存+熔断回退；内网私有域按后缀路由回系统 resolver）
