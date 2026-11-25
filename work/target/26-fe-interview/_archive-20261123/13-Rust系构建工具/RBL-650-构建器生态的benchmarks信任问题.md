---
title: [RBL-650] 构建器生态的 benchmark 信任问题：如何设计一份不会被质疑的性能对比
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-650：构建器生态的 benchmark 信任问题：如何设计一份不会被质疑的性能对比

**答**:
- 各构建器官网的性能对比图互相矛盾（都说自己最快）——根因是 benchmark 的自由度：选什么项目、开什么配置、算不算插件、比 dev 还是 prod。一份可信 benchmark 的设计原则：**可复现（脚本与输入公开）+ 变量控制（唯一变量是构建器）+ 指标全面（冷/热/内存/产物质量）**。
- 变量控制清单：1) 相同硬件与隔离（容器 CPU pin）；2) 相同语义配置（各工具用自己的等价配置，但语义等价要审计——比如都开 sourcemap、都关 minify 或都开）；3) 插件公平性（真实项目必须带等价插件集——React 快速刷新/TS 转换，裸跑对比是自欺）；4) 预热与采样（RBL-588 的统计口径）。
- 指标透明度：报告必须附带「排除项」说明（如排除 npm install、排除类型检查——并解释为何排除）；「构建时间」要拆阶段（resolve/transform/codegen）避免用单一总时长掩盖结构性差异。
- 中立性的组织机制：benchmark 由第三方维护（或社区 PR 驱动），工具厂商不得单方面改输入集；版本快照固定（对比结果绑定各工具具体版本号，升级即重跑）。
- 追问钩子：为什么「dev 冷启动」与「prod 全量」要分开报？——优化目标不同（dev 优化按需与取消，prod 优化并行与压缩），混合成单一数字（如「比 X 快 10 倍」）通常是营销而非工程结论；面试中你能指出这一点，就是加分项。

```javascript
// 可复现 benchmark 脚本骨架
const SUITES = [
  { name: 'three-real', repo: 'three.js', entry: 'src/Three.js' },
  { name: 'biz-monorepo', repo: 'internal-app', entry: 'apps/web/src/main.ts' },
];
const TOOLS = ['rolldown', 'rspack', 'vite', 'webpack'];   // 绑定版本
const VERSIONS = { rolldown: '1.0.0', rspack: '1.2.0', vite: '6.0.0', webpack: '5.94.0' };

async function runBench() {
  const report = { meta: { date: today(), versions: VERSIONS, machine: machineInfo() }, suites: {} };
  for (const s of SUITES) {
    report.suites[s.name] = {};
    for (const t of TOOLS) {
      const cfg = equivalentConfig(t, s);                 // 语义等价配置（审计记录在案）
      report.suites[s.name][t] = await measure(t, s, cfg, { runs: 7, cold: true, warm: true });
      // { coldP50, warmP50, peakMemMB, stageBreakdown }
    }
  }
  writeReport('bench-report.json', report);               // 输入+脚本+结果 全公开
}
// 语义等价审计表（附报告）
// { sourcemap: 'all tools on', minify: 'off（隔离压缩变量）', plugins: 'react+ts 各自官方实现' }
```
