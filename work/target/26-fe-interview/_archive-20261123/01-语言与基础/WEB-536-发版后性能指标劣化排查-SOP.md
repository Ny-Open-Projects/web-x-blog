---
title: [WEB-536] 发版后性能指标劣化的排查 SOP
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 排查SOP]
type: 面试题
---

## WEB-536：发版后性能指标劣化的排查 SOP

**答**：
- 先对齐时间轴：RUM 指标劣化起点是否与某次发布/配置变更/CDN 操作重合——对不齐就可能是外因（第三方脚本、流量结构变化）
- 拆指标归因：LCP 劣化看是哪张资源（Element 定位）→ 是慢在下载（体积/CDN）还是发现晚（preload 缺失）；CLS 劣化看新增的动态插入元素
- 常见劣化源：新版引入大依赖（bundle 分析）、字体策略从 swap 改 block、新增同步阻塞脚本、图片从固定尺寸改为自适应导致布局偏移
- 对比验证：新旧版本在同一流量池下对比（灰度看板），排除「流量构成变了」的假劣化
- 修复优先级：影响核心转化路径的先修，能用回滚止血的先回滚

```javascript
// RUM 关键指标的元素级归因
new PerformanceObserver(list => {
  const lcp = list.getEntries().at(-1);
  report({ el: lcp.element?.tagName, size: lcp.size, url: lcp.url, t: lcp.renderTime || lcp.startTime });
}).observe({ type: 'largest-contentful-paint', buffered: true });
```
