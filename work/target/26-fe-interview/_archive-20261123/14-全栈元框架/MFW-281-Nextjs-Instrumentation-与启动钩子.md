---
title: [MFW-281] Next.js Instrumentation 启动钩子与全局初始化
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-281：Instrumentation 启动钩子

**答**:
- 定位：服务端启动时执行一次（register() 导出）——OTel 初始化/定时任务注册/连接池预热/补丁（monkeys）的官方挂点（替代在模块顶层偷偷 init 的野路子）
- 运行时分域：register 区分 runtime（`process.env.NEXT_RUNTIME === 'edge'` 分支加载不同初始化文件——Edge 不能 require Node 模块）
- 与路由模块解耦：instrumentation 独立于页面编译（改它不触发全站重编）——全局副作用集中一处的可审计性
- 纪律：register 里只做「快且必须」的（<100ms——阻塞首请求）；重初始化异步后台跑 + 就绪探针 gating（K8s readiness 等待初始化完成标志）

```javascript
// instrumentation.ts
export async function register() {
  if (process.env.NEXT_RUNTIME === 'nodejs') {
    await initOtcl()                       // OTel 先于业务
    startBackgroundJobs()                  // 不 await：后台就绪即可
  } else {
    await initEdgeTracing()                // Edge 分支轻量
  }
}
```
