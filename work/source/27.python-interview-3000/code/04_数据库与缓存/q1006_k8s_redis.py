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
