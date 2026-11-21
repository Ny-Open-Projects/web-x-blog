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
