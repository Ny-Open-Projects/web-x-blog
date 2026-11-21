---
title: [H5-085] Blob、File、ArrayBuffer 之间的转化链完整梳理。
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-085：Blob、File、ArrayBuffer 之间的转化链完整梳理。
**答**：
- `File` 继承自 `Blob`（多了 name/lastModified），一切 Blob 能力 File 都有；`input.files[0]`、`DataTransferItem.getAsFile()` 产出 File。
- 方向：`Blob.arrayBuffer()` / `file.arrayBuffer()` 得 ArrayBuffer；`blob.stream()` 得 ReadableStream；`blob.text()` 得字符串。
- 反向：`new Blob([arrayBuffer], { type })`；`new File([blob], name, { type })` 可把 Blob 升级为 File（FormData、input 传输需要）。
- `URL.createObjectURL(blob)` 产出 `blob:` URL 供 `img/video/a` 使用，是"二进制到展示"的桥。
- 同步例外：`FileReader.readAsXxx` 是老 API，异步回调风格；新代码优先用 Promise 风格的 Blob 方法。

```javascript
// 1) input 得到 File（是 Blob 的子类）
const file = document.querySelector('input[type=file]').files[0];
console.log(file instanceof Blob);      // true
console.log(file.name, file.lastModified);

// 2) Blob -> 各种形态（全部 Promise 风格）
const buf = await file.arrayBuffer();   // -> ArrayBuffer：按字节处理
const text = await file.text();         // -> 文本：小文件直读
const stream = file.stream();           // -> ReadableStream：流式消费

// 3) ArrayBuffer -> Blob -> File（例：处理完再打包）
const processed = new Uint8Array(buf);  // 假设做了字节级修改
const blob = new Blob([processed], { type: file.type });
const newFile = new File([blob], `edited-${file.name}`, { type: file.type });

// 4) 进 FormData 上传：File/Blob 都可以，第三参可自定义文件名
const fd = new FormData();
fd.append('file', newFile);

// 5) Blob -> 展示：objectURL 桥接 img/video/a
const url = URL.createObjectURL(blob);
document.querySelector('img').src = url;
// 用完释放，防内存泄漏
setTimeout(() => URL.revokeObjectURL(url), 60_000);

// 6) 互转速查：Blob.slice 零拷贝分片（H5-031 的延伸）
const head = await blob.slice(0, 16).arrayBuffer();  // 读文件头 magic number
console.log(new Uint8Array(head));
```
