---
title: [Q647] 端口扫描原理:connect 扫描与 SYN 扫描概念
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q647 · 端口扫描原理:connect 扫描与 SYN 扫描概念

> 难度:★★☆ | 标签:端口扫描, connect, 安全

**问**:端口扫描怎么判断端口开放/关闭/被过滤?为什么 SYN 扫描更隐蔽?

**答**:TCP connect 扫描:完成完整三次握手,connect 成功=open,RST=close,超时=filtered(被防火墙丢弃);优点是无需特权、准确,缺点是留全连接日志。SYN 扫描(半开):发 SYN 后若收 SYN-ACK 就发 RST 中途拆除,不完成握手所以少留日志,但需要 raw socket 权限。UDP 扫描更模糊:无响应=可能 open|filtered,ICMP Port Unreachable=close。安全视角:扫描是攻防基本功,公司内做端口基线巡检是正当用途,对外扫描务必获得授权。

```python
# file: code/02_并发与网络工程/q647_port_scan.py
import socket
import threading
import time


def scan_port(host: str, port: int, timeout: float = 0.5) -> str:
    """TCP connect 扫描: open / closed / filtered 三态。"""
    s = socket.socket()
    s.settimeout(timeout)
    try:
        s.connect((host, port))
        return "open"
    except ConnectionRefusedError:
        return "closed"
    except socket.timeout:
        return "filtered"
    except OSError:
        return "filtered"
    finally:
        s.close()


def main() -> None:
    # 起两个真实服务作为 open 样本
    open_ports: list = []
    for _ in range(2):
        srv = socket.socket()
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind(("127.0.0.1", 0))
        srv.listen(2)
        open_ports.append(srv.getsockname()[1])
        threading.Thread(
            target=lambda s=srv: keep_accept(s), daemon=True
        ).start()
    time.sleep(0.1)

    targets = open_ports + [1, 2, 9] + open_ports  # 9=discard 通常无服务
    for port in dict.fromkeys(targets):  # 去重保序
        state = scan_port("127.0.0.1", port, timeout=0.3)
        print(f"  127.0.0.1:{port:<6} {state}")

    open_found = [p for p in dict.fromkeys(targets) if scan_port("127.0.0.1", p, 0.3) == "open"]
    print("扫描发现开放端口:", sorted(open_found))
    for srv_port in open_ports:
        assert srv_port in open_found


def keep_accept(srv: socket.socket) -> None:
    srv.settimeout(0.5)
    end = time.monotonic() + 2
    while time.monotonic() < end:
        try:
            conn, _ = srv.accept()
            conn.close()
        except socket.timeout:
            continue


if __name__ == "__main__":
    main()
```

**追问**:1) filtered 和 closed 的安全含义差别?——closed 说明主机在但没服务(可继续探测);filtered 是防火墙丢弃,说明有防护策略;资产测绘时 filtered 端口才是"不可达"而非"不存在"。2) 开放/关闭/过滤三种结果对应什么内核行为?——open:SYN→SYN-ACK;closed:SYN→RST(立即回,说明主机在);filtered:无响应超时或 ICMP unreachable(防火墙策略);connect 扫描在 open 后还要发 RST 拆除,全程留完整连接日志。3) 扫描为什么要控制速率与顺序?——高速扫描触发 SYN flood 防护/IDS 告警,结果反而失真(全部 filtered);串行+随机顺序+限速兼顾隐蔽与准确;UDP 扫描的无响应语义是 open|filtered 二义,天生模糊。4) 生产陷阱与合规?——未授权对外扫描违法;内网巡检也要避开峰值(连接日志与 conntrack 压力);把 filtered 当「服务不存在」漏掉真实资产;扫描结果不设基线,每次都是一次性数据。

---
