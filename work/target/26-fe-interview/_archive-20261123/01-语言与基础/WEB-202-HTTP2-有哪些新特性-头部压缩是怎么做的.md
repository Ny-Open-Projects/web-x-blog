---
title: [WEB-202] HTTP/2 有哪些新特性？头部压缩 HPACK 是怎么做的？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTP2]
type: 面试题
---

## WEB-202：HTTP/2 有哪些新特性？头部压缩 HPACK 是怎么做的？

**答**：
- 四大特性：二进制分帧、多路复用（一条 TCP 连接并行多个 stream）、头部压缩 HPACK、服务器推送 Server Push（现已被 Chrome 移除支持，实践上被 103 Early Hints / preload 取代）。
- HPACK 三招：静态表（61 个常见头如 `:method`、`user-agent` 的索引）、动态表（连接级缓存本次连接出现过的自定义头，后续只传索引）、Huffman 编码（对没进表的值做变长编码）。
- 头部压缩收益大的原因：HTTP/1.1 每次请求重复携带几百字节的 cookie / UA 等头；动态表让重复头只传 1~2 字节索引。
- 副作用：动态表依赖连接状态，HPACK曾有cracking风险，反向代理多连接复用时要注意动态表无法跨连接共享。

```bash
# 用 curl 观察 HTTP/2 帧与头部压缩
curl -s --http2 -v https://httpbin.org/get -o /dev/null 2>&1 \
  | grep -E 'HEADERS|Using HTTP2|Stream'
# 可以看到 HEADERS 帧里重复头变成索引引用，报文体积骤减
```
