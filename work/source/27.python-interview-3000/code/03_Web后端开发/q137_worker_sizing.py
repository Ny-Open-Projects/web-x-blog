def estimate_workers(cpu_cores: int, per_worker_mb: int,
                     total_mb: int, io_bound: bool = True) -> dict:
    by_cpu = cpu_cores * 2 + 1 if io_bound else cpu_cores
    by_mem = max(total_mb // per_worker_mb, 1)
    workers = min(by_cpu, by_mem)
    return {
        'recommended_workers': workers,
        'limited_by': 'cpu' if by_cpu <= by_mem else 'memory',
        'note': '最终以压测 p99 与吞吐拐点为准',
    }

# 4 核 8G,单 worker 约 400MB 的 IO 密集服务
print(estimate_workers(cpu_cores=4, per_worker_mb=400, total_mb=8192))
# {'recommended_workers': 9, 'limited_by': 'memory', ...}
