---
title: [PER-1055] 如何度量和优化"感知性能"（Perceived Performance）
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1055：如何度量和优化"感知性能"（Perceived Performance）

**答**：
- 感知 ≠ 实测：骨架屏、乐观 UI、进度反馈都能降低感知等待，即使真实耗时相同。
- 手段：非阻塞骨架（形状匹配真实内容，避免加载后跳动）、乐观更新（写操作立即反馈 + 失败回滚）、分层加载（先文字后图片渐进）。
- 度量：感知指标可用"首次有意义交互时间"与主观 NPS 关联；A/B 验证骨架屏对跳出率的影响。
- 反模式：假进度条、闪烁的骨架（闪 200ms 就出数据反而增加感知延迟）。

```javascript
// 乐观更新 + 失败回滚
async function likePost(id) {
  const prev = store.get(id).likes;
  store.set(id, { ...store.get(id), likes: prev + 1, liked: true });  // 立即反馈
  try {
    await api(`/posts/${id}/like`, { method: 'POST' });
  } catch (e) {
    store.set(id, { ...store.get(id), likes: prev, liked: false });   // 回滚
    toast('点赞失败，已恢复');
  }
}
// 感知对比：等待 800ms 后反馈 vs 立即反馈，后者主观等待感低 50%+
```
