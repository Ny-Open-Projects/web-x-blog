---
title: [OPS-131] rrweb 会话回放的原理是什么？隐私边界怎么处理？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-131：rrweb 会话回放的原理是什么？隐私边界怎么处理？
**答**：
- 原理：录制 DOM 快照 + 增量 mutation 事件流（含点击、滚动、输入事件），回放时在沙箱里按事件序列重建页面，不是录视频。
- 体积控制：事件流压缩后单会话控制在 MB 级；鼠标移动抽样、输入只记最终值、超出预算滚动丢弃最早事件。
- 隐私是红线：maskAllInputs 打码输入、blockSelector 整块排除敏感区域（手机号/证件）、排除 iframe 与密码字段。
- 合规动作：回放功能写入隐私政策并纳入 Cookie Consent 授权（OPS-151），用户关闭授权即停止录制并清空远端数据。
- 运维价值：错误聚类命中某组后，回放该组用户的会话直接看到出错前操作，复现成本大幅下降（OPS-179）。

```typescript
// rrweb 会话回放：录制事件流 + 隐私脱敏
import { record } from 'rrweb';

let buffer: unknown[] = [];
const stopRecord = record({
  emit(event) {
    buffer.push(event);
    if (buffer.length >= 50) flush();            // 批量上报，减少请求数
  },
  // 隐私边界：默认全部脱敏，敏感区域显式排除
  maskAllInputs: true,                            // 输入框内容统一打码为 *
  blockSelector: '.sensitive, [data-privacy]',    // 整块区域不录制（如手机号卡片）
  ignoreClass: 'rr-ignore',
  sampling: {
    mousemove: 50,                                // 鼠标事件抽样，控体积
    input: 'last',                                // 只记录最终输入值
  },
});

// 授权闸门：Consent 未授权不启动，用户撤回授权立即停止并清空远端
if (consent.replay) startRRWeb(); else stopRecord?.();
function flush() { /* 上报 buffer 并清空；单会话压缩后预算 ≤ 2MB，超出滚动丢弃 */ }
```
