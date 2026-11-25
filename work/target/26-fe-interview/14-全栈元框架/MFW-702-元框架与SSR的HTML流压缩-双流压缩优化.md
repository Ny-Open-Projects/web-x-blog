---
title: [MFW-702] SSR 双流压缩优化
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-702：SSR 双流压缩

**答**:
- HTML 流 + Flight 流的压缩：1) **同源压缩**（HTML 与 Flight 流在同一响应（Flight 附加在 HTML 后）——压缩流 = 压缩整个响应（br 压缩 HTML+Flight 联合——共享字典（HTML 的重复结构（`<!--$-->` 标记/类名）被字典压缩）；2) **分块压缩**（流式压缩的 chunk 边界（br 的 chunk 边界影响压缩效率——大 chunk 压缩率更高但延迟更高——压缩窗口权衡）；3) Flight 流的压缩率（文本协议 RBL-501 的重复模式（行格式重复）——br 的压缩效果显著（payload 60% 压缩）。
- 压缩的时序约束：流式响应的压缩 = 每块压缩后立即发送（不等全量——流式压缩的 chunk 大小权衡：小 chunk = 低延迟但低压缩率；大 chunk = 高压缩率但延迟）；「压缩延迟 vs 传输量」的权衡：LLM token 流（小 chunk 低延迟优先）vs SSR HTML（大 chunk 压缩率优先）。
- Next 的默认压缩：Next 内置压缩（br/gzip 自动协商）——standalone 模式的压缩配置（压缩级别——默认 4/6/9 的权衡）。
- 追问钩子：为什么「Flight payload 的 br 压缩率」比 JSON API 更高？——Flight 的重复模式：行格式重复（`0:["$","div"...` 的结构重复）、HTML 转义重复（`<!--$-->` × N）、组件引用重复——br 的滑动窗口捕捉重复模式（文本协议的压缩友好性 RBL-501 设计动机的压缩维度）；JSON API 的字段名不可预测（重复率低于 Flight 的结构化重复）——Flight 的「结构化重复」是压缩友好性内建于协议设计（行式 + 类型标记的重复模式）。

```javascript
// Next standalone 的压缩配置
// next.config
module.exports = {
  compress: true,                                        // 内置压缩（默认 br > gzip）
  // compressible: ['text/html', 'text/x-component'],    // Flight 的 content-type
};
// 压缩级别权衡
const COMPRESSION_LEVELS = {
  fast: { level: 4, chunkKB: 4, latency: 'low', ratio: 'medium' },
  balanced: { level: 6, chunkKB: 16, latency: 'medium', ratio: 'good' },
  max: { level: 9, chunkKB: 64, latency: 'high', ratio: 'best' },
};
// LLM token 流：小 chunk 低延迟
// SSE/Action 流：小 chunk（每 token 即发——压缩窗口小但延迟优先）
// SSR HTML：大 chunk（压缩率优先——shell 首包可达 60% 压缩）
// 双流的压缩效果（RBL-560 体积优化的传输层）
// Flight payload raw: 60KB → br compressed: 18KB（70% 压缩率）
// HTML shell raw: 40KB → br compressed: 10KB（75% 压缩率——HTML 结构重复多）
```
