---
title: [ARC-281] 特性开关（Feature Flag）与 AB 实验的区别与协同？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-281：特性开关（Feature Flag）与 AB 实验的区别与协同？
**答**：
- 本质区别：开关是**工程运维工具**（控制代码是否生效，目标是发布安全，目标是"尽快 100% 后删除代码"）；实验是**决策工具**（比较效果，目标是拿到结论）。开关追求"开完就删"，实验需要"稳定留存"。
- 类型谱系：发布开关（灰度释放）、运维开关（降级/熔断）、权限开关（内测）、实验开关（AB）——生命周期与治理策略完全不同，混在一个命名空间必乱。
- 协同模式：一个新功能先走发布开关（内部→灰度→全量），全量期间挂实验开关测"新旧交互效果"（如果有必要）；降级开关常驻，复用实验平台分桶设施但治理独立。
- 治理红线：开关必须带 owner+过期时间，平台每季度清理"僵尸开关"（30 天未变且无引用的强制删除流程），否则代码里 flag 组合爆炸不可测。

```typescript
// 开关元数据驱动治理
interface Flag {
  key: string;
  type: 'release' | 'ops' | 'permission' | 'experiment';
  owner: string;
  expiresAt: string;               // release 型强制 90 天过期
  default: boolean;
}
// 僵尸扫描：flags.filter(f => Date.now() > f.expiresAt) → 通知 owner → 逾期自动告警+禁用
// 代码：if (flags.enabled('new-checkout', user)) → 新路径；else → 旧路径（删除 flag 时一并删除）
```
