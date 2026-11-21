---
title: [ZSM-393] 场景题示范：无痕模式/Safari ITP 下存储受限的状态降级
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-393：场景题示范：无痕模式/ITP 下存储受限的状态降级

**答**:
- 能力探测：启动时探测 localStorage 可写性（try setItem/removeItem）、IndexedDB 可用性（无痕 Safari 旧版禁用）、storage estimate——探测结果进全局能力位
- 降级链：localStorage → sessionStorage（会话级可用）→ 内存 Map（页面级）→ 不可持久化；功能语义按层调整（草稿降级为「不跨刷新」要提示）
- 体验补偿：不可持久化时把「可恢复状态」尽量塞进 URL（恢复能力最强且不受存储限制）；敏感提示不静默丢数据
- 监控：storage 降级率上报，评估无痕用户占比与受影响功能面

```javascript
const caps = detectStorage()          // { local: true, idb: false }
const storage = caps.local ? localStorage : caps.session ? sessionStorage : memoryShim
if (!caps.local) {
  toast('当前模式无法保存草稿，关闭页面后将丢失')
  moveRecoverableToURL()              // 可恢复态进 URL
}
```
