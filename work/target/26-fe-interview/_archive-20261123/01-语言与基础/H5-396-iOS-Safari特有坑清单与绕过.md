---
title: [H5-396] iOS Safari 特有坑清单与绕过方案
date: 2026-11-21
categories: [HTML5]
tags: [前端面试, 面试题, 适配]
type: 面试题
---

## H5-396：iOS Safari 特有坑清单与绕过方案

**答**：
- 滚动/布局类：100vh 含地址栏导致底部被遮（用 svh/dvh 或 JS 修正）、fixed 元素随软键盘漂移、body 滚动链需 overscroll-behavior + touchmove 阻断配合
- 事件类：click 委托在 body/document 上可能失效（非交互元素不加 cursor: pointer 时不触发 click）、被动监听默认、300ms 历史（已基本解决）
- 音视频类：自动播放限 muted、audio 必须手势内 play（首次解锁音频 AudioContext resume）、video 全屏接管需 playsinline
- 存储与隐私：ITP 对第三方 cookie/storage 7 天清退、Safari 无 performance.memory、bfcache 行为与 Chrome 不同（pagehide/pageshow 事件适配）
- 渲染类：position: sticky 在复杂层级失效、backdrop-filter 性能差、canvas 大尺寸内存爆炸（尺寸上限约 16M 像素级）

```css
/* 100vh 修正 */
.hero { height: 100vh; height: 100dvh; }       /* dvh 动态视口 */
/* 固定底栏: 键盘期 fixed 漂移 → absolute + 内容区 padding 兜底 */
.tabbar { position: fixed; bottom: 0; }
@supports (-webkit-touch-callout: none) {       /* iOS 特定 */
  .tabbar { position: absolute; }
}
```

```javascript
// 音频解锁(iOS)
const unlockAudio = () => { audioCtx.resume(); audio.play().then(() => audio.pause()); document.removeEventListener('touchend', unlockAudio); };
document.addEventListener('touchend', unlockAudio, { once: true });
```
