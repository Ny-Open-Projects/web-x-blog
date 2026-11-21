---
title: [AV-017] LL-HLS 是怎么把延迟降到 2 秒以内的？
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-017：LL-HLS 是怎么把延迟降到 2 秒以内的？
**答**：
- 三大武器：Part Segments（把 4s 分片再切成 ~0.2-0.5s 的 part，边生产边可拉）、Blocking Playlist Reload（`_HLS_msn/_HLS_part` 参数，服务器 hold 住请求直到新内容到达，省轮询）、Preload Hints（`#EXT-X-PRELOAD-HINT` 提前预告下一个 part 的 URL）。
- 延迟降到分片时长 + 1~2 个 part，即 2~4s；配合极短分片可进 1s 级。
- 代价：请求频率暴涨，对 CDN 与源站压力大；需 HTTP/2 复用连接； Apple 官方与 hls.js（v1.2+）已支持。
- 与之竞争的方案：LL-DASH（chunked transfer）、HTTP-FLV、WebRTC；工业界国内更常用 HTTP-FLV 做低延迟直播。
- 面试要点：能说出 part 与 segment 的关系、阻塞式刷新消除了"猜下一个分片好了没"的轮询延迟。

```text
#EXTM3U
#EXT-X-VERSION:9
#EXT-X-TARGETDURATION:4
#EXT-X-PART-INF:PART-TARGET=0.334
#EXT-X-MEDIA-SEQUENCE:2680
#EXT-X-SERVER-CONTROL:CAN-BLOCK-RELOAD=YES,PART-HOLD-BACK=1.0,HOLD-BACK=3.0
#EXT-X-PART:DURATION=0.334,URI="part-2680-1.mp4",INDEPENDENT=YES
#EXT-X-PART:DURATION=0.334,URI="part-2680-2.mp4"
#EXTINF:4.0,
seg-2680.mp4
#EXT-X-PRELOAD-HINT:TYPE=PART,URI="part-2680-3.mp4"
```

```javascript
// Blocking reload：服务器 hold 到目标分片才返回，无需客户端轮询
async function blockingReload(baseUrl, msn, part) {
  const url = `${baseUrl}?_HLS_msn=${msn}&_HLS_part=${part}`;
  return (await fetch(url)).text(); // 可能挂起 1~2s，配合 HTTP/2 多路复用
}
```
