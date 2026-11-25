---
title: [RBL-832] 场景题：Monorepo 依赖提升的边界案例——幽灵依赖与双版本共存的构建裁决
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-832：场景题：Monorepo 依赖提升的边界案例——幽灵依赖与双版本共存

**答**:
- 依赖提升（hoisting）的边界案例：1) **幽灵依赖**（代码 import 未声明的包——npm 提升让它碰巧可用，pnpm 严格模式直接报错）；2) **双版本共存**（A 依赖 lodash@3、B 依赖 lodash@4——pnpm 隔离使 A/B 各拿各的；npm 提升则一个赢另一个拿错版本）；3) **peer 依赖冲突**（peer 声明与实际提升版本不符）。构建器的裁决：解析结果要显式暴露版本冲突（同包多版本进产物 = 体积与行为风险），诊断而非静默。
- 幽灵依赖的治理：构建器比对「import 的包 ⊆ package.json 声明」——未声明的导入诊断（depcheck 类能力内建）；理由是发布后（registry 安装）幽灵依赖不存在，dev 可用发布必挂。
- 双版本的处置策略：标记 + 决策（接受体积成本/统一版本/alias 合并）；「同一个包的两个版本都被打进同一 entry」是明确的坏味道（运行时双实例），构建器门禁阻断；「分属不同 chunk 的双版本」可接受（隔离语义）但要报告。
- peer 冲突：peer 声明（"react": "^18"）与提升的 19 不匹配 → 构建器 warn（运行时可能行为漂移）；「peer 兜底」的安装逻辑由包管理器负责，构建器负责校验一致性。
- 追问钩子：为什么「npm 可用、pnpm 报错」的迁移是幽灵依赖暴露器？——pnpm 的隔离 node_modules（每包只看见声明的依赖）是「发布态的忠实模拟」；npm 的提升目录是「开发态的宽容」——幽灵依赖本质是「开发态与发布态的解析差异」，pnpm 把差异前置成错误，构建器的声明完整性检查是同一目标（前置暴露）。

```javascript
// 幽灵依赖与双版本审计
function auditDeps(graph, declarations) {
  const problems = [];
  // 1) 幽灵依赖
  for (const mod of graph.modules())
    if (mod.inNodeModules)
      for (const pkg of topPkgs(mod.id)) {
        const declared = declarations[mod.owner]?.has(pkg);
        if (!declared)
          problems.push({ type: 'phantom', pkg, owner: mod.owner,
            detail: `${mod.owner} 使用未声明依赖 ${pkg}——发布后解析失败` });
      }
  // 2) 双版本共存
  const versions = new Map();                            // pkg -> Set(version)
  for (const mod of graph.modules())
    if (mod.inNodeModules)
      versions.get(pkgOf(mod.id)) || versions.set(pkgOf(mod.id), new Set()).get(pkgOf(mod.id)).add(versionOf(mod.id));
  for (const [pkg, vs] of versions)
    if (vs.size > 1)
      problems.push({ type: 'multi-version', pkg, versions: [...vs],
        detail: '同包多版本——检查是否进同一 entry（双实例）' });
  return problems;
}
```
