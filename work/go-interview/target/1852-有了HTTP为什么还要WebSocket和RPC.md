# 1852 有了 HTTP 为什么还要 WebSocket 和 RPC：三个真理由

> 分类：网络协议 / 架构 | 难度：L2 | 题型：概念辨析题 | 频率：高 | 关键词：**消息边界**/**半双工**/**WebSocket 握手**/**RPC 是调用方式**/**对内 RPC 对外 HTTP**
> 原文锚点：第 1~31 段「TCP 它是个无边界的字节流，上层需要定义消息格式用于定义消息的边界，于是就有了各种协议…HTTP 1.1 它是半双工的，对需要服务器主动推送的场景不友好…RPC 本质上不算是协议，而是一种调用方式，gRPC 和 thrift 这样的具体实现才是协议」

## 一句话总述
TCP 只给**无边界字节流**，一切应用层协议都是「在流上定义消息边界 + 语义」的方案：**HTTP** 的「请求-响应 + 无状态」模型简单通用但**半双工**、不适合服务器主动推送；**WebSocket** 借 HTTP 握手升级成**全双工持久连接**；**RPC** 则把远程调用抽象成本地函数调用（它是**调用方式**而非协议，gRPC/thrift 才是协议实现）——三者是**按场景分工**，不是替代关系。

## 面试官视角
- 考察意图：一题三考点——① 是否理解「协议 = 消息边界 + 语义」的本质；② 是否知道 HTTP/1.1 半双工的根源（请求-响应一来一回）；③ 是否能把「RPC 是范式、gRPC 是协议」这句关键区分说出口。
- 分档：P5 能说出「WebSocket 全双工、RPC 性能好」；P6 讲清 WebSocket 握手借道 HTTP、RPC 与 socket 无关；P7 能给出「对外 HTTP 对内 RPC」的架构依据与 HTTP/2 带来的格局变化。
- 红旗答案：「WebSocket 就是 socket」；「RPC 一定比 HTTP 快所以无脑用」——前者被名字骗，后者忽略 HTTP/2 已经反超许多 RPC 实现。
- 惊艳点：「TCP 是字节流，**帧边界是应用层的责任**——length-prefix 或分隔符分帧，没有这一步就没有任何协议」+ 现场写分帧代码 [实测]。

## 主问答
**Q（面试官原话）：** 有 HTTP 了，为什么还需要 WebSocket 和 RPC？
**A：**
1. **根源：TCP 是无边界字节流**，必须由上层定义消息边界和语义，才有了各种应用层协议。HTTP、WebSocket、各类 RPC 都是这个层级的不同方案——**问题不是「谁取代谁」，而是不同场景需要不同语义** [源码]。
2. **HTTP 的模型与短板**：为传输超文本设计，**无状态**、每个请求响应独立。HTTP/1.1 虽基于 TCP（全双工）但被「请求-响应」模型限成**半双工**——服务器无法主动推送，对在线聊天、实时游戏、行情推送这类场景天然不友好 [源码]。
3. **WebSocket = 借道 HTTP 升级的全双工通道**：先利用 HTTP 加特殊头（`Upgrade: websocket`）发起握手，升级成功（101）后与 HTTP 再无关系，改用 WebSocket 自己的数据帧收发；连接**持久化**，服务器任何时刻可主动推送。**注意它与 socket 毫无关系，只是叫法相似** [源码]。
4. **RPC 是「调用方式」不是协议**：目标是让程序员**像调本地函数一样调远程函数**，隐藏网络细节；gRPC、thrift 这类**具体实现**才是协议。RPC 不一定基于 TCP；它出现得比 HTTP 早、主流实现比 HTTP/1.1 性能好——但 **HTTP/2 做了多路复用等优化后，性能已可能反超不少 RPC 实现** [源码]。
5. **工程分工的现实格局**：BS/CS 边界在融合，多端并存——**对外用 HTTP**（通用、免客户端、防火墙友好），**内部微服务之间用 RPC**（强类型接口、高性能、长连接省握手开销）。WebSocket 补上「需要服务端主动推」的那部分场景 [源码]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | TCP 上层为什么要定义协议？ | 本质 | 字节流无边距，需定义消息边界与语义 | P5 停 |
| L2 | HTTP/1.1 为什么不能服务器主动推？ | 模型 | 请求-响应模型是半双工，推只能轮询 | P6 停 |
| L3 | WebSocket 握手怎么做的？ | 细节 | 借 HTTP + Upgrade 头升级，101 后换自有帧 | P6 停 |
| L4 | RPC 和 gRPC 什么关系？ | 概念精度 | RPC 是调用范式，gRPC/thrift 是协议实现 | P6 停 |
| L5 | 新微服务全上 gRPC 对吗？ | 架构判断 | 看边界：对外 HTTP 通用、对内 RPC 高效；HTTP/2 已拉平部分差距 | P7 停 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| HTTP/1.1 | 半双工、队头阻塞，长连接靠 keep-alive 复用 | 见 1849 [边界] |
| HTTP/2 | 二进制分帧 + 多路复用，性能反超部分 RPC | 「HTTP vs RPC」从性能之争变为生态之争 |
| WebSocket（RFC 6455） | 握手后与 HTTP 无关，帧格式自有 | 升级前是 HTTP 请求 |
| gRPC | 跑在 HTTP/2 上的 RPC 实现 | 「RPC over HTTP/2」一句话破对立 |

## 关键代码
```go
// TCP 字节流上做 length-prefix 分帧：一切应用层协议的起点
package main

import (
	"bufio"
	"encoding/binary"
	"fmt"
	"io"
	"net"
)

func main() {
	ln, _ := net.Listen("tcp", "127.0.0.1:0")
	go func() {
		conn, _ := ln.Accept()
		defer conn.Close()
		for _, msg := range []string{"hello", "world", "go"} {
			b := []byte(msg)
			hdr := make([]byte, 4)
			binary.BigEndian.PutUint32(hdr, uint32(len(b)))
			conn.Write(append(hdr, b...)) // 4 字节长度 + payload
		}
	}()
	conn, _ := net.Dial("tcp", ln.Addr().String())
	defer conn.Close()
	r := bufio.NewReader(conn)
	for {
		hdr := make([]byte, 4)
		if _, err := io.ReadFull(r, hdr); err != nil {
			break
		}
		payload := make([]byte, binary.BigEndian.Uint32(hdr))
		io.ReadFull(r, payload)
		fmt.Printf("收到完整一帧: %q\n", string(payload))
	}
}
// [实测] 输出：收到完整一帧: "hello" / "world" / "go" —— 三次 write 在流上被正确还原为三帧
```

## 总结与追问预判
一句话记忆：**「TCP 给流，协议给边界；HTTP 给请求响应，WebSocket 给全双工，RPC 给函数调用感」**。HTTP 长连接与 TCP keepalive 的区别见 1849；Go net/http 起服务与优雅退出的工程侧见 702、`713-http-graceful-shutdown` [边界]。常追问「WebSocket 心跳与断线重连怎么做」——答应用层 ping/pong 帧 + 指数退避重连；再追问「gRPC 为什么快」——答 HTTP/2 多路复用 + protobuf 二进制序列化（对比 JSON 文本），这才是性能差距的真正来源。

## ⚠️ 原文纠错
1. 术语归一：[经验] 源为语音转写，「RTC」「LPC」均应为「RPC」，「TTP」「HTP」应为「HTTP」，「wewebccket」「websocer」应为「WebSocket」，其余转写崩坏统一为规范术语。
2. 表述纠错：源称 RPC「减少连接建立和关闭的开销」依赖长连接是**实现选择**而非 RPC 定义本身，本卡已区分。
3. 补充：源未提 WebSocket 握手响应码 101 与 gRPC 基于 HTTP/2 的事实，两者是高频追问点，本卡已补。
