---
title: [PER-1156] 如何做"隐私默认值"的产品工程（Default Privacy）
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1156：如何做"隐私默认值"的产品工程（Default Privacy）

**答**：
- 清单化默认值：新用户默认关闭个性化、默认不公开资料、默认最小采集、默认不索引。
- 变更单向性：放宽隐私的变更需用户显式操作；收紧隐私可默认推进。
- 版本兼容：老用户不自动继承新放开项；每次默认值变更全量公告。
- 实现：默认值注册表 + 变更审计；设置中心展示"当前默认"与"我的选择"差异。

```javascript
// 隐私默认值注册表
const DEFAULTS = { personalization: false, publicProfile: false,
  indexing: false, analytics: false };
function mergeDefaults(userSettings, announced) {
  // 放宽项（默认 true 化）必须用户显式同意，不自动继承
  const merged = { ...DEFAULTS };
  for (const [k, v] of Object.entries(userSettings ?? {}))
    if (DEFAULTS[k] === false || v === false) merged[k] = v;   // 只继承收紧或既有选择
  report({ type: 'defaults-apply', announced, keys: Object.keys(merged) });
  return merged;
}
```
