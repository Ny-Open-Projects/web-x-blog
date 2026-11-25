---
title: [ZSM-314] 代码分割后两个 chunk 各自创建了 store 实例怎么办
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-314：代码分割后两个 chunk 各自创建了 store 实例怎么办

**答**:
- 根因：模块顶层 `create()` 单例，但两个异步 chunk 各自 bundle 了一份模块（bundler 复制/双包），或 SSR+CSR 各一份，出现「状态改了组件没反应」
- 治理一：共享模块提升到公共 chunk（vendors/共享层），保证物理上只有一份；治理二：store 挂到运行时单例（window.__store 或模块注册表）并做存在性检查
- React 侧更稳的方案：Provider 注入实例（Context 持有 store），模块只导出工厂不导出实例——创建权上收到应用根部
- 检测：dev 打印 store 的创建次数/实例 id；重复创建直接 console.error

```javascript
// ❌ 模块顶层单例，跨 chunk 可能被复制
export const store = create(() => ({ count: 0 }))
// ✅ 工厂 + Provider 注入
export const createStore = () => create(() => ({ count: 0 }))
const storeRef = useRef(createStore())     // 应用根部创建一次，Context 下发
```
