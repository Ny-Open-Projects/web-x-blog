---
title: [WEB-002] 一个完整的 HTTP 报文由哪几部分组成？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-002：一个完整的 HTTP 报文由哪几部分组成？
**答**：
- 请求报文：请求行（方法 + URL + 版本）、请求头、空行、请求体。
- 响应报文：状态行（版本 + 状态码 + 原因短语）、响应头、空行、响应体。
- 头部是键值对文本，Body 可以是表单、JSON、二进制等多种形态，由 `Content-Type` 决定解析方式。
- 面试时可现场用 curl 看真实报文，说明 start line、headers、body 的分界。

```bash
# -v 显示请求与响应的完整报文，可清晰看到请求行、头部、空行和响应体
curl -v https://httpbin.org/get

# 只看响应头
curl -I https://httpbin.org/get

# 发送带 JSON 体的 POST 请求，观察 Content-Type 与 body
curl -v -X POST https://httpbin.org/post \
  -H 'Content-Type: application/json' \
  -d '{"name":"fe","level":"senior"}'
```
