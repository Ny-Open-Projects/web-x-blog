---
title: [ZSM-258] 微前端应用反复挂载卸载后越来越卡怎么排查
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-258：微前端应用反复挂载卸载后越来越卡怎么排查

**答**:
- 高发根因：子应用 unmount 时没清理对共享 store/事件总线的订阅，主应用通知时回调堆积 + 已卸载组件内存驻留
- 排查三件：Performance 内存快照对比（挂载 10 次 vs 1 次）看 detached 节点与回调数量；给 subscribe 打点统计活跃订阅数；crash 场景看闭包引用链找到「谁没退订」
- 防线设计：共享层提供「应用作用域订阅」——`shared.scope(appId).sub(fn)`，scope.dispose() 一次性清理该应用全部订阅，卸载钩子只调一行
- 规范化：生命周期模板（脚手架生成）内置 unmount 清理清单，code review 检查项固化

```javascript
// 共享层 scope 设计
const scopeA = shared.scope('app-orders')
scopeA.sub((s) => render(s))          // 记账
scopeA.sub('cache:invalidate', h)
// 子应用 unmount
export async function unmount() { scopeA.dispose() }   // 一次性退订全部
```
