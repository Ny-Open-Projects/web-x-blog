---
title: [924] embedding 模型要升级换代，索引怎么迁移不影响线上
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 模型迁移]
type: 面试题
---

## 924：embedding 模型要升级换代，索引怎么迁移不影响线上

**答**：
- 铁律：新旧模型的向量空间不通用，必须全量重建索引，绝不能混着用（旧向量 + 新 query 向量检索等于乱序检索）。
- 迁移五步：新模型离线建影子索引 → 评估集跑新旧对比（准确率不得倒退才放行）→ 双写期（新文档同时写两索引）→ 别名切换灰度 → 旧索引保留两周后下线。
- 成本评估先行：全量 embedding 一次的成本与耗时决定走「一次性重建」还是「滚动重建」，滚动重建期间新旧检索结果差异要在监控里可见。
- 追问钩子：切换瞬间查询怎么不抖？——别名原子切换 + 双读兜底（新索引失败自动回落旧索引并告警），两套索引短时间共存是有意保留的。

```ts
async function migrate(newModel: string) {
  await rebuildShadowIndex(newModel);              // 影子索引
  const cmp = await evalBoth(evalSet, 'old', newModel);
  if (cmp.new.acc < cmp.old.acc - 0.005) return abort(cmp); // 准确率红线
  startDualWrite(newModel);                        // 双写期
  await aliasSwitch('rag-idx', 'rag-idx-' + newModel, { fallback: 'rag-idx-old' });
  scheduleRemoval('rag-idx-old', { afterDays: 14 });
}
```

