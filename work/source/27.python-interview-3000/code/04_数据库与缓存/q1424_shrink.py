"""maxmemory 打满的应急瘦身: 冷 且 大 优先"""
# key -> (bytes, seconds_since_last_hit)
usage = {
    "session:u1": (2048, 10),
    "feed:cache:big": (512000, 3600 * 26),
    "report:2023q4": (2000000, 3600 * 24 * 90),
    "hot:goods:1": (10000, 2),
    "cart:u9": (4096, 600),
    "tmp:export:17": (800000, 1800),
}
quota = 1000000

def shrink(usage, quota):
    freed, dropped = 0, []
    for k, (size, age) in sorted(usage.items(), key=lambda x: (-x[1][1], -x[1][0])):
        if freed >= quota:
            break
        freed += size
        dropped.append(k)
    return dropped, freed

dropped, freed = shrink(usage, quota)
for k in dropped:
    usage.pop(k)
print(f"需腾出 {quota} 字节, 实际释放 {freed} 字节, 删除顺序: {dropped}")
print("守则: 临时与导出类优先, 会话购物车谨慎, 全程留日志可对账")
