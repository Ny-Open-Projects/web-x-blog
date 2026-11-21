---
title: [AIC-097] Agent 改坏了怎么快速回滚？「任务级回滚」和「语义级回滚」有什么区别？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-097：Agent 改坏了怎么快速回滚？「任务级回滚」和「语义级回滚」有什么区别？
**答**：
- 任务级回滚：一个任务一个分支/一次提交，revert 整个提交即可回到任务前状态——前提是任务边界干净（commit 不混合多个任务）。
- 语义级回滚：只撤销某个「决策」（如撤掉它选的方案 B 换方案 A），保留其余改动——需要任务日志里记录「决策→涉及的文件/hunk」映射，按映射精确还原。
- 设计前提：① agent 每任务独立分支（AIC-096）② 提交信息带结构化元数据（taskId、决策清单）③ 产物标记——AI 产出的文件在 commit body 里列出，回滚时知道影响面。
- 回滚演练：把「撤销一个 agent 任务」作为常规操作测试过，别等事故才发现 revert 不了（比如 commit 里混了别人的改动）。
- 追问钩子：能区分两种回滚并说出「任务级靠工程纪律、语义级靠日志结构」的候选人是真的设计过。

```javascript
// 任务级回滚（基于结构化提交）
function revertTask(taskId) {
  const commit = git.findCommitByMessage(`agent-task: ${taskId}`);
  if (!commit) throw new Error('task commit not found');
  git.revert(commit.hash, '--no-edit');
}
// 语义级回滚：按决策映射还原
function revertDecision(taskId, decisionId) {
  const log = loadTaskLog(taskId);
  const decision = log.decisions.find(d => d.id === decisionId);
  decision.hunks.forEach(h => restoreHunk(h)); // 精确还原到决策前快照
}
```
