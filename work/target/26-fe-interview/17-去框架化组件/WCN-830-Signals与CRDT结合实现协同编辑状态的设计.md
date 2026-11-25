---
title: [WCN-830] Signals 与 CRDT 结合实现协同编辑状态的设计？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-830：Signals 与 CRDT 结合实现协同编辑状态的设计？

**答**：
- 结论先行：分工是「CRDT 负责分布式一致性（合并并发操作、最终收敛），Signals 负责本地响应式（状态变化驱动 UI）」——CRDT 是数据模型层，Signals 是视图响应层。
- 架构分层：底层一个 CRDT 文档（如 Yjs/Y.Map）维护可合并的状态；本地写操作先应用到本地 CRDT 并同步更新 Signal；远端操作通过同步协议（y-websocket）到达后合并进 CRDT，再刷新 Signal；UI 只读 Signal 做细粒度更新。
- 关键点：CRDT 的「操作」与 Signal 的「状态」要解耦——不要把整个文档塞进一个大 signal（会导致全量重渲染），而是按字段/块拆成细粒度 signal，合并后只刷新受影响部分。
- 冲突处理：CRDT 保证并发收敛（如字符级 RGA），Signals 不参与冲突解决——它只忠实反映合并后的状态。
- 追问钩子：面试官会问「离线编辑怎么做」——答：CRDT 天然支持离线（本地先改，重连后合并），Signals 在离线期间照常驱动本地 UI，重连合并后若状态变化再看信号刷新。

```javascript
import * as Y from 'yjs';
import { signal } from '@preact/signals-core';

// CRDT 文档管一致性
const doc = new Y.Doc();
const ytitle = doc.getText('title');
// Signal 管本地响应式（细粒度：只订阅标题）
const title = signal(ytitle.toString());

// 本地输入 → 写 CRDT → 同步 Signal
function localInput(next) {
  ytitle.delete(0, ytitle.length);
  ytitle.insert(0, next);
  title.value = ytitle.toString();
}
// 远端合并 → 刷新 Signal
ytitle.observe(() => { title.value = ytitle.toString(); });

// UI 只读 signal，拿到的是最终收敛后的文本
title.subscribe(v => console.log('UI 标题:', v));
localInput('协同编辑中');
```
