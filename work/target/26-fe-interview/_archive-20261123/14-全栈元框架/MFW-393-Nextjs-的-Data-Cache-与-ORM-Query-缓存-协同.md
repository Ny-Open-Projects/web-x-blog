---
title: [MFW-393] Data Cache × ORM 层缓存的协同与冲突

## MFW-393：Data Cache × ORM 层缓存的协同与冲突
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW→393：双层缓存协同

**答**:
- 冲突模型：Data Cache（fetch 结果）与请求内 ORM 缓存（Prisma cache/Redis 二级）同 key 双写——TTL 不同步时读到「新旧拼盘」（列表新、详情旧）
- 协同规则：同域数据只允许一个「新鲜度权威」——查询路径统一走数据函数工厂（单一出口内串双层：L1 请求内 → L2 Redis → L3 源），TTL 与失效 tag 在工厂内声明一次（散点 fetch 各自设 TTL = 必漂移）
- 写后读：mutation 后按域失效三层同发（tag + redis key 前缀 + ORM 清缓存——失效总线 MFW-242 的三层执行器）
- 演进建议：ORM 层缓存默认关（Prisma 不开 result cache）——先让单层正确，量化收益后再上二层（缓存层数与 bug 面成正比）

```text
规则：一域一权威；统一工厂内 L1→L2→L3 串行，TTL/tag 单点声明
失效：mutation → 总线三层同发
演进：ORM 缓存默认关，单层正确后再量化上二层
```
