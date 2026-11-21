---
title: [Q1006] Redis 容器化注意点
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1006 · Redis 容器化注意点

> 难度:★★★☆ | 标签:容器化, 运维

**问**:Redis 跑在 Kubernetes/容器里,哪些系统与编排层面的坑必须处理?

**答**:五类硬问题:一、内存超卖——容器 limit 与 Redis maxmemory 不一致,OS OOM killer 直接杀进程;limit 要略大于 maxmemory 并留 fork 的 copy-on-write 余量(RDB 时瞬时翻倍);二、透明大页 THP——必须关闭,否则 fork 后写放大导致延迟毛刺;三、磁盘 IO——RDB/AOF 落盘要挂本地 SSD PV,AOF everysec 对 fsync 延迟敏感;四、网络——hostNetwork 或高带宽保障,集群总线 16379 别被 NetworkPolicy 拦截;五、优雅关闭——preStop 发 SHUTDOWN SAVE/等待连接排空,terminationGracePeriodSeconds 覆盖持久化时长。K8s 里 StatefulSet + 反亲和分散节点,避免多副本同宿主机。健康检查用 redis-cli ping 而不是 TCP 探活(端口在进程假死时仍通)。

```python
# file: code/04_数据库与缓存/q1006_k8s_redis.py
"""容器化自检清单: 校验内存配置与持久化设置"""
def precheck(maxmemory_gb, container_limit_gb, thp_enabled,
             aof_policy, persistence_pv):
    issues = []
    if maxmemory_gb >= container_limit_gb:
        issues.append(f"maxmemory {maxmemory_gb}GB >= 容器 limit {container_limit_gb}GB, "
                      "OOM 风险; limit 应留 fork 余量约 1.5x")
    if thp_enabled:
        issues.append("THP 未关闭, fork 写放大将造成延迟毛刺")
    if aof_policy == "always":
        issues.append("AOF always 每次写都 fsync, 容器盘延迟敏感, 建议 everysec")
    if not persistence_pv:
        issues.append("未挂持久卷, 重启即丢数据(RDB/AOF 无处落盘)")
    return issues or ["检查通过"]

if __name__ == "__main__":
    print(precheck(maxmemory_gb=8, container_limit_gb=8, thp_enabled=True,
                   aof_policy="always", persistence_pv=False))
    print("---")
    print(precheck(maxmemory_gb=8, container_limit_gb=12, thp_enabled=False,
                   aof_policy="everysec", persistence_pv=True))
    print("补充: preStop 钩子执行 SHUTDOWN 排空连接; 健康检查用 redis-cli ping")
```

**追问**:
- 为什么 limit 要留 1.5 倍?——RDB/AOF 重写 fork 出的子进程共享父页,写入时按页复制(COW),高峰写入下额外内存可达 used 的 50% 以上。
- 容器里 swap 要不要开?——Redis 明确要求不 swap,Node 层 vm.swappiness=1 或关闭,依赖 limit 控制内存而非 swap 兜底。

---
