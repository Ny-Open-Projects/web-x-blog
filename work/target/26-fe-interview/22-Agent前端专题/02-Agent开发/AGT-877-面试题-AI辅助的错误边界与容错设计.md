---
title: [AGT-877] AI 生成的组件普遍缺错误边界/加载态/空态，如何用工程手段补齐？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-877：AI 生成的组件普遍缺错误边界/加载态/空态，如何用工程手段补齐

**答**：
- 工程手段三件：组件模板化（脚手架强制带 ErrorBoundary/Suspense/Empty 三态骨架，AI 在骨架内填充）、 lint 规则（自定义 lint 检查异步组件缺错误处理/fetch 无 loading 态模式）、ESLint 插件+AI 自检（生成后自跑三态检查清单）。
- 运行时兜底：全局 ErrorBoundary 兜底 + 上报（缺边界的问题在运行时暴露即记录到「组件三态缺失」台账，反哺模板与规则）。
- 用 AI 反向扫：定期让 AI 扫描存量组件的三态缺失清单（比新写更需要），产出补齐工单。

```javascript
const THREE_STATE_TEMPLATE = `
function X() {
  return (
    <ErrorBoundary fallback={<XError />}>
      <Suspense fallback={<XSkeleton />}>
        <XInner />          {/* AI 填充区 */}
      </Suspense>
      <XEmpty condition={...} />
    </ErrorBoundary>
  );
}`;
const missing = await aiScan(components, {
  check: ['errorBoundary', 'loadingState', 'emptyState'],
  out: '工单清单',
});
```

