---
title: [RBL-821] 迁移复盘：构建工具升级的规模化组织策略——「升级日」制度与集中作战
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-821：迁移复盘：构建工具升级的规模化组织策略——「升级日」制度与集中作战

**答**:
- 分散升级的失效模式：每个团队「有空再升」→ 版本碎片（RBL-648）→ 内部工具的兼容矩阵爆炸（构建工具团队要支持 N 个版本的行为差异）。「升级日」制度：每季度固定的集中升级窗口，全体仓库同一周升级到目标版本——碎片收敛，支持成本线性下降。
- 升级日的运行结构：1) 预备周（构建团队发升级指南 + codemod + 兼容自检脚本——各团队跑自检预估工作量）；2) 升级周（全体升级，构建团队全天候答疑/值班——集中的支持比分散等待高效一个量级）；3) 收尾周（未完成仓库清单化跟进 + 升级指标复盘）。
- 激励设计：升级日的完成率要进入团队健康度指标（工具化的考核——否则永远排在业务后面）；「豁免需申请 + 复审」与配置白名单（RBL-801）同构。
- 升级日的规模效应：一次升级日解决「所有仓库 × 一个版本」——对比「随时升级」的 N 仓库 × M 版本组合；兼容性 bug 只需要修一次全团队受益——这是平台化组织的杠杆。
- 追问钩子：为什么「集中作战」的答疑成本反而更低？——分散升级时，同一个问题被 20 个团队在不同时间踩到，构建团队回答 20 次；集中升级把问题在 1-2 天内暴露，问题归并（第一个团队踩的坑写进 FAQ 后续团队自查）——信息同步的密度决定支持效率；这也是为什么发布工程喜欢「切换窗口」而非「滚动切换」。

```javascript
// 升级日准备度自检
function upgradeReadiness(repo, { target, rules }) {
  const blockers = rules
    .map(r => r.check(repo))
    .filter(x => !x.ok);
  return {
    repo: repo.name,
    ready: blockers.length === 0,
    blockers,
    estimatedHours: blockers.length * 2 +
      (repo.customPlugins > 3 ? 4 : 1),                 // 工时预估
  };
}
// 升级日看板
const board = repos.map(r => upgradeReadiness(r, { target: 'rolldown@2', rules }));
console.table(board.map(b => ({ repo: b.repo, ready: b.ready, est: b.estimatedHours })));
const notReady = board.filter(b => !b.ready);
if (notReady.length) broadcast(`升级日前未就绪清单: ${notReady.map(b => b.repo)}`);
```
