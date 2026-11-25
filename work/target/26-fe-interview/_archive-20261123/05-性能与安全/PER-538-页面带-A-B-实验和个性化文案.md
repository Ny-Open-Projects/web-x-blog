---
title: [PER-538] 页面带 A/B 实验和个性化文案时，性能测试怎么保证可比性？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-538：页面带 A/B 实验和个性化文案时，性能测试怎么保证可比性？

**答**：
- 可比性三原则：**锁实验**（测试环境固定实验命中分支，关掉随机分流）、**锁内容**（个性化文案/推荐位用固定快照数据替换）、**锁时段**（新旧版本交叉采样抵消时段效应）。
- 具体手段：给测试入口加固定 query（如 `?ab=control&persona=snapshot`），前端把实验 SDK 切到确定性模式；CDN 与接口层 mock 推荐数据。
- 隐藏的坑：实验组本身性能就不同（实验新代码更慢），这时"线上慢"是实验效应不是回归，要把实验维度纳入 RUM 下钻，性能平台与实验平台打通分流标签。
- 报告口径：性能对比只在"同实验分支同内容快照"之间做，跨分支只看趋势不判回归。

```javascript

// 确定性测试入口：锁实验 + 锁内容快照
function initPerfTestMode(url) {
  const q = new URLSearchParams(url.search);
  if (!q.has('__perflock')) return null;
  return {
    abBranch: q.get('__perflock') === '1' ? 'control' : 'treatment', // 锁定分支
    contentSnapshot: 'snapshot-2026Q4',                              // 推荐/文案固定
    apply: (abSdk, recoSdk) => {
      abSdk.force('control');            // 实验确定性命中，禁止随机分流
      recoSdk.useSnapshot('snapshot-2026Q4'); // 个性化内容替换为固定快照
    },
  };
}
// 否则两次跑分的差异可能只是"推荐算法换了货"，与代码质量无关
```
