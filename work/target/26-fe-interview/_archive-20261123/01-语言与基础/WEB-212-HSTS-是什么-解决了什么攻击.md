---
title: [WEB-212] HSTS 是什么？解决了什么攻击？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 面试题
---

## WEB-212：HSTS 是什么？解决了什么攻击？

**答**：
- HSTS（Strict-Transport-Security）：服务端响应头告诉浏览器「接下来 max-age 秒内访问本域名必须用 HTTPS，且不允许忽略证书错误」。
- 解决 SSL 剥离攻击：用户在咖啡店输入 `example.com`（无协议），默认走 HTTP，中间人劫持该 HTTP 请求即可；有 HSTS 缓存的浏览器直接内部 307 跳 HTTPS，不给中间人机会。
- 解决用户点「继续访问不安全站点」的误操作：HSTS 期间浏览器禁止跳过告警。
- includeSubDomains 覆盖子域，preload 申请进浏览器内置列表让首次访问就强制 HTTPS（解决首次请求的窗口期）。
- 注意坑：一旦下发 HSTS 且 max-age 很长，回滚 HTTP 会导致站点无法访问；子域也要全部支持 HTTPS。

```nginx
# Nginx 配置
add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload" always;
# 验证：curl -sI https://example.com | grep -i strict
```
