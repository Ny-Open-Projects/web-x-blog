---
title: [HW-171] 手写 Navigation API 路由——navigate 事件拦截、canIntercept 域限制与拦截回滚
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 面试题, 09]
type: 笔试题
---

**答**：Navigation API（Chrome 102+）替代手写 history 劫持：navigate 事件可拦截（intercept 处理 SPA 渲染）与 preventDefault 取消（未保存表单守卫）；canIntercept 限制拦截域；navigation.transitionWhile/intercept 的回滚（handler 抛错自动回滚到旧页面——比 pushState 手动回滚可靠）。

```javascript
if ('navigation' in window) {
  navigation.addEventListener('navigate', (e) => {
    if (!e.canIntercept || e.hashChange) return;        // 只拦截同文档可拦截导航
    const url = new URL(e.destination.url);
    if (url.pathname.startsWith('/form-edit') && formDirty()) {
      e.preventDefault();                                // 守卫：未保存拦截（等效 beforeunload 但 SPA 内）
      if (!confirm('未保存的修改将丢失，确认离开？')) return;
      // 确认离开：继续导航（重新触发或手动 router.navigate）
      return router.navigate(url.pathname);
    }
    e.intercept({                                        // SPA 接管：不触发整页加载
      handler: async () => {
        await renderRoute(url.pathname);                 // 渲染；抛错自动回滚旧页面
      },
    });
  });
} else {
  // 降级：history 劫持 + popstate（HW-071 模式）
}
// 价值：拦截回滚（handler 抛错自动恢复旧视图）+ 真实导航生命周期（下载/表单提交也能感知）
// 降级链：Navigation API → history 劫持 + popstate（HW-071）
```

**评分点**：
- navigate 事件拦截与 preventDefault 守卫（SPA 内未保存提示）。
- intercept handler 抛错自动回滚——比 pushState 手动回滚可靠，本题核心。
- canIntercept/hashChange 过滤（只接管该接管的导航）。
- 降级链到 HW-071 模式。
