---
title: [JS-378] 错误传播策略：async 链路的失败语义
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 面试题, 并发]
type: 面试题
---

## JS-378：错误传播策略：async 链路的失败语义

**答**：
- 失败语义三档：致命（中断全链路，如鉴权失效）、可恢复（降级继续，如推荐接口挂）、可忽略（静默记录）——每个 await 都应明确「这个失败属于哪档」，未分类的失败默认致命是混乱之源
- Result 模式 vs 异常模式：前端推荐「Result 返回值」处理预期失败（{ ok, data | error }，类型系统强制处理），异常留给意外错误——预期失败不该走异常控制流
- 错误包装链：底层抛技术错误（NetworkError），中间层翻译为业务语义（「库存查询失败」），顶层决定 UI 反馈——包装保留 cause 链（Error cause 属性）用于诊断
- allSettled 后的聚合错误：多个独立任务失败要聚合上报（一次 toast 列出，不是连环弹窗）；聚合错误要保留各子错误详情
- 全局兜底：window.onerror/unhandledrejection 上报 + 「错误边界」组件隔离渲染树——兜底是最后防线不是第一处理点

```javascript
// Result 模式
const safe = (p) => p.then(v => ({ ok: true, v }), e => ({ ok: false, e }));
async function loadPage() {
  const [user, feed] = await Promise.all([safe(api.user()), safe(api.feed())]);
  if (!user.ok) throw new Error('致命: 无法获取用户', { cause: user.e });  // 致命上抛
  return {
    user: user.v,
    feed: feed.ok ? feed.v : { items: [], degraded: true },  // 可恢复降级
  };
}
```
