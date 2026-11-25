---
title: [WCN-972] 流式 SSR 下焦点管理与 aria-live：分块到达时读屏公告怎么不重不漏
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-972：流式 SSR 下焦点管理与 aria-live：分块到达时读屏公告怎么不重不漏

**答**：
- 结论先行：流式 SSR 分块插入 DOM 时，aria-live 区域若每块都写入会「重复播报」，若缓冲太多又「漏报」——要靠「单一 live 区域 + 去抖合并 + 优先级」策略。
- 单一入口：页面只有一个 aria-live polite 区域，各 chunk 的状态更新写进同一队列，合并成一条播报（如「商品列表已加载 20 件」而非逐条播报）。
- 焦点保护：chunk 插入不能抢走用户当前焦点——用 `document.activeElement` 记录并在插入后恢复；若焦点元素被替换，用 `aria-activedescendant` 指向新节点。
- 告警类用 assertive、普通更新用 polite，避免高优先级被淹没；一次性提示加 `aria-atomic=true` 整段朗读。
- 追问钩子：面试官问「SSR 阶段还没 JS 怎么播报」——答：关键状态用服务端输出的 aria-live 初始值（如加载态），后续 JS 接管后再走合并队列。

```javascript
// 单一 aria-live 区域 + 合并播报
const live = document.getElementById('sr-status'); // <div aria-live=polite aria-atomic=true>
let queue = [], timer = null;
function announce(msg, priority = 'polite') {
  queue.push(msg);
  clearTimeout(timer);
  timer = setTimeout(() => {
    live.textContent = queue.join('；'); // 合并成一次播报，不重复
    queue = [];
  }, 300);
}
// 流式 chunk 到达：
announce('商品列表已加载 20 件');
announce('价格已更新');
// 焦点保护：
const active = document.activeElement;
insertChunk();
if (active && document.contains(active)) active.focus();
```
