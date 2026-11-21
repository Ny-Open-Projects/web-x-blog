---
title: [SCN-136] 热门内容点赞 QPS 很高，点赞动画与数字更新如何不把页面拖垮？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-136：热门内容点赞 QPS 很高，点赞动画与数字更新如何不把页面拖垮？
**答**：
- 用户反馈要即时：点击瞬间本地 +1 并播放动画（一次性 CSS animation，不用 JS 逐帧），不等接口。
- 数字更新防抖：同一内容 800ms 内的多次点赞（自己点 + 收到的实时推送）合并渲染一次，避免数字疯狂跳动。
- 请求聚合：窗口内的点赞批量上报（数量 + 是否取消合并为净增量），服务端聚合扣减，把 QPS 压下来。
- 乐观更新要能回滚：批量上报失败时回退数字并静默重试一次，不打断用户浏览。

```javascript
// 点赞：即时动画 + 数字防抖聚合 + 批量上报可回滚
class LikeAggregator {
  pending = new Map();                                 // contentId -> 净增量
  shown = new Map();                                   // contentId -> 正在展示的数字
  constructor(flushInterval = 800) { this.flushInterval = flushInterval; }

  like(contentId, baseCount) {
    const delta = this.pending.get(contentId) ?? 0;
    this.pending.set(contentId, delta + 1);
    this.playAnim(contentId);                          // 动画立即播，不等网络
    this.scheduleFlush();
    this.scheduleRender(contentId, baseCount);
  }

  scheduleFlush() {
    if (this.timer) return;
    this.timer = setTimeout(async () => {
      this.timer = null;
      if (!this.pending.size) return;
      const batch = [...this.pending];                 // [[id, delta], ...]
      this.pending = new Map();
      try { await api.batchLike(batch); }
      catch {
        batch.forEach(([id, d]) => this.pending.set(id, (this.pending.get(id) ?? 0) + d));
        setTimeout(() => this.scheduleFlush(), 2000);  // 失败回滚进下一窗口静默重试
      }
    }, this.flushInterval);
  }

  scheduleRender(contentId, baseCount) {
    clearTimeout(this.renderTimers?.get(contentId));
    (this.renderTimers ??= new Map()).set(contentId, setTimeout(() => {
      const count = baseCount + [...this.pending].filter(([id]) => id === contentId)
        .reduce((s, [, d]) => s + d, 0);
      this.shown.set(contentId, count);
      updateLikeText(contentId, count);                // 窗口内只渲染一次，数字不跳动
    }, 400));
  }

  playAnim(contentId) {
    const el = document.querySelector(`#like-${contentId} .heart`);
    if (!el) return;
    el.classList.remove('heart-pop');                  // 一次性 CSS animation，无 JS 逐帧
    void el.offsetWidth;                               // 强制 reflow 以重启动画
    el.classList.add('heart-pop');
  }
}
```
