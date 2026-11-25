---
title: [OPT-052] Brotli 相比 Gzip 收益多大？生产环境怎么配置？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-052：Brotli 相比 Gzip 收益多大？生产环境怎么配置？

**答**：
- 同等级下 Brotli 比 Gzip 再省 15-25%，对 HTML/CSS/JS 文本收益最大；`br` 压缩等级 4 已近似 gzip 9 的压缩率但速度快得多。
- 部署模式：**静态构建期用 br 等级 10-11 预压缩**（慢但只压一次），**动态响应用 br 4 实时压缩**；二者不要混在 Nginx 动态压缩里全开 11。
- Nginx 需 1.11.4+ 的 `ngx_brotli` 模块（很多发行版没编译进去，用 openresty 或自编译）；CDN 场景直接在 CDN 侧开 Brotli 更省事。
- 注意 `Vary: Accept-Encoding` 必须带，否则代理层缓存可能把 br 内容发给不支持的用户。

```nginx
# 一一对应：Nginx Brotli + Gzip 双引擎配置
http {
    # 静态文件：构建期已生成 .br（-webpack 压缩插件产出），直接返回，零实时 CPU
    location ~* \.(js|css|html|svg|json)$ {
        brotli_static on;   # 优先找 file.br
        gzip_static on;     # 其次 file.gz
        add_header Vary Accept-Encoding always;
        try_files $uri =404;
    }

    # 动态响应：Brotli 实时压缩，等级 4 是压缩率/速度的甜点位
    brotli on;
    brotli_comp_level 4;
    brotli_types text/plain text/css application/javascript application/json image/svg+xml;

    # Gzip 只作为老客户端兜底
    gzip on;
    gzip_comp_level 5;
    gzip_vary on;
    gzip_types text/plain text/css application/javascript application/json image/svg+xml;
}

# 构建期对照实验命令（上线前实测收益，避免"听说"）：
# gzip -k -9 app.js  && brotli -k -q 11 app.js
# ls -l app.js app.js.gz app.js.br  —— 通常 br 比 gz 再小 15%~20%
```
