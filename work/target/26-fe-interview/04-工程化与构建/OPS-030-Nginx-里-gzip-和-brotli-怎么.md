---
title: [OPS-030] Nginx 里 gzip 和 brotli 怎么配？怎么取舍？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-030：Nginx 里 gzip 和 brotli 怎么配？怎么取舍？
**答**：
- gzip 全生态支持，CPU 开销低，保底开启；brotli 压缩率比 gzip 高 15%~25%，现代浏览器（有 br 的 Accept-Encoding）优先。
- 静态预压缩优于动态压缩：构建时产出 .gz/.br 文件，Nginx 用 gzip_static/brotli_static 直接发文件，线上零压缩开销。
- 压缩级别权衡：级别越高体积越小 CPU 越贵，动态压缩建议 gzip 5~6、brotli 4~5；只压缩文本类，图片视频字体（已压缩格式）不要压。
- 注意 proxy 场景下转发到后端时 gzip 的 Content-Encoding 与 Accept-Encoding 透传关系。

```nginx
# 静态预压缩优先 + 动态压缩兜底
# 构建期产物：app.js / app.js.gz / app.js.br（vite-plugin-compression 等）

gzip_static  on;              # 优先发送同路径的 .gz 预压缩文件
brotli_static on;             # 优先发送 .br（需 ngx_brotli 模块）

gzip on;
gzip_comp_level 5;
gzip_min_length 1024;         # 太小的不压，越压越大
gzip_vary on;                 # 告知 CDN/代理按 Accept-Encoding 区分缓存
gzip_proxied any;             # 代理来的响应也压缩
gzip_types
    text/plain
    text/css
    text/javascript
    application/javascript
    application/json
    application/xml
    image/svg+xml;

brotli on;
brotli_comp_level 5;
brotli_types
    text/css
    application/javascript
    application/json
    image/svg+xml;

location /assets/ {
    # 关闭动态压缩的重复劳动：预压缩文件已就位
    gzip off;
    add_header Vary "Accept-Encoding";
}
```
