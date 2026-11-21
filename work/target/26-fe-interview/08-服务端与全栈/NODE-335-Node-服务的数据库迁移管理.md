---
title: [NODE-335] Node 服务的数据库迁移（migration）管理如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-335：Node 服务的数据库迁移管理
**答**:
- 原则：schema 变更必须走版本化迁移脚本（up/down），禁止手工改库；迁移与代码同仓库同 MR 评审；执行记录入库（版本号 + 时间 + 校验和）。
- 向前兼容部署协议：滚动发布期间新旧代码并存——迁移分"加字段（可空/带默认）→ 回填 → 切换读 → 删旧字段"多步，每步独立发布兼容新旧代码；禁止一步到位 drop column。
- 大表迁移：backfill 用批量脚本（LIMIT 循环 + sleep 节流）而非单条 ALTER；加索引用 CONCURRENTLY（PG）防锁表；预估锁表时间（行数 × 单行操作成本）决定在线/停机窗口。
- 回滚策略：down 脚本必须存在且测试过；数据破坏性变更（删列）延迟一个版本周期执行；迁移前自动备份点。
- CI 校验：迁移脚本在干净库跑 up + down + up 幂等性验证；schema snapshot diff 评审可见。
```sql
-- 多步迁移示例（PostgreSQL）
-- V10: ALTER TABLE orders ADD COLUMN pay_channel text;          -- 1. 加可空列
-- V11: UPDATE orders SET pay_channel = 'unknown' WHERE pay_channel IS NULL;  -- 2. 回填
-- V12: ALTER TABLE orders ALTER COLUMN pay_channel SET NOT NULL; -- 3. 收紧
-- V13: 代码切读新列（应用发布）
-- V14: ALTER TABLE orders DROP COLUMN legacy_pay;               -- 5. 下个版本删旧
CREATE INDEX CONCURRENTLY idx_orders_created ON orders (created_at);
```
