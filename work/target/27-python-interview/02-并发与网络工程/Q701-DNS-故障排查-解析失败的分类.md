---
title: [Q701] DNS 故障排查:解析失败的分类
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q701 · DNS 故障排查:解析失败的分类

> 难度:★★☆ | 标签:DNS 排障, gaierror, 分类

**问**:"域名解析失败"其实有好几种病,怎么区分?

**答**:按 gaierror 的 errno 分:名称不存在(EAI_NONAME/NXDOMAIN)——域名打错或记录被删,是权威答案;临时失败(EAI_AGAIN)——DNS 服务器超时/网络不通,重试可能成功;参数类(EAI_FAMILY/EAI_SERVICE)——请求了本机不支持的地址族或服务名,是代码问题。再加环境坑:/etc/hosts 覆盖、resolv.conf 指向失效 DNS、nsswitch 顺序、IPv6-only 解析拖慢。处置:NONAME 查注册与配置;AGAIN 查 resolv 与网络;代码问题改参数。缓存类故障(NXDOMAIN 被缓存)要等 TTL 或刷缓存。

```python
# file: code/02_并发与网络工程/q701_dns_diag.py
import errno
import socket
import time


def diagnose_resolution(host: str, port: int = 443) -> str:
    try:
        infos = socket.getaddrinfo(host, port, proto=socket.IPPROTO_TCP)
        ips = [i[4][0] for i in infos]
        return f"OK {host} → {ips[:3]}"
    except socket.gaierror as e:
        code = e.errno
        if code in (socket.EAI_NONAME, -2):  # 平台差异: mac/linux errno 值不同
            return (f"NXDOMAIN {host}: 名称不存在 → 检查拼写/记录是否被删/"
                    f"是否本地 hosts 覆盖")
        if code in (socket.EAI_AGAIN,):
            return f"TEMPFAIL {host}: DNS 服务器超时 → 查 resolv.conf 上游与网络"
        if code in (socket.EAI_FAMILY,):
            return f"FAMILY {host}: 地址族不受支持 → 代码参数问题"
        return f"OTHER {host}: errno={code} ({e})"
    except OSError as e:
        return f"SYSERR {host}: {e!r}"


if __name__ == "__main__":
    cases = [
        ("localhost", "正常解析"),
        ("this-domain-does-not-exist.invalid", "NXDOMAIN 样本"),
        ("127.0.0.1", "IP 字面量快速路径"),
    ]
    for host, label in cases:
        print(f"[{label}]")
        print(" ", diagnose_resolution(host))

    # 参数类错误演示: 请求不存在的服务名
    try:
        socket.getaddrinfo("localhost", "not-a-service", type=socket.SOCK_STREAM)
    except socket.gaierror as e:
        print(f"[服务名错误] errno={e.errno} → {e}")

    # 解析耗时对比: 排障时先看耗时再下结论
    for host in ("localhost", "127.0.0.1"):
        t0 = time.monotonic()
        socket.getaddrinfo(host, 80)
        dt = (time.monotonic() - t0) * 1000
        print(f"解析 {host}: {dt:.2f}ms")
    print("若 localhost 也要几十毫秒, 说明 nsswitch/hosts 配置异常")
```

**追问**:1) 为什么"解析慢但能成功"也要告警?——通常意味着 DNS 链路退化(上游不可达走重试、超时边界),它在流量尖峰会被放大成建连延迟,是容量事故的常见前兆。2) 「解析慢但能成功」的病根在哪?——上游 DNS 退化走到重试/超时边界后才成功,或 IPv6 解析先超时再回退 v4(Q641);平时无感,流量尖峰被放大成建连延迟——按 p95 解析耗时告警而不是只告警失败。3) hosts/缓存/上游的排查顺序?——先 /etc/hosts(覆盖一切)、再本机缓存(nscd/systemd-resolved,可刷)、再 resolv.conf 上游链路、最后权威侧;NXDOMAIN 被中间缓存钉住要等 TTL 或刷缓存。4) 生产陷阱?——EAI_AGAIN 无脑硬重试打爆 DNS(要退避+熔断);NONAME 与 AGAIN 处理相同,排障方向全错;容器 DNS ndots 配置让外部域名先在内部搜索域里空转一圈,延迟翻倍。

---
