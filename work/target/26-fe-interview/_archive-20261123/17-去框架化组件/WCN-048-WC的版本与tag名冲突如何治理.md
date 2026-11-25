---
title: [WCN-048] 多个组件库同时注册同名 tag 冲突怎么办？版本共存与命名空间怎么治理？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-048：多个组件库同时注册同名 tag 冲突怎么办？版本共存与命名空间怎么治理？

**答**：
- 冲突场景：微前端/多团队页面同时加载两个版本的 `my-modal`，后 define 的直接抛 `NotSupportedError`，且先注册的版本继续生效（行为不可预期）。
- 治理一：强制命名空间——tag 加组织前缀 `acme-modal`，lint 校验（ESLint 规则 + custom-elements.json 清单对照）。
- 治理二：工厂注册——库导出 `register(tag?)`，宿主可传别名 `register('acme-modal-v2')`；配合 `customElements.get` 检查。
- 治理三：`customElements.setName` 不存在，但可在 define 前用 `document.createElement(tag)` 探测是否已被占用，冲突时自动升级为带版本后缀的 tag。
- 清单与契约：发布 `custom-elements.json`（manifest）供 IDE 补全与 lint；加载器统一收口 define 调用（禁止业务代码直接 define）。

```javascript
// registry.js：统一收口注册，冲突自动改名
const ns = 'acme';
export function define(tag, ctor) {
  let name = `${ns}-${tag}`;
  if (customElements.get(name)) {
    if (customElements.get(name) === ctor) return name;   // 同类重复注册幂等
    name = `${name}-${Date.now().toString(36)}`;          // 冲突自动别名 + 上报
    reportConflict(tag);
  }
  customElements.define(name, ctor);
  return name; // 调用方拿到最终 tag 名
}
```
