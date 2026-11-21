"""综合案例: 一次 Redis 延迟毛刺的排查链"""
timeline = [
    ("10:02", "p99 从 2ms 飙到 45ms", "先看慢日志: 无超 10ms 命令 -> 排除大命令"),
    ("10:05", "INFO: latest_fork_usec=380000", "fork 耗时 380ms -> bgsave / AOF rewrite 嫌疑"),
    ("10:06", "used_memory 30GB, 碎片率 1.6", "内存逼近 maxmemory, COW 空间紧张"),
    ("10:08", "rdb_bgsave_in_progress=1 与业务高峰重叠", "定位: 高峰期 fork 加 COW 加高碎片"),
    ("10:15", "持久化错峰 + activedefrag + 淘汰冷 key", "p99 回落 3ms"),
]
for t, fact, verdict in timeline:
    print(f"[{t}] {fact}")
    print(f"      -> {verdict}")
print("复盘: 排查链 = 慢日志 -> fork 指标 -> 内存与碎片 -> 持久化时点 -> 系统层")
