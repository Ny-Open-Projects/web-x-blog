---
title: [ARC-467] 前端状态的 owner 设计：每一份状态归谁管？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-467：前端状态的 owner 设计：每一份状态归谁管？
**答**:
- 状态归属决策树：仅组件内（表单草稿/悬浮态）→ useState；兄弟共享 → 提升到父组件；跨路由 → 模块级 store；全局单例 → 全局 store；服务端数据 → query 缓存（不复制进全局 store）；URL 可表达的状态（筛选/分页）→ 路由（ARC-389）。
- owner 唯一原则：一份状态只有一个权威 owner，其余全是订阅者——出现"同一数据存三处"就是 bug 温床（改了 A 忘了 B）。
- 服务端状态红线：服务端响应不复制进全局 store，query 缓存自带失效与去重；复制进去就要自己负责失效，早晚出不一致（ARC-386）。
- 临时态 vs 持久态：区分会话内临时态（重置成本低）与需持久化状态（草稿/偏好），持久态显式声明存储介质。
- 治理工具：状态清单审计（定期盘点全局 store 的 key：谁写谁读、是否有服务端数据混入），冗余状态合并。
```javascript
// 状态归属决策（代码评审用）
function stateOwner(state) {
  if (isFromServer(state)) return 'query 缓存（禁止复制进全局 store）';
  if (isSharableUrl(state)) return '路由 query（可分享可回退）';
  if (scope === 'component') return 'useState';
  if (scope === 'route') return '模块级 store（路由卸载即销毁）';
  return '全局 store（显式声明，需审计注册）';
}
```
