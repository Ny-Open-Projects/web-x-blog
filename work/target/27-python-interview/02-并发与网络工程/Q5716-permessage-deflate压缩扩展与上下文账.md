---
title: "[Q5716] permessage-deflate：WebSocket 压缩扩展的协商与上下文成本"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5716 · permessage-deflate：WebSocket 压缩扩展的协商与上下文成本

难度：P7 ｜ 标签：permessage-deflate、RFC 7692、WebSocket 扩展、zlib、窗口位、CRIME

**问**：WebSocket 握手里的 `Sec-WebSocket-Extensions: permessage-deflate` 在协商什么？压缩上下文是"每帧独立"还是"跨帧共享"？参数 `server_max_window_bits=10` 意味着什么？为什么消息体积大但重复率低的场景压缩反而亏本？CRIME 类攻击对这个扩展有什么影响？

**答**：
结论：RFC 7692 定义了 WebSocket 的唯一标准化压缩扩展 permessage-deflate：握手阶段双方交换能力参数（启用与否、每端窗口位 8-15、上下文是否接管），协商一致后**所有后续数据帧**（文本与二进制消息）按 deflate（RFC 1951）压缩。核心语义：**压缩上下文跨消息共享**——上一条消息的字典保留到下一条，重复内容（聊天热词、JSON 键名、协议头部）持续受益，这也是它相对"每帧独立压缩"省流量的关键。参数：`server_max_window_bits=10` 表示服务端只用 2^10=1KB 的滑动窗口（客户端压缩时也必须用对应窗口，否则字典不匹配解压失败）；`no_context_takeover` 表示每消息重置上下文（牺牲压缩率换内存与状态简单）。亏本场景：deflate 有每帧 2 字节头 + 状态维护成本，随机数据压缩后可能**变大**，且 CPU 成本随窗口与内容上升——压缩收益 = 传输节省 × 带宽成本 − CPU 增加 × CPU 成本，纯随机二进制（加密、图片）应协商关闭。

取舍：a) 文本 JSON 高频小消息（聊天、行情）：上下文接管 + 默认 15 窗口收益最大；b) 大二进制低重复：在扩展协商里直接不发 offer，或发 `no_context_takeover`；c) 服务端内存账：每连接持一对 zlib 压缩/解压上下文（各数百 KB 级，取决于窗口），万级长连接的上下文内存要进容量账（Q6054）；d) 安全：跨上下文压缩给 CRIME 类攻击开了门（攻击者控制部分明文、观察密文长度推断秘密）——敏感 payload 混合用户可控内容时压缩是信道泄漏面，高危场景禁用或隔离上下文；e) 与反代联动：中间层要透传 Sec-WebSocket-Extensions 头，Nginx 老版本会剥离导致降级为不压缩——功能静默丢失类事故的典型。

实战：事故形态是"长连接行情推送开 permessage-deflate 后网关 CPU 翻倍：每条消息压缩收益 30% 但单机连接 5 万，每条消息都过一遍 zlib；修复为小消息聚合再压缩 + 窗口降到 10 + 对二进制快照帧关闭压缩（no_context_takeover）"。下面演示协商与压缩账。

```python
import zlib


def negotiate(client_offers, server_ok=True):
    """RFC 7692 协商: 返回接受参数或 None"""
    for offer in client_offers:
        parts = [p.strip() for p in offer.split(";")]
        if parts[0] != "permessage-deflate" or not server_ok:
            continue
        params = dict(p.split("=", 1) for p in parts[1:] if "=" in p)
        return {
            "accepted": True,
            "server_max_window_bits": int(params.get("server_max_window_bits", 15)),
            "no_context_takeover": "no_context_takeover" in parts,
        }
    return {"accepted": False}


neg = negotiate(["permessage-deflate; server_max_window_bits=10", "permessage-deflate"])
print("[1] 协商结果:", neg)

hot = '{"sym":"AAPL","bid":100.1,"ask":100.2,"sym":"AAPL","bid":100.1,"ask":100.2}'


def frame(payload: bytes, bits: int, ctx=None):
    co = ctx or zlib.compressobj(level=6, wbits=-bits)
    return co.compress(payload) + co.flush(zlib.Z_SYNC_FLUSH), co


w = neg["server_max_window_bits"]
b1, ctx = frame(hot.encode(), w)
b2, ctx = frame(hot.encode(), w, ctx)
print(f"[2] 窗口 {w}: 首帧 {len(b1)}B(含字典热身), 复用上下文第二帧 {len(b2)}B, 原始 {len(hot)}B")

rnd = b"\x9a\x3f" * 512  # 高熵数据: 压缩可能变大
r1, _ = frame(rnd, w)
print("[3] 随机数据压缩后:", len(r1), "B vs 原始", len(rnd), "B -> 该类流量应协商关闭")
```

**追问一**：为什么压缩帧要用 `wbits=-15`（负值）？—— permessage-deflate 使用 **raw deflate**（RFC 1951）：不带 zlib 头（RFC 1950 的 2 字节头 + adler32 校验尾）。`zlib.compressobj(wbits=15)` 产出带 zlib 包装的流，而 WebSocket 扩展自己管帧边界、不需要再套一层流头，所以必须用 `wbits=-15`（负数=raw）。配套细节：消息结尾用 `Z_SYNC_FLUSH` 而不是 `Z_FINISH`——finish 会终结压缩流破坏跨消息上下文，sync flush 保持字典与状态、只把数据推干净。用错 wbits/flush 是自研 WS 服务端"解压失败/字典错位"的头号根因。

**追问二**：服务端上下文内存怎么算，怎么压账？—— 每连接两个 zlib 状态：压缩器 + 解压器，窗口 15 时各占用约 256KB 级（window + hash 表），窗口 10 时显著缩小（2^10=1KB 窗口，hash 表随之缩）。5 万连接 × 512KB ≈ 25GB——这就是大连接数服务必须降窗口或 `no_context_takeover` 的原因（no_context_takeover 每消息重建，CPU 换内存）。容量公式：上下文内存 ≈ 连接数 × (2 × 窗口相关常数)，把它和每连接内核缓冲（Q5586）一起计入"每连接常驻成本"，再决定是否值得开压缩。

## 背诵要点
- permessage-deflate（RFC 7692）：握手协商窗口位与上下文接管，压缩上下文跨消息共享，热词/JSON 键名持续受益。
- raw deflate 用 zlib.compressobj(wbits=-N) + Z_SYNC_FLUSH；Z_FINISH 会破坏跨帧上下文。
- 账本：每连接一对压缩/解压上下文（窗口 15 约 512KB 级）；随机数据压缩变大，应协商关闭；CRIME 类信道泄漏要防。

## 复盘追问
- WS 网关开压缩后 CPU 翻倍，怎么调？（聚合小消息、降窗口、二进制帧关压缩、算上下文内存账）
- 自研服务端解压偶发失败，最可能的根因？（wbits 正负用错 / Z_FINISH 终结了共享上下文）
