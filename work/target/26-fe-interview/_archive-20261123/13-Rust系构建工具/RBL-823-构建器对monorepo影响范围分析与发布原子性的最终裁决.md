---
title: [RBL-823] 场景题：Monorepo 发布的原子性裁决——半发布状态的回滚与恢复策略
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-823：场景题：Monorepo 发布的原子性裁决——半发布状态的回滚与恢复

**答**:
- 多包发布的中间态问题：发布 5 个包中途 2 个失败（registry 超时/版本冲突）——留下「半发布」状态：部分包已发新版、部分还是旧版，互相的版本引用可能不一致。裁决策略：1) **继续恢复**（重试失败者——已发布的不动，幂等续跑）；2) 全量回滚（npm 不允许 unpublish 已发布的——deprecate + 补发 patch 修正引用）；3) 状态记账（发布 ledger：每包的发布状态/版本/时间——恢复的依据）。
- 恢复的幂等设计：发布步骤天然幂等（同版本再发布会失败——用「已发布检测」跳过：registry 查询版本存在即跳过）；版本冲突的失败（依赖的包版本还没发布）需要按拓扑序重排——发布计划器（RBL-727）的运行时重排。
- 引用一致性的最终检查：全量发布完成后「引用完整性审计」——每个包的 deps 声明的版本在 registry 存在（RBL-682 校验器的发布态）；不一致的补救是「follow-up patch」。
- 通知与可观测：半发布状态的可见性（发布看板显示卡住的包 + 原因）——「静默的半发布」比失败更危险（下游以为发布了）。
- 追问钩子：为什么「全量回滚」在 npm 生态几乎不可行？——npm unpublish 有时间窗限制且已下载的用户不会消失；生态的回滚语义实际是「向前修正」（发一个 revert patch）而非「向后撤销」——这与 CDN/数据库的回滚模型不同，发布工程要接受「不可撤销、只能修正」的现实。

```javascript
// 发布 ledger 与幂等恢复
class ReleaseLedger {
  #entries = [];
  record(pkg, version, status, detail?) { this.#entries.push({ pkg, version, status, at: Date.now() }); }
  published(pkg, version) { return this.#entries.some(e =>
    e.pkg === pkg && e.version === version && e.status === 'ok'); }
}
async function resumeRelease(plan, ledger, registry) {
  for (const layer of plan.layers) {
    for (const pkg of layer) {
      if (ledger.published(pkg, plan.version)) continue;   // 已发布跳过（幂等）
      try {
        await publish(pkg, plan.version);
        ledger.record(pkg, plan.version, 'ok');
      } catch (e) {
        ledger.record(pkg, plan.version, 'failed', e.message);
        notify(`${pkg} 发布失败: ${e.message}——半发布状态可见`);
      }
    }
  }
  await verifyDepsConsistency(plan, registry);             // 引用完整性终检
}
```
