---
title: [NODE-623] Node 服务的 IM 信箱模型（写扩散 vs 读扩散混合）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-623：IM 信箱模型
**答**:
- 两极模型：写扩散（每消息写 N 份到成员信箱——读快写贵：小群/单聊）、读扩散（公共 timeline——读时过滤成员：大群 ARC-545）。混合（Hybrid）：单聊/小群写扩散、大群读扩散——按群规模自动分档。
- 信箱实现：信箱表（user_id + seq 索引——拉取 O(logn)）、写扩散路径（消息写 timeline → 扇出任务（MQ——批量写成员信箱，大群分批））、读扩散路径（timeline + 成员校验 + 入群水位过滤）。
- 一致性：扇出延迟（写扩散成员可见延迟——扇出进度监控）、信箱与 timeline 对账（抽检——扇出丢失检测）、seq 全局单调（timeline seq 权威——信箱复制 seq）。
- 性能权衡：写扩散的扇出风暴（万人群瞬间扇出——大群禁用写扩散）、读扩散的过滤成本（成员校验缓存）。
- 迁移：群规模增长跨档（小群变大群——信箱迁移策略：读扩散切换）。
```javascript
// 混合信箱
async function deliver(msg) {
  if (msg.groupSize <= WRITE_THRESHOLD) {
    await timeline.write(msg);
    await fanoutJob.add(msg);                                    // MQ 批量写成员信箱
  } else {
    await timeline.write(msg);                                   // 大群只写公共——读时过滤
  }
}
// 拉取：mailbox.get(uid, cursor) union timeline.groupGet(gid, uid, cursor)
```
