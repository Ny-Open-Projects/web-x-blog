---
title: [AGT-321] Prompt 资产版本化——prompt 的"发布流程"怎么建？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-321：prompt 当作代码管理——版本化与发布流程怎么设计？

**答**:
- 仓库化：prompt 进 Git（模板+变量分离：`{{policy}}` 引用知识块，避免全文复制导致版本漂移）、变更走 PR（diff 可见+评审+关联评测结果）——prompt 变更的严肃性等同代码变更。
- 发布流程：PR → 回归评测（AGT-255 门禁）→ 灰度（按流量比例双版本并行，AGT-256 影子对比）→ 全量 → 可秒级回滚（版本指针切换）——prompt 是最高频的变更源，流程完备才能快速迭代不翻车。
- 资产分层：系统提示/工具描述/模板/少样本示例分别版本化——工具描述变更影响调用准确率，同样要过评测（AGT-258）；变量化的知识块与 prompt 骨架分开更新频率。
- 审计与关联：每个线上决策记录 prompt 版本（AGT-289）——线上问题回放时能对到"当时是哪个版本"，这是调试的基础设施。

```javascript
// prompt 版本化渲染
async function renderPrompt(templateId, vars) {
  const tpl = await promptRepo.get(templateId);  // Git 版本化
  const kb = await kb.render(vars.kbRefs);       // 知识块独立更新
  const compiled = compile(tpl.body, { ...vars, kb });
  return { compiled, version: tpl.sha };         // 版本随决策留痕
}
// 发布：PR → 回归门禁 → 5% 灰度 → 全量；
// 回滚 = 指针切回上一版本，秒级生效。
```
