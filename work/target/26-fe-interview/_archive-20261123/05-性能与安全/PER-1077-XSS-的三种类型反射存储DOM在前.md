---
title: [PER-1077] XSS 的三种类型（反射/存储/DOM）在前端的各自成因与检测点
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1077：XSS 的三种类型（反射/存储/DOM）在前端的各自成因与检测点

**答**：
- 反射型：URL 参数直接进 DOM 或被后端回显；检测点：所有 location/searchParams 消费点。
- 存储型：评论/昵称等入库后所有访问者中招；检测点：UGC 渲染出口、富文本编辑器。
- DOM 型：纯前端拼接（innerHTML/href/style/eval），不经过后端；检测点：sink 扫描 + Trusted Types。
- 检测工具：CodeQL/自研 AST 扫描 source→sink 数据流；线上用 CSP report 探针捕获真实尝试。

```javascript
// sink 扫描清单（AST 规则示例）
const SINKS = ['innerHTML', 'outerHTML', 'document.write', 'eval',
  'insertAdjacentHTML', 'srcdoc'];
const SOURCES = ['location.search', 'location.hash', 'document.referrer',
  'postMessage.data', 'URLSearchParams'];
// 规则：SOURCES 流入 SINKS 且未经 sanitize -> 报警
function isTaintedPath(node) {   // 伪代码：数据流分析
  return SOURCES.some(s => node.deps.includes(s)) &&
         SINKS.some(k => node.calls.includes(k));
}
// 线上探针：CSP report-uri 的 script-src 违规聚合，
// 高频域名为攻击源，进应急流程
```
