---
title: [AGT-867] 用 AI 生成状态管理代码（store/action/selector），如何保证架构一致（不自创模式）？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-867：用 AI 生成状态管理代码（store/action/selector），如何保证架构一致（不自创模式）

**答**：
- 模式锁定：团队的 store 模板（文件结构/命名/中间件使用规范）固化为生成模板，AI 填充业务逻辑而不是自创架构——"AI 写逻辑，模板定骨架"。
- 类型推导校验：生成的 store 必须过端到端类型检查（selector 类型与 state 推导一致），类型错误=模式偏离的信号。
- 评审焦点：AI 生成的状态代码人工只审「状态边界」（什么该进全局/什么留局部/缓存策略），机械部分免审。

```javascript
function genStore(feature, schema) {
  const skeleton = STORE_TEMPLATE.render(feature); // 模板锁定骨架
  const logic = ai.fill(skeleton, schema, {
    rules: ['selector纯函数', 'action不可变更新',
      '异步统一middleware'],                        // 规则注入
  });
  return typeCheckEndToEnd(logic);                 // 端到端类型验证
}
```

