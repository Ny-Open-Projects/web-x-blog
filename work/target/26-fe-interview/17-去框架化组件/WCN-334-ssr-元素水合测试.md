---
title: [WCN-334] 元素水合一致性测试的设计（双端快照 diff）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-334：元素水合一致性测试的设计（双端快照 diff）？
**答**：
- 同 props 双端渲染：SSR renderDSD 输出解析后的 shadow 内容 vs 客户端渲染 shadow 内容。
- 语义 diff：忽略动态属性白名单（随机 id），比较结构/文本/关键属性。
- 场景覆盖：空数据/长文本/错误态/RTL——状态矩阵双端 diff。
- CI：水合 diff 非空即 fail（防止渲染函数分叉）。

```javascript
const ssrDom = parseShadow(renderDSD(props));
const csrDom = clientRenderShadow(props);
expect(semanticDiff(ssrDom, csrDom)).toEqual([]);   // 语义一致
r
```
