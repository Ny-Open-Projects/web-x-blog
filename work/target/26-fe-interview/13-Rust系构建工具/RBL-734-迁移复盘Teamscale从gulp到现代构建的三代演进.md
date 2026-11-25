---
title: [RBL-734] 迁移复盘：gulp 时代到现代构建器——三代构建体系的演进启示
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-734：迁移复盘：gulp 时代到现代构建器——三代构建体系的演进启示

**答**:
- 三代演进的任务语义变化：gulp 时代（任务流：task 管道手动编排 watch/压缩/拷贝）→ webpack（依赖图：入口+loader 自动推导）→ Rust 构建器（图+增量+并行：把依赖图的计算成本压到交互级）。每代解决的问题不同，迁移时要把「旧体系隐含知识」显式化（gulpfile 里手写的顺序依赖，往往对应现代配置里的特定需求）。
- 复盘要点 1「任务语义翻译」：gulp 的串联任务（clean→build→rev）在现代工具里多数变成内置能力（产物清理/内容 hash），少数变成编排器职责（clean 在现代构建器里几乎不需要——原子输出目录 RBL-583）。翻译时先问「这个任务在现代语义下还存在吗」。
- 复盘要点 2「隐式约定的显式化」：gulp 时代靠约定（目录结构/命名规则）传递信息，现代构建器靠声明（exports 条件/目标环境）——迁移是把约定转成声明的过程，漏掉的约定就是迁移 bug。
- 复盘要点 3「性能基线的诚实」：老体系慢是因为任务串行+全量，新体系的对比要区分「语义等价的部分」与「新能力带来的部分」——否则对比报告里混入「本来就该有但老体系做不到」的能力，数字失真。
- 追问钩子：为什么「老体系知识」的抢救比「新工具学习」更决定迁移成败？——老体系运行多年沉淀了边界情况处理（特殊资源处理/历史包袱的 workaround），这些知识不在文档里、在配置注释和老员工脑子里；迁移前用「配置考古」（逐行注释化旧配置）把隐含知识显式化，是迁移计划的第一步。

```javascript
// 配置考古：gulpfile 注释化提取
function archaeology(gulpfileCode) {
  const tasks = [];
  for (const m of gulpfileCode.matchAll(/gulp\.task\(['"](\w+)['"]/g)) {
    tasks.push({ name: m[1], deps: extractTaskDeps(gulpfileCode, m[1]) });
  }
  return tasks.map(t => ({
    ...t,
    modernEquivalent: guessEquivalent(t),   // 内置能力/编排器职责/仍需插件
    questions: [`任务 ${t.name} 的隐含约定是什么？（顺序依赖为何存在）`],
  }));
}
const guessEquivalent = (t) =>
  /clean/.test(t.name) ? '可移除：原子输出目录（RBL-583）替代'
  : /rev|hash/.test(t.name) ? '内置：contenthash 文件名'
  : /watch|serve/.test(t.name) ? '内置：dev server/HMR'
  : '需人工评估：可能仍是业务语义任务';
```
