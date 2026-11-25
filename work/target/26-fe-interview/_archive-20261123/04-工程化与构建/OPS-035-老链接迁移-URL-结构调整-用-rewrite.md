---
title: [OPS-035] 老链接迁移（URL 结构调整）用 rewrite 怎么做？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-035：老链接迁移（URL 结构调整）用 rewrite 怎么做？
**答**：
- 迁移目标：老 URL 用 301 永久重定向到新结构，保住 SEO 权重与用户收藏；参数需要透传或映射。
- rewrite 正则要精确锚定，避免误伤新结构；多条规则按顺序执行，last、break、permanent、redirect 的语义要清楚。
- 域名级迁移（old.com → new.com）在 server 级做整站 301；路径级迁移在 location 或 rewrite 层做。
- 上线前用小流量验证重定向结果（curl 批量测试表），上线后监控老 URL 的 301 命中量衰减趋势。

```nginx
# URL 结构迁移示例：/item/{id}.html -> /item/{id}，并兼容旧参数
server {
    listen 80;
    server_name www.example.com;

    # 1. 老详情页：/item/12345.html -> /item/12345，透传 query
    rewrite "^/item/([0-9]+)\.html$" /item/$1 permanent;

    # 2. 老分类页：/cate.php?id=x -> /category/x
    if ($arg_id) {
        rewrite ^/cate\.php$ /category/$arg_id? permanent;
    }

    # 3. 活动页整体迁移：return 比 rewrite 性能好，$is_args$args 透传原 query
    location = /act/618.html {
        return 301 /campaign/618$is_args$args;
    }

    # 4. 整站换域名（老站 server 全部 301）
    # server {
    #     server_name old.example.com;
    #     return 301 https://www.example.com$request_uri;
    # }
}

# 上线验证脚本配套（bash）：
# printf '%s\n' /item/123.html /cate.php?id=9 | while read u; do
#   curl -sI "https://www.example.com$u" | awk 'NR==1{print u, $2} u==""{}' u="$u" -
# done
```
