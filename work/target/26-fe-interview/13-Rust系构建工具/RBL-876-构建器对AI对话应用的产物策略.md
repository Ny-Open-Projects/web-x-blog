---
title: [RBL-876] 场景题：AI 对话应用的产物策略——流式渲染、长会话内存与构建配合
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-876：场景题：AI 对话应用的产物策略——流式渲染与长会话内存

**答**:
- AI 对话页的产物特征：1) **Markdown 流式渲染**（token 级追加 + markdown 增量解析——全量重渲染每 token 是性能灾难；增量 DOM patch 或 rAF 合帧）；2) **长会话内存**（千条消息的 DOM = 内存爆炸——虚拟列表 + 消息分页加载）；3) 流式库独立 chunk（RBL-874）+ 代码高亮懒加载（代码块出现时才加载 shiki 运行时或预高亮）。
- 构建配合的决策点：markdown 渲染器的选择影响体积（marked+DOMPurify ~20KB vs markdown-it ~100KB vs 编译期方案）——按「对话内容的 markdown 复杂度」选（聊天文本简单 → 轻量渲染器）；归因报告（RBL-739）定位「渲染器占对话页 bundle 的比例」。
- 长会话的构建期策略：消息历史的序列化边界（IndexedDB 持久化 + 会话分片加载）——构建器无关但「会话 store 的体积」参与代码审查（全局 store 塞全部历史 = 内存泄漏）。
- 流式渲染的 abort 语义：用户停止生成 → AbortController 中断 fetch（RBL-640 取消语义的应用侧）——部分响应的落库（半截消息保留 + 「已停止」标记）。
- 追问钩子：为什么「markdown 全量重渲染」在流式场景是灾难？——千字回复 = 千次 token 到达 = 千次全量 markdown parse + DOM 重建（每次 5-10ms → 主线程占用 50%+，输入卡顿）；正确姿势是「增量 append（最后段落重渲染）+ rAF 合帧」（渲染频率与屏幕刷新对齐）——流式 UI 的性能本质是「渲染批处理」，与 HMR 合帧（RBL-573）同构。

```javascript
// 增量流式渲染（rAF 合帧）
class StreamingRenderer {
  #pending = ''; #raf = null;
  append(token) {
    this.#pending += token;
    if (this.#raf) return;                               // 合帧：每帧最多渲染一次
    this.#raf = requestAnimationFrame(() => {
      this.#raf = null;
      const full = this.#pending; this.#pending = '';
      this.renderIncremental(full);                      // 只重渲染最后未闭合段落
    });
  }
  renderIncremental(text) {
    const blocks = text.split('\n\n');
    const last = blocks[blocks.length - 1];
    // 已闭合段落：缓存 DOM 不再重渲染；未闭合尾段：局部替换
    this.tail.innerHTML = mdLite(last);                  // 轻量渲染器（~5KB）
  }
}
// 虚拟列表 + 分页
const conv = useVirtualList(messages, { overscan: 5 });   // 千条消息只渲染可视区
// 构建配置：渲染器按需
manualChunks: { chat: ['src/lib/md-lite', 'src/lib/stream'] },   // RBL-597 共享 chunk
```
