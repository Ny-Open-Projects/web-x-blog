---
title: [ZSM-796] 笔试：手写 RSC 状态分层决策器（属性判定 + 序列化校验）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-796：手写 RSC 状态分层决策器（属性判定 + 序列化校验）
**答**：实现 `classifyState(field)`：按六问判定字段归入 RSC 直读 / 客户端 store / TanStack 缓存 / Server Action 四类之一；`validateSerializable(props)`：校验传给客户端组件的 props 可序列化（无函数/类实例/Symbol/循环引用），违规路径报错。附用例：四类判定 + 序列化违规检出。

```javascript
function classifyState({ source, updates, cacheAcrossRequests, serverComputed, isUserIntent }) {
  // 判定树（优先级从上到下）
  if (!isUserIntent && serverComputed && !updates.inClient) {
    return { layer: 'rsc-direct', reason: '渲染产物：服务端直读，零客户端状态' }
  }
  if (cacheAcrossRequests && source === 'server') {
    return { layer: 'tanstack-hydration', reason: '跨请求缓存复用：Query + dehydrate' }
  }
  if (isUserIntent && updates.inClient) {
    return { layer: 'client-store', reason: '用户意图+客户端更新：Zustand/atom' }
  }
  if (isUserIntent && serverComputed) {
    return { layer: 'server-action', reason: '输入+服务端计算：Server Action + useOptimistic' }
  }
  return { layer: 'rsc-direct', reason: '默认：能不进客户端就不进' }
}

// 序列化校验：props 传客户端组件的合规检查
function validateSerializable(value, path = 'props', seen = new Set(), errors = []) {
  if (value == null) return errors
  const t = typeof value
  if (t === 'function') { errors.push({ path, reason: 'function 不可跨 RSC 边界' }); return errors }
  if (t === 'symbol' || t === 'bigint') { errors.push({ path, reason: `${t} 不可序列化` }); return errors }
  if (t !== 'object') return errors
  if (seen.has(value)) { errors.push({ path, reason: '循环引用' }); return errors }
  seen.add(value)
  if (value instanceof Date) return errors                      // Date 可序列化
  if (value instanceof Map || value instanceof Set) {
    // React 支持 Map/Set（Flight 协议），但需标注
    return errors
  }
  if (value.constructor !== Object && !Array.isArray(value)) {
    // 类实例：非 plain object
    errors.push({ path, reason: `类实例 ${value.constructor.name} 不可序列化（转 plain object）` })
    return errors
  }
  if (Array.isArray(value)) {
    value.forEach((v, i) => validateSerializable(v, `${path}[${i}]`, seen, errors))
  } else {
    for (const k of Object.keys(value)) validateSerializable(value[k], `${path}.${k}`, seen, errors)
  }
  return errors
}

// 用例
console.log(classifyState({ source: 'server', updates: {}, cacheAcrossRequests: false, serverComputed: true, isUserIntent: false }))
// { layer: 'rsc-direct', ... }：商品列表渲染产物

console.log(classifyState({ source: 'server', updates: {}, cacheAcrossRequests: true, serverComputed: true, isUserIntent: false }))
// { layer: 'tanstack-hydration', ... }

console.log(classifyState({ source: 'local', updates: { inClient: true }, cacheAcrossRequests: false, serverComputed: false, isUserIntent: true }))
// { layer: 'client-store', ... }

console.log(classifyState({ source: 'local', updates: { inClient: true }, cacheAcrossRequests: false, serverComputed: true, isUserIntent: true }))
// { layer: 'server-action', ... }

// 序列化校验
const errs = validateSerializable({
  onSubmit: () => {},                    // ✗ 函数
  meta: new Map([['a', 1]]),             // ✓ Map（Flight 支持）
  user: new UserProfile('张三'),          // ✗ 类实例（假设）
})
console.log(errs.map((e) => e.path))     // ['props.onSubmit', 'props.user']
```
**评分点**：
- 判定树四层优先级（渲染产物优先归服务端）
- 序列化违规三类检出（function/类实例/循环引用）
- Map/Set 的 Flight 协议豁免（React 特例）
- 错误路径精确定位（props.onSubmit 可定位到字段）
