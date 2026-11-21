---
title: [Q1312] DNS 多地址轮询:getaddrinfo 结果的故障转移
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1312 · DNS 多地址轮询:getaddrinfo 结果的故障转移

> 难度:★★★☆ | 标签:DNS, happy eyeballs, 故障转移

**问**:域名解析出 5 个 IP,第一个连不上怎么办?"挨个试"有哪些讲究?

**答**:getaddrinfo 返回的地址列表天然就是候选集,工程上要把它变成"有序尝试 + 就近记住"。三个讲究:第一,逐个尝试要有独立超时,不能把 3 秒预算全押第一个 IP——这就是 happy eyeballs 的核心思想,真实实现还会并行竞速,标准库做串行版即可;第二,记住 last-good:上次成功的服务器优先试,避免每次都先撞一遍死地址;第三,尝试完一轮全失败要返回聚合错误,并把失败原因记下来供排障,而不是只抛最后一个异常。下面的演示解析 localhost 拿到真实多地址结果,再对一个"主备"候选列表做故障转移:主节点端口死掉,客户端自动切到备节点。

```python
# file: code/02_并发与网络工程/q1312_dns_failover.py
import socket
import threading


def show_addrinfo(host: str, port: int) -> None:
    infos = socket.getaddrinfo(host, port, type=socket.SOCK_STREAM)
    print(f"getaddrinfo({host}) 返回 {len(infos)} 条候选:")
    seen = set()
    for af, st, proto, _, sa in infos:
        key = (af, sa[0])
        if key not in seen:
            seen.add(key)
            print(f"  family={'IPv6' if af == socket.AF_INET6 else 'IPv4'} addr={sa[0]}")

def connect_first_alive(candidates, timeout=0.3):
    """有序尝试候选端点, 返回 (socket, 试到第几个), 全败抛聚合异常。"""
    errors = []
    for idx, (host, port) in enumerate(candidates):
        try:
            s = socket.create_connection((host, port), timeout=timeout)
            return s, idx
        except OSError as exc:
            errors.append(f"{host}:{port} -> {type(exc).__name__}")
    raise ConnectionError("全部候选失败: " + "; ".join(errors))


def main() -> None:
    show_addrinfo("localhost", 80)

    # 主备两个端点: 主端口无监听, 备端口由线程拉起
    dead_port = 59991
    live_port = 59992
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", live_port))
    srv.listen(1)
    threading.Thread(target=lambda: srv.accept()[0].close(), daemon=True).start()

    sticky = [0]  # last-good 记忆: 上次成功的下标
    order = [( "127.0.0.1", dead_port), ("127.0.0.1", live_port)]
    s, idx = connect_first_alive(order)
    print(f"主节点 {dead_port} 拒绝 -> 自动切到备节点 {live_port}, 试到第 {idx + 1} 个候选")
    s.close()

    # 把成功的备节点挪到队首, 下一轮不再撞死地址
    order.insert(0, order.pop(idx))
    s, idx = connect_first_alive(order)
    print(f"last-good 调序后: 首个候选即命中, 试到第 {idx + 1} 个候选")
    s.close()
    srv.close()


if __name__ == "__main__":
    main()
```

**追问**:1) 为什么真实 happy eyeballs 要并行竞速而不是串行?——串行时每个死 IP 都要吃满超时,5 个死 IP 就是 15 秒;并行竞速谁先完成握手用谁,代价是多发几个 SYN。2) 独立超时怎么分预算?——总预算 ÷ 候选数是下限,更好的是「首个候选给大头、后续递减」或按 last-good 加权;全失败时聚合错误要包含每个候选的失败原因——只抛最后一个异常,前 N-1 个的病因就被吞了。3) last-good 的持久化与失效?——记住上次成功地址能省每次撞死 IP 的超时,但 last-good 本身会过期(实例下线),要配健康检查兜底;这是客户端 LB(Q643)的简化版:地址池、选择策略、故障摘除三件套都在,只是规模小。4) 生产陷阱?——循环里共用一个超时变量,第一个候选吃光预算;失败候选没记冷却,每轮都从死 IP 开始;聚合错误只留最后一个,排障线索丢失;DNS 结果不缓存每次解析(Q641),故障转移被解析延迟放大。

---
