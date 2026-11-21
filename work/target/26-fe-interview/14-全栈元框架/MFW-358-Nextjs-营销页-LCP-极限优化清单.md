---
title: [MFW-358→MFW-358] 营销页 LCP 极限优化清单（75→95 分实战项）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## MFW→358：营销页 LCP 清单

**答**:
- 服务端段：整页 SSG+ISR 长 TTL（营销内容变更走发布不走向请求）、TTFB 预算 ≤200ms（边缘节点+预热）、HTML 内联首屏关键 CSS（其余异步）
- 资源段：LCP 图 priority+fetchpriority=high+精确尺寸（srcset 断点=真实布局断点）+AVIF 双源；字体 subset+swap 窗口缩短；三方脚本全部延后（营销页禁同步三方——MFW-333 分级表）
- 渲染段：首屏组件树浅化（LCP 元素不在深层 Suspense 后）、Speculation Rules 预渲染下一跳（MFW-324）
- 度量闭环：RUM 按 LCP 元素类型分桶归因（img/text/background）——清单项按数据排优先级而非全做

```text
清单分账：服务端(SSG+边缘+≤200ms) / 资源(priority 图+AVIF+字体) / 渲染(浅树+预渲染)
方法：RUM 按 LCP 元素分桶 → 数据排优先级
```
