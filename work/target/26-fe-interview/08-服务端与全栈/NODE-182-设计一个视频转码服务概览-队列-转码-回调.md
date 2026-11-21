---
title: [NODE-182] 设计一个视频转码服务概览（队列/转码/回调）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-182：设计一个视频转码服务概览（队列/转码/回调）？
**答**：
- 流水线：上传完成（NODE-126 直传回调）→ 转码队列 → **多清晰度并行转码**（ffmpeg HLS 切片）→ 分片上传 OSS → 回调业务方更新状态。
- 任务设计：ffmpeg `-progress` 解析实时进度写 Redis（前端进度条）；按输出时长/分辨率估算资源，队列按权重调度（VIP 优先）。
- 可靠性：转码幂等（同输入同输出可重试）、分片级断点续转、抢占式节点 + 失败重试控制成本。
- 输出协议：HLS（m3u8 + ts 分片）天然自适应码率；封面图从首帧/关键帧抽取。

```javascript
new Worker('transcode', async (job) => {
  const { fileId, src, presets } = job.data;   // presets: [{ name, height, bitrate }]
  const meta = await ffprobeMeta(src);          // 1. 探针：时长/分辨率/音轨
  const results = await Promise.all(presets.map((p) =>   // 2. 多清晰度并行
    transcodeOne(src, p)));
    // ffmpeg -i src -vf scale=-2:720 -f hls -hls_time 6 -hls_list_size 0 out.m3u8
  await uploadHlsToOss(results);                 // 3. m3u8 + ts 分片上传
  await db.file.update({ where: { id: fileId },
    data: { status: 'READY', durationMs: meta.durationMs } });
  await mq.publish('video.transcoded', { fileId });      // 4. 回调业务方
}, { concurrency: 2, timeout: 3_600_000 });

// 进度上报：ffmpeg -progress pipe:1 → 解析 out_time_ms → redis.setex(`tprog:${jobId}`, 3600, pct)
```
