
PROBES = {
    "startupProbe": "给慢启动服务留足时间, 失败超阈值才重启",
    "livenessProbe": "失败就重启容器, 绝不依赖外部服务",
    "readinessProbe": "失败只摘流量不重启, 可检查关键依赖",
    "resources.requests": "调度依据, 按压测 p95 定",
    "resources.limits": "超过即 OOMKill 或 CPU 节流, 内存要留余量",
}
for key, note in PROBES.items():
    print(f"{key}: {note}")
