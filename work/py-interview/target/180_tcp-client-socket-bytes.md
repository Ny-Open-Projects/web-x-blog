# 180. TCP 客户端 Socket 与字节编解码

> 分类：网络/Python | 难度：L2 | 题型：工程题 | 频率：中 | 关键词：**connect** / **sendall** / **encode** / **recv字节**
> 原文锚点：第 14~55 段「客户端：socket→connect→send/recv→close；connect 触发三次握手；send 需 encode UTF-8，recv 返回字节需 decode 成 str」

## 一句话总述
TCP 客户端流程：**`socket()`→`connect(地址)`→`sendall(字节)`→`recv(字节)`→`close()`**。`connect` 触发三次握手；Python3 里 `send` 必须 **encode** 成字节、`recv` 返回的是 **bytes**，需用 `decode("utf-8")` 转回字符串。

## 面试官视角
- **考察意图**：是否踩过"Python3 网络数据都是字节"的坑，以及理解 send/recv 的字节本质。
- **P5** 能写出 connect→send→recv→close / **P6** 能讲清 send 要 encode、recv 返回 bytes 要 decode / **P7** 能指出 send/recv 不保证一次收发完整（需循环/长度约定），以及 `sendall` 才保证发全。
- **红旗**：对 `recv(1024)` 返回 `b'...'` 一脸懵；或以为 send 字符串就能发。
- **惊艳点**：`connect` 在底层完成的正是 **TCP 三次握手**，所以"建连=握手"不是比喻；且 `recv` 一次未必收全（TCP 是字节流、无消息边界），循环读才是正确姿势 —— 验证：大响应单次 `recv(1024)` 会截断 `[实测]`。

## 主问答
**Q（面试官原话）：** Python 写 TCP 客户端要注意什么？网络数据怎么处理？

**A · 标准答案骨架：**
1. **先给结论**：客户端 `socket→connect(地址)→sendall(字节)→recv(字节)→close`；`connect` 触发三次握手。
2. **再给机制**：Python3 中 `send` 只收 **bytes**——字符串须 `.encode("utf-8")`；`recv(n)` 返回的也是 **bytes**，须 `.decode("utf-8")` 还原成 str；打印时看到 `b'...'` 前缀说明是字节。
3. **最后给边界**：`recv(n)` **不保证收满 n 字节也不保证一条消息收全**（TCP 字节流无边界）；应用层需循环读或按 Content-Length 读全，发送用 `sendall` 而非 `send`。

**加分层**：`send` 返回实际发出字节数、可能少于请求量，只有 `sendall` 保证发全——网络编程的"半包/粘包"根源就在这 `[经验]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 客户端几步 | 基本认知 | socket/connect/send/recv | 换题 → 不及格 |
| L2 | 为什么 encode/decode | 是否背的 | 网络传输的是字节 | 判 P5 |
| L3 | recv 一定收全吗 | 有没有真理解 | 字节流无边界/需循环 | 判 P6 |
| L4 | send 和 sendall 区别 | 架构判断 | 前者可能发一半 | 判 P6+ |
| L5 | 你处理过半包粘包吗 | 实战经验 | 长度前缀/定界符 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| Python 3.x | 2→3 最大断裂就是 str/bytes 分离 | 默认 encode UTF-8、recv 返回 bytes；可提 `socket.makefile` 按行读 |

## 关键代码
```python
import socket
cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect(("127.0.0.1", 8888))             # 触发 TCP 三次握手 [实测]
cli.sendall("helloworld".encode("utf-8"))    # 发送必须 encode 成字节
data = cli.recv(1024)                         # 返回 bytes，需 decode
print(data.decode("utf-8"))                   # 转回 str（Python3）
cli.close()
```

## ⚠️ 原文纠错
原文第 14~55 段音译需还原：「**TCB/TTP**」→ **TCP**；「**sooft/sobmit/sosolit/solid/soccit/surfit**」→ **socket**；「**s点setout**」→ **s.send（发送）**；「**tubo**」→ **tuple（元组，connect 的 (IP, 端口)）**；「**整机**」→ **本机/服务器**；「**四个八**」→ **8888（端口）**；「**date电影/decode**」→ **decode（解码）**；「**unioncode/pass三/STR**」→ **unicode/Python3/str**；「**b开头**」→ **bytes 前缀 `b'...'`**；「**surface**」→ **socket**。客户端流程与 encode/decode 字节要点正确。核对范围：第 14~55 段 TCP 客户端编程。

## 总结与追问预判
- 客户端：connect→sendall(encode)→recv(decode)→close；网络数据是字节。
- 顺势会问：**TCP 服务端（见 179 卡）**、**手工发 HTTP（见 181 卡）**。
