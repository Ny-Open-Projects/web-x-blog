---
title: [AGT-506] 产品里支持多个模型切换，前端要处理哪些状态语义（能力差异/降级提示/会话内切换）？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-506：产品里支持多个模型切换，前端要处理哪些状态语义（能力差异/降级提示/会话内切换）

**答**：
- 模型不只是"名字不同"：能力矩阵（是否支持工具调用/视觉/长上下文）、价格、延迟都不同，切换器要展示能力徽标而非只有名称。
- 会话中途切模型要处理上下文兼容：旧会话超出新模型窗口需要先压缩；不支持工具调用的模型要禁用相关按钮并说明原因。
- 服务端降级（主模型故障回落到备选）必须反馈到 UI：消息上标注"由备用模型生成"，避免用户以为质量下降是 bug。

```javascript
const MODELS = {
  'gpt-x': { tools: true, vision: true, ctx: 128000, tier: 'flagship' },
  'mini':  { tools: true, vision: false, ctx: 32000, tier: 'cheap' },
  'local': { tools: false, vision: false, ctx: 8000, tier: 'fallback' },
};
function useModelSwitcher(session) {
  const setModel = (id) => {
    const m = MODELS[id];
    if (session.usedTokens > m.ctx) compactSession(session); // 先压缩
    session.model = id;
    if (!m.tools) bus.emit('ui:disable', ['toolButton']); // 能力降级提示
  };
  return { setModel, badge: (id) => MODELS[id].tier };
}
```

