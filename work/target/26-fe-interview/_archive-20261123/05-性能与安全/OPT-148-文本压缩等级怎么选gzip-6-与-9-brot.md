---
title: [OPT-148] 文本压缩等级怎么选？gzip -6 与 -9、brotli 的权衡与配置？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-148：文本压缩等级怎么选？gzip -6 与 -9、brotli 的权衡与配置？

**答**：
- gzip：-6（默认）与 -9 的体积差通常 < 2%，但 CPU 时间差 2~4 倍。动态请求（网关实时压缩）用 -5/-6，CPU 优先；静态资源预压缩才考虑 -9 或 zopfli。
- brotli：质量 11 相比 gzip -9 再省 15~20%，但编码极慢，**只用于构建期预压缩静态文件**；动态请求用 br quality 4~5（体积接近 gzip -9、CPU 接近 gzip -6）。
- 组合策略：构建期产出 `.br` + `.gz` 双产物，Nginx `gzip_static`/`brotli_static` 直接发，业务服务零压缩开销。
- 权衡公式：节省带宽流量费 vs 编码 CPU/构建时长；大促流量高峰前记得预压缩产物覆盖率检查。

```bash
# 一一对应：压缩等级实测对比 + 双产物预压缩流水线
# 1. 实测：同一 bundle 三档压缩，看体积与耗时
app_js=dist/assets/main-abc123.js
echo "--- gzip -6 ---"; time gzip -6 -k -c $app_js | wc -c
echo "--- gzip -9 ---"; time gzip -9 -k -c $app_js | wc -c
echo "--- brotli -11 ---"; time brotli -q 11 -c $app_js | wc -c
# 典型输出：gzip -6  118KB / 80ms ；-9  116KB / 240ms ；br-11  102KB / 1900ms
# 结论：动态请求 gzip -6；静态预压缩 brotli -11

# 2. 构建期双产物（vite-plugin-compression2 示例）
npm i -D vite-plugin-compression2
# vite.config.js:
#   plugins: [compression({ algorithm: 'brotliCompress', quality: 11, include: /\.(js|css|html|svg)$/ }),
#             compression({ algorithm: 'gzip', level: 6 })]

# 3. Nginx 直接发预压缩产物，零实时压缩开销
# nginx.conf:
#   brotli_static on;      # 优先找 .br
#   gzip_static  on;       # 其次 .gz
#   gzip on;              # 兜底：未预压缩的动态响应
#   gzip_comp_level 6;
```
