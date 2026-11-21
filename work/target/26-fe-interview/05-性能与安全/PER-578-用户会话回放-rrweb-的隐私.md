---
title: [PER-578] 用户会话回放（rrweb）的隐私合规怎么落地？哪些数据必须在采集端脱敏？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-578：用户会话回放（rrweb）的隐私合规怎么落地？哪些数据必须在采集端脱敏？

**答**：
- 原则是采集端脱敏、传输加密、最小保留"：输入框（密码/验证码/搜索词）、身份证手机号等 PII 文本在采集时就被替换为占位符，`rrweb.record` 的 `maskAllInputs`/`ignoreElements`/文本替换回调是第一道闸——不能依赖服务端后处理（原始数据已经落地）。
- 分级策略：默认全量脱敏（所有输入框 mask），白名单页面（如客服演示页）放宽；图片/富文本内容可配置采样替换。
- 合规配套：隐私政策告知 + 用户可退出（退出即彻底停 SDK 与清已存回放）、回放数据加密存储、保留期限（如 30 天）到期自动删除、访问权限审计（谁能看回放要留记录）。
- 常见事故：把回放用于排障扩大用途到监控员工行为，超出告知范围即违规——用途范围要写进隐私政策并技术隔离。

```javascript

import rrweb from 'rrweb';
rrweb.record({
  emit: (e) => queue.push(e),
  maskAllInputs: true,                                    // 所有输入框内容脱敏
  maskTextClass: 'pii-mask',                              // 标记类名的文本替换
  maskTextSelector: '[data-pii]',
  ignoreElements: (el) => el.tagName === 'IFRAME' && el.dataset.ignore === '1',
  // 采集端脱敏是第一道闸，服务端不再碰原始 PII
});
// 配套：用户退出 -> rrweb.stop() + 清空队列 + 删除已上传会话
// 保留 30 天 -> 服务端 TTL 索引；查看权限 -> 审计日志
```
