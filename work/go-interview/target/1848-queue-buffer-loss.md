# 1848 建连队列与缓冲区丢包（服务端内侧）

> 分类：网络/TCP | 难度：L3 | 题型：八股题 | 频率：中 | 关键词：**半连接队列**/**全连接队列**/**零窗口**/**netstat**/**丢包**

> 原文锚点：第 3~12 段（三次握手/半连接队列/全连接队列/accept/队列满丢包/overflow 关键字）+ 第 23~42 段（发送/接收缓冲区/send/recv/TCP_RMEM/TCP_WMEM/零窗口/通知停止/仍发→丢包//proc/net/snmp/内核 5.9+）

## 一句话总述
建连与缓冲区两类丢包是**服务端内侧最常踩的坑**：半连接/全连接队列溢出会静默丢弃握手包，接收缓冲区满导致的**零窗口**则会在对端「仍发」时丢数据；二者都能用 `netstat -s` 与 `/proc/net/snmp` 定位。

## 面试官视角
这题考「内核队列与缓冲区」的实操认知。考点：① 半连接队列 vs 全连接队列分别何时满、怎么调（`tcp_max_syn_backlog` / `somaxconn`+backlog）；② 零窗口的成因与现象；③ 对应诊断命令与内核版本限制。能说出具体参数名和命令，是运维/后端高阶信号。

## 主问答
**Q（面试官原话）：** 服务端队列和缓冲区满了也会丢包？具体是什么队列、怎么查？

**A：**
1. **半连接队列（SYN 队列）溢出**：服务端收 SYN 后放入半连接队列，等待第三次握手；其大小受 `net.ipv4.tcp_max_syn_backlog` 限制。溢出时 `netstat -s` 出现 `SYNs to listened sockets ignored` / `ListenDrops`，新握手包被丢弃（也常被误判为 SYN flood）。
2. **全连接队列（accept 队列）溢出**：三次握手完成后连接进入全连接队列等待 `accept` 取走；大小 = `min(backlog, net.core.somaxconn)`。溢出时 `netstat -s` 出现 `ListenOverflows` / `Times the listen queue of a socket overflowed`，客户端连接被静默丢弃。
3. **接收缓冲区满 → 零窗口丢包**：接收方内核 recv buffer 满时，会在 ACK 中通告**窗口=0**，要求发送方停发；若发送方无视零窗口继续发，数据被丢弃。Linux 5.9+ 可在 `/proc/net/snmp` 的 `TcpExt.TCPBacklogDrop` 看到此类丢弃计数。
4. **收发缓冲区大小可调**：`net.ipv4.tcp_rmem`（min default max，单位字节）控制接收缓冲区，`net.ipv4.tcp_wmem` 控制发送缓冲区；应用层也可用 `SO_RCVBUF`/`SO_SNDBUF` 设置（见下 Go 示例）。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 有几个队列会溢出？ | 半/全连接队列区分 | 半连接(SYN) vs 全连接(accept) | 只说「队列」算 L1 未过 |
| L2 | 队列大小怎么定？ | 参数名 | 半连接=tcp_max_syn_backlog；全连接=min(backlog,somaxconn) | 无参数名算 L2 未过 |
| L3 | 零窗口是什么？ | 流控机制 | recv buf 满→通告窗口0→仍发则丢 | 说不清算 L3 未过 |
| L4 | 怎么查缓冲区丢包？ | 诊断命令 | /proc/net/snmp 的 TCPBacklogDrop（5.9+） | 不知命令算 L4 未过 |
| L5 | 应用层能调缓冲吗？ | SO_RCVBUF/SO_SNDBUF | setsockopt 设置，注意内核翻倍与上限 | 不知算 L5 未过 |

## 版本与兼容性
- `TcpExt.TCPBacklogDrop` 需 **Linux 5.9+**；旧内核改用 `netstat -s` 的 `TCPBacklogDrop` 行或 `ListenOverflows`/`ListenDrops` 推断。
- `tcp_rmem`/`tcp_wmem` 三元组为「最小/默认/最大」自动调节区间；`SO_RCVBUF` 设置后内核通常会**翻倍**（受 `tcp_rmem` 上限约束），这是常见认知坑。
- 全连接队列 = `min(listen backlog, net.core.somaxconn)`，二者都要看，调一个不调另一个会「看起来没生效」。

## 关键代码

```go
// 应用层调整接收缓冲区（注意：内核通常会把 SO_RCVBUF 翻倍，且受 tcp_rmem 上限约束）
func setRecvBuf(c net.Conn, size int) error {
	tc, ok := c.(*net.TCPConn)
	if !ok {
		return errors.New("not tcp conn")
	}
	raw, err := tc.SyscallConn()
	if err != nil {
		return err
	}
	return raw.Control(func(fd uintptr) {
		// SOL_SOCKET / SO_RCVBUF；设置值会被内核翻倍
		_ = unix.SetsockoptInt(int(fd), unix.SOL_SOCKET, unix.SO_RCVBUF, size)
	})
}

// 服务端 listen backlog 决定全连接队列上界（实际 = min(backlog, somaxconn)）
ln, _ := net.Listen("tcp", ":8080") // Go 默认 backlog 由系统 somaxconn 约束
_ = ln
```

## 总结与追问预判
收口：**内侧丢包两大源 = 建连队列溢出（半/全连接，查 `netstat -s`）+ 接收缓冲零窗口（查 `/proc/net/snmp` TCPBacklogDrop）**，参数层面 `tcp_max_syn_backlog`/`somaxconn`/`tcp_rmem` 可调。预判追问：① 网卡侧丢包 → 1848.md`；② 应用层如何用 `SO_RCVBUF` 兜底 → 见下方 Go 示例。回答时强调「队列溢出是静默丢、不报错」，是最隐蔽的一类。

## ⚠️ 原文纠错
源视频转写将半连接/全连接队列、零窗口、网卡队列长度(txqueuelen)、/proc/net/snmp 等音译为崩坏词（如「全链接队列」「半连接的对列」「TSqueenlenges」「leightstate 指代 snmp 文件」），本卡已还原为规范术语。交付卡禁止保留任何原词崩坏写法。

> **[经验]** 调全连接队列时**必须同时看 `listen(backlog)` 和 `net.core.somaxconn`**：实际生效值是二者取小。只改代码 backlog 不改 somaxconn，或反之，都会让人误以为「调了没生效」。这一条在排查「偶然连接超时」时极常用。
