---
title: [H5-285] 音视频 autoplay 被拒后的用户引导策略
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, 音视频]
type: 面试题
---

## H5-285：音视频 autoplay 被拒后的用户引导策略

**答**：
- 被拒后的三档体验：静音自动播（保持画面动）→ 封面+播放按钮（明确可点）→ 自动尝试后失败才显示引导
- 引导文案设计：不写「点击播放」而写「点击开启声音」——画面已经在动（静音播），引导用户恢复声音是二次转化
- 解锁时机：全站任意首次交互都算解锁（click/scroll/keydown），在 document 级监听 once，解锁后自动恢复声音
- 记忆状态：localStorage 记住用户选择（允许声音/始终静音），下次直接执行不再打扰
- 直播场景特例：拉流类直播静音自动播 + 大角标「点击进入直播间」是行业通用解

```javascript
const unlocked = { muted: localStorage.getItem('sound') === 'off' };
document.addEventListener('pointerdown', () => { window.__userGesture = true; }, { once: true });
video.addEventListener('playing', () => {
  if (!unlocked.muted && window.__userGesture) video.muted = false; // 有手势记录后恢复声音
});
```
