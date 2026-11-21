---
title: [Q1599] RST 与 FIN 的语义差:SO_LINGER 实验
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1599 · RST 与 FIN 的语义差:SO_LINGER 实验

> 难度:★★★★ | 标签:TCP, RST, FIN

**问**:对端关闭连接时,我收到空字节串和 ConnectionResetError 有什么本质区别?怎么主动制造 RST?

**答**:FIN 是我说完了:四次挥手,缓冲区未发的数据仍会送达,对端 recv 读到空——干净的下线,业务走收尾逻辑。RST 是这条连接死了:跳过挥手直接重置,未读数据直接丢弃,对端 recv 抛 ConnectionResetError——含义是对端崩溃、进程被杀或防火墙重置,应标记连接死亡并快速失败。主动制造 RST 的开关是 SO_LINGER:pack 两个 int 为开与 0,close 改发 RST 而不是 FIN。排障意义:先分清是哪种断开,再决定重试还是告警。

```python
# file: code/02_并发与网络工程/q1599_rst_fin.py
"""RST 与 FIN 的语义差: SO_LINGER 实验。

- FIN(四次挥手的关闭): "我说完了", 缓冲区数据仍会送达, 对端 recv 得 b"";
- RST(重置): "这条连接死了", 未读数据直接丢弃, 对端 recv 抛
  ConnectionResetError; SO_LINGER(l_onoff=1, l_linger=0) 让 close 改发 RST。
对端感知不同: 前者是干净的下线, 后者是"要么对端崩溃, 要么被防火墙重置"。
"""
import socket
import struct
import threading
import time


def serve(port_slot, behavior):
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(5)
    port_slot.append(srv.getsockname()[1])
    conn, _ = srv.accept()
    time.sleep(0.1)                         # 等客户端 connect 返回, 再谈断开
    if behavior == "fin":
        conn.recv(1024)                     # 读一条, 表示业务收到
        conn.close()                        # 正常 close -> FIN
    else:                                   # rst
        conn.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,
                        struct.pack("ii", 1, 0))
        conn.close()                        # 立即 RST, 未读数据一并丢弃
    srv.close()


def client_check(port):
    s = None
    for attempt in range(3):                # 连接竞态防护: 服务端刚起时重试
        try:
            s = socket.create_connection(("127.0.0.1", port), timeout=1.0)
            break
        except OSError:
            if attempt == 2:
                raise
            time.sleep(0.1)
    s.settimeout(1.0)
    s.sendall(b"hello")                     # RST 场景下服务端根本不读
    try:
        data = s.recv(1024)
        return ("recv-eof", data)
    except ConnectionResetError:
        return ("reset", None)
    except socket.timeout:
        return ("timeout", None)
    finally:
        s.close()


def main():
    fin_slot, rst_slot = [], []
    t1 = threading.Thread(target=serve, args=(fin_slot, "fin"), daemon=True)
    t2 = threading.Thread(target=serve, args=(rst_slot, "rst"), daemon=True)
    t1.start()
    t2.start()
    while not (fin_slot and rst_slot):      # bind 完成即端口可用
        threading.Event().wait(0.01)

    out_fin = client_check(fin_slot[0])
    print("FIN 场景客户端感知:", out_fin)
    assert out_fin == ("recv-eof", b""), "正常关闭应读到干净 EOF"

    out_rst = client_check(rst_slot[0])
    print("RST 场景客户端感知:", out_rst)
    assert out_rst == ("reset", None), "SO_LINGER 0 关闭应触发 ConnectionResetError"

    print("结论: FIN 是'说完了', RST 是'死了'; 排障时先分清是哪种断开")


if __name__ == "__main__":
    main()
```

**追问**:1) 服务端还有未读数据时 close 会怎样?——默认也是优雅关闭发 FIN,但接收方继续发会收到 RST;linger 开与 0 则连未发数据一起丢弃直接 RST。2) SO_LINGER 的三种配置语义?——关闭(默认):close 优雅关闭,缓冲数据尽力发完,close 调用可能阻塞;开启+超时>0:带超时的优雅关闭,超时后 RST;开启+0:立即 RST,未发数据丢弃——第三种用于「确知连接已坏」的快速回收,滥用于正常路径会丢数据。3) RST 的排障价值怎么用?——客户端看到 ConnectionResetError:先判断是「对端进程死」(连接曾正常)还是「防火墙重置」(特定载荷触发);与 FIN(空字节串)区分后,重试策略完全不同:RST 后连接不可复用必须重建,FIN 后资源已正常释放(Q1311 分诊表的延伸)。4) 生产陷阱?——linger 0 用于「想快点回收」的正常关闭(数据丢失+对端 RST 报错);把 RST 一律重试(对端可能已把请求做了一半,要幂等兜底 Q706);忽略「接收方继续向已 FIN 连接发送会收到 RST」的时序(半关闭后仍写,Q664)。

---
