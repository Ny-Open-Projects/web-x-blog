---
title: [PER-727] 移动端 storage 事件与多页面同步的性能坑：高频 storage 写入造成的广播风暴怎么治？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-727：移动端 storage 事件与多页面同步的性能坑：高频 storage 写入造成的广播风暴怎么治？

**答**：
- 坑：同源多 Tab（或 WebView 多实例）下，每次 localStorage 写入都触发所有页面的 storage 事件——高频写入（滚动位置同步、计数器）造成广播风暴，每页都要 parse JSON。
- 治理：高频同步改用 **BroadcastChannel**（点对点消息、不落盘、无 storage 事件开销）或 SharedWorker（单点聚合）；localStorage 只留低频配置类同步；写入节流 + 变更检测（值没变不写）。
- WebView 场景特殊性：Android 多 WebView 可能不共享 localStorage（分进程），跨实例同步要靠容器桥（Native 转发）而不是 storage。
- 度量：storage 事件频率、每事件平均 payload 大小、监听端处理耗时。

```javascript

const storageStorm = {
  trap: '每次 localStorage 写入广播到同源所有页面（storage 事件）',
  fix: { highFreq: 'BroadcastChannel 点对点（不落盘无事件开销）',
    aggregate: 'SharedWorker 单点聚合', lowFreqOnly: 'localStorage 只留低频配置',
    throttle: '写入节流 + 值变更检测（不变不写）' },
  webview: 'Android 多 WebView 分进程不共享 storage -> 跨实例用容器桥转发',
};
class SyncChannel {
  constructor(name) {
    this.ch = 'BroadcastChannel' in window ? new BroadcastChannel(name) : null;
    this.last = null;
  }
  publish(msg) {
    const json = JSON.stringify(msg);
    if (json === this.last) return;                             // 变更检测
    this.last = json;
    if (this.ch) this.ch.postMessage(msg);                      // 高频走 BC
    else this.debouncedStorage(msg);                            // 降级节流 storage
  }
  debouncedStorage(msg) {
    clearTimeout(this.t);
    this.t = setTimeout(() => localStorage.setItem('sync', JSON.stringify(msg)), 200);
  }
}
```
