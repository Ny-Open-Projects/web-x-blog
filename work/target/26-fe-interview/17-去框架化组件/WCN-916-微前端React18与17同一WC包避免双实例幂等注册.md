---
title: [WCN-916] 微前端宿主 React18、子应用 React17：同一份 WC 组件包怎么避免双实例
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-916：微前端宿主 React18、子应用 React17：同一份 WC 组件包怎么避免双实例

**答**：
- 结论先行：自定义元素注册表（customElements registry）是全局单例，重复 `customElements.define` 同一 name 会报错；组件包必须做「注册幂等 + 单例共享」。
- 注册守卫：`if (!customElements.get('ds-button')) customElements.define(...)`，多个 bundle 各自引入时只真正注册一次（微前端多技术栈共存常态）。
- 依赖去重：把组件包放宿主 webpack Module Federation 的 shared/singleton，或打成 ESM 用 import maps 指向同一 URL，避免 React 本身双实例（双 React 会破坏 hooks）。
- 版本协商：组件包用语义化版本，宿主与子应用声明可接受范围，加载器按最高兼容版本提升（hoist）；不兼容则隔离到不同 iframe/shadow realm。
- 追问钩子：追问「两个子应用依赖不同大版本 WC 怎么办」——答：用不同元素名（ds-button-v1/v2）或不同 registry（ShadowRealm），物理隔离而非强行共用。

```javascript
// 幂等注册 + 版本协商
const VERSION = '2.3.0';
function registerOnce(name, ctor) {
  if (customElements.get(name)) {
    console.log(`${name} 已注册，跳过`);
    return customElements.get(name);
  }
  customElements.define(name, ctor);
  return ctor;
}
class DsButton extends HTMLElement {}
registerOnce('ds-button', DsButton);
// Module Federation shared 配置（示意）:
// shared: { 'ds-kit': { singleton: true, requiredVersion: '^2.0.0' } }
// 版本协商：取满足双方范围的最高版本
function resolveVersion(ranges) {
  return ranges.includes('^2.0.0') ? '2.3.0' : 'v1-isolated';
}
console.log(resolveVersion(['^1.0.0', '^2.0.0']));
```
