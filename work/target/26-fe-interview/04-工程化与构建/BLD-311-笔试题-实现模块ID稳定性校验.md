---
title: [BLD-311] 笔试题——实现模块 ID 稳定性校验？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## BLD-311：手写模块 ID 校验

**需求与边界**：
- 需求：校验模块 ID 的确定性（SCN-BLD-219 长缓存根基）——① 同源码两次构建 ID 一致（构建间确定性）；② 新增模块不改变既有模块 ID（插入不平移——deterministic 检测）；③ ID 算法检查（自增 vs 路径 hash——配置审计）。
- 边界：① 双次构建在干净环境（排除文件系统顺序干扰）；② 平移检测方法（新增模块前后 ID 映射对比——移位幅度统计）；③ 修复建议（moduleIds: deterministic）。

**答**：
```javascript
async function moduleIdStability(bundler, project) {
  // 1. 同源码双构建一致性
  const a = await bundler.build(project);
  const b = await bundler.build(project);
  const deterministicBetween = shallowEqual(a.moduleIds, b.moduleIds);
  // 2. 插入不平移
  const withNew = await bundler.build(insertModule(project));
  const shifts = Object.entries(a.moduleIds)           // 旧模块 ID 是否被挤动
    .filter(([file, id]) => withNew.moduleIds[file] !== id);
  const algorithm = detectIdAlgorithm(a.moduleIds);    // 自增（连续数字）vs hash
  return {
    deterministicBetween, insertShiftCount: shifts.length,
    algorithm,
    verdict: deterministicBetween && shifts.length === 0 ? 'STABLE' : 'UNSTABLE',
    impact: shifts.length && `长缓存杀手：${shifts.length} 个模块 ID 平移 → 引用它们的 chunk 全部 hash 变化`,
    fix: algorithm === 'incremental' ? 'moduleIds: "deterministic"（路径 hash——SCN-BLD-219）' : null,
  };
}
```

**评分点**:
- 双检测（构建间一致 + 插入不平移）。
- 平移检测方法（新旧 ID 映射对比 + 移位统计）。
- ID 算法审计（自增 vs hash——配置级根因）。
- 影响量化（平移数 → chunk 失效数——长缓存杀手的说服力）。

## 变体与延伸（补充）

**变体与延伸**：

1. 为什么标识哈希 ID 比自增 ID 稳定？ → ID 由模块相对路径（+ loader 请求串）算出，增删模块不会引起其余模块 ID 位移，内容改动也不改 ID，长缓存才保得住；注意它**不是内容 hash**——真按内容寻址，改一个字符 ID 就变，引用它的 chunk 全失效，反而毁掉长缓存。
2. `deterministic` 与 `named` 怎么选？ → 生产用 deterministic 兼顾稳定与体积，开发用 named 便于调试但会把路径暴露到产物里。
3. 怎么校验稳定性？ → 两次构建导出 ID 映射表做 diff，断言交集比例达到阈值，并检查是否有模块 ID 从数字变成了字符串。
