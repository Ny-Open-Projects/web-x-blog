---
title: [CSS-173] 键盘弹起把输入框遮挡，有哪些解决方案（visualViewport）？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-173：键盘弹起把输入框遮挡，有哪些解决方案（visualViewport）？

**答**：
- 病灶：iOS 上键盘弹起不改 layout viewport，`position: fixed` 的底栏仍在“视口底部”但被键盘盖住。
- 核心方案：监听 `visualViewport` 的 resize/scroll，`window.innerHeight - vv.height - vv.offsetTop` 即键盘遮挡高度，用 translateY 抵消。
- 辅助方案：聚焦时 `scrollIntoView({ block: 'center' })`；纯展示页可改用“键盘弹起时把 fixed 改 static”的布局降级。
- Android 键盘默认会压缩视口，通常自动正确；iOS Safari 15+ 的 interactive-widget 也值得在 meta 上声明。

```html
<input class="ipt" placeholder="请输入">
<div class="chat-box">底部输入条</div>
<style>
  .chat-box {
    position: fixed;
    left: 0; right: 0; bottom: 0;
    padding: 12px;
    background: #fff;
    border-top: 1px solid #eee;
    transition: transform .1s;   /* 可选：跟随更顺滑 */
  }
</style>
<script>
  const box = document.querySelector('.chat-box');
  const vv = window.visualViewport;
  function sync() {
    if (!vv) return;
    // 键盘遮挡高度 = 布局视口高 - 可视视口高 - 可视视口偏移
    const overlap = Math.max(0, window.innerHeight - vv.height - vv.offsetTop);
    box.style.transform = `translateY(-${overlap}px)`;
  }
  if (vv) {
    vv.addEventListener('resize', sync);
    vv.addEventListener('scroll', sync);
    sync();
  }
  // 辅助：聚焦时把输入框滚到可视区中部
  document.querySelector('.ipt').addEventListener('focus', e =>
    e.target.scrollIntoView({ block: 'center' }));
</script>
```
