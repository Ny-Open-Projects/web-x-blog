---
title: [MFW-339→MFW-339] 表单校验错误的跨端映射测试
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-339：校验映射测试

**答**:
- 漂移点：client zod 与 server zod 版本不同步/规则改一头忘另一头/错误文案两处维护——映射测试锁死三处
- 测试设计：①共享 schema 单测（双端 import 同一模块——结构上杜绝两份）②错误码→文案映射表测试（server 错误码 ∈ client 文案表键集——双向包含断言）③E2E 提交非法值断言服务端字段级错误回显位置正确
- 版本策略：schema 包 semver 锁 minor（client/server 同仓升级——跨仓用 changesets 联动）
- 禁用模式：server 返回自由文本错误（client 只能 toast 整条——字段定位能力丧失——错误协议必须是结构化 code+path）

```text
三测：同 schema 双端导入 / 错误码↔文案双向包含 / E2E 字段级回显位置
协议：{ code, path, message } 结构化——禁自由文本错误
```
