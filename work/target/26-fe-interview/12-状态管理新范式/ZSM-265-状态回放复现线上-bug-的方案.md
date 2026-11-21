---
title: [ZSM-265] 怎么用状态回放在本地复现线上 bug
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-265：怎么用状态回放在本地复现线上 bug

**答**:
- 数据源两层：DOM/视觉层用 rrweb 录制（事件流），状态层录 action/patch 流（redux actions 或自定义事件日志）——视觉重现 + 状态重现双轨
- 落地：错误发生时把「初始状态 + action 流」打包上报（脱敏、限长），本地开发工具加载后从初始态重放 action 直到崩溃点
- 关键工程约束：action 必须可序列化且重放确定性（同一 action 流 + 初始态 = 同一结果）；异步副作用（请求）要么 mock 回放录制时的响应，要么只重放状态不重放请求
- 隐私：payload 脱敏白名单（用户名/手机号/ token 全脱），录制开关默认关、按用户同意开启

```javascript
// 录制：拦截所有 action
function record(store) {
  let stream = [store.getState()]
  store.subscribe((s, prev, partial) => stream.push(partial))
  window.addEventListener('error', () => report({ stream: compress(stream) }))
}
// 回放：stream 依次 store.set → 精确复现崩溃前状态序列
```
