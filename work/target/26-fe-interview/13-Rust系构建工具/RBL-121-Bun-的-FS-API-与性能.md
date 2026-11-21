---
title: [RBL-121] Bun 的文件 API（Bun.file / Bun.write）有什么设计亮点？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-121：Bun 的文件 API（Bun.file / Bun.write）有什么设计亮点？
**答**：
- Bun.file(path)：返回 Blob 形状的对象，支持 .text()/.json()/.arrayBuffer()，惰性读取；路径即读，API 面（Web 标准 Blob）。
- Bun.write(dest, data)：写文件一步到位，支持从 URL/Response 直接写入（内置下载）、零拷贝 fast path（sendfile 系统调用级）。
- 亮点：IO 快路径——写网络响应到文件走系统级零拷贝，比 Node 的 pipe 链更快；读大文件返回 Blob 惰性句柄不立即载入内存。
- 与 Node fs 对比：Node 的 fs promises API 功能全但组合繁琐；Bun API 面向"常见操作最短路径"，fs 兼容 API 仍然可用。
- 适合脚本与工具：构建脚本、日志处理、缓存读写这类 IO 密集小工具收益明显。
- 追问钩子：API 设计趋势是 Web 标准（Blob/Response）统一 Node/Deno/Bun 三端代码。

```typescript
// 下载并写文件：一步零拷贝
await Bun.write('./logo.png', await fetch('https://example.com/logo.png'));

// 读 JSON
const pkg = await Bun.file('./package.json').json();

// 大文件流式处理
const blob = Bun.file('./huge.log');
for await (const line of blob.stream()) { /* 处理 */ }
```
