---
title: [NODE-706] 读写分离与主从延迟怎么处理？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-706：读写分离怎么做？
**答**：
- 路由策略：写主读从（默认）+ 读己之写 bypass（SCN-NODE-654）+ 强一致查询显式走主（事务内/结算类）——路由策略声明式（query 标注 consistency 级别）。
- 主从延迟应对：延迟感知路由（副本延迟超阈值摘流——副本健康度）+ 关键业务读主（库存/资金——C 优先）；延迟监控（seconds_behind_master 告警）。
- 复制方式权衡：异步复制（延迟小可能丢——主挂时）vs 半同步（至少一从确认——折中）vs 组复制（强一致——成本高）；按数据敏感度选。
- 会话一致性增强：全局时间戳方案（GTID/版本号——读时校验副本是否覆盖最新写）。
- 追问钩子：为什么「延迟感知摘流」优于「固定阈值切主」——固定阈值（延迟 >2s 全读主）让主库在从库抖动时被打爆（所有读压主——雪崩转移）；延迟感知按副本逐个摘流（延迟高的副本摘，其他继续）——故障隔离到副本粒度而非全局切换。

```javascript
const router = {
  read: async (q, { consistency = 'eventual' } = {}) => {
    if (consistency === 'strong' || recentWrite(user)) return primary(q);   // 强一致/读己之写
    const replica = pickHealthyReplica();                // 延迟感知摘流
    return replica.query(q);
  },
};
repllicas.forEach(r => monitor(r, { maxLag: 2 }));     // 延迟超 2s 摘流
```
