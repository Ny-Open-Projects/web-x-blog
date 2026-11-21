---
title: [Q812] Uvicorn 直接部署的关键参数
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q812 · Uvicorn 直接部署的关键参数

> 难度:★★★☆ | 标签:Uvicorn, 部署

**问**:裸跑 uvicorn 上生产,哪几个命令行参数必须显式设置?

**答**:`--workers N` 多进程(N 按 CPU 与内存评估);`--limit-concurrency` 并发上限,超过直接 503,是过载保护阀门,防止无限排队拖垮整个实例;`--timeout-keep-alive` 与网关侧对齐,避免连接堆积;`--proxy-headers --forwarded-allow-ips` 修正真实客户端 IP;`--backlog` 内核 accept 队列。注意 uvicorn 自身**不做进程守护**,崩溃拉起要靠 systemd/K8s,或者用 Gunicorn 的 UvicornWorker 获得进程管理。

```python
# file: code/03_Web后端开发/q812_uvicorn_flags.py

FLAGS = {
    "--workers 4": "多进程, 数量按 CPU 核数与内存评估, 不是越多越好",
    "--limit-concurrency 200": "超过并发的请求返回 503, 防雪崩的过载阀",
    "--timeout-keep-alive 5": "空闲连接回收, 与 Nginx keepalive 对齐",
    "--backlog 2048": "内核 accept 队列长度, 突发流量缓冲",
    "--proxy-headers --forwarded-allow-ips 10.0.0.0/8": "信任代理并修正 client IP",
}
for flag, note in FLAGS.items():
    print(f"{flag}: {note}")
```

**追问**:
- limit-concurrency 设多大?——按压测出的单进程安全并发定,宁可早 503 让重试与降级接管,不可让延迟无界增长。
- uvicorn 与 gunicorn+uvicorn worker 怎么选?——K8s 里单容器单进程常直接 uvicorn(靠编排做守护);虚拟机多 worker 或需要 pre-fork 语义时用 gunicorn 托管。
