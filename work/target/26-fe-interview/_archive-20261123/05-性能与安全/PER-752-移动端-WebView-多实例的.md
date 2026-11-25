---
title: [PER-752] 移动端 WebView 多实例的内存治理：多 WebView 场景的进程模型与前端配合策略
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-752：移动端 WebView 多实例的内存治理：多 WebView 场景的进程模型与前端配合策略

**答**：
- 进程模型：iOS WKWebView 独立进程（每实例约 30~80MB 基础开销）；Android WebView 共享渲染进程（崩溃一锅端）但堆隔离弱——多实例策略两平台不同。
- 治理策略：**实例数上限**（iOS 3 个，Android 2 个，超限销毁最旧）、**预创建池**（667）与上限联动（池大小计入实例预算）、**页面栈与实例绑定**（同容器内页面复用同一 WebView 实例，跨容器才新开）。
- 前端配合：收到容器内存告警（701）时主动瘦身（释放图片位图/清缓存）；页面间大数据传递走容器桥（Native 中转）而不是 window/ storage 塞大对象；销毁页面前 `location` 置空释放文档。
- 度量：实例数曲线、单实例内存分布（容器侧提供）、跨页切换内存峰值。

```javascript

const multiWebviewMemory = {
  model: { ios: 'WKWebView 独立进程，每实例 30~80MB 基础开销', android: '共享渲染进程，堆隔离弱' },
  policy: { cap: 'iOS 3 / Android 2 个实例上限，超限销毁最旧',
    pool: '预创建池大小计入实例预算', reuse: '同容器页面复用实例，跨容器才新开' },
  fe: ['内存告警时主动瘦身', '页面间大数据走容器桥不塞 storage', '销毁前置空 location 释放文档'],
  metrics: ['实例数曲线', '单实例内存分布', '跨页切换内存峰值'],
};
console.log(multiWebviewMemory.policy.cap);
```
