---
title: [AGT-896] 手写 instrument：schema匹配、AI不发明事件、占位符校验、漏埋点提示？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-896：手写 instrument：schema匹配、AI不发明事件、占位符校验、漏埋点提示

**需求与边界**：
- 实现 instrument(el, intent, params, registry)。
- 边界要求：① 事件必须匹配 registry 已注册 schema（按意图匹配），无匹配返回需注册标记（不发明事件名）；② 参数按 schema 校验（类型/必填/枚举）；③ 占位符完整性（模板变量不丢失）；④ dev 环境校验失败 console.error 带修复提示；⑤ 新增交互（diff 中无埋点的可交互元素）产出漏埋清单。

**答**：
```javascript
function instrument(el, intent, params, registry, { dev } = {}) {
  const match = registry.findByIntent(intent);
  if (!match)
    return { needRegister: true, intent,
      hint: '先在事件中心注册 schema 再埋点' };      // 不发明
  const v = match.schema.validate(params);
  if (!v.ok && dev)
    console.error(`[埋点] ${match.name} 参数不合法：`,
      v.errors, '修复：', match.schema.example);
  return { name: match.name, params: v.data, ok: v.ok };
}
function missingIn(diff, registry) {
  return diff.addedInteractive.filter(el =>
    !registry.hasBinding(el)).map(el => ({
      el: el.selector, hint: '新增交互未埋点' }));   // 漏埋清单
}
```

**评分点**:
- 事件只从 registry 匹配（AI 不发明事件名——命名漂移防线）。
- schema 校验+dev 修复提示；占位符完整性。
- 漏埋点清单（从 diff 推断，闭环提示）。

