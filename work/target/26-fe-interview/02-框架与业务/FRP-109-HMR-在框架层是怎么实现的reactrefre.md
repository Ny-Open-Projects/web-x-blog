---
title: [FRP-109] HMR 在框架层是怎么实现的？react-refresh 的签名机制与 Vue 的 rerender 边界各是什么？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-109：HMR 在框架层是怎么实现的？react-refresh 的签名机制与 Vue 的 rerender 边界各是什么？

**答**：
- 公共链路：bundler（webpack/vite）监听文件变化 → 重新编译该模块 → 通过 ws 通知浏览器 → runtime 执行模块更新回调（`module.hot.accept` / `import.meta.hot.accept`）→ **框架的 HMR 运行时**决定"只是重渲染"还是"整页刷新"。
- **react-refresh**：编译器给每个组件函数注入 `$RefreshReg$(type, id)`（注册组件）与 `$RefreshSig$()`（生成签名函数，运行时经 `setSignature(fn, sig)` 登记）；runtime 在模块更新时比较新旧组件的**签名**（自定义 Hook 列表 + 源码结构 hash）——签名不变 → `setType` 原地替换组件函数引用，fiber 复用、**state 保留**；签名变了（Hook 数量/顺序变了）→ 强制 remount 该组件子树（state 必然丢，否则 Hooks 链表对不上）。
- **Vue HMR**：SFC 编译产物带 `__hmrId`；运行时把组件实例注册到 `instancesMap`，文件更新时走 `rerender`（只重跑 render，setup 不重跑，state 保留）或 `reload`（重新执行 setup，当 script 部分变化时）。
- 边界本质相同：**变更是否影响"组件形状"**——纯 render/模板改 → 热替换渲染层；setup/逻辑结构改 → 重执行初始化；模块级副作用/store 定义改 → 往上传直到整页 reload。

```javascript
// 简化实现，帮助理解 react-refresh 的签名比对与 setType
const families = new Map(); // 签名 key -> 组件家族（当前最新版本）

function register(type, key) {              // 编译器注入：组件定义处调用
  if (!families.has(key)) families.set(key, { sig: signatureOf(type), latest: type });
  return families.get(key);
}
function signatureOf(fn) {
  // 真实实现解析源码提取 Hook 调用序列；这里用函数源码长度模拟
  return String(fn).replace(/\s+/g, '').length;
}

function performReactRefresh(oldType, newType, key) {
  const family = register(oldType, key);
  const oldSig = family.sig, newSig = signatureOf(newType);
  if (oldSig === newSig) {
    // 签名一致：Hook 链结构不变 -> 原地替换函数引用，fiber.memoizedState 全保留
    family.latest = newType;
    return 'rerender：type 引用已替换，state 保留';
  }
  // 签名变化（Hook 增删）：链表对不上，必须 remount
  family.sig = newSig; family.latest = newType;
  return 'remount：Hook 结构变化，state 重置';
}

// 模拟：只改了 JSX 结构（Hook 数量不变）
const CounterV1 = function Counter() { const x = useStateLike(0); return x; };
const CounterV2 = function Counter() { const x = useStateLike(0); return x + 1; };
console.log(performReactRefresh(CounterV1, CounterV2, 'Counter'));
// 改动加了一个 useState：
const CounterV3 = function Counter() { const a = useStateLike(0); const b = useStateLike(1); return a + b; };
console.log(performReactRefresh(CounterV2, CounterV3, 'Counter')); // remount

// Vue 侧等价逻辑：__hmrId -> rerender（只重跑 render）或 reload（重跑 setup）
function vueHmr(instance, newRender, scriptChanged) {
  if (!scriptChanged) { instance.render = newRender; instance.update(); return 'rerender：state 保留'; }
  return 'reload：重新执行 setup，state 丢失';
}
function useStateLike(v) { return v; }
```

## 追问（补充）

**追问**：

1. 为什么只改了一个自定义 Hook，调用它的组件也会被 remount？ → 签名里包含被调用 Hook 的序列与结构，Hook 自身签名变化会沿调用链向上冒泡，所有调用它的组件签名一并失效，只能 remount 以保证 Hooks 链表对得上。
2. 签名一致、state 保留的情况下，useEffect 会不会重跑？ → 不会。组件函数引用被原地替换，fiber 与 memoizedState 全部保留，依赖未变的 effect 不重跑、也不触发 cleanup；只有组件被 remount 才会重新执行。
3. 什么写法会让 Fast Refresh 退化成整页 reload，Vue 侧对应哪一类？ → 导出非组件（如模块级常量、store 实例、工具函数）或组件用匿名箭头高阶包裹导致签名丢失，react-refresh 只能往上传；Vue 侧对应改了 `<script>` 里的模块级副作用，走 reload 而非 rerender。
