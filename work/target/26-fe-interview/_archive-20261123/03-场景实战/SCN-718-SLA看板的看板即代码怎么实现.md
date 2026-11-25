---
title: [SCN-718] 看板即代码（dashboard-as-code）怎么实现？配置怎么过评审？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-718：看板即代码怎么实现？
**答**：
- 配置仓库化：看板布局/指标绑定/告警阈值以 YAML 定义进 Git，PR 评审变更（谁改的/为什么/影响哪些告警），CI 校验 schema 与指标存在性——配置漂移和口头变更都消灭。
- 渲染器与配置分离：看板引擎渲染 YAML；本地 `board dev` 预览工具支持改配置即时看效果。
- CI 门禁：指标 key 必须存在于指标注册表、SLO 阈值变更需要 owner approve、告警规则与指标口径版本兼容。
- 变更可追溯：每次发布记录 diff 与操作者，回滚 = git revert。
- 追问钩子：为什么不直接在界面上拖拽配置——拖拽无评审、无审计、无环境隔离；看板配置涉及告警阈值，属于「影响值班行为的变更」，必须走流程。

```yaml
# boards/oncall.yaml
metrics:
  - key: ux.core_page.lcp_p95
    slo: { target: 2500, compliance: 0.999 }
    alerts:
      - burn_rate: { fast: 14.4, slow: 6, window: [1h, 6h] }
layout:
  core: [ux.core_page.availability, ux.core_page.lcp_p95]
  side: [trend_30d, budget_burn]
```
```javascript
// CI 校验
test('metrics registered & slo owner approved', () => {
  for (const m of board.metrics)
    expect(registry.has(m.key)).toBe(true);
});
```
