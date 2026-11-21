---
title: [Q5557] IPv6 双栈迁移与 dualstack 监听的版本演进
date: 2026-11-20
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5557 · IPv6 双栈迁移与 dualstack 监听的版本演进

> 难度:★★★ | 标签:IPv6, dualstack, socket.create_server, V6ONLY, 版本演进

**问**：机房推行 IPv6-only 网段，老服务只 bind 了 0.0.0.0，迁移窗口全挂。双栈监听怎么做？`socket.create_server(dualstack_ipv6=True)` 帮你省了什么？应用层拿到的对端地址长什么样、要怎么处理？

**答**：迁移正确姿势是**单 socket 双栈监听**：创建 `AF_INET6` socket，置 `IPV6_V6ONLY=0`，bind `[::]`——内核把 IPv4 请求映射成 `::ffff:a.b.c.d`（v4-mapped 地址）进同一个 accept 队列。3.8+ 的 `socket.create_server(("", port), family=AF_INET6, dualstack_ipv6=True)` 把这套三步封装了，且在不支持双栈的平台上**显式抛错**而不是静默降级（逼你显式选择"监听两个 socket"方案）。应用层三个必改点：a) 日志/ACL 里对 `::ffff:1.2.3.4` 要**解映射回 IPv4** 再匹配老规则，否则 CIDR 判断全失效；b) 白名单校验用 `ipaddress.ip_address(addr)` 归一化后再比，v4-mapped 的 `.ipv4_mapped` 属性直接给出原 IPv4；c) 反代后拿 X-Forwarded-For 同理。平台坑：某些内核/容器网络默认 `net.ipv6.bindv6only=1`，dualstack 参数会失败——所以生产代码要 hasattr/try 降级为"两个 socket 分别监听"或直接跑在 v4 上。演进视角：云厂商双栈 → IPv6-only 内网，Python 应用层唯一要守住的是"**地址归一化一处做、全局用**"。

```python
# file: code/02_并发与网络工程/q5557_dualstack.py
import socket, ipaddress

try:
    srv = socket.create_server(("", 0), family=socket.AF_INET6, dualstack_ipv6=True)
except (OSError, ValueError) as e:
    print("当前环境不支持 dualstack, 降级: 分别监听 AF_INET/AF_INET6 两个 socket |", e)
    raise SystemExit(0)
print("dualstack v6 socket:", srv.getsockname())

c = socket.create_connection(("127.0.0.1", srv.getsockname()[1]), timeout=2)  # v4 客户端
conn, addr = srv.accept()
print("对端原始地址:", addr[0], "(v4-mapped)")
ip = ipaddress.ip_address(addr[0])
v4 = ip.ipv4_mapped            # ::ffff:a.b.c.d -> 归一化回 IPv4
print("解映射后:", v4, "| 老规则匹配:", str(v4).startswith("127."))
conn.sendall(b"ok")
print("收到:", c.recv(2))
conn.close(); c.close(); srv.close()

# 规范化函数模板: ACL/日志统一走它
def normalize_peer(addr):
    ip = ipaddress.ip_address(addr)
    return ip.ipv4_mapped or ip
print("模板验证:", normalize_peer("::ffff:192.168.1.5"))
```

**追问**：1) `IPV6_V6ONLY` 置 1 和 0 的行为差异与默认值？——1 表示 v6 socket 只收 v6（v4 需另开 v4 socket），0 表示双栈收映射流量；Linux 默认 0，BSD/部分平台默认 1——这就是"换台机器就收不到 v4"事故的来源，永远显式设置而不是依赖默认。2) `socket.create_connection` 为什么优先尝试 AAAA？——它按 `getaddrinfo` 顺序迭代并回退（Happy Eyeballs 的简化版），双栈环境建议连接侧也保留这种"多地址尝试"逻辑，写死第一个地址会在 v6 不通时挂。3) 应用层拿 `::ffff:` 地址直接存库有什么长期问题？——同一个客户端两种记录形态（v4 与 v4-mapped），聚合/去重/风控全乱；入库前统一 normalize，历史数据迁移用同一函数回填。

## 背诵要点
- 双栈正解：AF_INET6 + `IPV6_V6ONLY=0` bind `[::]`；`socket.create_server(dualstack_ipv6=True)`（3.8+）封装且不支持时显式报错。
- v4 请求以 `::ffff:a.b.c.d` 进入 accept，ACL/日志用 `ipaddress.ip_address(addr).ipv4_mapped` 归一化回 IPv4。
- `bindv6only` 平台默认值不同，永远显式设 V6ONLY；生产保留降级路径（两 socket 或 v4-only）。

## 复盘追问
- 你们的连接日志/风控规则里，v4-mapped 地址现在是怎么处理的？（提示：grep "::ffff" 与 ipaddress 使用点，统一 normalize 入口）
- IPv6-only 网段演练时，应用哪个环节最容易先挂？（提示：DNS 返回顺序、bind 假设、第三方 SDK 写死 AF_INET——逐层列检查单）
