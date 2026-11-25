---
title: [WEB-529] 埋点数据丢失的排查 SOP
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 排查SOP]
type: 面试题
---

## WEB-529：埋点数据丢失的排查 SOP

**答**：
- 丢失环节定位：先二分「客户端没发」还是「服务端没收」——本地抓包（或 debug 模式日志）确认客户端行为
- 客户端常见原因：页面跳转时 sendBeacon 未发出（Chrome 对 unload 时机限制）、队满被丢弃、JS 错误中断、SDK 未初始化（路由懒加载页）
- 传输层原因：CSP 拦截外联域名、广告插件拦截上报域名（现象：某类用户系统性缺数据）、跨域被预检失败
- 服务端原因：上报接口限流丢弃、字段解析失败整条丢弃、时区/日期切分导致统计口径错
- 补救机制：关键事件本地暂存 + 下次启动补发；上报失败重试一次；对账任务（客户端发送量 vs 服务端入库量日 diff）

```javascript
function trackSafe(evt) {
  try { queue.push(evt); } catch {}
  const ok = navigator.sendBeacon('/api/track', JSON.stringify(queue));
  if (!ok) localStorage.setItem('track_retry', JSON.stringify(queue)); // 失败暂存补发
  else queue.length = 0;
}
```
