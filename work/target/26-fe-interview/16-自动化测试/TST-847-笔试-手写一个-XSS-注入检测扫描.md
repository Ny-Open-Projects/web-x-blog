---
title: [TST-847] 笔试：手写一个「XSS 注入检测扫描器」（DOM sink 检测 + payload 注入）
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-847：笔试：手写一个「XSS 注入检测扫描器」（DOM sink 检测 + payload 注入）
**答**：
- 需求：实现 scanXSS(html, payloads) —— 对每个 payload 注入到模拟 DOM sink（innerHTML/eval 等），检测是否被执行。
- 规则：用受控的「执行标记」判断（如 payload 设置 window.__xss=true）；命中任一 payload 即报告漏洞点。
- 边界：sink 列表可配置；检测在隔离环境进行，不执行真实网络请求；无 sink 返回安全。

```javascript
function scanXSS(sinks, payloads = [
  '<img src=x onerror="window.__xss=true">',
  '<svg onload="window.__xss=true">',
]) {
  const found = [];
  for (const sink of sinks) { // sink: { name, run(v) }
    for (const payload of payloads) {
      globalThis.__xss = false;
      try { sink.run(payload); } catch { /* 解析失败视为未执行 */ }
      if (globalThis.__xss) {
        found.push({ sink: sink.name, payload });
        break; // 该 sink 已确认漏洞
      }
    }
  }
  return { vulnerable: found.length > 0, found };
}
// 模拟 sink：用正则提取 onerror/onload 内容并 eval（仅演示，真实用沙箱）
const domSink = { name: 'innerHTML', run: v => {
  const m = v.match(/on(error|load)="([^"]+)"/); if (m) eval(m[2]);
} };
console.log(scanXSS([domSink])); // vulnerable:true
```
**评分点**：
- 对每个 sink × payload 注入并用执行标记判定，逻辑正确。
- 命中即报告漏洞点，支持 sink 可配置。
- 强调隔离沙箱执行、不发真实请求——安全意识是核心加分项。
- 命中后 break 避免重复报告，体现工程细节。
