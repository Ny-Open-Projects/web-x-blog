---
title: [Q702] MTU 与分片:大包不通的排查
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q702 · MTU 与分片:大包不通的排查

> 难度:★★★☆ | 标签:MTU, 分片, PMTUD

**问**:"小包能通、大包卡死"是什么问题?怎么定位 MTU 黑洞?

**答**:链路 MTU(以太网常见 1500,VPN/隧道再减)限制单帧大小;IP 层可分片,但 TCP 常设 DF 位不分片并依赖 PMTUD(ICMP Frag Needed 回报合适 MSS)——中间设备丢弃该 ICMP 就形成"黑洞":握手(小包)成功,数据传输(满 MSS)卡死,典型如 VPN、PPPoE、云隧道。定位:逐级二分探测包大小(ping -s 或应用层递减 payload),找到通/不通的边界即路径 MTU;修复:调低接口 MSS clamping、修防火墙放行 ICMP type3/code4。UDP 大包则直接 EMSGSIZE(本地)或静默丢失。

```python
# file: code/02_并发与网络工程/q702_mtu_probe.py
import socket
import threading
import time


def udp_echo(stop: threading.Event, port_box: list) -> None:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("127.0.0.1", 0))
    port_box.append(s.getsockname()[1])
    s.settimeout(0.2)
    while not stop.is_set():
        try:
            data, addr = s.recvfrom(65535)
            s.sendto(data, addr)  # 原样回显
        except socket.timeout:
            continue
        except OSError:
            continue
    s.close()


def probe_mtu(host: str, port: int, lo: int = 1200, hi: int = 65000) -> int:
    """二分探测 UDP 回环可达的最大数据报 (含应用载荷)。"""
    best = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0.5)
        try:
            s.sendto(b"x" * mid, (host, port))
            s.recvfrom(mid + 64)
            best = mid
            lo = mid + 1
        except socket.timeout:
            hi = mid - 1  # 超过上限: 丢弃或 EMSGSIZE 后的超限
        except OSError as e:
            if e.errno == 90:  # EMSGSIZE: 超过本地 socket 上限
                hi = mid - 1
            else:
                hi = mid - 1
        finally:
            s.close()
    return best


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    threading.Thread(target=udp_echo, args=(stop, box), daemon=True).start()
    while not box:
        time.sleep(0.01)
    port = box[0]

    max_payload = probe_mtu("127.0.0.1", port)
    print(f"回环 UDP 单报文最大载荷: {max_payload} 字节")
    print(f"  (上限 65507 = 65535 - IP头20 - UDP头8, 实际受 SO_SNDBUF 影响可能更小)")

    print("\nTCP 场景的对应概念: MSS = MTU - 40 (IP+TCP头)")
    print("  MTU 1500 → MSS 1460; VPN 封装 MTU 1400 → MSS 1360")
    print("  MSS 协商不当时: 握手成功但大包反复重传 = PMTUD 黑洞")

    # 演示本地 EMSGSIZE 边界
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.sendto(b"x" * 70000, ("127.0.0.1", port))
    except OSError as e:
        print(f"\n超限报文: {e} (errno={e.errno})")
    s.close()
    stop.set()
```

**追问**:1) 为什么云环境 MTU 问题特别多?——VXLAN/Geneve 封装吃掉 50-100 字节(1500→1450/1400),实例间正常、跨隧道大包卡;标准做法是云内网口 MTU 调成 9000 或统一 MSS clamping。2) PMTUD 黑洞的形成机理?——TCP 设 DF 位不分片,依赖中间路由回 ICMP Frag Needed 告知合适 MSS;防火墙把该 ICMP 丢了,发送方不知道要缩小,满 MSS 包静默丢失、重传再丢——表现正是「握手(小包)通、传数据(满 MSS)卡死」。3) 定位与修复手段?——逐级二分 payload 找路径 MTU(ping -s/应用层递减);修复:接口 MTU 调低、MSS clamping、放行 ICMP type3/code4;云环境 VXLAN/Geneve 封装吃 50-100 字节,内网口 MTU 要配套。4) 生产陷阱?——VPN 内小包测试全过、文件传输全挂(黑洞只咬大包);UDP 大包静默丢(无 EMSGSIZE 反馈),应用以为发出去了;TLS 握手证书包恰好超 MSS,表现为「握手卡死」极难归因。

---
