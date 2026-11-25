---
title: [Q6609] Redis 许可证变更（RSALV2/AGPL）与 Valkey 迁移决策
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6609 · Redis 许可证变更（RSALV2/AGPL）与 Valkey 迁移决策

难度：P6 ｜ 标签：版本演进 / 开源许可 / Redis

**问**：Redis 从 7.4 起把协议从 BSD 换成 RSALV2/AGPL 双许可，2025 年又加回了 AGPL。团队有的服务用云托管的 Redis，有的自建在 K8s 里。许可证变更到底影响什么？要不要迁 Valkey？

**答**：
- **结论**：先分清"影响谁"：RSALV2（Redis Source Available License）限制的是**把 Redis 软件本身作为服务卖给第三方**（竞争性云厂商），自用、内部业务使用完全不受限；AGPL 变体则要求"通过网络提供服务时向用户提供源码"，对企业内部使用同样宽松（2025.5 Redis 8 加回 AGPL 是为了回归 OSI 开源）。所以绝大多数应用公司**代码合规风险≈0**，真正的影响是生态与供给面：① 云托管版本——各云厂商基于 Valkey/自研兼容层提供"Redis 兼容"服务；② 自建镜像——官方 docker hub 镜像许可变更后，社区主流转向 valkey/valkey 镜像；③ 客户端协议——Valkey 保持 RESP 协议兼容，redis-py 等客户端无需换。
- **取舍**：决策矩阵：① 用云托管 Redis 兼容服务 → 无迁移必要，关注厂商的版本路线（是否基于 Valkey 演进）；② 自建且不依赖 Redis 7.4+ 独有功能（Functions、ACL 增强）→ 留在 Redis 7.2/7.4 BSD 版本最稳，或在下个窗口切 Valkey 8（性能改进 + 开源协议）；③ 对协议/许可有法务红线（如对外交付的产品捆绑 Redis）→ 直接 Valkey，它是 Linux 基金会中立项目，fork 自 Redis 7.2.4。**迁移成本**：协议兼容使切换接近"换镜像 + 灰度"，风险点在持久化格式与运维脚本（RDB 兼容、集群模式差异、监控指标名差异）。
- **实战**：迁移路线：① 盘点所有 Redis 实例的版本/功能依赖（是否用了 7.4+ 特性）；② 测试环境用 valkey/valkey 镜像双跑对拍（QPS/P99/内存占用/持久化恢复）；③ 按实例灰度切换（先无持久化的缓存实例，再持久化实例）；④ Python 侧零改动验证：redis-py 连接串不变，跑既有集成测试；⑤ 复盘项：把"上游许可变更监控"加进依赖治理（和 SBOM 一起，见 Q7020），下次 fork 事件早发现。

```python
# Redis 兼容层切换的冒烟验证（标准库模拟判定逻辑）
# 基线：Python 3.9+；真实环境 redis-py 5.x 连 Redis 7.2 / Valkey 8 同一套代码

from dataclasses import dataclass


@dataclass
class Instance:
    name: str
    engine: str          # redis-7.2 / redis-7.4 / valkey-8
    has_persistence: bool
    uses_new_features: bool   # 是否依赖 7.4+ 特性（Functions/新 ACL）


def migration_plan(instances: list[Instance]) -> dict[str, str]:
    plan = {}
    for ins in instances:
        if ins.uses_new_features and ins.engine.startswith("redis"):
            plan[ins.name] = "stay-redis(依赖7.4+特性)"
        elif ins.has_persistence:
            plan[ins.name] = "valkey-灰度后切(持久化实例，先对拍)"
        else:
            plan[ins.name] = "valkey-直接切(缓存实例，低风险)"
    return plan


def smoke_check(resp_impl: str, ops: list[str]) -> bool:
    """RESP 协议兼容冒烟：同一组操作在两个引擎上结果一致"""
    return all(op in ("GET", "SET", "HSET", "LPUSH", "SCAN", "EXPIRE") for op in ops) and resp_impl in ("redis", "valkey")


def main() -> None:
    fleet = [
        Instance("cache-a", "redis-7.2", False, False),
        Instance("cache-b", "redis-7.4", True, False),
        Instance("func-c", "redis-7.4", True, True),
        Instance("cache-valkey", "valkey-8", False, False),
    ]
    plan = migration_plan(fleet)
    assert plan["cache-a"] == "valkey-直接切(缓存实例，低风险)"
    assert plan["cache-b"] == "valkey-灰度后切(持久化实例，先对拍)"
    assert plan["func-c"] == "stay-redis(依赖7.4+特性)"
    assert smoke_check("valkey", ["GET", "SET", "EXPIRE", "SCAN"])
    assert smoke_check("redis", ["GET", "SET"])
    print("OK: 按功能依赖/持久化分级迁移，RESP 兼容冒烟通过")
    for k, v in plan.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么 Valkey 能做到"客户端零改动"？
→ 一句话提示：Valkey fork 自 Redis 7.2.4 并保持 RESP2/RESP3 协议兼容，redis-py/aioredis 等客户端只讲协议不关心服务端实现；风险不在客户端而在持久化文件与集群运维工具的细节差异。

**追问 2**：RSALV2 和 AGPL 的关键区别是什么？
→ 一句话提示：RSALV2 是"源码可用但限制竞争性服务"，不算 OSI 开源；AGPL 是网络服务也要提供源码的开源协议——两者对"用 Redis 跑自己业务"的公司都宽松，约束对象是把它当服务转售的云厂商。

## 背诵要点
- 许可变更影响的是"转售服务者"，自用业务合规风险≈0；真正要管理的是云托管供给面与镜像生态迁移。
- 迁 Valkey 的分级：依赖 7.4+ 特性的留 Redis，缓存实例直接切，持久化实例双跑对拍后灰度；RESP 兼容使 redis-py 零改动。
- 把上游许可变更纳入依赖治理（SBOM/法务红线清单），fork 事件要早于"镜像下架"发现。

## 复盘追问
- Redis 8 加回 AGPL 对自建团队的决策有什么改变？提示：AGPL 回归 OSI 开源，消除了"许可证不算开源"的采购合规争议，自建留在 Redis 8 的理由增强；但云托管生态已大量基于 Valkey，双轨将长期共存。
- 切换引擎时持久化恢复怎么验证？提示：用生产 RDB 副本在 Valkey 上做恢复演练（RTO/RPO 口径见 Q6563），核对大 key、过期键语义与内存占用差异，再决定切换顺序。
