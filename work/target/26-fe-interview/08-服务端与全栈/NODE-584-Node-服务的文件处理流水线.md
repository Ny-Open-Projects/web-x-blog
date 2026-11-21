---
title: [NODE-584] Node 服务的文件处理流水线（上传后异步处理编排）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-584：文件处理流水线
**答**:
- 场景：上传后多步处理（图片：缩略图+水印+审核；视频：转码多档+截图封面——多步异步编排 ARC-341/343）。
- 编排模型：处理 DAG（上传完成事件 → 各处理任务并行/串行依赖——模板化：按文件类型选流水线）、步骤幂等（每步可重跑——产物存在即跳过）、失败隔离（单步失败不影响独立步骤——部分产物可用）。
- 状态呈现：文件处理状态（处理中/部分可用/可用——前端展示渐进可用：缩略图好了先显示 ARC-595 骨架→内容）、处理失败重试入口。
- 资源调度：处理任务资源分级（视频转码重——独立 worker 池限并发 NODE-418）、优先级（用户正在看的文件优先——交互优先级）。
- 产物管理：产物与源文件关联（产物清单——源文件删除级联清理）、产物复用（同内容 hash 处理结果复用——秒处理）。
```javascript
// 文件处理 DAG
const pipelines = {
  image: ['thumbnail', 'watermark', 'moderate'],                 // 并行无依赖
  video: ['probe', ['transcode-480', 'transcode-720'], 'cover', 'moderate']  // 转码并行后封面
};
upload.on('done', (f) => orchestrate(pipelines[f.type], f, { idempotent: true }));
// 状态：pipeline.progress(f.id) → { thumbnail: done, transcode-720: 40% } 渐进可用
```
