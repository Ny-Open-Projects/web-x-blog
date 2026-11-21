---
title: [PER-088] 第三方脚本的“性能税”怎么量化？facade 模式如何实现？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-088：第三方脚本的“性能税”怎么量化？facade 模式如何实现？

**答**：
- 性能税量化：对比加载第三方前后的 LCP/INP/带宽占用，或用 Performance 面板看它占的长任务时长与请求数；典型如地图/视频/客服脚本动辄 300KB+ 且同步阻塞。
- facade（门面）模式：页面只渲染一个**假组件**（静态海报 + 播放按钮），用户点击才真正加载第三方 SDK——把 200KB 的税变成“用户点击后 5KB 假组件”。
- 实现要点：假组件用真实封面图 + 原生按钮保可访问性；点击后动态 inject 脚本并在加载完成时把交互转发给真组件。
- 适合对象：YouTube/Bilibili 嵌入、Google 地图、在线客服、社交媒体挂件——它们都在首屏外或首交互前不必要。

```jsx
// React：facade 模式 —— 点击才加载 200KB 的视频播放器
function VideoFacade({ videoId, title }) {
  const [loaded, setLoaded] = useState(false);

  if (loaded) return <iframe
    src={`https://www.youtube.com/embed/${videoId}?autoplay=1`}
    title={title} allow="autoplay" allowFullScreen
    style={{ width: '100%', aspectRatio: '16/9', border: 0 }} />;

  // 未点击时只渲染 5KB 的假组件：封面图 + 原生按钮
  return (
    <button
      className="video-facade"
      style={{ width: '100%', aspectRatio: '16/9', background: `url(https://i.ytimg.com/vi/${videoId}/hqdefault.jpg) center/cover` }}
      aria-label={`播放视频 ${title}`}
      onClick={() => setLoaded(true)}>  {/* 点击这一刻才引入第三方 iframe 与脚本 */}
      <span className="play-icon" aria-hidden="true" />
    </button>
  );
}
```
