---
title: [AIC-055] 用 AI 辅助依赖升级（如 React 18→19）能做什么？哪些升级 AI 帮不上忙？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-055：用 AI 辅助依赖升级（如 React 18→19）能做什么？哪些升级 AI 帮不上忙？
**答**：
- AI 能做的：读官方 changelog 生成「本项目影响清单」（扫出用到了被废弃 API 的文件）、机械改写 codemod 覆盖不到的模式、批量修 TS 类型报错、为新 API 写适配层。
- 关键输入：官方升级指南 + codemod 结果 + 报错日志；让 AI 先输出「迁移计划（分几批、每批风险）」再动手。
- AI 帮不上忙的：运行时行为的隐性变化（并发渲染下副作用时序）、三方依赖尚未适配导致的死锁选择、性能回归的测量与取舍——这些需要真实环境验证和人的决策。
- 安全流程：小批量灰度（先工具模块再业务模块）、每批跑全量测试与关键路径冒烟、可整体回滚。
- 追问钩子：升级任务的 AI 产出评估要看「改写正确率」——抽查 20 个文件 diff，错了就说明该模型/该 prompt 还不合格。

```javascript
// 依赖升级影响面扫描（喂给 AI 之前先确定性扫描）
function scanDeprecatedApi(files, deprecatedList) {
  const hits = [];
  for (const f of files) {
    const src = read(f);
    for (const dep of deprecatedList) {
      if (new RegExp(`\\b${dep}\\b`).test(src)) {
        hits.push({ file: f, api: dep, line: src.slice(0, src.indexOf(dep)).split('\n').length });
      }
    }
  }
  return hits; // 输出清单作为 AI 迁移任务的任务队列
}
```
