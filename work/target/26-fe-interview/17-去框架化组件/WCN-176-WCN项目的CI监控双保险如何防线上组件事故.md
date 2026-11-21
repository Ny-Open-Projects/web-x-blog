---
title: [WCN-176] WCN 项目的"CI + 监控"双保险：如何把线上组件事故的影响压到最小？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 选型与工程落地]
type: 面试题
---

## WCN-176：WCN 项目的"CI + 监控"双保险：如何把线上组件事故的影响压到最小？

**答**：
- 事故面拆解：加载失败（CDN/CORS）→ define 失败（语法/重复注册）→ 渲染异常（运行时错误）→ 交互异常（事件/竞态）——每层都要有独立防线。
- CI 防线：双宿主冒烟、体积预算、manifest diff、a11y 门禁——把"可预知"问题挡在发布前。
- 监控防线：加载失败率（import 异常）、define 失败（whenDefined reject 捕获）、wc-error 事件聚合、版本分布；全部按 tag+version+宿主三维聚合。
- 自动熔断：错误率超阈值（如 5 分钟内 1%）→ 加载器自动回切稳定版本（WCN-114 的熔断逻辑），同时告警。
- 兜底 UI：组件加载/渲染失败渲染降级占位（SafeElement），不影响页面其余部分；关键业务组件提供宿主侧 fallback 渲染开关。
- 演练：季度做一次"CDN 故障演练 + 回滚演练"，验证熔断链路真实可用。

```javascript
// 加载器熔断（整合版）
async function loadWithFuse(tag) {
  const ver = await pickVersion(tag);           // 灰度选择
  const start = Date.now();
  try {
    await import(wcUrl(tag, ver));
    track('wc_define_ok', { tag, ver, ms: Date.now() - start });
  } catch (e) {
    track('wc_define_fail', { tag, ver, msg: e.message });
    await fuseOpen(tag);                        // 计数熔断：回切 stable
    await import(wcUrl(tag, stableOf(tag)));
  }
}
```
