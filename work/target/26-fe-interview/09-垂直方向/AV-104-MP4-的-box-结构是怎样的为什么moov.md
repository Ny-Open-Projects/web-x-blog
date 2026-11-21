---
title: [AV-104] MP4 的 box 结构是怎样的？为什么"moov 在前"对网络播放很重要？（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-104：MP4 的 box 结构是怎样的？为什么"moov 在前"对网络播放很重要？（高频）
**答**：
- MP4 由嵌套 box 组成：ftyp（文件类型）→ moov（索引元数据）→ mdat（音视频数据），box 头 8 字节 = 4 字节长度 + 4 字节类型。
- moov 里的 sample 表记录每帧的偏移/大小/时长，播放器没拿到 moov 就无法定位任何一帧。
- 传统 MP4 写完文件才知道索引（moov 在尾部），网络播放要下完整文件；faststart 把 moov 移到头部，支持边下边播。
- MSE 场景建议 fMP4：每个 moof+mdat 自带小索引，天然适合分片流式喂 SourceBuffer。
- 前端工程点：上传服务要校验 moov 位置（转码 pipeline 里 qt-faststart/-movflags +faststart 兜底）。

```javascript
// MP4 box 树遍历：找出 moov 与 mdat 位置判断是否 faststart
function walkBoxes(u8, start = 0, end = u8.length, depth = 0) {
  const boxes = [];
  let offset = start;
  while (offset < end - 7) {
    const size = (u8[offset] << 24) | (u8[offset+1] << 16) | (u8[offset+2] << 8) | u8[offset+3];
    const type = String.fromCharCode(...u8.subarray(offset + 4, offset + 8));
    boxes.push({ type, offset, size, depth });
    if (['moov', 'trak', 'mdia', 'minf', 'stbl'].includes(type)) {
      boxes.push(...walkBoxes(u8, offset + 8, offset + size, depth + 1)); // 容器 box 递归
    }
    if (size <= 0) break;
    offset += size;
  }
  return boxes;
}
// 用法：Range 请求拿头部 64KB 解析，moov.offset < mdat.offset 即 faststart
// const head = new Uint8Array(await (await fetch(url, { headers: { Range: 'bytes=0-65535' } })).arrayBuffer());
// const boxes = walkBoxes(head);
// console.log(boxes.filter((b) => ['moov', 'mdat', 'ftyp'].includes(b.type)));
```
