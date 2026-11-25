---
title: [ZSM-351] 视口驱动（进屏才加载）的状态订阅怎么设计
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-351：视口驱动（进屏才加载）的状态订阅怎么设计

**答**:
- 模式：IntersectionObserver 判断可见性 → 可见才 enabled 查询/激活订阅（WS 频道/轮询），离屏降级或停订阅——滚动长页的性能核心手段
- 停订阅分层：查询用 enabled:false（保留缓存停请求）、轮询用 refetchIntervalInBackground:false、推送用动态订阅/退订频道
- 抖动防护：可见性回调有边界抖动，加 rootMargin 缓冲带与最小保持时间（离屏 N 秒才停），避免滚动往返造成请求风暴
- 数据一致性：离屏停订阅期间数据可能陈旧，回屏时强制 stale 重拉（invalidate 或 staleTime 置零）

```javascript
const [visible, setVisible] = useState(false)
useEffect(() => {
  const io = new IntersectionObserver(([e]) => setVisible(e.isIntersecting), { rootMargin: '200px' })
  io.observe(ref.current)
  return () => io.disconnect()
}, [])
useQuery({ queryKey: ['panel', id], queryFn: fetchPanel, enabled: visible })
```
