---
title: [NODE-768] 笔试题——实现契约测试 provider 验证器（交互回放 + 状态机）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-768：手写契约验证器

**需求与边界**：
- 需求：provider 契约验证（SCN-NODE-677）——① 交互回放（契约的请求 → provider 真实响应 → 比对期望）；② 状态机 setup（stateHandlers——验证前置状态）；③ diff 输出（字段级不匹配——SCN-ENG-290 分类）；④ can-i-deploy 集成（发布门禁——SCN-OPS-229）。
- 边界：① 响应匹配的宽松规则（pact matching rules——类型匹配 vs 精确值）；② 状态清理（每交互后重置——测试隔离）；③ 契约版本绑定（provider version ↔ 契约版本）。

**答**：
```javascript
async function verifyPacts(pacts, app) {
  const server = app.listen(0);
  const failures = [];
  for (const pact of pacts) {
    for (const interaction of pact.interactions) {
      await interaction.states?.setup?.();             // 状态机 setup（SCN-NODE-677）
      const resp = await request(server, interaction.request);
      const mismatch = matchResponse(resp, interaction.response, {
        matchingRules: interaction.response.matchingRules });   // 宽松规则
      if (mismatch) failures.push({ consumer: pact.consumer,
        interaction: interaction.description,
        diffs: classifyMismatch(mismatch) });          // 字段级 diff（SCN-ENG-290）
      await interaction.states?.teardown?.();          // 状态清理（隔离）
    }
  }
  server.close();
  return { ok: !failures.length, failures,
    gate: await canIDeploy({ provider: 'order-svc', version: VERSION }) };   // 发布门禁
}
```

**评分点**:
- 交互回放 + 状态机 setup/teardown（SCN-NODE-677 完整语义）。
- 宽松匹配规则（类型 vs 精确——契约语义）。
- 字段级 diff 分类（SCN-ENG-290 复用）。
- can-i-deploy 门禁（SCN-OPS-229 发布联动）。
