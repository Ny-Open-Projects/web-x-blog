---
disableNunjucks: true
title: 19-5-8 使用keep-alive减少多次TCP连接
date: 2026-11-17 10:22:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

上节课我们通过压缩算法优化了 HTTP 传输，这节课继续看 HTTP 协议传输过程中的其他优化手段。

先明确 HTTP 的定位：它处于计算机网络的应用层，建立在 TCP 协议之上，所以 HTTP 的瓶颈和优化技巧都是基于 TCP 协议本身的特性，比如建立连接的三次握手、断开连接的四次挥手，以及每次建立连接带来的延迟。减少这些时间至关重要。

第一个优化手段叫 Keep-Alive，这是个大家熟悉又陌生的字段：似乎听说过，但不太清楚它是干什么的。在现代 Web 世界里它已经是默认开启的标配，但我们还是要搞清楚它的来龙去脉。

HTTP 请求默认在每次请求完就关闭连接。当用户访问我们的站点时，站点有一大堆静态文件，浏览器会为每个请求新建连接。用图来描述 keep-alive 关闭时的过程：浏览器和服务器先握手建立连接，第一次请求 index.php，服务器返回文件，请求结束后连接就被关闭了；接下来请求第二个资源，又要重复一遍建连、请求、断开的流程。这样会造成加载时间的浪费。

Keep-Alive 字段就是为了解决这个问题而诞生的：它让客户端和服务器端的连接不断开，出现后续请求时直接复用已经建立的连接。建连一次，后面的所有资源请求都可以在这个连接上继续进行。在 HTTP 1.0 时代，Keep-Alive 没有官方支持；到了 1.1，它已经默认支持并开启。

下面看一个线上例子，本地响应太快不够直观。登录服务器，keep-alive 的配置在 server block 里，也就是 `/etc/nginx/sites-enabled` 下对应域名的配置文件。里面有个 `keepalive_timeout` 字段，后面的数字表示长连接持续的秒数。要关闭它，把这个字段删掉（或改成 0），然后 `service nginx restart` 重启（我这里用的是 Ubuntu 系统）。

重启后刷新线上页面，查看某个资源的 Response Header，里面有一个 connection 字段显示 close，说明每次请求完毕连接都会被关闭。再看它的 Waterfall 瀑布图：Connection Start 中有两个字段，DNS Lookup 和 Initial Connection，用黄色短线表示。云主机比较快，这两个时间很短，但都存在，而且每个请求上都能看到。

这两个字段的含义可以在 Chrome 的 Network Features Explanation 里查到：DNS Lookup 是浏览器在解析请求的 IP 地址；Initial connection 是建立连接的过程，包括 TCP 握手和重试等。它们证明了每个请求都要独立发起建连，耗费一定时间。

现在把 keep-alive 开启，还是改 server block，直接把那行注释掉即可，因为 1.1 下它默认开启。重启 nginx 后刷新页面：Response Header 里的 connection 变成了 keep-alive；再看瀑布图，Connection Start 里之前的 DNS Lookup 和 Initial Connection 大部分都消失了，只有第一次连接的请求还有，其余请求全部复用了这条连接，节省了一系列时间。

从中不难总结出 Keep-Alive 的优点：第一，TCP 连接更少了，节省了连接建立和释放的时间，也降低了主机和路由器上 CPU、内存的开销；第二，网络拥塞减少，拿到响应的延时自然也减少了。

Keep-Alive 能在一定程度上弥补 TCP 协议本身的弊端。下节课我们来看质的飞跃：HTTP 新版本的推出会带来怎样的巨大影响。
