# 14. 后端校招面试直通车: TCP 粘包的原理与三种解法

## 纲要

- TCP 是面向字节流的协议，本身没有"消息""包"的概念
- 粘包的本质：应用层未能正确界定消息边界
- HTTP 是怎么做的：用 Content-Length 标识消息体长度
- 两种通用解法：基于长度的拆分、基于特殊分隔符的拆分
- Nagle 算法为什么会放大粘包问题
- Go 实战：复现粘包 + 用长度前缀法解决

## 粘包的本质

很多应用层协议都把 TCP 作为传输层协议，因为 TCP 提供了可靠、有连接的服务，并且解决了数据顺序问题。但 TCP 是**面向字节流的传输协议**，它只保证字节按顺序、完整地送达，**不识别数据边界**。

这意味着一个重要结论：**粘包不是 TCP 协议的缺陷，而是应用层协议设计缺陷导致的问题**。TCP 没有"消息"和"数据包"的概念，把字节流切分成一条条业务消息，是应用层自己的职责。

所谓粘包，就是数据在应用层被错误地组合或拆分：

- 两个报文被当成一条消息解析
- 一条消息被拆成两个报文处理
- 多个 send 写入的数据在一次 receive 中全部读出

这几种情况都会导致业务数据被错误解释。

## HTTP 是怎么解决边界问题的

HTTP 是构建在 TCP 之上的应用层协议，它界定消息边界的方式是使用 **Content-Length** 这个实体首部：

- Content-Length 是 HTTP 的首部字段（Header）
- 它的值是一个十进制数字，表示发送给接收方的**消息主体的字节大小**
- 接收方读到 Content-Length 指定的字节数后，就知道这条消息结束了

由此可以反推一个结论：如果 Content-Length 的值与实际内容长度不一致，HTTP 就无法拿到完整的报文——可能截断，也可能多读，这对协议来说是不可接受的，会直接报错。

这个例子说明了一件事：**边界必须由应用层自己声明**。

## 两种通用解法

| 解法 | 思路 | 代表 |
| --- | --- | --- |
| 基于长度 | 在消息头部声明消息体的字节长度，接收方按长度读取 | HTTP 的 Content-Length、自定义协议的 4 字节长度前缀 |
| 基于分隔符 | 在字节流中约定一个特殊分隔符，按分隔符切分 | 按 `\n` 切分的文本协议、Redis RESP 的 CRLF |

基于长度的方式更通用，也更适合二进制协议；基于分隔符的方式简单直观，但要求消息体中不能出现分隔符，否则需要转义。

## Nagle 算法与粘包

Nagle 算法是一个**通过减少小数据包来提升 TCP 传输性能**的算法。早期网络带宽有限，如果每个小数据块都立刻发出去，带宽利用率极低。

举例：telnet 这类协议一次可能只传输 1 个字节数据，而 TCP 首部加 IP 首部至少 40 字节，带宽利用率约为 `1 / (40 + 1) ≈ 2.44%`。

Nagle 算法的做法是：不把小数据块直接发往目的主机，而是先在本端缓冲区等待，凑够更多待发送数据后批量发送。触发发送的条件有两个：

- 缓冲区数据达到最大报文段长度（MSS）
- 上一个数据段已被确认

代价是影响实时性、增大延迟；收益是降低网络拥塞概率、减少额外开销。

**Nagle 算法与粘包的关系**：它把多个小报文合并进同一个 TCP 报文发送，接收方一次读到的数据就可能包含多条业务消息。因此启用 Nagle 时，应用层必须正确拆分数据，否则必然出现粘包。

反过来说，即使关闭 Nagle（如 Go 的 `net.TCPConn.SetNoDelay(true)`，Go 默认即开启），粘包依然可能发生——因为接收方一次 `Read` 的缓冲区大小与发送方的写入次数毫无关系。

## Go 实战：复现粘包并用长度前缀法解决

下面用一个可运行的示例完整演示：先复现粘包，再用 4 字节长度前缀的自定义协议解决它。

### 完整代码

```go
package main

import (
	"bufio"
	"encoding/binary"
	"fmt"
	"io"
	"net"
	"time"
)

// messages 模拟业务层连续发出的四条消息
var messages = []string{"hello", "world", "hello", "golang"}

// encode 使用 4 字节大端长度前缀对消息封帧
func encode(msg string) []byte {
	buf := make([]byte, 4+len(msg))
	binary.BigEndian.PutUint32(buf[:4], uint32(len(msg)))
	copy(buf[4:], msg)
	return buf
}

// serveSticky 启动服务端，只做一次大缓冲 Read，用于复现粘包
func serveSticky() string {
	ln, err := net.Listen("tcp", "127.0.0.1:0")
	if err != nil {
		panic(err)
	}
	go func() {
		conn, err := ln.Accept()
		if err != nil {
			return
		}
		defer conn.Close()
		// 稍作等待，让客户端的多次写入都到达本端缓冲区，
		// 从而稳定复现"一次读出多条消息"的粘包现象
		time.Sleep(100 * time.Millisecond)
		buf := make([]byte, 1024)
		n, _ := conn.Read(buf)
		fmt.Printf("[粘包] 一次 Read 收到 %d 字节: %q\n", n, buf[:n])
	}()
	return ln.Addr().String()
}

// serveFramed 启动服务端，按长度前缀逐条解帧
func serveFramed() string {
	ln, err := net.Listen("tcp", "127.0.0.1:0")
	if err != nil {
		panic(err)
	}
	go func() {
		conn, err := ln.Accept()
		if err != nil {
			return
		}
		defer conn.Close()
		r := bufio.NewReader(conn)
		for i := 0; i < len(messages); i++ {
			head := make([]byte, 4)
			if _, err := io.ReadFull(r, head); err != nil {
				return
			}
			body := make([]byte, binary.BigEndian.Uint32(head))
			if _, err := io.ReadFull(r, body); err != nil {
				return
			}
			fmt.Printf("[定长解帧] 第 %d 条: %q\n", i+1, body)
		}
	}()
	return ln.Addr().String()
}

// serveDelim 启动服务端，按换行符逐条切分
func serveDelim() string {
	ln, err := net.Listen("tcp", "127.0.0.1:0")
	if err != nil {
		panic(err)
	}
	go func() {
		conn, err := ln.Accept()
		if err != nil {
			return
		}
		defer conn.Close()
		scanner := bufio.NewScanner(conn)
		scanner.Split(bufio.ScanLines)
		for i := 0; i < len(messages) && scanner.Scan(); i++ {
			fmt.Printf("[分隔符解帧] 第 %d 条: %q\n", i+1, scanner.Text())
		}
	}()
	return ln.Addr().String()
}

func dial(addr string) net.Conn {
	conn, err := net.Dial("tcp", addr)
	if err != nil {
		panic(err)
	}
	return conn
}

func main() {
	// 场景一：连续写入，服务端一次读出全部内容，产生粘包
	addr := serveSticky()
	conn := dial(addr)
	for _, m := range messages {
		conn.Write([]byte(m))
	}
	time.Sleep(300 * time.Millisecond)
	conn.Close()

	// 场景二：基于长度前缀封帧
	addr = serveFramed()
	conn = dial(addr)
	for _, m := range messages {
		conn.Write(encode(m))
	}
	time.Sleep(300 * time.Millisecond)
	conn.Close()

	// 场景三：基于分隔符封帧
	addr = serveDelim()
	conn = dial(addr)
	for _, m := range messages {
		conn.Write(append([]byte(m), '\n'))
	}
	time.Sleep(300 * time.Millisecond)
	conn.Close()
}
```

### 运行说明

> 以下代码根据讲稿所述的 socket 发送/接收逻辑补充实现，用于直观复现粘包与验证解帧方案。

将代码保存为 `main.go`，执行：

```bash
go run main.go
```

典型输出：

```text
[粘包] 一次 Read 收到 21 字节: "helloworldhellogolang"
[定长解帧] 第 1 条: "hello"
[定长解帧] 第 2 条: "world"
[定长解帧] 第 3 条: "hello"
[定长解帧] 第 4 条: "golang"
[分隔符解帧] 第 1 条: "hello"
[分隔符解帧] 第 2 条: "world"
[分隔符解帧] 第 3 条: "hello"
[分隔符解帧] 第 4 条: "golang"
```

### 代码说明

- **场景一（粘包复现）**：客户端连续四次 `Write`，每次写入一个单词；服务端只用一次 `Read` 且缓冲区为 1024 字节，一次性把 21 字节全部读出，四条消息粘成了一条。这与讲稿中"send hello / send world / send hello / send golang，一次 receive 得到全部内容"完全对应。为了让现象稳定复现，服务端在读之前先等待 100ms；实际生产中如果不做这层等待，一次 `Read` 也可能只读到其中一部分（半包），这同样是字节流协议的正常表现。
- **场景二（长度前缀）**：`encode` 在每条消息前加 4 字节大端长度头；服务端先 `io.ReadFull` 读满 4 字节得到长度，再按长度读取消息体。注意这里必须用 `io.ReadFull` 而不是普通 `Read`，因为 `Read` 不保证一次读满。
- **场景三（分隔符）**：每条消息末尾追加 `\n`，服务端用 `bufio.Scanner` + `bufio.ScanLines` 按行切分。
- 三个服务端都监听 `127.0.0.1:0`，由内核分配空闲端口，通过 `ln.Addr()` 取回实际地址，避免端口冲突。

### 技术点总结

- TCP 面向字节流，不保留消息边界，写入次数与读取次数没有对应关系
- 粘包是应用层协议设计问题，必须在应用层自行定义消息边界
- 长度前缀法：通用、适合二进制协议，务必用 `io.ReadFull` 读满固定长度的头与体
- 分隔符法：实现简单，需要处理消息体内的分隔符转义
- Nagle 算法会合并小包，进一步放大粘包概率；Go 默认关闭 Nagle（`SetNoDelay(true)`），但关闭它并不能消除粘包

## API 速览

| API | 签名 | 说明 |
| --- | --- | --- |
| `net.Listen` | `func Listen(network, address string) (Listener, error)` | 监听端口，地址写 `:0` 由内核分配空闲端口 |
| `Listener.Accept` | `func Accept() (Conn, error)` | 阻塞等待并接受一个连接 |
| `net.Dial` | `func Dial(network, address string) (Conn, error)` | 建立 TCP 连接 |
| `Conn.Read` | `func Read(b []byte) (n int, err error)` | 读一次数据，**不保证读满**，可能少于 `len(b)` |
| `io.ReadFull` | `func ReadFull(r Reader, buf []byte) (n int, err error)` | 保证读满 `len(buf)`，解固定长度帧时必须使用 |
| `binary.BigEndian.PutUint32` | `func PutUint32(b []byte, v uint32)` | 以大端序写入 4 字节长度，保证跨机器一致 |
| `bufio.NewScanner` | `func NewScanner(r io.Reader) *Scanner` | 构造扫描器，配合 `Split` 可按分隔符切分流 |
| `TCPConn.SetNoDelay` | `func (c *TCPConn) SetNoDelay(noDelay bool) error` | 关闭/开启 Nagle 算法，Go 默认为 `true`（关闭） |

### 分隔符解帧的最小示例

```go
// 按换行符从 TCP 字节流中逐条读取消息
scanner := bufio.NewScanner(conn)
scanner.Split(bufio.ScanLines)
for scanner.Scan() {
    fmt.Printf("收到: %q\n", scanner.Text())
}
if err := scanner.Err(); err != nil {
    fmt.Println("连接异常:", err)
}
```

## 面试答题要点

- 先定性：粘包不是 TCP 的问题，TCP 面向字节流、没有消息边界；是应用层没有正确拆分数据
- 描述现象：多个报文被错误地合并解析，或一个报文被错误拆分
- 给解法：基于长度（Content-Length / 长度前缀）与基于分隔符两种
- 主动加分：提到 Nagle 算法——它合并小包以提升带宽利用率，但会加剧粘包，接收方必须正确拆包
- 工程细节：读定长头与定长体要用 `io.ReadFull`；长度字段要约定字节序

