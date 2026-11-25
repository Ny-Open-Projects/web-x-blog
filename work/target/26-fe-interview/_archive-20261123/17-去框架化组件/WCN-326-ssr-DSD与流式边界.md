---
title: [WCN-326] 流式 SSR 中 DSD 模板跨 chunk 边界的输出问题？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-326：流式 SSR 中 DSD 模板跨 chunk 边界的输出问题？
**答**：
- 元素模板必须与元素开标签同 chunk 输出（不能壳先行模板后补——解析器语义）。
- 流式实现：元素渲染在数据就绪后一次性 flush（元素级原子输出）。
- 降级：数据慢的元素输出「壳 + 占位」，水合后填充（不用 DSD 流式补洞）。
- 验证：流式抓包断言（元素开标签到闭模板完整出现在同一 chunk）。

```javascript
// 元素级原子 flush
stream.write(await renderGoodsCard(props));   // 模板与内容同 chunk
// 慢数据：write(shellWithSkeleton) 先行，水合后填充
r
```
