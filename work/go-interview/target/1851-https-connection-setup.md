# 1851 HTTPS 建连 vs HTTP：多出的是一个 TLS 握手

> 分类：网络协议 / 安全 | 难度：L2 | 题型：原理题 | 频率：高 | 关键词：**TLS 握手**/**对称密钥**/**证书链**/**change cipher spec**/**额外 RTT**
> 原文锚点：第 1~32 段「HTTPS 是在 HTTP 与 TCP 层之间加入了 TLS/SSL 协议将加密传输数据…第三步是 TLS/SSL 握手…client hello 包含客户端支持的 TLS 版本、加密套件和随机数…后续数据使用共享密钥加密」

## 一句话总述
HTTPS = HTTP + **TLS 层**（夹在 HTTP 与 TCP 之间）。建连流程比 HTTP 多出整个 **TLS 握手**：DNS → TCP 三次握手 → **TLS 四步握手**（ClientHello / ServerHello+证书 / 客户端密钥交换+ChangeCipherSpec+Finished / 服务端 ChangeCipherSpec+Finished）→ 加密的 HTTP 请求响应 → 四次挥手。**HTTP 是一次 TCP 握手就能发数据，HTTPS 要多付 TLS 的往返与计算开销**，换来的是机密性、完整性与身份认证。

## 面试官视角
- 考察意图：区分「背过 HTTPS 是加密的」与「真正理解建连全流程」——面试官要从你说 DNS 开始的完整叙述中判断你是否画得出时序图。
- 分档：P5 知道 HTTPS = HTTP + TLS、明文 vs 密文；P6 能按序讲全五步（DNS/TCP/TLS/HTTP/挥手）与握手消息名；P7 能答出 TLS 1.2 vs 1.3 的往返差异、共享密钥由三个随机数推导。
- 红旗答案：「HTTPS 建连就是三次握手加验证一下证书」——漏掉密钥交换与 ChangeCipherSpec 两个状态切换点；以为 TLS 在应用层之上。
- 惊艳点：「**HTTP 在 TCP 之上、TLS 在两者之间**——分层位置决定建连顺序：先 TCP 后 TLS，所以 HTTPS 建连 = TCP 握手 + TLS 握手两段开销」+ 实测本地握手耗时 [实测]。

## 主问答
**Q（面试官原话）：** HTTPS 建立连接跟 HTTP 相比有什么区别？
**A：**
1. **本质区别：多了 TLS 加密层**。HTTP 明文传输易截获篡改；HTTPS 在 HTTP 与 TCP 之间插入 TLS/SSL，数据加密传输。**分层位置决定建连顺序**——TLS 之下是 TCP，所以必须先完成 TCP 三次握手（SYN / SYN+ACK / ACK，实测流程见 `1843-tcp-handshake-recap` [边界]），再开始 TLS 握手 [源码]。
2. **TLS 握手第一步（ClientHello）**：客户端发送支持的 **TLS 版本、加密套件列表、客户端随机数**——随机数是后续生成对称密钥的材料之一 [源码]。
3. **TLS 握手第二步（服务端三连发）**：ServerHello（选定版本、加密方法、会话 ID、服务端随机数）→ Certificate（**证书链**：域名、发行方、有效期）→ ServerKeyExchange（公钥/签名），可选 CertificateRequest 要求客户端证书 [源码]。
4. **TLS 握手第三、四步（双向确认切换加密）**：客户端验证证书后发 ClientKeyExchange（用服务端公钥加密的预主密钥/随机串）→ **ChangeCipherSpec**（通知：从现在起我加密了）→ Finished（加密的握手摘要）；服务端同样回 ChangeCipherSpec + Finished。**双方用「客户端随机数 + 服务端随机数 + 预主密钥」推导出对称会话密钥** [源码]。
5. **之后才是正常的 HTTP**：加密通道就绪，HTTP 请求响应在密文上进行；结束仍走 TCP 四次挥手。**总结：HTTPS 建连 = HTTP 建连 + 完整 TLS 握手**，TLS 1.2 下多约 2 个 RTT、TLS 1.3 压缩到 1 个 RTT（见深卡 [边界]）。本地实测：纯 TCP 连接 **397µs**，TLS1.3 握手 **1.80ms**（localhost 无 RTT 开销，广域网差距按 RTT 数放大） [实测]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | HTTPS 和 HTTP 的本质区别？ | 概念 | 多了 TLS 加密层：机密性+完整性+身份认证 | P5 停 |
| L2 | HTTPS 建连完整流程？ | 全景 | DNS→TCP 握手→TLS 握手→HTTP→四次挥手 | P6 停 |
| L3 | TLS 握手交换了什么？ | 细节 | 版本/套件/随机数/证书链/密钥交换 | P6 停 |
| L4 | 对称密钥怎么来的？ | 密码学 | 三方材料：客户端随机数+服务端随机数+预主密钥 | P7 停 |
| L5 | TLS 握手多花几个 RTT？ | 量化 | 1.2 约 2 个、1.3 优化到 1 个 | P7 停 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| TLS 1.2 | 握手约 2 个 RTT，RSA 密钥交换无前向安全 | 按源流程答，注意 1.2 与 1.3 消息集不同 |
| TLS 1.3 | **1-RTT 握手**（ClientHello 捎带 key share）、删 RSA 静态交换、0-RTT 可选恢复 | 现代答法： fewer 消息 + 前向安全 |
| HTTP/2 | 实践中几乎强制 TLS（浏览器 h2 仅 TLS） | h2c 明文只限内部 |
| QUIC/HTTP/3 | 把传输+TLS 融合进 UDP，握手 0/1-RTT | 下一步演进：TLS 不再夹层而是内嵌 |

## 关键代码
```go
// 实测: 纯 TCP 连接 vs TLS 握手 的耗时差 (localhost, TLS1.3)
// 服务端: tls.Listen + 自签证书; 客户端复用 TCP 连接后单独计时 Handshake
start := time.Now()
raw, _ := net.Dial("tcp", ln.Addr().String()) // 三次握手完成
tcpCost := time.Since(start)

tlsConn := tls.Client(raw, &tls.Config{InsecureSkipVerify: true})
start = time.Now()
tlsConn.Handshake() // ClientHello...Finished, 对称密钥就绪
tlsCost := time.Since(start)
// [实测] 纯 TCP 连接 397.461µs; TLS1.3 握手 1.798333ms —— localhost 无 RTT 也有约 4.5 倍差
// 广域网上 TLS1.2 多 2 个 RTT / 1.3 多 1 个 RTT, 差距按 RTT(数十 ms) 放大
```

## 总结与追问预判
一句话记忆：**「HTTPS = HTTP 夹一层 TLS；建连多一段握手，数据从明文变密文，密钥由两个随机数 + 预主密钥推导」**。TCP 握手与挥手细节见 `1843-tcp-handshake-recap`、`1849-http-vs-tcp-keepalive` [边界]。常追问「证书验证验什么」——答证书链到受信根 CA、域名匹配、有效期、签名与吊销状态；再追问「为什么用非对称交换密钥却用对称加密数据」——答非对称慢百倍、对称快，取长补短：非对称只护送预主密钥一次。

## ⚠️ 原文纠错
1. 术语归一：[经验] 源为语音转写，「TNS」应为 DNS，「SYS/SYSSSK/SCK」应为 SYN/SYN+ACK/ACK，「cls」应为 ClientHello，「servercontesting」应为 ServerKeyExchange，「excechangesaferesspect」应为 ChangeCipherSpec，「非利息」应为 Finished，「TRS/TRSSSL」应为 TLS，统一为规范术语。
2. 结构纠错：源把第二次握手中 ServerHello、Certificate、ServerKeyExchange、CertificateRequest、ServerHelloDone 压成一段且「最后发送 serverhello」表述错乱，实为 ServerHelloDone（通知握手消息发完），本卡已按标准时序重组。
3. 补充：源未提 TLS 1.3 的 1-RTT 与「三随机数推导对称密钥」的完整表述，均为高频考点，本卡已补。
