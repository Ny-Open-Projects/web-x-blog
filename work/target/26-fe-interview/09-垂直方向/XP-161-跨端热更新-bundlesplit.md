---
title: [XP-161] 跨端热更新 bundlesplit：按页面拆分与按需下载
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 笔试题, 27]
type: 笔试题
---

## XP-161：跨端热更新 bundlesplit：按页面拆分与按需下载

**答**：
- 题目：bundle 按页面拆分——每个页面独立 chunk，进页面时按需下载（未访问页面不占流量）；核心 chunk 常驻。
- 思路：manifest 记录页面 → chunk 映射；路由跳转时检查 chunk 是否已下载（未下载则先拉取+校验）；预下载（用户浏览路径预测）。
- 评分点：chunk 映射；按需下载；预下载策略。

```javascript
class PageBundleSplit {
  constructor(manifest) { this.manifest = manifest; this.loaded = new Set(['core']); }
  async navigate(pageId) {                                   // 路由跳转
    if (this.loaded.has(pageId)) return this.mount(pageId);   // 已加载
    const chunk = this.manifest.pages[pageId];
    if (!chunk) throw new Error('unknown-page');
    await this.downloadChunk(chunk);                          // 按需下载（含校验）
    this.loaded.add(pageId);
    return this.mount(pageId);
  }
  prefetch(likelyPages) {                                    // 预下载（浏览路径预测）
    likelyPages.filter(p => !this.loaded.has(p))
      .forEach(p => this.downloadChunk(this.manifest.pages[p]).catch(() => {}));
  }
}
```
