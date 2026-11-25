---
title: [NODE-488] Node 服务幂等消费的实现矩阵（各场景选型）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-488：幂等消费实现矩阵
**答**:
- 场景矩阵：天然幂等（set 覆盖写/状态机终态幂等——免防重）、计数累加类（积分/计数——必须去重：消息 ID 表 + 唯一索引）、资金类（扣款——幂等键 + 事务 + 条件更新三保险）、外部副作用（发短信——幂等记录 + 外部请求 ID 传递）。
- 去重实现谱系：Redis SETNX（快但非严格——宕机窗口丢，适合容忍极小重复的计数）、DB 唯一索引消费表（严格，写放大——资金类必选）、状态机检查（先查状态再操作——有竞态需配合条件更新）。
- 组合模式（推荐）：轻量预检（Redis 快筛已处理）+ 严格兜底（DB 唯一索引）——性能与正确性兼得；预检误放行由唯一索引兜住。
- 失败处理：重复消息到达时返回成功（ACK——防止重放风暴）但记录重复统计（重复率异常 = 上游重发配置问题）。
- 验证：重复注入测试（同消息双发断言单次生效 NODE-408 注入场景）。
```javascript
async function consume(msg) {
  if (await redis.set(`seen:${msg.id}`, 1, 'EX', 86400, 'NX') === null)
    return ackDuplicate(msg);                                    // 预检：已处理
  try {
    await db.tx(async t => {                                    // 严格兜底：唯一索引
      const r = await t.query(`insert into consumed(msg_id) values($1) on conflict do nothing`, [msg.id]);
      if (r.rowCount === 0) return ackDuplicate(msg);
      await doBusiness(msg, t);                                  // 业务与去重同事务
    });
  } catch (e) { await redis.del(`seen:${msg.id}`); throw e; }    // 失败释放预检可重试
}
```

**追问**：

1. 预检 Redis 写成功但事务回滚、`seen` 没删会怎样？→ 这条消息被永久吞掉；`del` 必须写在 catch 里，Redis 异常时退化成只靠 DB 唯一索引。
2. 下游短信发出去了、本地事务却回滚怎么办？→ 外部副作用不能和本地事务同生共死，要用本地消息表加补偿，别指望事务覆盖 HTTP。
3. 上游重发时消息 id 会变怎么防重？→ 不能信任 transport 层 id，用业务键（订单号加动作类型）派生幂等键。
