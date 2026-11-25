---
title: "[Q5719] WebSocket 关闭码：1006 幽灵断开与关闭握手纪律"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5719 · WebSocket 关闭码：1006 幽灵断开与关闭握手纪律

难度：P6 ｜ 标签：WebSocket、关闭码、1005、1006、close frame、重连策略

**问**：客户端日志里全是"closed with 1006"，但 RFC 里 1006 到底是什么——它会在报文里出现吗？1005 和 1006 的区别是什么？哪些关闭码是"必须回应"的错误码？优雅关闭的完整帧序列是什么，跳过 close frame 直接断 TCP 会导致什么？

**答**：
结论：WebSocket 的关闭协商是**应用层帧**（opcode 0x8，2 字节状态码 + UTF-8 原因）：主动方发 close frame，被动方回一个 close frame（**不得重复回**），然后才允许断 TCP。状态码分三层：1xxx 协议级（1000 正常、1001 端点离开、1002 协议错误、1003 不接受的数据类型、1007 数据不一致、1008 策略违规、1009 消息过大、1010 客户端要求扩展、1011 服务端内部错误）、3xxx 注册段、4xxx 私有段；1000-2999 里 1004/1005/1006 **禁止在报文里出现**——它们是"给实现留的合成码"。**1005** = 对端发了 close frame 但没带状态码；**1006** = **连接异常死亡**（TCP 断了/超时/没收到 close frame），由本端实现合成，用于告知应用层"没有收到对方的关闭意图"——所以 1006 大量出现 = 网络层异常断开（NAT 超时、进程被杀、LB 闲置回收），不是应用主动关。跳过 close frame 直接 RST/FIN 的后果：对端无法区分"正常关闭"与"崩溃"，只能报 1006，触发重连风暴（Q5603）与消息确认状态机的重置成本。

取舍：a) 服务端踢除慢连接/限流超限：发 1008（策略违规）+ 原因文本，让客户端能区分"被管理性断开"（退避重连）与"网络故障"（立即重连）；b) 应用级自定义码用 4000-4999 私有段（如 4001 限流、4002 会话过期），配重连策略矩阵；c) 客户端收到 close frame 后必须**回一个** close frame 再断——回码通常镜像或 1000，回 1011 只在自身错误时；d) 关闭码 + 原因的总长限制 123 字节（控制帧上限 125 减 2），原因超长会触发协议错误；e) 排障矩阵：1006 高频 = 看网络层（idle 超时、LB、NAT）；1001 = 端点正常离开（页面关闭）；1009 = 消息大小限制（Q6218）；1011 = 服务端异常——先分码再查因，别一律当网络抖动。

实战：事故形态是"发布滚动重启时旧实例直接 kill -9，客户端全部报 1006 并立即重连，新实例被连接风暴打挂；修复为 SIGTERM 时服务端发 close(1001, 'server restart') 等待 3 秒再退出，客户端见到 1001 使用指数退避而不是立即重连，重连峰值下降 95%"。下面实现关闭码解析器与合成逻辑。

```python
import struct

VALID_PROTOCOL = {1000, 1001, 1002, 1003, 1007, 1008, 1009, 1010, 1011}


def parse_close(payload: bytes):
    """解析 close frame 负载, 返回 (状态码, 原因, 是否协议错误)"""
    if len(payload) == 0:
        return 1005, "no status code", False      # 1005: 合成码
    if len(payload) == 1:
        return 1002, "invalid close payload", True
    code = struct.unpack("!H", payload[:2])[0]
    try:
        reason = payload[2:].decode("utf-8")
    except UnicodeDecodeError:
        return 1002, "reason not utf-8", True
    if code in (1004, 1005, 1006) or code == 1005:
        return 1002, f"reserved code {code} in wire", True
    if not (VALID_PROTOCOL and (code in VALID_PROTOCOL or 3000 <= code <= 4999)):
        return 1002, f"invalid code {code}", True
    return code, reason, False


def synthesize(wire_seen: bool, tcp_dead: bool):
    """本端未收到合法 close frame 时的合成码"""
    if not wire_seen and tcp_dead:
        return 1006   # 幽灵断开: TCP 层死亡, 无应用关闭意图
    if not wire_seen:
        return 1005   # 有 close 帧但无状态码
    return None


print("[1] 正常关闭:", parse_close(struct.pack("!H", 1001) + "server restart".encode()))
print("[2] 空负载 -> 1005:", parse_close(b"")[:2])
print("[3] 报文携带 1006 -> 协议错误:", parse_close(struct.pack("!H", 1006))[:2])
print("[4] 私有段:", parse_close(struct.pack("!H", 4001) + "rate limited".encode()))
print("[5] TCP 异常断开 -> 本端合成 1006:", synthesize(False, True), "(1006 永不出现在报文中)")
```

**追问一**：为什么收到 close frame 后"回一个"是强制的，而"回两个"是错的？—— RFC 6455 的关闭握手设计成"请求-确认"：第一方发 close 表示"我想关"，对方必须回 close 表示"我知道了"，之后**先发的一方**等待对方帧、后发的一方可以立即断 TCP。如果双方都各自再回一次，就变成无限乒乓；如果被动方不回直接断，主动方只能合成 1006（把协商好的关闭误判为异常）。实现的常见 bug 是在收到 close 后又处理了一条消息才回 close——标准要求收到 close 后**立即**停止发送数据帧，先回 close。

**追问二**：重连策略怎么按关闭码分级？—— 三级矩阵：①1008/4001（策略类）——退避重连（指数 + 抖动，Q2901），可能被服务端暂时拉黑；②1001/1000（正常离开）——若客户端是 SPA 页面关闭场景无需重连；服务端滚动重启场景用指数退避；③1006/1011（异常类）——立即重连 + 快速上限，但要有**连接风暴保护**：全局并发重连数限制与随机延迟（否则一次全网断线同时重连就是 DDoS 自己）。所有策略都应带重连预算与告警，1006 占比持续 > x% 直接触发网络层排查（LB idle timeout、NAT 会话时长）而不是应用层修修补补。

## 背诵要点
- 关闭握手 = close frame 请求-确认各一次；1004/1005/1006 是合成码，禁止出现在报文中。
- 1005 = close 帧无状态码；1006 = 未收到 close 帧 TCP 即死（NAT 超时/被杀/LB 回收）——高频 1006 查网络层。
- 踢人用 1008/私有段 4xxx 配分级重连策略；滚动重启先发 1001 再退出；重连要有全局风暴保护。

## 复盘追问
- 滚动重启后客户端 1006 风暴打挂新实例，怎么修？（SIGTERM 先发 close(1001)，客户端按码分级退避重连）
- 1005 和 1006 的区别？（有 close 帧但无码 vs 无 close 帧 TCP 直接死；都是本端合成）
