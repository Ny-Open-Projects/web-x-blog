---
title: [AGT-593] 手写 UISchema 渲染守卫：白名单组件、深度限制、actionId 唯一、事件锁定？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-593：手写 UISchema 渲染守卫：白名单组件、深度限制、actionId 唯一、事件锁定

**需求与边界**：
- 实现 renderUISchema(schema)：渲染模型输出的 UI schema。
- 边界要求：① 组件类型白名单外的整卡降级为 alt 文本；② 嵌套深度 ≤3、单卡组件数 ≤20（防恶意爆炸布局）；③ actionId 必须唯一且可定位（重复则丢弃重复项）；④ 已消费的 action 再次点击无效（锁定态）。

**答**：
```javascript
const ALLOWED = new Set(['button', 'select', 'form', 'card', 'text']);
function renderUISchema(schema) {
  if (!Array.isArray(schema.components)
    || !schema.components.every(c => ALLOWED.has(c.type)))
    return renderAlt(schema.alt ?? '该内容暂不支持交互展示');
  const seen = new Set();
  const nodes = flatten(schema.components, 0).filter(c => {
    if (!c.actionId) return true;
    if (seen.has(c.actionId)) return false;     // 重复 actionId 丢弃
    seen.add(c.actionId); return true;
  });
  return nodes.map(c => renderNode(c, { consumed: consumeRegistry }));
}
function flatten(list, depth) {                 // 深度限制 ≤3、数量 ≤20
  if (depth > 3 || list.length > 20) throw new Error('SCHEMA_LIMIT');
  return list.flatMap(c => c.children
    ? [c, ...flatten(c.children, depth + 1)] : c);
}
function onAction(actionId, value) {
  if (consumeRegistry.has(actionId)) return;    // 已消费：锁定无效
  consumeRegistry.add(actionId);
  sendNextTurn({ uiAction: { actionId, value } });
}
```

**评分点**:
- 白名单外整卡降级（不部分渲染恶意混入项）；深度与数量双重限额。
- actionId 去重 + 消费锁定（防重复提交与注入重复按钮）。

