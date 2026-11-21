---
title: [AV-086] 移动端 H5 播放有哪些经典适配坑？（inline/全屏/内核差异）（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-086：移动端 H5 播放有哪些经典适配坑？（inline/全屏/内核差异）（高频）
**答**：
- iOS：video 默认全屏接管，必须 `playsinline + webkit-playsinline`；低电量模式/自动播放策略拦截；音量 API 只读（volume 属性无效），静音只能 muted。
- 安卓 X5/UC 内核：`x5-video-player-type="h5-page"` 同层播放，否则视频永远盖在 DOM 上；部分内核 video 尺寸必须撑满或居中，否则黑边。
- 全屏差异：`requestFullscreen` iOS 不支持 video 元素级（用 `webkitEnterFullscreen`）；安卓自定义全屏 = 播放器容器 transform + 横竖屏锁定（screen.orientation.lock）。
- 事件差异：timeupdate 频率不一（iOS 250ms~1s），进度条动画要用 rAF 插值；iOS seek 后可能触发完整 load。
- 实践清单：统一封装内核检测 + 属性全集 + 静音自动播放降级（AV-010）+ 手势播放队列。

```javascript
// 移动端播放适配器：内核检测 + 全屏封装
class MobilePlayerAdapter {
  constructor(video) {
    this.v = video;
    this.kernel = this.detect();
    this.applyInlineFix();
  }
  detect() {
    const ua = navigator.userAgent;
    if (/iPhone|iPad/.test(ua)) return 'ios';
    if (/MicroMessenger/.test(ua)) return 'wechat-x5';
    if (/QQ\//.test(ua)) return 'qq-x5';
    if (/Android/.test(ua)) return 'android';
    return 'desktop';
  }
  applyInlineFix() { // 差异属性一次性补齐
    const v = this.v;
    v.setAttribute('playsinline', '');
    v.setAttribute('webkit-playsinline', '');
    v.setAttribute('x5-playsinline', '');
    if (this.kernel.includes('x5')) {
      v.setAttribute('x5-video-player-type', 'h5-page');
      v.setAttribute('x5-video-orientation', 'portraint');
    }
  }
  async requestFullscreen() { // 全屏封装：三种实现
    if (this.v.enterFullscreen) return this.v.webkitEnterFullscreen();  // iOS video 原生
    if (document.documentElement.requestFullscreen) {
      await this.container.requestFullscreen();
      try { await screen.orientation.lock('landscape'); } catch (e) {}   // 安卓锁横屏
      return;
    }
    this.container.classList.add('fake-fullscreen'); // 老内核 CSS 伪全屏
  }
}
```
