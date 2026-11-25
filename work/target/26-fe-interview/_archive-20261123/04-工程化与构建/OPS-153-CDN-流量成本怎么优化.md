---
title: [OPS-153] CDN 流量成本怎么优化？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-153：CDN 流量成本怎么优化？
**答**：
- 三板斧：传小（brotli/gzip、图片参数化处理）、少传（immutable 长缓存让回访近乎零流量）、不白传（防盗链挡外站盗用）。
- 图片是流量大头：处理参数出图（OPS-113）+ 响应式尺寸 + webp/avif 协商，通常可省 40-60% 图片流量。
- 防盗链要留 none/blocked 放行：App 内嵌 WebView 与直接打开图片的场景 Referer 为空，一刀切会误伤。
- 按月复盘流量 TOP URL：找可懒加载、可降尺寸、可下线的资源；异常流量（盗刷）从访问日志地域/UA 异常发现。
- 带宽计费模式（按峰值/按流量/95 峰值）对账单影响巨大，规模上去后要主动与商务谈。

```nginx
# CDN 流量成本三板斧（源站/边缘同构配置）
server {
    # 1. 传小：brotli 优先，gzip 兜底
    brotli on;
    brotli_comp_level 5;        # 5 以上 CPU 收益比急剧变差
    brotli_types text/css application/javascript application/json image/svg+xml;
    gzip on;
    gzip_vary on;

    # 2. 少传：版本化资源永久缓存，回访请求近乎零流量
    location /static/ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }

    # 3. 不白传：Referer 防盗链，none/blocked 放行 App 内嵌与直接打开场景
    location ~* \.(jpe?g|png|gif|webp|mp4)$ {
        valid_referers none blocked server_names *.example.com *.example.cn;
        if ($invalid_referer) { return 403; }
        expires 30d;
        # 图片本体优化走处理参数（OPS-113）：响应式尺寸 + webp 协商
    }

    # 4. 月度流量 TOP 复盘入口
    # awk '{print $7}' access.log | sort | uniq -c | sort -rn | head -50
}
```
