---
title: [Q641] DNS 解析与 getaddrinfo 的行为细节
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q641 · DNS 解析与 getaddrinfo 的行为细节

> 难度:★★★☆ | 标签:DNS, getaddrinfo, 解析

**问**:socket.getaddrinfo 到底做了什么?有哪些容易忽略的行为?

**答**:getaddrinfo 完成主机名+服务名→地址列表的完整解析:IP 字面量直接走快速路径不查 DNS;服务名 "http" 会查 /etc/services 映射成 80;默认 AF_UNSPEC 可能同时返回 IPv4 与 IPv6(顺序受 RFC 6724 排序影响),双栈环境有时 v6 优先导致连接慢。关键认知:libc 解析器通常不做 TTL 缓存(nscd/systemd-resolved 配置了才有),热路径高频解析要自己缓存(Q642);解析失败抛 socket.gaierror,要按 errno 区分"域名不存在"(EAI_NONAME)与"临时故障"(EAI_AGAIN)。

```python
# file: code/02_并发与网络工程/q641_getaddrinfo.py
import socket
import time


def show(label: str, infos: list) -> None:
    print(f"--- {label}: {len(infos)} 条结果")
    for family, stype, proto, canon, sockaddr in infos[:4]:
        ip = sockaddr[0]
        kind = "IPv4" if family == socket.AF_INET else "IPv6"
        print(f"  {kind} {ip} type={stype}")


if __name__ == "__main__":
    # 1. IP 字面量: 快速路径, 不查 DNS
    t0 = time.perf_counter()
    infos = socket.getaddrinfo("127.0.0.1", 80)
    t1 = time.perf_counter()
    show(f"IP 字面量 耗时 {(t1 - t0) * 1000:.2f}ms", infos)

    # 2. 服务名映射: http → 80
    infos = socket.getaddrinfo("127.0.0.1", "http", type=socket.SOCK_STREAM)
    print("服务名 http 解析为端口:", infos[0][4][1])

    # 3. 主机名解析: 双栈可能返回多族结果
    infos = socket.getaddrinfo("localhost", None)
    show("localhost", infos)
    for info in infos:
        print("   sockaddr:", info[4])

    # 4. 失败分类: 域名不存在 vs 参数错误
    for bad in ("no-such-host.invalid", "256.256.256.256"):
        try:
            socket.getaddrinfo(bad, 80)
        except socket.gaierror as e:
            print(f"gaierror for {bad}: errno={e.errno} {e}")

    # 5. 重复解析耗时: 观察 libc 是否缓存 (通常没有)
    t0 = time.perf_counter()
    for _ in range(20):
        socket.getaddrinfo("localhost", 80)
    t1 = time.perf_counter()
    print(f"重复解析 20 次总耗时 {(t1 - t0) * 1000:.1f}ms → 平均 {(t1 - t0) * 20:.3f}ms 级别")
```

**追问**:1) 连接时拿到的 addrinfo 列表该怎么用?——按序尝试(Happy Eyeballs 思想):优先上一次成功的族,并发发起 v4/v6 竞速,谁先成功用谁;Python 里 create_connection 已经按序回退。2) 为什么说 libc 解析器通常没有 TTL 缓存?——glibc resolver 直接询问 DNS 服务器,只有 nscd/systemd-resolved 等外部组件配置了才缓存;这解释了「每请求一次 getaddrinfo」既慢(毫秒级)又给 DNS 压力,热路径必须应用层自缓存(Q642)。3) gaierror 怎么分类处理?——EAI_NONAME(域名不存在,立即失败,重试无意义)vs EAI_AGAIN(临时故障,可退避重试);不区分就会对「不存在的域名」持续重试打爆 DNS,这是故障放大的常见路径。4) 生产陷阱?——双栈环境 v6 优先但 v6 不通,每请求先等 v6 失败再回退 v4(延迟翻倍,用 create_connection 的按序回退/Happy Eyeballs);缓存了可变 list 被下游改坏;在事件循环里同步调 getaddrinfo 阻塞全部连接(asyncio 版默认走线程池,自写的别阻塞)。

---
