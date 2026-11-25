---
title: [WEB-183] Content-Length 与 Transfer-Encoding: chunked 同时出现会怎样？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-183：Content-Length 与 Transfer-Encoding: chunked 同时出现会怎样？
**答**：
- 规范裁决：两者同时存在时按 Transfer-Encoding 处理，Content-Length 被忽略。
- 实现不一致就产生"请求走私"空间：前端设备按 CL 解析、后端按 TE 解析，请求边界切错位，攻击者夹带第二个走私请求。
- 治理：网关统一标准化（剥离冲突头之一再转发）；CL 数值必须与实际 body 字节数一致，不符时按 400 处理而非静默截断。
- 服务端发送原则：定长用 Content-Length，未知长度用 chunked，绝不并发声明。

```http
# 冲突样例：同一报文同时带 CL 与 TE，规范规定 TE 优先
POST /api HTTP/1.1
Host: api.example.com
Content-Length: 6
Transfer-Encoding: chunked

0

GET /admin HTTP/1.1
Host: api.example.com

# 按 TE 解析：0 结束第一个请求，后面的 GET /admin 成了走私的第二个请求
# 按 CL 解析：只读 6 字节，GET /admin 被当作下一个请求的起始，两种实现因此分叉
```

## 三十、移动网络与混合环境
