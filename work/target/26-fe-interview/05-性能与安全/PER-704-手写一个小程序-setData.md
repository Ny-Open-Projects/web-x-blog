---
title: [PER-704] 手写一个小程序 setData 审计器：自动统计调用频次/单次大小/路径化比例，输出优化清单
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-704：手写一个小程序 setData 审计器：自动统计调用频次/单次大小/路径化比例，输出优化清单

**答**：
- 实现：包装 Page 的 setData（重写 Page 构造或用 Behavior 注入），每次调用记录：数据大小（JSON 长度）、字段数、是否路径写法（key 含 `[` 或 `.`）、调用间隔；页面 onUnload 时聚合输出该页审计报告。
- 要点：大对象阈值分级（>100KB 高危、>30KB 中）；频次统计（每秒 > 5 次为高频）；路径化比例（< 50% 说明大量全量更新）；输出按可优化收益排序（大小×频次）。
- 边界：审计包装自身开销要小（JSON.stringify 大对象会卡，抽样序列化）；开发/预发开启，生产关闭。
- 评分点：路径化比例统计与抽样序列化。

```javascript

function installSetDataAudit({ sampleRate = 1 } = {}) {
  const origPage = Page;
  Page = function (config) {
    const origSetData = config.setData;
    const log = [];
    config.setData = function (data, callback) {
      const keys = Object.keys(data);
      const pathLike = keys.filter(k => /\[|\./.test(k)).length;
      const entry = { keys: keys.length, pathLike,
        big: keys.some(k => typeof data[k] === 'object' && data[k] !== null), ts: Date.now() };
      // 抽样序列化控制开销
      if (Math.random() < sampleRate * 0.2)
        entry.size = JSON.stringify(data).length;
      log.push(entry);
      return origSetData.call(this, data, callback);
    };
    const origUnload = config.onUnload;
    config.onUnload = function (...args) {
      const total = log.length, big = log.filter(e => e.size > 100 * 1024).length;
      const pathRatio = total ? log.reduce((s, e) => s + (e.pathLike / e.keys || 0), 0) / total : 1;
      if (total > 50 || big > 0 || pathRatio < 0.5)
        console.warn('[setData-audit]', route(), { total, big,
          pathRatio: +(pathRatio * 100).toFixed(0) + '%',
          advice: pathRatio < 0.5 ? '大量全量更新，改路径写法' : big > 0 ? '存在超 100KB 大对象' : '调用过频' });
      return origUnload?.apply(this, args);
    };
    return origPage(config);
  };
}
```
