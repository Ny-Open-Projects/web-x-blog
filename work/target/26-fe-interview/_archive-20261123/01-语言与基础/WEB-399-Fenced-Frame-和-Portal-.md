---
title: [WEB-399] Fenced Frame 和 Portal 是什么？和普通 iframe 有什么区别？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 浏览器]
type: 面试题
---

## WEB-399：Fenced Frame 和 Portal 是什么？和普通 iframe 有什么区别？
**答**：
- Fenced Frame（隐私沙盒）：广告等嵌入内容与外站完全隔离，内嵌页读不到自己的 URL/外站数据，用于替代第三方 Cookie 的广告场景，通信走受限信道。
- Portal（实验中）：像"预渲染的 iframe"可无缝过渡成顶级页面，解决 iframe 不能变成主页面的问题。
- 前端意义：了解即可，广告/内容联盟场景会逐步遇到；常规业务仍用 iframe + postMessage。

```javascript
// <fencedframe src="ads.example.com"> 内部无法读 location/外站数据
// <portal src="next.com" onactivate=transition> 可无缝转正
console.log('Fenced Frame=广告隔离；Portal=可转正的 iframe');
```
