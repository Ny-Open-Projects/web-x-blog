---
title: [ARC-052] 服务端状态库（TanStack Query / SWR / 自研）如何选型？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-052：服务端状态库（TanStack Query / SWR / 自研）如何选型？
**答**：
- TanStack Query：能力最全（缓存/去重/乐观更新/Infinite Query/devtools），适合复杂中后台；SWR 轻、API 简洁，适合以读为主的场景。
- 自研的合理动机只剩两个：特殊缓存协议（如 IM 消息序号）或极小包体积诉求；一般不该自研。
- 架构视角：选型重点是"缓存失效模型"是否匹配业务（tag invalidation、mutate 精确失效）。

```typescript
// TanStack Query：默认推荐，能力覆盖最全
const qc = new QueryClient({
  defaultOptions: { queries: { staleTime: 30_000, retry: 2, refetchOnWindowFocus: true } },
});
const { data } = useQuery({ queryKey: ['order', id], queryFn: () => fetchOrder(id) });

// SWR：轻量读场景
const { data: user } = useSWR('/api/me', fetcher, { revalidateOnFocus: true });

// 自研仅当存在协议级特殊需求，示例：按序号拉取 IM 消息
function useMessages(channelId: string) {
  const [msgs, setMsgs] = useState<Msg[]>([]);
  useEffect(() => {
    let seq = 0;
    return poll(async () => {
      const res = await fetch(`/im/channels/${channelId}/messages?after=${seq}`);
      seq = res.nextSeq;                 // 通用缓存库无法表达 seq 协议，才值得自研
      setMsgs(prev => [...prev, ...res.items]);
    }, 3000);
  }, [channelId]);
}
```
