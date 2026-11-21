---
title: 手机验证码六步防刷：Redis 关键设计
date: 2026-11-17
categories: [课程, 低代码]
tags: [25-lowcode, 实战, Redis, 验证码, 安全]
---

## 手机验证码六步防刷：Redis 关键设计

动机先行：短信按条收费，盗刷就是烧钱——防刷的第一动机是成本，面试讲亮点要能讲出"为什么做"。

六步防线：
1. **60 秒限流**：dayjs diff 比对上次发送时间戳，拒绝重发；
2. **图形验证码存在性检查**：svg-captcha 生成的验证码必须先比对通过（比对依赖 Redis），挡住脚本机；
3. **忽略大小写比对**；
4. 发短信；
5. **删图形验证码**（一次性）+ 按「时间戳_验证码」格式写 Redis 60 秒过期；
6. 按短信返回 code 处理，失败清理 Redis 并抛异常交统一拦截器。

**关键 key 设计**：
- 图形验证码 key = MD5(IP+设备指纹)，`CaptchaDto.type` 区分 register/login 场景实现缓存隔离；
- 短信验证码三层 key `register:code:phone` / `login:code:phone`；
- Redis 冒号分层 + EX 过期，value 必须转字符串。

坑：全局 Redis 模块要走 `imports` 不能塞进子模块 `providers`；验证码 type 传错则 key 不匹配永远校验失败。

出处「课程25 · 11-1~11-6；scan3」
