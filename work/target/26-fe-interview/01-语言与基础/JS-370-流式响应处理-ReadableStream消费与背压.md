---
title: [JS-370] 流式响应处理：ReadableStream 消费与背压
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 面试题, 并发]
type: 面试题
---

## JS-370：流式响应处理：ReadableStream 消费与背压

**答**：
- 消费模式：reader.read() 手动循环（控制力最强）、for await（语法糖）、pipeTo/pipeThrough（管道链接转换器）——LLM 流式输出用「手动读 + 行缓冲解析」
- 背压的真实含义：ReadableStream 的 pull 机制让「消费速度决定生产速度」——fetch body 流在客户端消费慢时 TCP 窗口收缩（自动背压），但要理解 UI 渲染才是瓶颈（解析快渲染慢要队列缓冲）
- 大文件下载的处理：不缓冲整包（arrayBuffer 会全驻内存）——pipeTo WritableStream（写磁盘/IndexedDB/SW 缓存）或逐块处理聚合 hash（进度 + 校验）
- 流的错误与取消：reader.cancel() 触发上游中止（连接断开）；try/catch 包 read 循环处理网络中断——下载断点续传靠 Range 请求 + 已收字节数
- 转换器设计：TransformStream 封装「解析/解压/解密」中间步骤——TextDecoderStream/DecompressionStream 现成可用，自定义解析器按同样接口

```javascript
async function streamDownload(url, onProgress) {
  const res = await fetch(url);
  const total = +res.headers.get('content-length');
  let received = 0;
  const sink = new WritableStream({
    write(chunk) {
      received += chunk.byteLength;
      onProgress(received / total);           // 进度
      return appendToStorage(chunk);           // 逐块落盘, 不整驻内存
    },
  });
  await res.body.pipeTo(sink);                // 管道: 背压自动传导
}
```

**追问**：

1. 已经 `getReader()` 拿到 reader，还能对同一个 body 调 `pipeTo` 吗？ → 流被 getReader() 锁住（locked）时直接 pipeTo 会抛 TypeError，必须先 releaseLock() 解锁；但两种消费方式本身互斥——选了 reader 手动读就不该再 pipeTo，示例里不需要 reader，直接 pipeTo 即可。
2. 消费慢产生的背压，真能一路传到服务端吗？ → 原理上可以，但要等 TCP 窗口和各级缓冲区填满才生效；中间有 CDN/代理缓冲时传导会失效，所以进度必须按已读字节算，别假设服务端会限速。
3. 下载中断后做断点续传，需要持久化哪些信息？ → 已落盘字节数加上 ETag/Last-Modified；续传发 `Range: bytes=N-`，校验返回 206 与 Content-Range，资源变了就作废重下。
