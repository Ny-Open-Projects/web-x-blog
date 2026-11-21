---
title: [ZSM-133] 分层架构下怎么设计统一的加载/错误 UI 约定？每层各管哪些反馈？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-133：分层架构下怎么设计统一的加载/错误 UI 约定？每层各管哪些反馈？
**答**：
- 缓存层反馈：isLoading（首取）、isFetching/isValidating（重取）、error（网络/服务端错），UI 约定骨架屏 vs 进度条 vs 降级旧数据。
- 客户端层反馈：transition pending（useTransition 的 isPending）、表单提交中、乐观操作 pending，UI 约定按钮 loading 与禁用态。
- URL 层反馈：路由切换的 Suspense/transition，Next 的 loading.js 约定文件，页面级 loading 归它。
- 统一原则：错误三问——能重试吗（给重试按钮）、有旧数据吗（降级）、是权限问题吗（引导登录/申请权限）；约定写成组件库级别的 `<AsyncBoundary>`，业务不重复造。

```javascript
// 统一异步边界组件：业务组件只关心成功态渲染
function AsyncBoundary({ queryKey, children, skeleton }) {
  const { data, error, isLoading, refetch } = useQuery({ queryKey, enabled: false })
  const loading = isLoading
  if (loading) return skeleton ?? <Skeleton/>
  if (error) {
    if (error.status === 401) return <LoginPrompt/>
    return <ErrorView onRetry={refetch}/>
  }
  return typeof children === 'function' ? children(data) : children
}

// 业务侧一行接入
<AsyncBoundary queryKey={['goods', id]} skeleton={<DetailSkeleton/>}>
  {(goods) => <GoodsDetail goods={goods}/>}
</AsyncBoundary>
```
