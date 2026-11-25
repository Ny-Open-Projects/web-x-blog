---
title: [ZSM-210] 多个 mutation 并发乱序覆盖怎么办
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-210：多个 mutation 并发乱序覆盖怎么办

**答**：
- 相同 `mutationKey` 的 mutation 默认并发；设置 `mutationScope: { id: 'cart' }` 后同 scope 内自动串行执行
- 乱序覆盖的根因：两个请求都基于旧 state 计算，后发先至时旧值覆盖新值；解法是服务端幂等/版本号，前端串行只是缓解
- 用 `isMutating({ mutationKey })` 可对特定作用域做「进行中禁用提交按钮」
- 高频连续提交（快速双击、批量操作）应在入口做节流/去重，mutation 队列只是最终防线

```javascript
const updateQty = useMutation({
  mutationKey: ['cart-update'],            // 相同 key 组成逻辑组
  mutationScope: { id: 'cart' },           // cart 作用域内串行
  mutationFn: (p) => api.updateCart(p),
})

const isCartBusy = useIsMutating({ mutationKey: ['cart-update'] }) > 0
<button disabled={!!isCartBusy}>保存</button>
```
