---
title: [ZSM-150] 为什么说「用 Query 缓存当跨组件总线」是反模式？getQueryData 的正确用途是什么？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-150：为什么说「用 Query 缓存当跨组件总线」是反模式？getQueryData 的正确用途是什么？
**答**：
- 反模式：往缓存里 setQueryData 塞「根本不是服务端数据」的客户端状态（弹窗开关、选中项），跨组件共享——后果是缓存里混入无 queryFn 的「幽灵 key」，devtools 一屏垃圾、invalidate 前缀误伤、语义完全混乱。
- getQueryData 的正确用途只有两类：① 在 mutation 回调/事件处理器里读缓存做乐观更新的基准值；② 迁移过渡期适配旧状态库（136 场景），有明确退役时间。
- 判别标准一句话：缓存里的 key 必须对应「一个可重取的服务端请求」；没有 queryFn 的 key 不许存在。需要客户端总线就用 Zustand/Jotai。
- 面试要点：主动给出识别信号——「key 不像 URL」「永远不会 stale」「组件卸载后数据不回服务端」。

```javascript
// ❌ 反模式：客户端状态塞缓存
queryClient.setQueryData(['ui', 'drawer-open'], true)     // 幽灵 key
function useDrawer() {
  const open = useQuery({ queryKey: ['ui', 'drawer-open'] }).data
  return { open, setOpen: (v) => queryClient.setQueryData(['ui','drawer-open'], v) }
}

// ✅ 客户端状态归 store
const useDrawerStore = create((set) => ({
  open: false, setOpen: (open) => set({ open }),
}))

// ✅ getQueryData 正确用途：乐观更新基准
onMutate: async (patch) => {
  const prev = queryClient.getQueryData(['goods', patch.id])   // 读缓存做快照
  queryClient.setQueryData(['goods', patch.id], { ...prev, ...patch })
  return { prev }
}
```
