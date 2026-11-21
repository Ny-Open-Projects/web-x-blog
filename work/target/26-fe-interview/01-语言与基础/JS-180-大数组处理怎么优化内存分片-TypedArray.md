---
title: [JS-180] 大数组处理怎么优化内存？分片、TypedArray、流式各适合什么场景？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-180：大数组处理怎么优化内存？分片、TypedArray、流式各适合什么场景？

**答**：
- 10 万+ 数据三个不要：不要一次性 JSON.parse 巨大字符串（峰值翻倍）、不要链式 map/filter 生成多份中间数组、不要同步全量渲染 DOM。
- 分片处理：把大数组切块、块间让出主线程，避免长任务阻塞渲染；内存峰值不降，适合"必须全量算且要求不卡 UI"。
- TypedArray：数值场景用 Float32Array/Int32Array，连续内存无装箱，比普通数组省一半以上内存且更快；配合 ArrayBuffer transfer 可零拷贝传给 Worker。
- 流式处理：Web Streams 或逐行解析，边读边算边丢，内存 O(1)，适合超大文件与日志分析。
- 原地算法与惰性求值：能用 for 原地写回就不用 map 新建数组；中间变换用生成器，消费时才计算。

```javascript
// 1. 分片处理：每 2000 条一块，块间让出事件循环
async function processInChunks(arr, fn, size = 2000) {
  for (let i = 0; i < arr.length; i += size) {
    const end = Math.min(i + size, arr.length);
    for (let j = i; j < end; j++) fn(arr[j], j);
    await new Promise((r) => setTimeout(r, 0)); // 让出主线程，页面不卡死
  }
}

// 2. TypedArray：数值密集场景，内存与速度双赢
const n = 100000;
const floats = new Float32Array(n);            // 4 字节/元素约 0.4MB
for (let i = 0; i < n; i++) floats[i] = Math.random();
// 对比 new Array(n).fill(0).map(...)：普通数组元素是装箱对象，峰值可达数倍

// 3. 生成器惰性变换：全程只有一份源数组
function* mapLazy(arr, fn) { for (let i = 0; i < arr.length; i++) yield fn(arr[i]); }
function sumOf(it) { let s = 0; for (const v of it) s += v; return s; }
// sumOf(mapLazy(bigArr, (x) => x * 2)) 不产生中间数组

// 4. 流式读取大文件：内存 O(1)
async function countLines(fileUrl) {
  const resp = await fetch(fileUrl);           // 本地 File 用 file.stream() 同理
  const reader = resp.body.getReader();
  const decoder = new TextDecoder();
  let buf = '', lines = 0;
  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    buf += decoder.decode(value, { stream: true });
    const parts = buf.split('\n');
    lines += parts.length - 1;
    buf = parts.pop();                         // 半行留给下一块继续拼
  }
  return lines + (buf ? 1 : 0);
}

// 5. 原地写回代替 map：省一整份新数组
for (let i = 0; i < arr.length; i++) arr[i] = arr[i].trim();
```
