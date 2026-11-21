"""一致性策略光谱: 从强一致到最终一致的取舍"""
SPECTRUM = """
CP 方向(分区时拒绝写):
  etcd/zk 共识 -> 分布式锁/配置中心
  DB 同步复制 + 强制读主 -> 资金核心
中间地带:
  Redis 半同步语义: min-replicas-to-write=1 -> 拒绝写保不丢
  缓存强一致读: 写后短窗口读主(Q897)
AP 方向(分区时保可用):
  Redis 主从异步复制 -> 读可能旧值
  Cache Aside + TTL -> 最终一致 BASE
"""
if __name__ == "__main__":
    print(SPECTRUM)
    print("BASE 三要素: 基本可用(降级) 软状态(允许不一致窗口) 最终一致(TTL/对账收敛)")
