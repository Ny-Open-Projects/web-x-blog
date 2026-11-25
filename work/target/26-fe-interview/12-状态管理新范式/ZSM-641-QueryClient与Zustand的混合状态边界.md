---
title: [ZSM-641] QueryClient 与 Zustand 的混合架构边界：谁管什么
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-641：QueryClient 与 Zustand 的混合架构边界：谁管什么

**答**:
- 边界一句话：**TanStack Query 管「服务端状态」（事实数据的缓存），Zustand 管「客户端状态」（UI/会话态）**。判断标准：这个状态「刷新后应该恢复成服务端最新值」→ Query；「刷新后应回到默认/持久化」→ Zustand(+persist)。
- 分域清单：Query 管——列表/详情/搜索结果/统计报表/用户资料（只读镜像）；Zustand 管——筛选条件草稿、弹窗栈、多选集合、滚动位置、乐观队列、主题设置。禁止双向：不要把 API 数据塞 Zustand（绕过缓存失效机制），也不要用 Query 缓存当 UI 态（refetch 会覆盖用户输入）。
- 连接点设计（唯一合法桥）：1) mutation 的 onSuccess/onMutate 里写两侧（Zustand 更新 + queryClient.invalidate）；2) Zustand 里的「查询参数」作为 queryKey 的输入（`useQuery({ key: ['list', useFilterStore().filters] })`）——参数流从客户端态 → 服务端态是单向的；3) WS 事件同时驱动两者。
- 优化效果：分域后列表重渲只受 Query 缓存影响，输入框打字只更新 Zustand 的小切片，两者互不干扰——这就是「形状分离」（ZSM-618）在库选型层的落地。
- 追问钩子：面试验证分层理解的高频追问「为什么不用 Redux 一把梭」——RTK Query 也行，但「缓存的时效/失效/gc 语义」自建成本极高，Query 库的价值就在这些语义内建。

```javascript
// 客户端态（Zustand）：筛选草稿
const useFilters = create((set) => ({
  q: '', page: 1, sort: 'time',
  setQ: (q) => set({ q, page: 1 }),       // 改筛选回第一页
  setPage: (page) => set({ page }),
}))

// 服务端态（Query）：列表缓存，key 消费 Zustand 的参数
function useTodoList() {
  const { q, page, sort } = useFilters(useShallow((s) => ({ q: s.q, page: s.page, sort: s.sort })))
  return useQuery({
    queryKey: ['todos', 'list', { q, page, sort }],
    queryFn: () => api.list({ q, page, sort }),
    placeholderData: keepPreviousData,     // 翻页时保留旧数据防闪烁
  })
}

// 唯一桥：mutation 同步两侧
useMutation({
  mutationFn: api.updateTodo,
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: ['todos'] })   // 服务端态失效
    useFilters.getState().bumpVersion()                       // 客户端态标记（如角标数）
  },
})

// 反模式警戒
// ✗ api 数据塞 Zustand：
// useUserStore.setState({ profile: await api.me() })   // 绕过缓存时效/失效语义
// ✗ UI 态进 Query：
// useQuery({ queryKey: ['modal'], ... })               // refetch 覆盖用户输入
```
