---
title: [Q1593] TCP connect 扫描实现:并发与状态分类
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1593 · TCP connect 扫描实现:并发与状态分类

> 难度:★★★☆ | 标签:端口扫描, connect_ex, 并发

**问**:用 Python 写一个只扫自己授权环境的端口扫描器,connect 扫描怎么实现?open、closed、filtered 怎么区分?

**答**:核心是 connect_ex:它不抛异常而返回 errno。返回 0 是 open——有服务监听;ECONNREFUSED 是 closed——主机可达但端口没人听,内核回了 RST;超时或 host unreachable 是 filtered——防火墙吞包或链路问题,无法判定。用 ThreadPoolExecutor 并发探测,把串行 O(n 乘 timeout) 压到 O(n 除以并发);每个 socket 用完即关,带超时防挂死。伦理边界:connect 扫描会在目标留下完整连接日志,只扫授权资产;SYN 半开扫描需要原始 socket 权限,是另一回事(Q647)。

```python
# file: code/02_并发与网络工程/q1593_port_scan.py
"""TCP connect 扫描实现: 并发、超时分级与状态分类。

connect_ex 不抛异常而返回 errno, 是扫描的正确入口:
- 0            -> open, 有服务监听;
- ECONNREFUSED -> closed, 端口没人听但主机可达;
- 超时/不可达  -> filtered, 可能防火墙吞包, 也可能链路慢。
线程池并发把串行 O(n×timeout) 压到 O(n/并发)。只扫自己授权的环境。
"""
import errno
import random
import socket
import threading
import time
from concurrent.futures import ThreadPoolExecutor


def hold(srv, stop):
    """只占着端口不接受业务, 给扫描提供 open 判定靶子。"""
    srv.listen(5)
    while not stop.is_set():
        try:
            conn, _ = srv.accept()
        except OSError:
            break
        conn.close()


def open_ports_on(count=3):
    ports = []
    holders = []
    for _ in range(count):
        srv = socket.socket()
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind(("127.0.0.1", 0))
        stop = threading.Event()
        threading.Thread(target=hold, args=(srv, stop), daemon=True).start()
        ports.append(srv.getsockname()[1])
        holders.append((srv, stop))
    return ports, holders


def probe(host, port, timeout=0.3):
    s = socket.socket()
    s.settimeout(timeout)
    try:
        rc = s.connect_ex((host, port))
        if rc == 0:
            return port, "open"
        if rc == errno.ECONNREFUSED:
            return port, "closed"
        return port, "filtered/%s" % errno.errorcode.get(rc, rc)
    except socket.timeout:
        return port, "filtered/timeout"
    finally:
        s.close()


def scan(host, ports, workers=64):
    results = {}
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for port, state in ex.map(lambda p: probe(host, p), ports):
            results[port] = state
    return results


def main():
    open_ports, holders = open_ports_on(3)
    closed = random.sample(range(20000, 30000), 12)
    closed = [p for p in closed if p not in open_ports]
    targets = open_ports + closed

    t0 = time.monotonic()
    results = scan("127.0.0.1", targets)
    wall = time.monotonic() - t0

    found = sorted(p for p, st in results.items() if st == "open")
    print("扫描 %d 个端口耗时 %.2fs" % (len(targets), wall))
    for p in sorted(results):
        print("  端口 %-6d %s" % (p, results[p]))
    assert found == sorted(open_ports), "open 判定必须与真实监听一致"
    for srv, stop in holders:
        stop.set()
        srv.close()
    print("结论: connect_ex 的 errno 就是扫描的判决书, 并发把墙钟压下来")


if __name__ == "__main__":
    main()
```

**追问**:1) 扫描被 IDS 拦了怎么办?——降并发、加随机抖动、分批扫;但合规优先——授权范围外一个端口都不要碰。2) connect_ex 与 connect 的选择逻辑?——connect 异常流(try/except)慢且代码乱,connect_ex 返回 errno 一次调用拿到分类;ECONNREFUSED(closed)与 timeout(filtered)语义不同:前者确定「主机在服务不在」,后者「无法判定」——扫描结果的三态与 errno 映射必须精确。3) 并发与速率控制的平衡?——并发太高触发 IDS/防火墙限速,结果全是 filtered(假阴性);随机顺序+并发上限+每连接超时,让扫描又快又不惊动防护;授权环境也要留连接日志容量(conntrack 压力)。4) 生产陷阱?——扫描结果不区分三态(全标「开放/关闭」,filtered 被误读);socket 用完不关(fd 泄漏,Q648);超时设太长(每个 filtered 端口吃满 timeout,扫描时间爆炸);扫了非授权资产(合规红线,Q1593 原问)。

---
