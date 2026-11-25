---
title: [DP-449] 案例：错误监控 SDK 的模式
date: 2026-11-21
categories: [设计模式]
tags: [前端面试, 面试题, 设计模式]
type: 面试题
---

## DP-449：错误监控 SDK

**答**：
- 错误监控 SDK 的模式全景：观察者（全局错误事件订阅：error/unhandledrejection）、责任链（处理管道：解析→聚合→采样→上报）、策略（采样与限流策略）、命令（面包屑记录——用户轨迹）、装饰器（fetch/XSS 包装——自动捕获）
- 包装器的捕获面：fetch/XHR/addEventListener 的装饰（统一入口捕获异步错误——装饰器批量应用）
- 聚合与限流：同指纹 1 分钟限流 + 计数补报（错误风暴防刷爆）
- 深水点：sourcemap 的「版本对齐」——错误堆栈的还原依赖版本对应 map（发版上传 map——版本错配=堆栈无意义）——监控的版本管理

```javascript
// 装饰器批量捕获
const wrap = (target, name) => { const orig = target[name]; target[name] = function (...a) { try { return orig.apply(this, a); } catch (e) { capture(e); throw e; } }; };
wrap(window, 'fetch'); wrap(XMLHttpRequest.prototype, 'open');
// 责任链: capture → parse → fingerprint → aggregate → sample → report
```
