---
title: [OPT-018] 第三方脚本（地图/视频/客服）如何用 facade 模式优化？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-018：第三方脚本（地图/视频/客服）如何用 facade 模式优化？

**答**：
- 问题：YouTube/高德地图等第三方脚本动辄数百 KB，且会在页面加载早期执行，挤占主线程（伤 TBT/INP）。
- facade 模式：页面先渲染一个"假外观"——封面缩略图 + 播放按钮 + 加载提示，**不加载任何第三方 JS**；用户点击时才动态插入真实 SDK。
- 视频封面可用 `https://i.ytimg.com/vi/<id>/hqdefault.jpg` 官方缩略图，配合大按钮满足无障碍。
- 收益案例：web.dev 用 lite-youtube 后，首屏渲染时间从 5.5s 降到 650ms 量级。

```jsx
// 一一对应：视频 facade 组件 —— 点击前不加载任何第三方脚本
import { useState } from 'react';

export default function VideoFacade({ videoId, title }) {
  const [activated, setActivated] = useState(false);

  if (activated) {
    // 点击后才真正插入 iframe，加载 YouTube 脚本
    return (
      <iframe
        src={`https://www.youtube.com/embed/${videoId}?autoplay=1`}
        title={title}
        allow="autoplay; fullscreen"
        style={{ width: '100%', aspectRatio: '16 / 9' }}
      />
    );
  }

  // facade：静态缩略图 + 按钮，零第三方脚本成本
  return (
    <button
      onClick={() => setActivated(true)}
      aria-label={`播放视频 ${title}`}
      style={{ position: 'relative', width: '100%', aspectRatio: '16 / 9', border: 'none' }}
    >
      <img
        src={`https://i.ytimg.com/vi/${videoId}/hqdefault.jpg`}
        alt=""
        style={{ width: '100%', height: '100%', objectFit: 'cover' }}
      />
      <span style={{ position: 'absolute', inset: 0, display: 'grid', placeItems: 'center', fontSize: 48 }}>
        ▶
      </span>
    </button>
  );
}
```
