---
title: [RBL-077] 笔试：手写构建警告收敛器（去重 + 分级 + 白名单）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-077：笔试：手写构建警告收敛器（去重 + 分级 + 白名单）
**题目**：实现 WarningSink：1) 收集 { code, message, file } 警告；2) 同 code+file 去重计数；3) 白名单（如 CIRCULAR_DEPENDENCY）降级为 silent；4) 阈值规则：同 code 超过 N 条升级为 error；5) flush 输出按 code 分组汇总，返回是否有 error。

```javascript
class WarningSink {
  constructor({ ignore = [], thresholds = {} } = {}) {
    this.map = new Map();       // key: code|file -> { count, sample }
    this.ignore = new Set(ignore);
    this.thresholds = thresholds; // code -> max
    this.errors = [];
  }
  add(warn) {
    if (this.ignore.has(warn.code)) return this;         // 白名单静默
    const key = `${warn.code}|${warn.file || ''}`;
    const item = this.map.get(key) || { count: 0, sample: warn };
    item.count++;
    this.map.set(key, item);
    return this;
  }
  flush() {
    // 聚合 per-code 总量并应用阈值
    const byCode = new Map();
    for (const [key, item] of this.map) {
      const code = key.split('|')[0];
      const agg = byCode.get(code) || { total: 0, files: [] };
      agg.total += item.count;
      if (item.file) agg.files.push(item.file);
      byCode.set(code, agg);
    }
    for (const [code, agg] of byCode) {
      const max = this.thresholds[code];
      if (max !== undefined && agg.total > max) {
        this.errors.push(`${code} 超阈值: ${agg.total} > ${max}`);
      }
      console.log(`[warn] ${code} x${agg.total} (${agg.files.length} files)`);
    }
    return { hasError: this.errors.length > 0, errors: this.errors };
  }
}
module.exports = { WarningSink };

// 用法
// const sink = new WarningSink({ ignore: ['CIRCULAR_DEPENDENCY'],
//   thresholds: { UNUSED_EXPORT: 50 } });
// sink.add({ code: 'UNUSED_EXPORT', file: 'a.ts' }).flush();
```
**评分点**：
- code+file 组合去重并计数（信息不丢失）。
- 白名单静默（构建噪音治理）。
- 阈值升级 error（CI 门禁思想）。
- flush 按 code 聚合输出（可读性）。
- hasError 返回值供 CI 判定退出码。
