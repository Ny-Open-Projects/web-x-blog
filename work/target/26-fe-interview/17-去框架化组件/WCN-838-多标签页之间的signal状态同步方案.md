---
title: [WCN-838] 多标签页（多 tab）之间的 signal 状态同步怎么设计？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-838：多标签页（多 tab）之间的 signal 状态同步怎么设计？

**答**：
- 结论先行：跨 tab 同步用 `BroadcastChannel`（或 localStorage 事件兜底）广播变更，每个 tab 维护本地 signal，收到广播时更新——核心是「避免回声循环」和「处理并发写冲突」。
- 通道选择：`BroadcastChannel` 首选（不触发存储事件、性能好、支持结构化克隆），兼容性要求高时用 `localStorage` + `storage` 事件兜底（注意同源限制与序列化）。
- 避免回声：每个写入带一个唯一 tabId 与递增序号，收到自己发出的消息直接忽略；更新 signal 时「标记来源」避免再次广播。
- 冲突处理：多 tab 同时写同一值需要策略——最后写入者胜（带时间戳/逻辑时钟）、或按业务规则合并（如购物车取并集）；简单场景 LWW 足够。
- 边界：不是所有状态都该跨 tab 同步（如输入中的草稿通常不该），要明确「白名单」；页面关闭时广播清理消息；加订阅生命周期避免内存泄漏。
- 追问钩子：面试官会问「 Broadcasting 大量高频更新怎么办」——答：批量合并 + 节流广播（如 rAF/定时器合帧），只广播最终值而非每次中间态。

```javascript
import { signal } from '@preact/signals-core';
const TAB_ID = crypto.randomUUID();
const bc = new BroadcastChannel('app-signals');
const state = signal(0);

// 本地写 → 广播（带来源与序号）
let seq = 0;
function setLocal(v) {
  state.value = v;
  bc.postMessage({ key: 'count', value: v, from: TAB_ID, seq: ++seq });
}
// 收到广播 → 忽略自己 + 更新（不再次广播，避免回声）
bc.onmessage = ({ data }) => {
  if (data.from === TAB_ID) return;
  if (data.key === 'count') state.value = data.value; // LWW 简化
};
setLocal(5);                 // 其他 tab 收到后 state 也变 5
// 清理：bc.close() 在页面卸载时调用
```
