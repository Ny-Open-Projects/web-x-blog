---
title: [PER-800] 手写一个小程序 setData 数据量审计器：单次调用、每帧累计与路径冗余三指标输出报告
date: 2026-11-21
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-800：手写一个小程序 setData 数据量审计器：单次调用、每帧累计与路径冗余三指标输出报告

**答**：
- 需求：包装 wx.setData，记录每次调用（页面、数据量 KB、是否路径更新、时间戳），按页面输出报告：单次最大 KB、每帧内累计 KB（同一 16ms 窗口）、路径更新占比、可合并调用次数。
- 边界：路径更新单独统计（只算增量大小）；同一帧内多次调用标记为"可合并"（建议合并为一次）；报告按累计 KB 降序输出 Top 问题页面。
- 评分点：帧窗口累计口径；可合并判定；报告可落地到页面。

```javascript
function createSetDataAuditor(report) {
  const logs = [];
  return {
    wrap(page) {
      const raw = page.setData.bind(page);
      page.setData = function (data, cb) {
        const keys = Object.keys(data);
        const isPath = keys.some(k => k.includes('.') || k.includes('['));   // 路径写法识别
        const sizeKB = JSON.stringify(data).length / 1024;
        logs.push({ page: page.route, sizeKB, isPath, t: Date.now() });
        return raw(data, cb);
      };
    },
    build() {                                   // 按 16ms 帧窗口聚合
      const byPage = new Map();
      for (const l of logs) {
        const s = byPage.get(l.page) ??= { maxKB: 0, frameKb: [], calls: 0, path: 0 };
        s.maxKB = Math.max(s.maxKB, l.sizeKB); s.calls++;
        if (l.isPath) s.path++;
        s.frameKb.push(l);
      }
      return [...byPage].map(([page, s]) => {
        s.frameKb.sort((a, b) => a.t - b.t);
        let merged = 0, frameAcc = 0, lastT = 0;
        for (const l of s.frameKb) {
          if (l.t - lastT < 16) { merged++; frameAcc += l.sizeKB; }   // 同帧可合并
          else frameAcc = l.sizeKB;
          lastT = l.t;
        }
        return { page, maxKB: +s.maxKB.toFixed(1), pathRatio: s.path / s.calls,
          mergeableCalls: merged, estFrameKB: +frameAcc.toFixed(1) };
      }).sort((a, b) => b.estFrameKB - a.estFrameKB);
    },
  };
}
```
