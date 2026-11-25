---
title: [MFW-396→MFW-396] UGC 内容进 RSC 流的安全链（转义/协议/沙箱）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-396：UGC 进流安全链

**答**:
- 链上四处：①存储前消毒（富文本白名单标签+属性——script/onhas 被 schema 拒）②渲染期自动转义（React 文本插值天然转义——危险点在 dangerouslySetInnerHTML 与 href/src javascript: 协议）③链接协议门（a href 只许 http/https/mailto——统一 LinkSafe 组件）④图片与嵌入（外域图走代理/ referrer 裁剪；iframe 只许注册表内 embed 域）
- RSC 特有面：props 进 Client Component 同样经序列化——UGC 字段直达 client 再插 HTML 的路径要断（client 侧渲染也走同一 Safe 组件——双端同规则）
- 回归测试：XSS 载荷语料库（经典 bypass 集合）进 CI——每次渲染链改动全量回放
- 治理：富文本 schema 版本化（新标签需求走审批——白名单膨胀即攻击面膨胀）

```text
四处：存前白名单消毒 / 渲染 React 转义+禁 raw HTML / LinkSafe 协议门 / embed 域注册表
双端：client 侧同 Safe 组件；XSS 语料库 CI 回放；白名单变更=审批
```
