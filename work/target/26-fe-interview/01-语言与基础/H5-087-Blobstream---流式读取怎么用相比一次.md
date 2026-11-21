---
title: [H5-087] Blob.stream() 流式读取怎么用？相比一次性读取好在哪？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-087：Blob.stream() 流式读取怎么用？相比一次性读取好在哪？
**答**：
- `blob.stream()` 返回 `ReadableStream`，按块产出 `Uint8Array`，**内存占用恒定**，适合 GB 级文件与边读边传。
- 一次性 `arrayBuffer()` 会把整个文件拉进内存，大文件直接 OOM 或触发移动端崩溃。
- 管道组合：`stream.pipeTo(writable)` 或 `pipeThrough` 接入解压/变换流（如 `DecompressionStream('gzip')`），形成处理流水线。
- 进度可控：手动 `for await (const chunk of stream)` 循环里累加字节数即得读取进度。
- 配合 fetch 上传：`fetch(url, { method: 'POST', body: blob.stream() })`（注意部分浏览器要求设置 `duplex: 'half'` 且不支持重试，工程上需权衡）。

```javascript
const bigFile = document.querySelector('input[type=file]').files[0]; // 2GB 视频

// 1) 流式读取 + 进度上报
async function readWithProgress(file, onProgress) {
  const stream = file.stream();
  const reader = stream.getReader();
  let received = 0;
  const chunks = [];

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    chunks.push(value);
    received += value.byteLength;
    onProgress(received / file.size);        // 0~1，可驱动进度条
  }
  return new Blob(chunks, { type: file.type });
}

// 2) 流式解压：gzip 文件边解边收，全程低内存
async function gunzip(file) {
  const ds = new DecompressionStream('gzip');
  const out = file.stream().pipeThrough(ds);
  return new Response(out).blob();           // Response 可直接消费 ReadableStream
}

// 3) 流式上传（边读边发，不落内存）
async function uploadStream(file) {
  await fetch('/api/upload', {
    method: 'POST',
    body: file.stream(),
    headers: { 'Content-Type': file.type },
    duplex: 'half',                          // Chrome 要求：流式请求体需声明
  });
}

// 4) 对比：错误示范——大文件一次性进内存
// const all = await bigFile.arrayBuffer();   // 2GB 直接占满内存
```
