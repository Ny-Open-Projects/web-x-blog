---
title: [PER-028] 如何在 nginx 上配置 Gzip/Brotli 压缩？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-028：如何在 nginx 上配置 Gzip/Brotli 压缩？

**答**：
- 两种模式：动态压缩（请求时实时压，耗 CPU）与静态预压缩（构建期生成 `.gz`/`.br`，直接下发，推荐）。
- Brotli 比 gzip 同级别再省 15%~20%，文本类资源收益明显，需 nginx 编译 brotli 模块。
- 只对文本类资源开压缩（JS/CSS/HTML/JSON/SVG），图片视频已压缩，再压无益反耗 CPU。
- `gzip_comp_level` 取 5 左右平衡 CPU 与压缩率；小于 1KB 的文件不值得压缩。

```nginx
server {
    listen 443 ssl http2;

    # 动态压缩：请求时实时压缩，注意控制压缩级别省 CPU
    gzip on;
    gzip_types text/css application/javascript application/json image/svg+xml;
    gzip_min_length 1024;
    gzip_comp_level 5;

    # 静态预压缩：构建阶段已生成 .br 和 .gz 文件，直接下发，节省 CPU
    location /assets/ {
        brotli_static on;   # 需要 nginx 编译 brotli 模块
        gzip_static on;
        add_header Cache-Control "public, max-age=31536000, immutable";
    }
}
```

## 五、运行时性能排查
