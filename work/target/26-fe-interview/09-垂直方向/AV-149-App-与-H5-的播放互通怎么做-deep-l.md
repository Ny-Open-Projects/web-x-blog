---
title: [AV-149] App 与 H5 的播放互通怎么做？（deep link / 接力）（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-149：App 与 H5 的播放互通怎么做？（deep link / 接力）（高频）
**答**：
- 场景：H5 分享页唤起 App 续播（进度接力）；App 内嵌 H5 跳原生播放器。
- 技术：Universal Links（iOS）/ App Links（安卓）直达具体页 + 自定义 URL Scheme 兜底；参数带 videoId + currentTime。
- 接力实现：H5 把进度写入 URL 参数或短链服务，App 启动后取参 seek 续播；未装 App 降级留在 H5。
- 反向：App 内 H5 用 JSBridge（postMessage）请求原生播放器接管，原生播完回传进度。
- 坑：微信内屏蔽自定义 Scheme（需开放标签 wx-open-launch-app）；iOS Universal Links 依赖域名校验（AASA 文件）配置正确。

```javascript
// H5 唤起 App 续播（含降级链）
function handoffToApp({ videoId, currentTime }) {
  const payload = encodeURIComponent(JSON.stringify({ videoId, t: Math.floor(currentTime), from: 'h5' }));
  const universalLink = `https://app.example.com/play?ctx=${payload}`; // 首选 装了App直达
  const scheme = `myapp://player?ctx=${payload}`;                       // 兜底
  location.href = universalLink;
  setTimeout(() => {
    if (!document.hidden) {                        // 页面仍在前台说明未唤起
      const ifr = document.createElement('iframe'); // iframe 触发 scheme 防当前页跳走
      ifr.src = scheme;
      document.body.appendChild(ifr);
      setTimeout(() => ifr.remove(), 100);
      showStayHint();                              // 最终兜底 留在 H5 继续播
    }
  }, 1500);
}
```
