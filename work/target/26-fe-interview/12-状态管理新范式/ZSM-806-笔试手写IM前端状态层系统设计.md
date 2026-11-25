---
title: [ZSM-806] 笔试：IM 前端状态层系统设计（45 分钟白板演练）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-806：IM 前端状态层系统设计（45 分钟白板演练）
**答**：设计题（口述+伪码）——设计一个 IM 应用（会话列表 + 聊天窗 + 多端同步 + 离线）的状态层。评分点按设计题四段：
**① 澄清（3min）**：同步半径（多端）、离线（要）、规模（千会话/万消息）。
**② 分层建模（12min）**：会话列表（Map 归一化+order）、消息（seq 升序插入+分页游标）、presence（TTL 三级）、UI 态（弹窗/输入草稿）分离。
**③ 可靠性（15min）**：WS 信封+seq 三防+追平、乐观发送（pending 区+ack 转正）、多端已读游标、离线队列。
**④ 闭环（10min）**：故障路径+可观测+性能预算（会话列表排序 O(n log n) 降频、消息窗口虚拟化、扇出监控）。

```javascript
// 伪码骨架（白板输出）
const DESIGN = {
  ①_澄清: { radius: '多端', offline: true, scale: '千会话/万消息/百人群' },
  ②_分层: {
    sessions: 'Map<sessionId, Session> + order[] —— 新消息 O(1) 更新+置顶（530）',
    messages: 'seq 升序二分插入 + pending 区 + 游标分页（734/695）',
    presence: 'TTL 三级 active/idle/removed（596/694）',
    ui: '弹窗栈/输入草稿独立 store —— 与数据层隔离（545）',
  },
  ③_可靠性: {
    transport: 'WS 信封 {v,type,seq,ack} + 心跳25s + 全抖动退避（726）',
    gap: 'onGap → 补拉（hold-back buffer 按 seq 补齐）（727/734）',
    optimistic: '发送进 pending 区，ack 携带正式 seq 转正重排（733）',
    readCursor: '多端取最小游标 + 上报去抖（540）',
    offline: 'IndexedDB op 队列 + baseVersion 冲突（738）',
  },
  ④_闭环: {
    failure: 'leader 交接带 lastSeq / 追平失败 410 全量 / 撤回挂起队列',
    perf: '会话排序降频 + 消息虚拟化 + 扇出监控（530/753/643）',
    observability: 'seq 断点日志 + 变更时间线 + 指纹一致性校验（559）',
  },
}
// 评分落点：pending 区与 seq 转正的时序描述（最易错）、离线队列与 WS 追平的衔接
```
**评分点**：
- pending 区与 ack 转正的时序（乐观发送的正确性核心）
- seq 缺口补拉与离线队列的衔接（两套补数据的协调）
- 分层边界（UI 态不进数据 store）
- 主动给出性能预算与扇出监控（闭环意识）
