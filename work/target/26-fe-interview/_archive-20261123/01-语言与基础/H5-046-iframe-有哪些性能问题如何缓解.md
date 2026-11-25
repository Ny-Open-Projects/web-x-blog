---
title: [H5-046] iframe 有哪些性能问题？如何缓解？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-046：iframe 有哪些性能问题？如何缓解？
**答**：
- iframe 是独立文档：独立的解析、渲染、样式计算，等于开一个"子页面"，主线程开销大。
- 阻塞父页面 onload（影响部分性能指标）；每个 iframe 是独立合成层，内存与 GPU 开销高。
- 缓解：`loading="lazy"` 延迟创建、把 iframe 挂载推迟到需要时、用 `content-visibility: auto` 包裹、不可信内容配 sandbox。
- 替代思路：能合并的合并成组件，地图/播放器类用官方 JS SDK 按需初始化，广告类限制数量并懒加载。

```html
<!-- 视口外的 iframe 懒加载：滚动接近时才创建文档 -->
<iframe src="https://maps.example.com/embed" loading="lazy" width="600" height="400" title="门店地图"></iframe>

<!-- content-visibility：不在视口内时跳过子树渲染开销 -->
<div style="content-visibility: auto; contain-intrinsic-size: 400px;">
  <iframe src="https://player.example.com/video/1" title="视频"></iframe>
</div>

<script>
  // 更彻底的方案：交互时才注入 iframe
  const slot = document.querySelector('.video-slot');
  slot.querySelector('.play-btn').addEventListener('click', () => {
    const iframe = document.createElement('iframe');
    iframe.src = 'https://player.example.com/video/1?autoplay=1';
    iframe.allow = 'autoplay; fullscreen'; // 权限策略按需放行
    slot.replaceChildren(iframe);
  }, { once: true });
</script>
```
