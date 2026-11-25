---
title: "[Q5742] PROXY protocol：真实客户端 IP 的 TCP 层传递与头解析"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5742 · PROXY protocol：真实客户端 IP 的 TCP 层传递与头解析

难度：P6 ｜ 标签：PROXY protocol、HAProxy、真实 IP、L4 负载均衡、v1/v2、安全边界、后端解析、XFF 对比

**问**：L4 负载均衡（HAProxy/nginx stream）转发 TCP 时后端为什么看不到真实客户端 IP？PROXY protocol 的 v1（文本行）与 v2（二进制）格式各是什么、怎么选？为什么头部必须出现在"连接的第一个字节"、伪造头有什么风险、怎么防？与 HTTP 层的 X-Forwarded-For（Q2186）是什么分工关系？

**答**：
结论：L4 透传模式下后端 `getpeername()` 看到的是**负载均衡器的地址**（连接是 LB 发起的），业务需要真实客户端 IP 时 LB 在**转发数据前**先注入一段协议头——这就是 PROXY protocol（HAProxy 作者 Willy Tarreau 设计，v1/v2 两种编码）。格式：①**v1 文本行**——`PROXY TCP4 203.0.113.7 10.0.0.1 51000 443\r\n`（协议字、源/目的 IP、源/目的端口，一行 CRLF 结尾），可读性好但只能 IPv4/IPv6；②**v2 二进制**——12 字节魔数 `\r\n\r\n\x00\r\nQUIT\n`（设计成"误收到时立即断开"的安全哨兵）+ ver/cmd 各 1 字节 + family/proto 1 字节 + 长度 2 字节 + 地址块，还支持 Unix socket、TLV 扩展（SSL CN/授权信息、命名空间）。两条铁律：①**头部必须是连接的第一个字节**——解析器先读头再读业务数据，头混进业务流就废了（这也是"非 PROXY 客户端直连"必须被识别并拒绝的原因）；②**信任边界在"谁被允许发头"**——头由 LB 注入，后端必须只对 LB 的连接做头解析；若把 PROXY 端口直接暴露公网，攻击者手写一个头就能**伪造任意源 IP**（绕过基于 IP 的风控/审计），这是 PROXY protocol 的头号安全事故形态。与 XFF 分工：PROXY protocol 在 **TCP 层**（任何协议适用、LB 必须支持），XFF 在 **HTTP 层**（仅 HTTP 适用、由代理逐跳追加）——L4 场景没有 HTTP 可加头，只能 PROXY protocol；L7 场景 XFF+信任链（Q2186）更普遍，PROXY protocol 反而少用。

取舍：a) 版本选择：新部署一律 v2（二进制解析无歧义、TLV 可扩展、魔数哨兵防误解析）；v1 仅兼容历史设备；b) 后端实现：不要手写生产解析器——主流框架/server 都有开关（uvicorn 的 `--proxy-headers` + `--forwarded-allow-ips`、gunicorn 的 PROXY protocol 模块），自研要点是"读头 → 解析 → 覆盖 peer 地址 → 严格限来源 IP"；c) 安全三闸：来源 IP 白名单（只信 LB）、长度上限（防畸形头耗内存）、cmd=LOCAL（0x0）表示这是健康检查连接不含地址、直接关闭；d) TLS 场景：PROXY 头在 TLS 之前（明文可解析），SNI/证书信息放 TLV——链路是 client → LB(注入头) → 后端(先解头再解 TLS)；e) 与 PROXY 协议并存的另一条路：LB 直接改写源地址（DNAT/TPROXY）让 peer 地址自然真实——更透明但要内核配合，跨 LB 集群难维护。

实战：事故形态是"后端服务为兼容某 LB 打开了 PROXY 解析，但端口同时被运维直连排障使用——攻击者（或误配的探针）直连手写 `PROXY TCP4 8.8.8.8 ...`，风控日志全是伪造的美国 IP，基于 IP 的频控整体失效。修复为：解析前置来源 IP 白名单（仅 LB 段），直连运维端口与业务端口分离，监控加'头来源与 peer 不符'告警"。下面手写 v2 头的构建、本地回环注入与后端解析，附 v1 文本行对照。

```python
# PROXY protocol v2/v1: 构建、注入与后端解析
import socket
import struct
import threading

PP2_SIGNATURE = b"\r\n\r\n\x00\r\nQUIT\n"          # 12 字节魔数: 误配时立刻断开的安全哨兵

def build_v2(src_ip: str, dst_ip: str, src_port: int, dst_port: int) -> bytes:
    """v2 头: 魔数 + ver/cmd + family/proto + 长度 + 地址块 (IPv4/STREAM)"""
    body = (socket.inet_aton(src_ip) + socket.inet_aton(dst_ip)
            + struct.pack(">HH", src_port, dst_port))
    ver_cmd = 0x21                                  # version=2, cmd=PROXY(0x1)
    fam_proto = 0x11                                # family=INET, proto=STREAM
    return PP2_SIGNATURE + struct.pack(">BBH", ver_cmd, fam_proto, len(body)) + body

def build_v1(src_ip: str, dst_ip: str, src_port: int, dst_port: int) -> bytes:
    """v1 文本行: PROXY TCP4 <src> <dst> <sport> <dport>\r\n"""
    return f"PROXY TCP4 {src_ip} {dst_ip} {src_port} {dst_port}\r\n".encode()

print("[1] 两种编码对照")
v2 = build_v2("203.0.113.7", "10.0.0.1", 51000, 443)
v1 = build_v1("203.0.113.7", "10.0.0.1", 51000, 443)
print("    v2:", v2.hex(), f"({len(v2)} 字节)")
print("    v1:", v1.decode().strip())

print("[2] 本地回环: LB 角色注入头, 后端角色先解头再读业务")
srv = socket.socket()
srv.bind(("127.0.0.1", 0))
srv.listen(1)
port = srv.getsockname()[1]

def backend() -> None:
    conn, addr = srv.accept()
    print(f"    [后端] getpeername (未解析前) = {addr}  <- 只看到 LB")
    def recvn(n: int, buf: bytes) -> bytes:        # 头部定长读取
        while len(buf) < n:
            buf += conn.recv(4096)
        return buf
    buf = recvn(16, b"")
    assert buf[:12] == PP2_SIGNATURE, "第一个字节必须是 PROXY 头"
    ver_cmd, fam_proto, length = struct.unpack_from(">BBH", buf, 12)
    buf = recvn(16 + length, buf)                  # 补齐地址块
    src = socket.inet_ntoa(buf[16:20])
    dst = socket.inet_ntoa(buf[20:24])
    sp, dp = struct.unpack_from(">HH", buf, 24)
    rest = buf[16 + length:]
    print(f"    [后端] v2 解析: ver={ver_cmd >> 4} cmd={ver_cmd & 0xF} "
          f"真实源={src}:{sp} -> 目标={dst}:{dp}")
    print(f"    [后端] 业务首字节: {rest!r}  (头与业务严格分离)")
    conn.close()
    srv.close()

t = threading.Thread(target=backend)
t.start()
client = socket.create_connection(("127.0.0.1", port))
client.sendall(build_v2("203.0.113.7", "127.0.0.1", 51000, port)   # LB 注入的 PROXY 头
               + b"GET / HTTP/1.0\r\n\r\n")                        # 业务数据紧随其后
t.join()

print("[3] 安全三闸: 来源白名单 / 长度上限 / cmd=LOCAL 健康检查直关")
print("[rule ] 头必须是第一个字节; 只解析可信 LB 的连接; 伪造头=伪造源 IP 的事故源")
```

**追问一**：PROXY protocol 的 TLV 扩展能携带什么？为什么 SSL/TLS 信息放 TLV 而不是让后端自己握手？—— TLV（type-length-value）挂在 v2 地址块之后：type 0x01 ALPN、0x02 authority(SNI)、0x03 CRC32c 校验、0x20-0x2F SSL 系列（client 标志位、证书版本号、CN、摘要算法与签名算法列表、**客户端证书的 SPKI 摘要**）等。为什么 SSL 信息放 TLV：LB 做 **TLS 终结**（client → LB 是 TLS，LB → 后端是明文）时，客户端证书、SNI、密码套件这些"TLS 会话属性"只存在于 LB 与 client 的握手里——后端根本没参与握手，无从得知；LB 把它们编进 TLV 才能传给后端做授权决策（如 mTLS 的客户端证书身份校验移到应用层逻辑）。三条注意：①TLV 里的 SSL 字段本质是"LB 的转述"，后端的信任边界仍然是"LB 来源白名单"——LB 被攻破/误配时 TLV 同样可伪造；②TLV 有长度上限约束，大字段（完整证书链）不放 TLV，放摘要让后端按需拉取；③CRC32c（type 0x03）可对整个头校验，防中间设备改写。口径：PROXY protocol v2 = "LB → 后端的会话元数据快车"，TLS 终结架构里它是客户端身份信息的唯一通道。

**追问二**：后端解析 PROXY 头的实现里，"读到一半客户端断开"、"发来 HTTP 请求而不是 PROXY 头"这两种异常路径怎么处理？—— 异常路径设计：①**半头断开**——recvn 循环里 chunk 为空即对端关闭，头没读全：直接关闭并计数告警（正常 LB 不会半途断），要防止"半头 buf 无限等待"——整体加读取超时（如 5s）兜底；②**误连客户端**（直接发了 HTTP/TLS 数据）——第一个字节不是魔数/v1 的 "PROXY " 前缀：**立即关闭**，绝不把这段数据当业务处理（防止伪造流量绕过头检查进入业务层）；这就是 v2 魔数设计成 `\r\n\r\n\x00\r\nQUIT\n` 的深意——对 HTTP 客户端来说这串是"空行+异常字符"，而 `QUIT` 对部分协议是"断开指令"，历史原因让误解析最容易触发连接关闭；③**来源不匹配**——连接源 IP 不在 LB 白名单：不管发什么都按②处理并告警（这既是安全闸也是排障信号）；④**头后无业务数据**——cmd=LOCAL（健康检查）或空连接：按 LB 约定关闭。实现纪律：解析器是状态机（魔数→固定头→地址块→TLV），每步带长度上限与超时，任何一步失败统一走"关闭+分类计数"——把异常路径做成一等公民，PROXY 解析层的稳定性就有了下限。

## 背诵要点
- L4 透传下后端 peer 地址=LB；PROXY protocol 由 LB 在业务数据前注入头：v1 文本行（PROXY TCP4 src dst sport dport）可读，v2 二进制（12 字节魔数+ver/cmd+fam+长度+地址+TLV）是新部署标准。
- 铁律：头必须是连接第一个字节（误连即关闭）；只对 LB 白名单来源解析——端口直暴露公网则攻击者可伪造任意源 IP，风控/审计全废。
- 与 XFF 分工：PROXY 在 TCP 层（任何协议，含 TLS 终结后的 SNI/客户端证书 TLV 转述），XFF 在 HTTP 层逐跳追加（信任链 Q2186）；TLS 终结架构里 TLV 是后端拿客户端身份的唯一通道。

## 复盘追问
- 为什么 PROXY 头必须出现在第一个字节、伪造头怎么防？（解析器先读头再读业务，混流即废；防线=LB 来源白名单+长度上限+误连立即关闭，绝不让伪造头进入业务层）
- v2 的 TLV 为什么能携带 TLS 信息、后端该不该无条件信任？（LB 做 TLS 终结后客户端证书/SNI 只在 LB 侧存在，靠 TLV 转述；信任边界仍是 LB 白名单，LB 误配同样可伪造）
