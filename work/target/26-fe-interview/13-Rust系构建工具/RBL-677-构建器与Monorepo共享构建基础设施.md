---
title: [RBL-677] Monorepo 共享构建基础设施：集中配置与各仓自治的博弈
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-677：Monorepo 共享构建基础设施：集中配置与各仓自治的博弈

**答**:
- 多仓库/多包构建配置的演进路径：各自配置（碎片化、重复踩坑）→ 复制粘贴模板（腐化）→ **共享配置包**（@org/build-config，npm 依赖统一升级）→ 配置即代码服务（CLI 从注册表生成）。核心张力：集中度越高越一致但灵活性越低。
- 共享配置包的设计：分层暴露（`base` + `react-app` + `node-lib` 预设组合）、可覆盖（preset 展开后用户可 merge 覆盖——覆盖行为要显式记录在产物日志里防静默偏移）、版本化（preset 变更走 semver + 升级公告）。
- 升级协调：共享配置大版本升级（如换构建器）要提供 codemod + 迁移窗口（双轨一个 minor）；内部仓库的构建器版本看板（RBL-648）驱动升级进度追踪。
- 集中式构建服务 vs 仓库自治：极大型组织把构建变成服务（提交配置声明，CI 侧统一执行）——好处是全局优化（缓存调度/资源池）、坏处是迭代慢（服务团队成为瓶颈）；工程答案常是「默认统一 + 逃生门」（特殊仓库可申请豁免但定期复审）。
- 追问钩子：为什么共享配置包的「覆盖」必须显式记录？——覆盖即分叉，分叉即维护债；没有记录的覆盖会让「统一性」假象持续存在（大家都以为用的是统一配置），出问题时才发现各自魔改过——显式化是治理的前提。

```javascript
// 共享配置包 API
// @org/build-config
export const presets = {
  base: { output: { format: 'es' }, resolve: { extensions: ['.ts', '.tsx', '.js'] } },
  reactApp: (base) => ({
    ...base,
    plugins: [react(), tsStrip()],
    output: { ...base.output, dir: 'dist' },
  }),
  nodeLib: (base) => ({ ...base, output: { format: 'cjs', dir: 'lib' } }),
};

// 使用方
import { presets, apply } from '@org/build-config';
export default apply(presets.reactApp, {
  overrides: {                          // 覆盖必须显式声明，构建日志记录
    output: { dir: 'build' },           // 日志：[preset] 覆盖 output.dir -> build
  },
});

// 覆盖审计（构建日志 + CI 汇总）
function auditOverrides(applied, overrides) {
  for (const [path, val] of flatten(overrides))
    log(`[preset] 覆盖 ${path} -> ${JSON.stringify(val)}`);
  reportToDashboard({ repo, overrides: Object.keys(flatten(overrides)) });  // 覆盖率看板
}
```
