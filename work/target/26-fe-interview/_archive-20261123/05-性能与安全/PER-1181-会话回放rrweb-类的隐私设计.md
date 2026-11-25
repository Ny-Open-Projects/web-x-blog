---
title: [PER-1181] 会话回放（rrweb 类）的隐私设计
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1181：会话回放（rrweb 类）的隐私设计

**答**：
- 风险：回放录下用户输入（密码/身份证）、页面显示的他人数据。
- 控制：输入框全掩码（默认遮蔽所有 input/select/textarea）、敏感区域手动标记（CSS class 标记录制时遮挡）、文本采样（只录 DOM 结构不录文本或脱敏后录）。
- 合规：回放属系统性监控，需政策披露+同意（部分辖区）+短保留。
- 访问：回放查看需工单关联+留痕（1145）。

```javascript
// 回放录制脱敏配置
const rrwebConfig = {
  maskAllInputs: true,                            // 全输入掩码
  maskTextClass: 'rr-mask',                       // 手动标记遮挡
  blockClass: 'rr-block',                         // 整块不录
  sampling: { input: 'last', scroll: 150 },       // 降采样
  retention: 14,                                  // 天
  consentRequired: 'analytics',
};
// 查看留痕：playbackViewer(uid, sessionId) 必须 assertTicket
```
