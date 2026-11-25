---
title: [AV-342] HLS 与 DASH 协议对比
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-342：HLS 与 DASH 协议对比

**答**：
- HLS：m3u8 文本清单 + TS/fMP4 切片，苹果原生、延迟原版 6~30s（LL-HLS 可到 2~5s）。
- DASH：XML 清单（MPD），标准更开放，MSE 配合好，Chrome 生态主流。
- 选型：Apple 生态必 HLS；Web 优先 HLS（工具链成熟）或 DASH（需要 SegmentTemplate 低延迟）。

```javascript
// HLS 清单解析
function parseHLS(text) {
  const lines = text.split('\n');
  if (lines[0].includes('EXT-X-STREAM-INF')) {        // master
    return lines.reduce((acc, l, i) => {
      if (l.startsWith('#EXT-X-STREAM-INF')) {
        const bw = +/BANDWIDTH=(\d+)/.exec(l)[1];
        acc.push({ bandwidth: bw, url: lines[i + 1] });
      }
      return acc;
    }, []);
  }
  const segs = [];
  let dur = 0;
  for (const l of lines) {
    if (l.startsWith('#EXTINF:')) dur = +l.split(':')[1].split(',')[0];
    else if (l && !l.startsWith('#')) segs.push({ url: l, dur });
  }
  return { segments: segs, total: segs.reduce((s, x) => s + x.dur, 0) };
}
```
