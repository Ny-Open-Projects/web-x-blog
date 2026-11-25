---
title: [AGT-672] 提示词仓库（版本/评审/灰度）与评测平台如何深度联动？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-672：提示词仓库（版本/评审/灰度）与评测平台如何深度联动

**答**：
- 提示词 PR 必须带评测证据：PR 模板强制粘贴冒烟层跑分（机器人自动跑并盖章，防手工粘贴伪造）；无跑分不能进评审。
- 版本与分数绑定存档：每个 prompt 版本档案里存「当时评测集版本+分数+失败样本」，任何时刻可回溯"这个版本当时为什么过/挂"。
- 灰度联动：prompt 灰度批次自动跑线上评测（抽样 judge），灰度结束自动生成「线上vs离线」一致性对照，脱节的归因进评测改进。

```javascript
function onPromptPR(pr) {
  const run = evalBot.run(pr.diff, 'smoke');
  requireBadge(pr, run);                          // 机器人盖章
  archive({ promptVer: pr.version, evalSet: currentSetVer(),
    scores: run, fails: run.failures });          // 版本-分数档案
}
function onCanaryEnd(batch) {
  const offline = archive.get(batch.promptVer).scores;
  const online = batch.onlineJudgeSample;
  reportAlignment(offline, online);               // 离线vs线上对照
}
```

