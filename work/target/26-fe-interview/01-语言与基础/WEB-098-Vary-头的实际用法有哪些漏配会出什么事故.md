---
title: [WEB-098] Vary 头的实际用法有哪些？漏配会出什么事故？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-098：Vary 头的实际用法有哪些？漏配会出什么事故？
**答**：
- Vary 告诉缓存：响应会随这些请求头的取值而不同，缓存键必须把该头算进去，否则会串版本。
- 经典场景一：`Vary: Accept-Encoding`，区分 gzip/br 压缩版本，防止不支持压缩的客户端收到压缩数据——nginx gzip_vary 自动加。
- 场景二：服务端按 UA 返回不同 HTML（PC/移动版）时必须 `Vary: User-Agent`，否则共享缓存的代理可能把手机版发给 PC。
- 事故模式：CDN 默认忽略 UA 做 key，页面样式错乱；配置 Vary 后缓存命中率下降属于预期代价。

```nginx
# nginx 配置 Vary 的两种典型来源
gzip on;
gzip_vary on;            # 自动为压缩响应添加 Vary: Accept-Encoding

server {
    location / {
        # PC 与移动端返回不同 HTML 时，必须声明 UA 参与缓存键
        add_header Vary "Accept-Encoding, User-Agent";
        proxy_pass http://backend;
    }
}
```
