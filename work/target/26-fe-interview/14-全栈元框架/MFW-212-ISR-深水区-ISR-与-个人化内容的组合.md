---
title: [MFW-212] ISR 深水区：个性化内容与静态页的组合（cookie 分层）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-212：个性化内容与 ISR 的组合

**答**:
- 反模式：整个页面因「用户名」个性化而放弃静态化——正确做法是「静态骨架（ISR）+ 动态岛（流式 Suspense 段读 cookie）」
- PPR 模式的落地：页面 95% 静态（ISR 缓存）+ 5% 个人化区域独立流式段（每请求渲染读 session）——静态与动态在同一响应内流式合并
- 实现细节：动态段读 cookies() 会退出静态——把它圈进 Suspense 边界（让框架知道这段可延后）、静态段不读任何请求级 API
- 客户端补个人化替代：纯展示个人化（问候语）用客户端 localStorage 读（零服务端成本）——分层决定「哪层管个性」

```javascript
// PPR：静态壳 + 个人化动态岛
export default function Page() {
  return (
    <>
      <StaticContent />                              {/* ISR 缓存 */}
      <Suspense fallback={<UserSkeleton />}>
        <PersonalBar />                              {/* 读 cookie，每请求流式 */}
      </Suspense>
    </>
  )
}
```
