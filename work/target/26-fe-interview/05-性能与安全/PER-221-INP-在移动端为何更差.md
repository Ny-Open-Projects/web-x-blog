---
title: [PER-221] 为什么同样的页面移动端 INP 明显更差？有哪些针对性手段？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-221：为什么同样的页面移动端 INP 明显更差？有哪些针对性手段？

**答**：
- 硬件差距：移动端 CPU 单核性能、内存带宽、GPU 都弱于桌面，同样 100ms 的 handler 在中低端安卓上可能翻 2~3 倍；主线程与合成器线程共享更紧张的算力，presentation 段也被拉长。
- 触发密度：移动端手势事件高频（scroll/pointermove 触发的 handler），且触摸事件有合成开销；键盘用户每秒几次输入，触屏用户一次滑动可能派发几十个事件。
- 网络与首帧挤压：移动端弱网下资源加载慢，用户在页面仍在加载时就点击，事件与解析任务挤在主线程排队，input delay 段被放大。
- 针对手段：① 以中端安卓设备为性能预算基准（如 4 倍降速 CPU 模拟）；② pointermove/scroll handler 被动化（passive:true）+ rAF 节流；③ 触摸反馈用 CSS 伪类（合成器线程）替代 JS class 切换；④ 首屏 JS 预算砍半，长任务全部切片；⑤ 输入场景优先用 transition/transform 动画。

```javascript
// 移动端高频手势 handler 的标准形态：passive + rAF 合帧
let ticking = false;
document.addEventListener('touchmove', (e) => {
  // passive: true 声明不 preventDefault，滚动不被 handler 阻塞
  if (ticking) return;
  ticking = true;
  requestAnimationFrame(() => {     // 每帧最多执行一次
    updateHeaderShadow(scrollY);
    ticking = false;
  });
}, { passive: true });
// 触摸按压反馈交给 CSS：.btn:active { transform: scale(.96); }，不写 JS class 切换
```
