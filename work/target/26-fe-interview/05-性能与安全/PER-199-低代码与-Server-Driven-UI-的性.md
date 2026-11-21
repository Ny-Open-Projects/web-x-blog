---
title: [PER-199] 低代码与 Server Driven UI 的性能与安全要注意什么？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-199：低代码与 Server Driven UI 的性能与安全要注意什么？

**答**：
- **schema 即代码**：服务端下发的渲染描述必须按"不可信输入"处理——组件白名单、URL 过滤、动作映射到客户端注册的 handler，schema 里绝不携带可执行代码。
- schema 来源要**验签**：防止配置中心被攻陷或中间人注入恶意 UI（钓鱼表单收集密码是真实攻击面）。
- 性能账单：schema 驱动多一层解析与映射，列表页必须虚拟滚动 + schema 预取；schema 体积纳入预算管理。
- 渐进增强：schema 解析失败的兜底是整块降级（空态/骨架），不能白屏——SDUI 的可用性不能低于原生渲染。

```javascript
// 低代码 / Server Driven UI：schema 按不可信输入处理
const ALLOWED_COMPONENTS = new Set(['Text', 'Image', 'Button', 'List', 'Section']);

export function renderSchema(schema, ctx) {
  if (!ALLOWED_COMPONENTS.has(schema.type)) {
    console.warn('未知组件被丢弃', schema.type);   // 白名单外组件直接丢弃
    return renderFallback();
  }
  switch (schema.type) {
    case 'Text':   return h('span', { class: 'sdui-text' }, String(schema.text ?? ''));
    case 'Image':  return h('img', { src: sanitizeUrl(schema.src), alt: schema.alt ?? '' }); // URL 过滤
    case 'Button':
      // 动作必须映射到客户端注册的 handler，schema 不得携带可执行代码
      return h('button', { onClick: () => actions[schema.action]?.(schema.args, ctx) }, schema.label);
    case 'Section': return h('div', {}, (schema.children ?? []).map((c) => renderSchema(c, ctx)));
    default: return renderFallback();
  }
}

// 来源验签：schema 响应带签名头，前端或网关校验，防配置中心被攻陷后注入恶意 UI
export async function fetchPageSchema(pageId) {
  const res = await fetch(`/api/sdui/${pageId}`);
  if (!verifySignature(res.headers.get('X-Schema-Signature'), await res.clone().text())) {
    return { components: [] }; // 验签失败整块降级，不白屏
  }
  return res.json();
}
```
