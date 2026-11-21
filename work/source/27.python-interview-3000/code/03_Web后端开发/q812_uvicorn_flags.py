
FLAGS = {
    "--workers 4": "多进程, 数量按 CPU 核数与内存评估, 不是越多越好",
    "--limit-concurrency 200": "超过并发的请求返回 503, 防雪崩的过载阀",
    "--timeout-keep-alive 5": "空闲连接回收, 与 Nginx keepalive 对齐",
    "--backlog 2048": "内核 accept 队列长度, 突发流量缓冲",
    "--proxy-headers --forwarded-allow-ips 10.0.0.0/8": "信任代理并修正 client IP",
}
for flag, note in FLAGS.items():
    print(f"{flag}: {note}")
