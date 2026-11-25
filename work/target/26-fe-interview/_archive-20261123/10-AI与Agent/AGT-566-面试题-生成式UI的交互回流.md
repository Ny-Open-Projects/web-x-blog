---
title: [AGT-566] 生成式 UI（模型输出按钮/表单），用户交互结果如何回传给模型进入下一轮？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-566：生成式 UI（模型输出按钮/表单），用户交互结果如何回传给模型进入下一轮

**答**：
- 模型输出的 UI schema 中每个交互组件带 actionId 与 payload schema；用户操作后前端封装成「结构化事件」（actionId + 值）随下一轮消息发送，模型据此继续——而不是把点击翻译成自然语言（丢精度）。
- UI 组件状态管理：组件是消息的一部分，发送后应锁定（防止重复提交），重发/编辑消息时对应组件要重置。
- 安全边界：schema 只能渲染白名单组件集合，位置/样式由前端模板决定，防止模型输出恶意布局（钓鱼按钮）。

```javascript
function onGenUIAction(msg, action) {
  markConsumed(action.id);                    // 锁定防重复提交
  sendNextTurn({
    parts: [{ type: 'ui_action', ref: msg.id,
      actionId: action.id, value: action.value }],   // 结构化回传
  });
}
const ALLOWED_COMPONENTS = ['button', 'select', 'form', 'card'];
function renderUISchema(schema) {
  if (!schema.components.every(c => ALLOWED_COMPONENTS.includes(c.type)))
    return <FallbackText text={schema.alt} />;   // 白名单外的降级
  return schema.components.map(renderComponent);
}
```

