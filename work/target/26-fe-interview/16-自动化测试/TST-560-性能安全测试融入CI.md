---
title: [TST-560] 如何把性能与安全测试融入 CI 而不拖慢交付
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-560：如何把性能与安全测试融入 CI 而不拖慢交付

**答**：
- 结论：分层触发——快速静态检查（依赖扫描/CSP/敏感数据扫描）进每次提交；耗时动态测试（性能基线/Lighthouse/渗透）进合入或夜间；结果以门禁或报告呈现。
- 做法：安全左移用 quick scan 卡提交、深度扫描定时跑；性能测试用缓存与基线对比减少误报；所有结果汇总到同一报告，避免多套系统割裂。
- 追问钩子：深度安全扫描太慢卡发布怎么办？——异步化：提交只跑快检，深度扫描在预发环境定时执行并异步通知，发布门禁只看「是否已完成深度扫描且无高危」而非同步等待。

```javascript
// CI 分层：按触发时机选择检查集
const CI_CHECKS = {
  commit: ['lint', 'type', 'unit', 'dep-quick-scan', 'secret-scan'],
  merge:  ['contract', 'component', 'csp-check', 'lighthouse'],
  nightly:['perf-baseline', 'full-sca', 'dast', 'a11y-full'],
};
function checksFor(trigger) { return CI_CHECKS[trigger] || []; }
console.log(checksFor('commit')); // 快速反馈集
console.log(checksFor('nightly')); // 慢速深度检查集
// 汇总一次提交需要跑的全部检查（去重后按阶段顺序）
const allChecks = ['commit', 'merge'].flatMap(checksFor);
console.log([...new Set(allChecks)]);
```
