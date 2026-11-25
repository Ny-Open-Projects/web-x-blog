---
title: [RBL-671] 构建器社区的 RFC 流程： breaking change 如何做出不挨骂的决策
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-671：构建器社区的 RFC 流程：breaking change 如何做出不挨骂的决策

**答**:
- 构建器是基础设施，API 变更影响整个生态——RFC 流程（rollup/esbuild/rust RFC 模式）：提案 → 公开讨论窗口（静默期强制 ≥2 周）→ 决策记录（ADR：动机/选项/取舍/否决理由）→ 实施里程碑 + 迁移期。流程的价值不是民主而是「决策可追溯」——半年后没人记得为什么这样改，ADR 是记忆。
- breaking change 的减震设计：deprecate 先行（旧 API 保留两个 minor + 运行时警告）、codemod 同步提供（迁移机械化）、行为差异用 flag 双轨（新旧模式并存一个版本）；「破坏前先修路」。
- 社区异议的处理框架：意见分歧时按「证据等级」裁决——issue 复现/基准数据 > 个人偏好；决策记录里明确「否决理由」，避免同一争论反复。
- 内部工具团队的对应实践：内部 RFC + 变更公告（使用面统计——谁在用要变的 API，直接定向通知而不是全员广播）；API 使用面数据（AST 扫描内部仓库）让 breaking 的影响范围可预估。
- 追问钩子：为什么构建器的 RFC 讨论常陷入「性能 vs 正确性」死循环？——两者都是合法目标且不可通约；工程答案不是投票而是「分层默认」（正确性默认、性能 opt-in，反之亦然，取决于工具定位）+ 用基准数据说话（RBL-650）。

```javascript
// RFC/ADR 记录结构
const adr = {
  id: 'ADR-0142',
  title: 'transform 钩子返回协议增加 meta 字段',
  status: 'accepted',
  motivation: '插件需要传递转换统计（提取的翻译键等）到下游插件，目前只能挂全局变量——并行构建下有竞态',
  options: [
    { name: 'A: 返回对象增加 meta', pro: '零破坏', con: '字符串返回的插件无法使用' },
    { name: 'B: 新钩子 transformWithMeta', pro: '显式', con: '钩子数量翻倍' },
  ],
  decision: '选 A（渐进增强），字符串返回视为 { code }；meta 跨插件传递由宿主合并',
  rejectedReason: 'B 方案钩子爆炸，生态迁移成本高',
  migration: { deprecateVersion: '1.8', removeVersion: '2.0', codemod: 'npx rolldown-codemod meta-hook' },
};

// API 使用面扫描（内部团队）
async function scanApiUsage(codename, apiPattern) {
  const repos = await listInternalRepos();
  const hits = [];
  for (const repo of repos) {
    const found = await grepRepo(repo, apiPattern);
    if (found.length) hits.push({ repo, count: found.length });
  }
  return hits.sort((a, b) => b.count - a.count);         // 定向通知受影响最多的团队
}
```
