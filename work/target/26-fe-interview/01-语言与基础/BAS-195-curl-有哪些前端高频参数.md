---
title: [BAS-195] curl 有哪些前端高频参数？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-195：curl 有哪些前端高频参数？
**答**：
- 看过程：`-i` 带响应头、`-v` 完整握手与请求头调试、`-o` 落文件。
- 发请求：`-X` 指方法、`-H` 加头、`-d` 带请求体（默认触发 POST）、`-L` 跟随重定向。
- 调试利器：`-w '%{http_code}'` 只输出状态码，适合写进脚本做健康检查。

```bash
curl -i http://localhost:3000/api/users          # 显示响应头
curl -v http://localhost:3000/api/users          # 显示完整请求响应过程
curl -X POST -H 'Content-Type: application/json' \
     -d '{"name":"a"}' http://localhost:3000/api/users
curl -L http://example.com                       # 跟随重定向
curl -s -o /dev/null -w '%{http_code}' http://x  # 只看状态码
```

## 二十二、综合辨析
