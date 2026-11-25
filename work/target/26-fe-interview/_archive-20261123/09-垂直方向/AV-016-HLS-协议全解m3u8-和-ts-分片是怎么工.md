---
title: [AV-016] HLS 协议全解？m3u8 和 ts 分片是怎么工作的？延迟由什么构成？（高频压轴）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-016：HLS 协议全解？m3u8 和 ts 分片是怎么工作的？延迟由什么构成？（高频压轴）
**答**：
- HLS（HTTP Live Streaming）把流切成小分片（TS 或 fMP4），用 m3u8 索引文件描述顺序，客户端像下载普通文件一样循环拉取。
- m3u8 关键标签：`#EXTM3U`、`#EXT-X-VERSION`、`#EXTINF`（分片时长）、`#EXT-X-TARGETDURATION`、直播还有 `#EXT-X-MEDIA-SEQUENCE`（滑动窗口首序号）与 `#EXT-X-ENDLIST`（点播结束标志）。
- 直播播放循环：拉 playlist → 等待/下载新分片 → 下载间隙 sleep（约分片时长）→ 再拉 playlist；playlist 只保留最近几个分片（滑动窗口）。
- 延迟构成 ≈ 分片时长 × 缓冲分片数 + playlist 刷新周期 + 编码/CDN 缓存，标准 4s 分片约 12~20s 延迟。
- 优点：走 HTTP/80 端口、CDN 天然友好、自适应性靠多码率 playlist；缺点：延迟高。

```text
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:4
#EXT-X-MEDIA-SEQUENCE:1024
#EXTINF:4.0,
seg-1024.ts
#EXTINF:4.0,
seg-1025.ts
#EXTINF:4.0,
seg-1026.ts
```

```javascript
// 极简 HLS 直播拉流循环（说明原理，生产用 hls.js）
async function hlsLiveLoop(playlistUrl, onSegment) {
  let seq = 0;
  while (true) {
    const text = await (await fetch(playlistUrl)).text();
    const lines = text.split('\n');
    if (lines.includes('#EXT-X-ENDLIST')) break; // 点播结束
    const segs = [];
    for (let i = 0; i < lines.length; i++) {
      if (lines[i].startsWith('#EXTINF')) {
        segs.push({ duration: parseFloat(lines[i].slice(8)), url: lines[i + 1] });
      }
    }
    const mediaSeq = +lines.find((l) => l.startsWith('#EXT-X-MEDIA-SEQUENCE')).slice(20);
    for (const s of segs) {
      if (s.index = segs.indexOf(s) + mediaSeq, s.index > seq) {
        seq = s.index;
        onSegment(await (await fetch(s.url)).arrayBuffer()); // 喂给 MSE
      }
    }
    await new Promise((r) => setTimeout(r, 2000)); // 约半个分片周期再刷 playlist
  }
}
```
