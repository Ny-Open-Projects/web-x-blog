---
title: [DP-195] Server Driven UI（服务端驱动 UI）是什么模式组合？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-195：Server Driven UI（服务端驱动 UI）是什么模式组合？（高频）
**答**：
- 本质：解释器模式——服务端下发 UI 描述（JSON 协议），客户端解释求值为组件树；配合工厂（组件注册表）、策略（动作分发：navigate/submit/api 调用）、观察者（数据绑定与状态广播）、备忘录（页面状态快照用于回退）。
- 与低代码同构（DP-182）：低代码是"人写 schema"，SDUI 是"服务端生成 schema"，客户端解释器完全复用。
- 安全边界：协议白名单组件注册（工厂只认注册过的 type），未知组件降级占位不崩溃。

```javascript
// 协议样例：服务端下发的 UI 描述
const pageSchema = {
  version: '1.2',
  state: { count: 0 },
  body: {
    type: 'column',
    children: [
      { type: 'text', text: '当前库存 {state.count}' },
      { type: 'button', text: '下单', action: { type: 'submit', api: '/order', body: { sku: 'A1' } } },
      { type: 'banner', img: 'https://cdn/x.png', action: { type: 'navigate', url: '/act/618' } },
    ],
  },
};
class SDUIRenderer {                                           // 解释器 + 工厂
  #registry = new Map(); #listeners = new Set(); #actions = new Map();
  register(type, comp) { this.#registry.set(type, comp); return this; }   // 工厂：白名单组件目录
  registerAction(type, fn) { this.#actions.set(type, fn); return this; }  // 策略：动作分发器
  on(fn) { this.#listeners.add(fn); return () => this.#listeners.delete(fn); }
  render(schema) {
    const walk = (node) => {                                   // 解释器：递归求值
      const Comp = this.#registry.get(node.type);
      if (!Comp) return h(Fallback, { type: node.type });      // 未知组件：安全降级
      const bound = interpolateProps(node, schema.state);      // 观察者语义：状态插值
      return h(Comp, { ...bound, onPress: node.action ? () => this.#dispatch(node.action) : undefined,
                       children: (node.children ?? []).map(walk) });
    };
    return walk(schema.body);
  }
  #dispatch(action) {                                          // 策略：动作类型分派
    const handler = this.#actions.get(action.type);
    handler?.(action);
    this.#listeners.forEach((f) => f(action));                 // 埋点观察
  }
}
const renderer = new SDUIRenderer()
  .register('column', Column).register('text', Text).register('button', Button).register('banner', Banner)
  .registerAction('navigate', (a) => router.push(a.url))
  .registerAction('submit', (a) => http.post(a.api, a.body));
render(renderer.render(pageSchema));
// 版本协商：协议 version 高于客户端支持版本时走 H5 兜底（策略降级）
if (semverGt(pageSchema.version, CLIENT_MAX)) return openH5Fallback();
```
