
SERVICES = {
    "api": {"Rate": "http_requests_per_s", "Errors": "5xx_per_s", "Duration": "p99_ms"},
    "worker": {"Rate": "jobs_per_s", "Errors": "failed_jobs_per_s", "Duration": "job_p99_ms"},
}
RESOURCES = {
    "db": {"Utilization": "conn_pool_used_ratio", "Saturation": "wait_queue_len", "Errors": "deadlocks_per_s"},
    "disk": {"Utilization": "used_ratio", "Saturation": "io_wait", "Errors": "io_errors_per_s"},
}

def panel(scope, metrics):
    print(f"[{scope}]")
    for k, v in metrics.items():
        print(f"  {k:<12} -> {v}")

if __name__ == "__main__":
    for s, m in SERVICES.items():
        panel(f"RED 服务 {s}", m)
    for r, m in RESOURCES.items():
        panel(f"USE 资源 {r}", m)
    print("四信号:延迟 流量 错误 饱和度,面板要回答问题而不是堆图")
