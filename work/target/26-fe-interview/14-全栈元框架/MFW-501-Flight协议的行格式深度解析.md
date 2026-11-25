---
title: [MFW-501] Flight 协议的行格式深度解析：ID、类型标记与引用语法
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-501：Flight 协议的行格式深度解析：ID、类型标记与引用语法

**答**:
- Flight payload 是行式文本协议：每行 `ID:TYPE标记+值`——1) `I["dca66"]`（module 引用：客户端组件的模块 id+导出名）、`H["<div>..."]`（HTML 片段）、`S["fname","ref"]`（流式：Suspense 边界的完成标记）、`0:["$L1"]`（chunk 引用）、`J0:["children","$L2"]`（对象字段——数字引用其他行）；2) **引用语法**：`$L2`（lazy chunk 引用）、`$@1`（已解析 Promise）、`$K1`（流式 FormData/blob）、`$Q1`（Map）、`$W1`（Set）、`$D`（Date）；3) 行 ID 的意义：服务端流式输出时 ID 顺序 = 完成顺序（不等于树顺序——Suspense 使乱序合法）。
- 协议的设计动机：文本流式（可 HTTP 分块传输）、可增量解析（每行独立）、引用解耦树结构（渲染完成顺序与组件树顺序解耦——这是 Suspense 流式的协议基础）。
- 与 SSR HTML 的双轨：Flight 同时输出「HTML 壳」（首屏直接可见）+「RSC payload」（客户端水合用的虚拟树）——两份数据共享 ID 空间（`<!--$?-->` 模板标记与 payload chunk 对应）。
- 追问钩子：为什么 Flight 选「行式文本」而不是二进制/JSON？——JSON 无法表达「引用 + 循环 + 流式」三件事（循环引用 JSON 直接死）；行式协议让解析器可以逐行处理（收到即 resolve 引用），且 HTML 与 payload 可共享流——序列化协议的选型由「流式 + 循环结构 + 渐进解析」三需求共同决定。

```javascript
// Flight payload 样例与解析
const payload = [
  'I["dca66",{"name":"Button","chunks":[]}]',          // 客户端组件模块引用
  'H0',                                                 // 开始 HTML 流
  '0:["$","div",null,{"className":"wrap","children":["$L1"]}]',  // 元素树，children 引用 chunk 1
  'S1:["react.suspense","$L2"]',                        // Suspense 完成标记
  '1:["$","p",null,{"children":"异步内容"}]',            // chunk 1 的内容
  '2:I[1234,[],""]',
];
function parseFlight(line) {
  const m = /^(\d+):(.+)$/.exec(line);
  if (!m) return null;
  const [id, body] = [m[1], m[2]];
  const type = body[0];                                 // I/H/S/0-9/J
  return { id, type, body: body.slice(type.match(/[\dA-Z]/) ? 1 : 0) };
}
// 客户端解析器：收到行 -> 按类型 resolve（$L 引用延迟绑定）
```
