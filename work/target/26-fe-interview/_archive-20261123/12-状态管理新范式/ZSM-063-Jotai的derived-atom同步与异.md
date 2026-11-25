---
title: [ZSM-063] Jotai 派生 atom 里能不能发起副作用（fetch、埋点）？为什么不推荐？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-063：Jotai 派生 atom 里能不能发起副作用（fetch、埋点）？为什么不推荐？
**答**：
- 派生 read 应是纯函数：无订阅者时 atom 求值可能被跳过、被 GC 后重新求值，副作用次数不可控。
- 并发渲染下 read 可能被调用多次（React 严格模式、tearing 校验），埋点会翻倍，fetch 会重复。
- 异步需求用显式异步 atom（fetch 是「求值」不是副作用，可接受幂等请求），埋点/写 storage 这类动作放到 write-only action 或 subscribe。
- 兜底：副作用型派生用 `atomEffect`（jotai-effect 库）声明式管理触发条件与清理。

```javascript
// 差：read 里埋点，StrictMode 下双倍上报
const viewAtom = atom(get => { report('view'); return get(pageAtom) })

// 好：订阅式副作用，次数可控
import { atomEffect } from 'jotai-effect'
const viewEffect = atomEffect((get, set) => {
  report('view', get(pageAtom))
  return () => {} // 清理
})
// <ViewEffect /> 挂载即生效
```
