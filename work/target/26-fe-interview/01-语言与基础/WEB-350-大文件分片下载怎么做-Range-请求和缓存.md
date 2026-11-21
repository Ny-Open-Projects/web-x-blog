---
title: [WEB-350] 大文件分片下载怎么做？Range 请求和缓存怎么配合？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 缓存]
type: 笔试题
---

## WEB-350：大文件分片下载怎么做？Range 请求和缓存怎么配合？
**答**：
- Range: bytes=start-end 请求文件片段，服务器回 206 Partial Content + Content-Range；不支持则回 200 全量。
- 用途：断点续传（记住已下 offset）、视频拖动播放（seek 即 Range）、并行加速（多连接分段）。
- 缓存配合：分片也可被缓存（Cache-Control 有效时），校验一致性靠 If-Range + ETag，ETag 变了则整个重下。

```javascript
async function download(url, total) {
  const CHUNK = 1024 * 1024, parts = [];
  for (let s = 0; s < total; s += CHUNK) {
    const res = await fetch(url, {
      headers: { Range: 'bytes=' + s + '-' + Math.min(s + CHUNK - 1, total - 1) } });
    if (res.status !== 206) throw new Error('服务器不支持 Range');
    parts.push(await res.arrayBuffer());
  }
  return new Blob(parts);   // 合并分片
}
console.log('206 + Content-Range + If-Range = 断点续传核心');
```

**评分点**：
- 结论先行，机制一句话讲透
- 覆盖攻击面/异常分支与边界条件
- 代码可运行、命名清晰、有防御性处理
- 主动给出工程取舍与常见坑
