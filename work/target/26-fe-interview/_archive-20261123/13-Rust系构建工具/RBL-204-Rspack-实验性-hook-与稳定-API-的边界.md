---
title: [RBL-204] Rspack 实验 API 与稳定 API 的边界怎么判断
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-204：Rspack 实验 API 与稳定 API 的边界怎么判断

**答**:
- 判定依据：webpack 兼容面内的 API（compiler/compilation 主流钩子、配置项）稳定；`experiments.*`、新内置能力（如 lazyCompilation 细节、Rspack 特有 stats 字段）属实验面，minor 版本可能变更
- 工程策略：实验 API 集中封装一层适配（如 `rspackApi.ts`），升级时只改适配层；CI 锁定版本 + 升级跑全量构建快照对比
- 版本升级节奏：跟随 minor 升级收益大（性能改进频繁），但每次升级必须跑「产物一致性 diff」守门
- 文档习惯：团队插件统一标注使用的 API 层级（stable/experimental），升级影响面评估有据可查

```javascript
// experiments 适配层
export function getExperiments(config) {
  const e = config.experiments ?? {}
  return {
    lazyCompilation: e.lazyCompilation ?? false,       // 实验面：集中收口
    asyncWebAssembly: e.asyncWebAssembly ?? false,
  }
}
// 升级流程：bump → build snapshot diff → 适配层修改 → 全量回归
```
