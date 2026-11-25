---
title: [JS-350] transferable 与零拷贝：大数据跨线程传输
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 面试题, 并发]
type: 面试题
---

## JS-350：transferable 与零拷贝：大数据跨线程传输

**答**：
- 结构化克隆 vs transfer：默认克隆深拷贝（100MB buffer 拷贝数百 ms）；transfer 转移所有权（O(1)，原线程 buffer detach）——大二进制必走 transfer
- transferable 家族：ArrayBuffer、MessagePort、ImageBitmap、OffscreenCanvas、ReadableStream——canvas 转移给 Worker 是零拷贝渲染的基础
- 所有权模型：转移后原引用失效（byteLength 0）——代码要显式管理「谁拥有 buffer」，用完归还/复用（对象池）而不是频繁转移新建
- 混合传输：一个消息里部分字段克隆、部分 transfer（postMessage 第二参数只列 transferable）——大结构中只 transfer 数值缓冲部分
- 测量方法：大 buffer 克隆 vs 转移耗时对比（performance.now），1MB 级差距就开始明显——「多少大算大」的量化意识

```javascript
// 零拷贝管线: 主线程拿图 → worker 处理 → 转回
const bmp = await createImageBitmap(file);
const off = new OffscreenCanvas(bmp.width, bmp.height);
worker.postMessage({ canvas: off, bmp }, [off, bmp]);       // 双 transfer
// worker 返回:
postMessage({ buf: result.buffer }, [result.buffer]);       // 结果转移回来
```
