---
title: [OPT-043] 如何做弱网模拟？Chrome throttling 的参数应该怎么设？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-043：如何做弱网模拟？Chrome throttling 的参数应该怎么设？

**答**：
- DevTools 内置档位：Slow 3G（400kbps 下行/400ms RTT）、Fast 3G（1.6Mbps/150ms RTT），但内置值偏"实验室友好"，真实弱网更差（印度/P75 约 300kbps、RTT 500ms+）。
- 自定义档位建议贴近 **RUM 里真实用户的 P75**，而不是照抄内置值；同时开 CPU 4x，弱网用户往往也是低端机。
- HTTP/1.1 与 HTTP/2 在限速下表现差异大，模拟时确认协议与线上一致。
- WPA 层还要模拟丢包（netem/Clumsy），纯带宽限速测不出队头阻塞与重传影响。

```javascript
// 一一对应：CDP 精确设置弱网参数（等价 DevTools Network conditions 自定义档位）
import puppeteer from 'puppeteer';

const browser = await puppeteer.launch({
  args: ['--cpu-throttling-rate=4'], // 低端机 CPU 降速，与弱网同时开
});
const page = await browser.newPage();
const client = await page.createCDPSession();
await client.send('Network.enable');
// 自定义"真实弱网"档位：下行 400kbps 上行 300kbps RTT 500ms
// 注意单位是字节/秒：400kbps = 50_000 B/s
await client.send('Network.emulateNetworkConditions', {
  offline: false,
  latency: 500,            // RTT 一半，每次请求额外延迟 ms
  downloadThroughput: 50_000, // 下行 400kbps
  uploadThroughput: 37_500,   // 上行 300kbps
});
const t0 = Date.now();
await page.goto('https://example.com', { waitUntil: 'load' });
console.log('弱网下 load 耗时:', Date.now() - t0, 'ms');
await browser.close();
```
