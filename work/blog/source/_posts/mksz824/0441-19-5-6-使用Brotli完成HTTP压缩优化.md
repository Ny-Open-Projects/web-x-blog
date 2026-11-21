---
disableNunjucks: true
title: 19-5-6 使用Brotli完成HTTP压缩优化
date: 2026-11-17 09:21:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

上节课我们介绍了 HTTP 传输中最常用的压缩算法 Gzip，它能有效减少传输过程中的流量。不过 HTTP 支持的压缩算法不止这一种，这节课来扩展一下知识面，介绍一个后起之秀、如今已经大面积普及的新算法：Brotli。

Brotli 是谷歌的软件工程师在 2015 年 9 月发布的通用无损数据压缩算法，它侧重于对 Gzip 的编码器进行了部分改写，从而提高了压缩比。

它的高效体现在哪里？看一张各算法的对比图，三列分别是压缩比（越大越好）、压缩速度、解压缩速度。gzip 的压缩比从 2.8 到 3.63，其中 1 到 9 是不同的 compression level，级别越高压缩比越大，但速度也越慢。而 Brotli 的级别从 1 到 11，起点就是 3.22，最高级别 11 能达到 4.63。压缩和解压缩时间虽然比 gzip 稍慢一点，但差距不大，所以它明显是更好的算法。

当然，这个 2015 年推出的现代算法有一些使用前提。第一个前提是浏览器支持，可以在 Can I use 上查到 Brotli content encoding 的兼容情况：它比 gzip 和 deflate 更有效率，Edge 从 15 开始支持，Firefox 从 44 开始，Chrome 从 50 开始，也就是说现在的浏览器基本都支持 Brotli。第二个前提是必须使用 HTTPS 协议。

想在 Nginx 上启用它，需要安装谷歌推出的 ngx_brotli 模块。Nginx 由一系列 module 组成，这个模块安装完之后会提供对应的 directives，包括 brotli_static、brotli（值是 on 或 off）、brotli_types（指定哪些文件开启压缩），用法和 gzip 非常类似。

由于本地 localhost 没有启动 HTTPS，这里用一台线上机器演示。登录后执行 `nginx -V`，可以看到线上机器编译的模块比本地多不少，其中就有一个标记为 dynamic module 的 ngx_brotli 动态模块，说明这台机器已经可以启用 Brotli 压缩了。

再看配置文件 `/etc/nginx/nginx.conf`。gzip 那一系列配置我们已经比较熟悉，本地也添加过。下面是 brotli 的部分：`brotli on` 开启 Brotli 压缩；`brotli_static on` 的含义之后解释；`brotli_types *` 表示对所有类型的文件开启，和 gzip_types 类似。添加这几个指令之后压缩就生效了。

看线上最终的结果。刷新页面时勾选 Disable Cache，保证每次都加载新资源。打开请求的详情，要特别关注 Response Headers 里的 `Content-Encoding: br`，br 就代表 Brotli 压缩，说明服务器使用了它，且浏览器支持解压。

再看压缩比，从 size 面板可以看到 resource size 是 605k，压缩传输后只有 139k，压缩比达到了 4 倍多，非常可观。

总结一下：Brotli 是一种更优秀、更高效的 HTTP 压缩算法，但要求也更苛刻，需要较新的浏览器和 HTTPS 协议支持。在 HTTPS 普及的今天，强烈建议把 Brotli 作为候选项，我自己的线上项目都是这么做的。接近四倍的压缩比，值得你在面试中也拿出来讲一讲，面试官会对这样的知识面刮目相看。拿 Brotli 和 Gzip 对比一下，就可以获得最终的决策。
