---
title: [AIC-357] AI 重构时改了对外兼容行为（如函数开始抛异常而以前返回 null），如何防？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-357：AI 重构时改了对外兼容行为（如函数开始抛异常而以前返回 null），如何防？
**答**：
- 兼容契约显式化：公共 API 的行为契约（错误处理方式/返回值范围）写进 JSDoc 或契约文件，rules 要求 AI 遵守。
- 行为快照测试：公共 API 全量「行为快照」（输入→输出/异常）作为特征测试，重构前锁定。
- 评审重点位：AI 评审把「异常行为变更」列为高危检查项（try/catch 范围变化、新增 throw）。
- 兼容层模式：大重构要求保留旧入口（deprecated 包装），给调用方迁移期。

```javascript
// 行为快照：锁定公共 API 契约
it('parseInput 契约：非法输入返回 null 而非抛错（对外承诺）', () => {
  expect(parseInput('bad')).toBeNull();  // 重构若改为 throw 即红
});
r
```
