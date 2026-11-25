---
title: [BLD-205] HMR（热更新）的原理与边界是什么？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-205：HMR 原理与边界？
**答**：
- 链路：文件变更 → 增量构建（只重转变更模块及其依赖闭包）→ HMR runtime 通过 WS 推送更新 manifest（模块 ID + hash）→ 客户端 fetch 更新 chunk → module.hot.accept 回调应用更新。
- accept 语义：模块声明「我能接受自己的更新」；未声明向上冒泡到父级，冒到入口则整页刷新——accept 边界决定局部热更粒度。
- React Fast Refresh 的增强：组件级热更保留 state（通过注册表映射组件实例），hook 违规（条件 hook）导致回退整页刷新。
- 边界：模块顶层副作用（事件监听没清理）会累积；非组件模块（工具/store）需要手写 accept。
- 追问钩子：为什么 HMR 后「页面行为诡异」多半是顶层副作用——热更新替换模块代码但不重置运行环境，旧模块注册的定时器/监听器仍在跑（新模块又注册一份）；HMR 的 accept 回调里清理旧副作用（dispose 钩子）是正确姿势。

```javascript
// HMR 协议
if (import.meta.hot) {
  import.meta.hot.accept((newModule) => applyUpdate(newModule));
  import.meta.hot.dispose(() => teardown());         // 清理旧副作用
}
// Fast Refresh 边界：hook 条件调用 → 无法映射 → 整页 reload
```
