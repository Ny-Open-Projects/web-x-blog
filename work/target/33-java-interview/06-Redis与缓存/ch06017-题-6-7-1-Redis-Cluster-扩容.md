---
title: "题 6.7.1：Redis Cluster 扩容怎么迁移 slot？业务无感知靠什么？"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 面试题, 33]
type: 面试题
disableNunjucks: true
---

### 题 6.7.1：Redis Cluster 扩容怎么迁移 slot？业务无感知靠什么？

**【面试官意图】** Cluster 运维深度——多数人只会说 16384 槽，不会迁移。
**【参考回答（可背）】** 流程：① 新节点加入（cluster meet）→ ② 规划槽位分配（从重负载节点各匀一些）→ ③ 按槽迁移：源节点 MIGRATING、目标节点 IMPORTING、逐 key `CLUSTER GETKEYSINSLOT` + MIGRATE 原子搬迁（MOVE 选项，ttl 保留）→ ④ 更新槽归属广播。**业务无感知的关键**：迁移中对该槽的请求，源节点返回 **ASK 重定向**（带临时跳转语义），客户端（Smart Client）缓存槽位映射并处理 MOVED/ASK——客户端"无感"其实依赖客户端实现的正确性。
**【追问链】** ① MOVED 与 ASK 区别？（MOVED=槽已永久归属他节点，客户端应更新映射缓存；ASK=槽在迁移中，本次临时跳、不更新缓存）② 迁移期间多 key 命令会怎样？（跨槽多 key 操作报 CROSSSLOT 错——hash tag {user123} 强制同槽是解法，但会制造新热点）。
**【P10 加分项】** "扩容预案里最值钱的是'限速迁移'：MIGRATE 是同步阻塞的，大 key 迁移会卡源节点——所以大 key 治理（6.3.2）是 Cluster 扩容的前置工程，两件事必须串起来讲。"
