---
title: [SCN-216] IM 群聊大群——千人群消息洪峰的渲染治理？
date: 2026-11-20
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-216：千人裙每秒上百条消息，消息列表渲染怎么撑住？

**答**:
- 洪峰聚合：消息到达聚合渲染（100ms 窗口批量 flush，一次渲染一批而非逐条）、频率上限（同会话渲染 ≤10 次/秒）、洪峰模式（>50 条/秒时折叠计数："有 132 条新消息，点击查看"——用户在滚动阅读时不自动插入）。
- 渲染优化：虚拟列表（消息项高度预估+动态测量）、消息项 memo（内容不变不重渲）、富消息懒解析（图片/卡片进场才解析渲染，纯文本直接渲）。
- 洪峰期间策略降级：未读会话不实时更新列表（聚合）、@我消息优先渲染（洪峰中 @ 与回复置顶提示）、图片消息先占位后加载。
- 分级拉取：进入群只拉最近 50 条（不拉全量），历史消息按需上滑分页拉取，洪峰中的历史拉取排队降级（洪峰结束再补）。

```javascript
class MessageRenderer {
  constructor() { this.queue = []; this.rendering = false; }
  onMessages(msgs) {
    this.queue.push(...msgs);
    if (!this.rendering) this.flush();       // 聚合渲染
  }
  flush() {
    this.rendering = true;
    requestAnimationFrame(() => {
      const batch = this.queue.splice(0, 50);
      if (this.floodMode && batch.length > 20 && userScrolling()) {
        this.pendingCount += batch.length;   // 洪峰折叠
        showCollapsedBar(this.pendingCount);
      } else {
        batch.forEach(m => vlist.append(memoItem(m)));
      }
      this.rendering = false;
      if (this.queue.length) this.flush();
    });
  }
}
// @我检测：batch.filter(isMentionMe) → 置顶提示条。
```
